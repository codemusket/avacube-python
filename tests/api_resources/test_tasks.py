# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from avacube import Avacube, AsyncAvacube
from tests.utils import assert_matches_type
from avacube.types import (
    BoolValue,
    TaskListResponse,
    TaskCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Avacube) -> None:
        task = client.tasks.create(
            action={
                "amount": "amount",
                "destination": "destination",
            },
            task_type="ETHTransferTask",
            trigger={},
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Avacube) -> None:
        task = client.tasks.create(
            action={
                "amount": "amount",
                "destination": "destination",
            },
            task_type="ETHTransferTask",
            trigger={
                "cron": "cron",
                "fixed": [0, 0, 0],
                "trigger_type": "TimeCondition",
            },
            expired_at=0,
            memo="memo",
            start_at=0,
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Avacube) -> None:
        response = client.tasks.with_raw_response.create(
            action={
                "amount": "amount",
                "destination": "destination",
            },
            task_type="ETHTransferTask",
            trigger={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Avacube) -> None:
        with client.tasks.with_streaming_response.create(
            action={
                "amount": "amount",
                "destination": "destination",
            },
            task_type="ETHTransferTask",
            trigger={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Avacube) -> None:
        task = client.tasks.list()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Avacube) -> None:
        response = client.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Avacube) -> None:
        with client.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Avacube) -> None:
        task = client.tasks.delete(
            id="id",
        )
        assert_matches_type(BoolValue, task, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Avacube) -> None:
        response = client.tasks.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(BoolValue, task, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Avacube) -> None:
        with client.tasks.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(BoolValue, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Avacube) -> None:
        task = client.tasks.cancel(
            id="id",
        )
        assert_matches_type(BoolValue, task, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Avacube) -> None:
        response = client.tasks.with_raw_response.cancel(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(BoolValue, task, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Avacube) -> None:
        with client.tasks.with_streaming_response.cancel(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(BoolValue, task, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncAvacube) -> None:
        task = await async_client.tasks.create(
            action={
                "amount": "amount",
                "destination": "destination",
            },
            task_type="ETHTransferTask",
            trigger={},
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAvacube) -> None:
        task = await async_client.tasks.create(
            action={
                "amount": "amount",
                "destination": "destination",
            },
            task_type="ETHTransferTask",
            trigger={
                "cron": "cron",
                "fixed": [0, 0, 0],
                "trigger_type": "TimeCondition",
            },
            expired_at=0,
            memo="memo",
            start_at=0,
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAvacube) -> None:
        response = await async_client.tasks.with_raw_response.create(
            action={
                "amount": "amount",
                "destination": "destination",
            },
            task_type="ETHTransferTask",
            trigger={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAvacube) -> None:
        async with async_client.tasks.with_streaming_response.create(
            action={
                "amount": "amount",
                "destination": "destination",
            },
            task_type="ETHTransferTask",
            trigger={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncAvacube) -> None:
        task = await async_client.tasks.list()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAvacube) -> None:
        response = await async_client.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAvacube) -> None:
        async with async_client.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncAvacube) -> None:
        task = await async_client.tasks.delete(
            id="id",
        )
        assert_matches_type(BoolValue, task, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAvacube) -> None:
        response = await async_client.tasks.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(BoolValue, task, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAvacube) -> None:
        async with async_client.tasks.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(BoolValue, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncAvacube) -> None:
        task = await async_client.tasks.cancel(
            id="id",
        )
        assert_matches_type(BoolValue, task, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncAvacube) -> None:
        response = await async_client.tasks.with_raw_response.cancel(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(BoolValue, task, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncAvacube) -> None:
        async with async_client.tasks.with_streaming_response.cancel(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(BoolValue, task, path=["response"])

        assert cast(Any, response.is_closed) is True
