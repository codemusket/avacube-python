# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KeyRetrieveParams"]


class KeyRetrieveParams(TypedDict, total=False):
    expired_at: Required[int]
    """The epoch time when your key will expire."""

    owner: Required[str]
    """Your wallet address."""

    signature: Required[str]
    """Signature of the message."""
