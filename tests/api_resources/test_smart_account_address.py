# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avacube import Avacube, AsyncAvacube
from tests.utils import assert_matches_type
from avacube.types import AddressResp

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSmartAccountAddress:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Avacube) -> None:
        smart_account_address = client.smart_account_address.retrieve(
            owner="owner",
        )
        assert_matches_type(AddressResp, smart_account_address, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Avacube) -> None:
        response = client.smart_account_address.with_raw_response.retrieve(
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_account_address = response.parse()
        assert_matches_type(AddressResp, smart_account_address, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Avacube) -> None:
        with client.smart_account_address.with_streaming_response.retrieve(
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_account_address = response.parse()
            assert_matches_type(AddressResp, smart_account_address, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSmartAccountAddress:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAvacube) -> None:
        smart_account_address = await async_client.smart_account_address.retrieve(
            owner="owner",
        )
        assert_matches_type(AddressResp, smart_account_address, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAvacube) -> None:
        response = await async_client.smart_account_address.with_raw_response.retrieve(
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_account_address = await response.parse()
        assert_matches_type(AddressResp, smart_account_address, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAvacube) -> None:
        async with async_client.smart_account_address.with_streaming_response.retrieve(
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_account_address = await response.parse()
            assert_matches_type(AddressResp, smart_account_address, path=["response"])

        assert cast(Any, response.is_closed) is True
