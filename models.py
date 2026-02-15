"""Data models for Markster FleetMind AI warehouse simulation."""

from enum import Enum
from pydantic import BaseModel
from typing import Optional
import time
import uuid


class RobotState(str, Enum):
    IDLE = "idle"
    MOVING_TO_PICKUP = "moving_to_pickup"
    PICKING = "picking"
    MOVING_TO_DROPOFF = "moving_to_dropoff"
    DROPPING = "dropping"
    MOVING_TO_CHARGE = "moving_to_charge"
    CHARGING = "charging"
    ERROR = "error"


class TaskStatus(str, Enum):
    QUEUED = "queued"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


class TaskPriority(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    NORMAL = "normal"
    LOW = "low"


class Position(BaseModel):
    x: int
    y: int

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def distance_to(self, other: "Position") -> float:
        return abs(self.x - other.x) + abs(self.y - other.y)


class Robot(BaseModel):
    id: str
    name: str
    position: Position
    target: Optional[Position] = None
    path: list[Position] = []
    state: RobotState = RobotState.IDLE
    battery: float = 100.0
    speed: float = 1.0
    current_task_id: Optional[str] = None
    tasks_completed: int = 0
    distance_traveled: float = 0.0
    error_message: Optional[str] = None


class Task(BaseModel):
    id: str
    order_id: str
    pickup: Position
    dropoff: Position
    priority: TaskPriority = TaskPriority.NORMAL
    status: TaskStatus = TaskStatus.QUEUED
    assigned_robot_id: Optional[str] = None
    created_at: float = 0.0
    started_at: Optional[float] = None
    completed_at: Optional[float] = None
    item_description: str = ""

    def model_post_init(self, __context):
        if self.created_at == 0.0:
            self.created_at = time.time()
        if not self.id:
            self.id = str(uuid.uuid4())[:8]


class Alert(BaseModel):
    id: str
    type: str  # low_battery, stuck, failed_task, throughput_drop
    message: str
    robot_id: Optional[str] = None
    task_id: Optional[str] = None
    timestamp: float = 0.0
    acknowledged: bool = False

    def model_post_init(self, __context):
        if self.timestamp == 0.0:
            self.timestamp = time.time()


class WarehouseConfig(BaseModel):
    width: int = 40
    height: int = 30
    num_robots: int = 12
    num_charging_stations: int = 4
    task_generation_rate: float = 3.0  # seconds between new tasks
    max_queued_tasks: int = 25  # soft cap to keep the demo stable/legible
    max_total_tasks: int = 2000  # prevent unbounded growth over long runtimes
    # Demo-tuned: keep the fleet moving for long sessions without "dying off".
    battery_drain_per_move: float = 0.06
    battery_charge_per_tick: float = 2.5
    low_battery_threshold: float = 35.0
    critical_battery_threshold: float = 20.0


class MetricsSnapshot(BaseModel):
    timestamp: float
    tasks_completed: int
    tasks_failed: int
    tasks_in_queue: int
    avg_completion_time: float
    throughput_per_minute: float
    fleet_utilization: float
    avg_battery: float
    robots_charging: int
    robots_active: int
    robots_idle: int
    robots_error: int
    total_distance: float
    alerts_active: int
