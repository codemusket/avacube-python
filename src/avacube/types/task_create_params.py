# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TaskCreateParams",
    "Action",
    "ActionEthTransfer",
    "ActionContractExecution",
    "Trigger",
    "TriggerSchedule",
    "TriggerContractQuery",
    "TriggerExpression",
]


class TaskCreateParams(TypedDict, total=False):
    action: Required[Action]
    """Union type for different task actions."""

    task_type: Required[Literal["ETHTransferTask", "ContractExecutionTask"]]
    """The type of task to create."""

    trigger: Required[Trigger]
    """Union type for different trigger conditions."""

    expired_at: int
    """The epoch time (in seconds) after which the task is no longer valid."""

    memo: str
    """Optional field to store arbitrary notes or metadata related to the task."""

    start_at: int
    """The epoch time (in seconds) after which the task becomes valid."""


class ActionEthTransfer(TypedDict, total=False):
    amount: Required[str]
    """The hex string of ETH amount."""

    destination: Required[str]
    """The hex string address of the recipient."""


class ActionContractExecution(TypedDict, total=False):
    calldata: Required[str]
    """The encoded contract method and its arguments."""

    contract_address: Required[str]
    """The target contract address in hex."""

    encoded_params: str
    """Optional - only used for display/format purposes."""

    method: str
    """Optional - only used for display/format purposes."""


Action: TypeAlias = Union[ActionEthTransfer, ActionContractExecution]


class TriggerSchedule(TypedDict, total=False):
    cron: str
    """A crontab expression representing when the task can be triggered."""

    fixed: Iterable[int]
    """A list of epoch timestamps when the task can be triggered."""

    trigger_type: Literal["TimeCondition", "ContractQueryCondition", "ExpressionCondition"]
    """The type of trigger condition."""


class TriggerContractQuery(TypedDict, total=False):
    callmsg: Required[str]
    """Encoded payload in hex format to send to the contract."""

    contract_address: Required[str]
    """Target contract address in hex format."""

    trigger_type: Literal["TimeCondition", "ContractQueryCondition", "ExpressionCondition"]
    """The type of trigger condition."""


class TriggerExpression(TypedDict, total=False):
    expression: str
    """The raw expression to be evaluated."""

    trigger_type: Literal["TimeCondition", "ContractQueryCondition", "ExpressionCondition"]
    """The type of trigger condition."""


Trigger: TypeAlias = Union[TriggerSchedule, TriggerContractQuery, TriggerExpression]
