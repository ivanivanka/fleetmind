"""Warehouse simulation engine with pathfinding, battery management, and collision avoidance."""

import asyncio
import heapq
import random
import time
import uuid
from typing import Optional

from models import (
    Alert, MetricsSnapshot, Position, Robot, RobotState,
    Task, TaskPriority, TaskStatus, WarehouseConfig,
)

# Item names for realistic order generation
ITEMS = [
    "Electronics Kit A", "Electronics Kit B", "Phone Cases (50pk)",
    "USB Cables (100pk)", "Bluetooth Speakers", "Wireless Chargers",
    "Laptop Stands", "Keyboard Bundle", "Mouse Pack (20)",
    "Monitor Arms", "Webcam Pro", "Headset Pack",
    "Tablet Cases", "Power Banks", "Smart Watch Band",
    "LED Strip Kit", "HDMI Adapters", "Network Switch",
    "SSD Drive 1TB", "RAM Module 16GB", "Thermal Paste",
    "Fan Assembly", "Cable Management Kit", "Surge Protector",
]


class WarehouseSimulation:
    def __init__(self, config: Optional[WarehouseConfig] = None):
        self.config = config or WarehouseConfig()
        self.grid: list[list[int]] = []  # 0=floor, 1=shelf, 2=charging, 3=pickup, 4=dropoff
        self.robots: dict[str, Robot] = {}
        self.tasks: dict[str, Task] = {}
        self.alerts: list[Alert] = []
        self.metrics_history: list[MetricsSnapshot] = []
        self.running = False
        self.paused = False
        self.tick_count = 0
        self.start_time = 0.0
        self.last_task_time = 0.0
        self.total_completed = 0
        self.total_failed = 0
        self.completion_times: list[float] = []
        self.charging_stations: list[Position] = []
        self.pickup_zones: list[Position] = []
        self.dropoff_zones: list[Position] = []
        self._subscribers: list[asyncio.Queue] = []
        self._setup_warehouse()
        self._setup_robots()

    def _setup_warehouse(self):
        """Create warehouse layout with shelves, aisles, charging stations."""
        w, h = self.config.width, self.config.height
        self.grid = [[0] * w for _ in range(h)]

        # Shelf rows (leaving aisles between them)
        shelf_rows = [4, 5, 8, 9, 12, 13, 16, 17, 20, 21]
        for row in shelf_rows:
            if row < h - 2:
                for col in range(4, w - 4):
                    # Leave gaps every 6 cells for cross-aisles
                    if col % 8 not in (0, 7):
                        self.grid[row][col] = 1

        # Charging stations in corners
        station_positions = [
            Position(x=1, y=1),
            Position(x=w - 2, y=1),
            Position(x=1, y=h - 2),
            Position(x=w - 2, y=h - 2),
        ]
        for pos in station_positions:
            self.grid[pos.y][pos.x] = 2
            self.charging_stations.append(pos)

        # Pickup zones (left side, rows 2-3)
        for col in range(1, 4):
            for row in [2, 3, h - 4, h - 3]:
                if row < h:
                    self.grid[row][col] = 3
                    self.pickup_zones.append(Position(x=col, y=row))

        # Dropoff zones (right side)
        for col in range(w - 4, w - 1):
            for row in [2, 3, h - 4, h - 3]:
                if row < h:
                    self.grid[row][col] = 4
                    self.dropoff_zones.append(Position(x=col, y=row))

    def _setup_robots(self):
        """Initialize robot fleet at various positions."""
        names = [
            "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta",
            "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu",
            "Nu", "Xi", "Omicron", "Pi",
        ]
        # Place robots in open floor areas
        open_positions = []
        for y in range(self.config.height):
            for x in range(self.config.width):
                if self.grid[y][x] == 0:
                    open_positions.append(Position(x=x, y=y))

        random.shuffle(open_positions)
        for i in range(min(self.config.num_robots, len(open_positions))):
            rid = f"R{i+1:02d}"
            robot = Robot(
                id=rid,
                name=names[i % len(names)],
                position=open_positions[i],
                battery=random.uniform(60.0, 100.0),
            )
            self.robots[rid] = robot

    def subscribe(self) -> asyncio.Queue:
        """Subscribe to simulation state updates."""
        q: asyncio.Queue = asyncio.Queue(maxsize=50)
        self._subscribers.append(q)
        return q

    def unsubscribe(self, q: asyncio.Queue):
        if q in self._subscribers:
            self._subscribers.remove(q)

    async def _broadcast(self, data: dict):
        dead = []
        for q in self._subscribers:
            try:
                q.put_nowait(data)
            except asyncio.QueueFull:
                dead.append(q)
        for q in dead:
            self._subscribers.remove(q)

    def _is_walkable(self, x: int, y: int) -> bool:
        if 0 <= x < self.config.width and 0 <= y < self.config.height:
            return self.grid[y][x] != 1  # shelves are not walkable
        return False

    def _find_path(self, start: Position, end: Position) -> list[Position]:
        """A* pathfinding avoiding shelves and other robots."""
        if start == end:
            return [end]

        robot_positions = {(r.position.x, r.position.y) for r in self.robots.values()}

        open_set = [(0, 0, start.x, start.y)]
        came_from: dict[tuple[int, int], tuple[int, int]] = {}
        g_score: dict[tuple[int, int], float] = {(start.x, start.y): 0}
        counter = 1

        while open_set:
            _, _, cx, cy = heapq.heappop(open_set)

            if cx == end.x and cy == end.y:
                path = []
                current = (cx, cy)
                while current in came_from:
                    path.append(Position(x=current[0], y=current[1]))
                    current = came_from[current]
                path.reverse()
                return path

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = cx + dx, cy + dy
                if not self._is_walkable(nx, ny):
                    continue
                # Allow destination even if robot is there
                if (nx, ny) in robot_positions and not (nx == end.x and ny == end.y):
                    if (nx, ny) != (start.x, start.y):
                        continue

                new_g = g_score.get((cx, cy), float("inf")) + 1
                if new_g < g_score.get((nx, ny), float("inf")):
                    came_from[(nx, ny)] = (cx, cy)
                    g_score[(nx, ny)] = new_g
                    h = abs(nx - end.x) + abs(ny - end.y)
                    heapq.heappush(open_set, (new_g + h, counter, nx, ny))
                    counter += 1

        return []  # no path found

    def _nearest_charging_station(self, pos: Position) -> Optional[Position]:
        if not self.charging_stations:
            return None
        return min(self.charging_stations, key=lambda s: pos.distance_to(s))

    def _generate_task(self):
        """Create a new warehouse task with random pickup/dropoff."""
        if not self.pickup_zones or not self.dropoff_zones:
            return
        pickup = random.choice(self.pickup_zones)
        dropoff = random.choice(self.dropoff_zones)
        priority_weights = {
            TaskPriority.CRITICAL: 5,
            TaskPriority.HIGH: 15,
            TaskPriority.NORMAL: 60,
            TaskPriority.LOW: 20,
        }
        priority = random.choices(
            list(priority_weights.keys()),
            list(priority_weights.values()),
        )[0]
        task = Task(
            id=str(uuid.uuid4())[:8],
            order_id=f"ORD-{random.randint(1000, 9999)}",
            pickup=pickup,
            dropoff=dropoff,
            priority=priority,
            item_description=random.choice(ITEMS),
        )
        self.tasks[task.id] = task

    def _queued_task_count(self) -> int:
        return sum(1 for t in self.tasks.values() if t.status == TaskStatus.QUEUED)

    def _prune_tasks(self):
        """Prevent unbounded growth by dropping oldest terminal tasks."""
        max_total = int(getattr(self.config, "max_total_tasks", 2000) or 0)
        if max_total <= 0 or len(self.tasks) <= max_total:
            return

        terminal = [t for t in self.tasks.values() if t.status in (TaskStatus.COMPLETED, TaskStatus.FAILED)]
        terminal.sort(key=lambda t: t.created_at)  # oldest first
        to_remove = len(self.tasks) - max_total
        for t in terminal[:to_remove]:
            self.tasks.pop(t.id, None)

    def _assign_tasks(self):
        """Assign queued tasks to idle robots based on proximity and priority."""
        priority_order = {
            TaskPriority.CRITICAL: 0,
            TaskPriority.HIGH: 1,
            TaskPriority.NORMAL: 2,
            TaskPriority.LOW: 3,
        }
        queued = sorted(
            [t for t in self.tasks.values() if t.status == TaskStatus.QUEUED],
            key=lambda t: (priority_order.get(t.priority, 2), t.created_at),
        )
        idle_robots = [
            r for r in self.robots.values()
            if r.state == RobotState.IDLE
            and r.battery > self.config.low_battery_threshold
        ]

        for task in queued:
            if not idle_robots:
                break
            # Find nearest idle robot
            best = min(idle_robots, key=lambda r: r.position.distance_to(task.pickup))
            path = self._find_path(best.position, task.pickup)
            if path:
                best.state = RobotState.MOVING_TO_PICKUP
                best.target = task.pickup
                best.path = path
                best.current_task_id = task.id
                task.status = TaskStatus.ASSIGNED
                task.assigned_robot_id = best.id
                task.started_at = time.time()
                idle_robots.remove(best)

    def _check_battery(self):
        """Send low-battery robots to charge."""
        for robot in self.robots.values():
            if robot.state in (RobotState.IDLE, RobotState.ERROR):
                if robot.battery < self.config.low_battery_threshold:
                    station = self._nearest_charging_station(robot.position)
                    if station:
                        path = self._find_path(robot.position, station)
                        if path:
                            robot.state = RobotState.MOVING_TO_CHARGE
                            robot.target = station
                            robot.path = path
                            if robot.battery < self.config.critical_battery_threshold:
                                self._add_alert(
                                    "low_battery",
                                    f"Robot {robot.name} ({robot.id}) battery critical: {robot.battery:.0f}%",
                                    robot_id=robot.id,
                                )

            # Emergency: robot runs out mid-task
            if robot.battery <= 1.0 and robot.state not in (RobotState.CHARGING, RobotState.ERROR):
                robot.state = RobotState.ERROR
                robot.error_message = "Battery depleted"
                robot.path = []
                if robot.current_task_id and robot.current_task_id in self.tasks:
                    task = self.tasks[robot.current_task_id]
                    task.status = TaskStatus.FAILED
                    self.total_failed += 1
                    robot.current_task_id = None
                self._add_alert(
                    "stuck",
                    f"Robot {robot.name} ({robot.id}) battery depleted, stuck at ({robot.position.x}, {robot.position.y})",
                    robot_id=robot.id,
                )

    def _move_robots(self):
        """Move each robot one step along its path."""
        for robot in self.robots.values():
            if robot.state == RobotState.CHARGING:
                robot.battery = min(100.0, robot.battery + self.config.battery_charge_per_tick)
                if robot.battery >= 95.0:
                    robot.state = RobotState.IDLE
                    robot.target = None
                continue

            if robot.state == RobotState.ERROR:
                continue

            if robot.path:
                next_pos = robot.path[0]
                # Collision check - is another robot at next position?
                blocked = any(
                    r.position == next_pos and r.id != robot.id
                    for r in self.robots.values()
                )
                if not blocked:
                    robot.position = next_pos
                    robot.path.pop(0)
                    robot.battery -= self.config.battery_drain_per_move
                    robot.distance_traveled += 1

            # State transitions when path completed
            if not robot.path and robot.target:
                if robot.state == RobotState.MOVING_TO_PICKUP:
                    robot.state = RobotState.PICKING
                elif robot.state == RobotState.MOVING_TO_DROPOFF:
                    robot.state = RobotState.DROPPING
                elif robot.state == RobotState.MOVING_TO_CHARGE:
                    robot.state = RobotState.CHARGING

            # Handle picking -> moving to dropoff
            if robot.state == RobotState.PICKING:
                if robot.current_task_id and robot.current_task_id in self.tasks:
                    task = self.tasks[robot.current_task_id]
                    task.status = TaskStatus.IN_PROGRESS
                    path = self._find_path(robot.position, task.dropoff)
                    if path:
                        robot.state = RobotState.MOVING_TO_DROPOFF
                        robot.target = task.dropoff
                        robot.path = path

            # Handle dropping -> task complete
            if robot.state == RobotState.DROPPING:
                if robot.current_task_id and robot.current_task_id in self.tasks:
                    task = self.tasks[robot.current_task_id]
                    task.status = TaskStatus.COMPLETED
                    task.completed_at = time.time()
                    self.total_completed += 1
                    robot.tasks_completed += 1
                    if task.started_at:
                        self.completion_times.append(task.completed_at - task.started_at)
                robot.current_task_id = None
                robot.target = None
                robot.state = RobotState.IDLE

    def _add_alert(self, alert_type: str, message: str, robot_id: str = None, task_id: str = None):
        # Limit alerts and avoid duplicates
        recent = [a for a in self.alerts if not a.acknowledged and a.type == alert_type and a.robot_id == robot_id]
        if len(recent) >= 2:
            return
        alert = Alert(
            id=str(uuid.uuid4())[:8],
            type=alert_type,
            message=message,
            robot_id=robot_id,
            task_id=task_id,
        )
        self.alerts.append(alert)
        # Keep last 50 alerts
        if len(self.alerts) > 50:
            self.alerts = self.alerts[-50:]

    def get_metrics(self) -> MetricsSnapshot:
        now = time.time()
        elapsed = max(now - self.start_time, 1.0) if self.start_time else 1.0
        active = sum(1 for r in self.robots.values() if r.state in (
            RobotState.MOVING_TO_PICKUP, RobotState.PICKING,
            RobotState.MOVING_TO_DROPOFF, RobotState.DROPPING,
        ))
        charging = sum(1 for r in self.robots.values() if r.state == RobotState.CHARGING)
        idle = sum(1 for r in self.robots.values() if r.state == RobotState.IDLE)
        error = sum(1 for r in self.robots.values() if r.state == RobotState.ERROR)
        avg_battery = sum(r.battery for r in self.robots.values()) / max(len(self.robots), 1)
        avg_time = sum(self.completion_times[-50:]) / max(len(self.completion_times[-50:]), 1) if self.completion_times else 0
        throughput = (self.total_completed / elapsed) * 60

        return MetricsSnapshot(
            timestamp=now,
            tasks_completed=self.total_completed,
            tasks_failed=self.total_failed,
            tasks_in_queue=sum(1 for t in self.tasks.values() if t.status == TaskStatus.QUEUED),
            avg_completion_time=avg_time,
            throughput_per_minute=throughput,
            fleet_utilization=active / max(len(self.robots), 1),
            avg_battery=avg_battery,
            robots_charging=charging,
            robots_active=active,
            robots_idle=idle,
            robots_error=error,
            total_distance=sum(r.distance_traveled for r in self.robots.values()),
            alerts_active=sum(1 for a in self.alerts if not a.acknowledged),
        )

    def get_state(self) -> dict:
        """Return full simulation state for WebSocket broadcast."""
        metrics = self.get_metrics()
        recent_tasks = sorted(
            self.tasks.values(),
            key=lambda t: t.created_at,
            reverse=True,
        )[:20]

        return {
            "type": "state_update",
            "tick": self.tick_count,
            "paused": self.paused,
            "grid": {
                "width": self.config.width,
                "height": self.config.height,
                "cells": self.grid,
                "charging_stations": [{"x": s.x, "y": s.y} for s in self.charging_stations],
                "pickup_zones": [{"x": p.x, "y": p.y} for p in self.pickup_zones],
                "dropoff_zones": [{"x": d.x, "y": d.y} for d in self.dropoff_zones],
            },
            "robots": [
                {
                    "id": r.id,
                    "name": r.name,
                    "x": r.position.x,
                    "y": r.position.y,
                    "state": r.state.value,
                    "battery": round(r.battery, 1),
                    "target": {"x": r.target.x, "y": r.target.y} if r.target else None,
                    "path": [{"x": p.x, "y": p.y} for p in r.path[:10]],
                    "task_id": r.current_task_id,
                    "tasks_completed": r.tasks_completed,
                    "distance": round(r.distance_traveled, 1),
                    "error": r.error_message,
                }
                for r in self.robots.values()
            ],
            "tasks": [
                {
                    "id": t.id,
                    "order_id": t.order_id,
                    "item": t.item_description,
                    "priority": t.priority.value,
                    "status": t.status.value,
                    "robot_id": t.assigned_robot_id,
                    "pickup": {"x": t.pickup.x, "y": t.pickup.y},
                    "dropoff": {"x": t.dropoff.x, "y": t.dropoff.y},
                    "created_at": t.created_at,
                }
                for t in recent_tasks
            ],
            "metrics": metrics.model_dump(),
            "alerts": [
                {
                    "id": a.id,
                    "type": a.type,
                    "message": a.message,
                    "robot_id": a.robot_id,
                    "timestamp": a.timestamp,
                    "acknowledged": a.acknowledged,
                }
                for a in self.alerts[-10:]
                if not a.acknowledged
            ],
        }

    async def tick(self):
        """Run one simulation tick."""
        now = time.time()

        # E-stop / pause: keep broadcasting but don't mutate the world.
        if self.paused:
            await self._broadcast(self.get_state())
            return

        self.tick_count += 1

        # Generate new tasks periodically
        if now - self.last_task_time >= self.config.task_generation_rate:
            # Soft-cap the queue to keep the demo stable/legible.
            if self._queued_task_count() < int(getattr(self.config, "max_queued_tasks", 25) or 25):
                self._generate_task()
            self.last_task_time = now

        self._check_battery()
        self._assign_tasks()
        self._move_robots()
        self._prune_tasks()

        # Broadcast state
        state = self.get_state()
        await self._broadcast(state)

        # Record metrics every 10 ticks
        if self.tick_count % 10 == 0:
            self.metrics_history.append(self.get_metrics())
            if len(self.metrics_history) > 360:
                self.metrics_history = self.metrics_history[-360:]

    async def run(self, tick_interval: float = 0.3):
        """Main simulation loop."""
        self.running = True
        self.start_time = time.time()
        self.last_task_time = time.time()

        # Generate initial batch of tasks
        for _ in range(5):
            self._generate_task()

        while self.running:
            await self.tick()
            await asyncio.sleep(tick_interval)

    def stop(self):
        self.running = False

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def acknowledge_alert(self, alert_id: str) -> bool:
        for alert in self.alerts:
            if alert.id == alert_id:
                alert.acknowledged = True
                return True
        return False

    def emergency_stop_robot(self, robot_id: str) -> bool:
        if robot_id in self.robots:
            robot = self.robots[robot_id]
            robot.state = RobotState.IDLE
            robot.path = []
            robot.target = None
            if robot.current_task_id and robot.current_task_id in self.tasks:
                self.tasks[robot.current_task_id].status = TaskStatus.QUEUED
                self.tasks[robot.current_task_id].assigned_robot_id = None
            robot.current_task_id = None
            return True
        return False

    def add_manual_task(self, pickup_x: int, pickup_y: int, dropoff_x: int, dropoff_y: int, priority: str = "normal") -> Optional[Task]:
        task = Task(
            id=str(uuid.uuid4())[:8],
            order_id=f"MAN-{random.randint(1000, 9999)}",
            pickup=Position(x=pickup_x, y=pickup_y),
            dropoff=Position(x=dropoff_x, y=dropoff_y),
            priority=TaskPriority(priority),
            item_description="Manual Order",
        )
        self.tasks[task.id] = task
        return task
