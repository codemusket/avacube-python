# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["KeyRetrieveResponse"]


class KeyRetrieveResponse(BaseModel):
    key: Optional[str] = None
    """The authentication key to be used in subsequent requests."""
