# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TaskListResponse", "Task"]


class Task(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the task."""

    status: Optional[Literal["Active", "Completed", "Failed", "Canceled"]] = None
    """The current status of the task."""


class TaskListResponse(BaseModel):
    tasks: Optional[List[Task]] = None
