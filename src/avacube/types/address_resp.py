# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AddressResp"]


class AddressResp(BaseModel):
    nonce: Optional[str] = None
    """The current nonce of the smart wallet."""

    smart_account_address: Optional[str] = None
    """The retrieved smart wallet address for the specified owner."""
