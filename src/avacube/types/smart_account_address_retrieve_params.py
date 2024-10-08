# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SmartAccountAddressRetrieveParams"]


class SmartAccountAddressRetrieveParams(TypedDict, total=False):
    owner: Required[str]
    """
    The hex address of the account owner whose smart wallet address is being
    requested.
    """
