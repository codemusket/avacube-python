# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avacube import Avacube, AsyncAvacube
from tests.utils import assert_matches_type
from avacube.types import KeyRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Avacube) -> None:
        key = client.key.retrieve(
            expired_at=0,
            owner="owner",
            signature="signature",
        )
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Avacube) -> None:
        response = client.key.with_raw_response.retrieve(
            expired_at=0,
            owner="owner",
            signature="signature",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Avacube) -> None:
        with client.key.with_streaming_response.retrieve(
            expired_at=0,
            owner="owner",
            signature="signature",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyRetrieveResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKey:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAvacube) -> None:
        key = await async_client.key.retrieve(
            expired_at=0,
            owner="owner",
            signature="signature",
        )
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAvacube) -> None:
        response = await async_client.key.with_raw_response.retrieve(
            expired_at=0,
            owner="owner",
            signature="signature",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyRetrieveResponse, key, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAvacube) -> None:
        async with async_client.key.with_streaming_response.retrieve(
            expired_at=0,
            owner="owner",
            signature="signature",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyRetrieveResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True
