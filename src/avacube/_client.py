# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import AvacubeError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import key, tasks, smart_account_address
    from .resources.key import KeyResource, AsyncKeyResource
    from .resources.tasks import TasksResource, AsyncTasksResource
    from .resources.smart_account_address import SmartAccountAddressResource, AsyncSmartAccountAddressResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Avacube",
    "AsyncAvacube",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "grpc://aggregator.avaprotocol.org:2206",
    "environment_1": "grpc://aggregator-holesky.avaprotocol.org:2206",
    "environment_2": "grpc://127.0.0.1:2206",
}


class Avacube(SyncAPIClient):
    # client options
    auth_key: str

    _environment: Literal["production", "environment_1", "environment_2"] | NotGiven

    def __init__(
        self,
        *,
        auth_key: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Avacube client instance.

        This automatically infers the `auth_key` argument from the `AUTH_KEY` environment variable if it is not provided.
        """
        if auth_key is None:
            auth_key = os.environ.get("AUTH_KEY")
        if auth_key is None:
            raise AvacubeError(
                "The auth_key client option must be set either by passing auth_key to the client or by setting the AUTH_KEY environment variable"
            )
        self.auth_key = auth_key

        self._environment = environment

        base_url_env = os.environ.get("AVACUBE_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `AVACUBE_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("AVACUBE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def smart_account_address(self) -> SmartAccountAddressResource:
        from .resources.smart_account_address import SmartAccountAddressResource

        return SmartAccountAddressResource(self)

    @cached_property
    def tasks(self) -> TasksResource:
        from .resources.tasks import TasksResource

        return TasksResource(self)

    @cached_property
    def key(self) -> KeyResource:
        from .resources.key import KeyResource

        return KeyResource(self)

    @cached_property
    def with_raw_response(self) -> AvacubeWithRawResponse:
        return AvacubeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvacubeWithStreamedResponse:
        return AvacubeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_key = self.auth_key
        return {"authkey": auth_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        auth_key: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_key=auth_key or self.auth_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncAvacube(AsyncAPIClient):
    # client options
    auth_key: str

    _environment: Literal["production", "environment_1", "environment_2"] | NotGiven

    def __init__(
        self,
        *,
        auth_key: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncAvacube client instance.

        This automatically infers the `auth_key` argument from the `AUTH_KEY` environment variable if it is not provided.
        """
        if auth_key is None:
            auth_key = os.environ.get("AUTH_KEY")
        if auth_key is None:
            raise AvacubeError(
                "The auth_key client option must be set either by passing auth_key to the client or by setting the AUTH_KEY environment variable"
            )
        self.auth_key = auth_key

        self._environment = environment

        base_url_env = os.environ.get("AVACUBE_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `AVACUBE_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("AVACUBE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def smart_account_address(self) -> AsyncSmartAccountAddressResource:
        from .resources.smart_account_address import AsyncSmartAccountAddressResource

        return AsyncSmartAccountAddressResource(self)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        from .resources.tasks import AsyncTasksResource

        return AsyncTasksResource(self)

    @cached_property
    def key(self) -> AsyncKeyResource:
        from .resources.key import AsyncKeyResource

        return AsyncKeyResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncAvacubeWithRawResponse:
        return AsyncAvacubeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvacubeWithStreamedResponse:
        return AsyncAvacubeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_key = self.auth_key
        return {"authkey": auth_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        auth_key: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_key=auth_key or self.auth_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AvacubeWithRawResponse:
    _client: Avacube

    def __init__(self, client: Avacube) -> None:
        self._client = client

    @cached_property
    def smart_account_address(self) -> smart_account_address.SmartAccountAddressResourceWithRawResponse:
        from .resources.smart_account_address import SmartAccountAddressResourceWithRawResponse

        return SmartAccountAddressResourceWithRawResponse(self._client.smart_account_address)

    @cached_property
    def tasks(self) -> tasks.TasksResourceWithRawResponse:
        from .resources.tasks import TasksResourceWithRawResponse

        return TasksResourceWithRawResponse(self._client.tasks)

    @cached_property
    def key(self) -> key.KeyResourceWithRawResponse:
        from .resources.key import KeyResourceWithRawResponse

        return KeyResourceWithRawResponse(self._client.key)


class AsyncAvacubeWithRawResponse:
    _client: AsyncAvacube

    def __init__(self, client: AsyncAvacube) -> None:
        self._client = client

    @cached_property
    def smart_account_address(self) -> smart_account_address.AsyncSmartAccountAddressResourceWithRawResponse:
        from .resources.smart_account_address import AsyncSmartAccountAddressResourceWithRawResponse

        return AsyncSmartAccountAddressResourceWithRawResponse(self._client.smart_account_address)

    @cached_property
    def tasks(self) -> tasks.AsyncTasksResourceWithRawResponse:
        from .resources.tasks import AsyncTasksResourceWithRawResponse

        return AsyncTasksResourceWithRawResponse(self._client.tasks)

    @cached_property
    def key(self) -> key.AsyncKeyResourceWithRawResponse:
        from .resources.key import AsyncKeyResourceWithRawResponse

        return AsyncKeyResourceWithRawResponse(self._client.key)


class AvacubeWithStreamedResponse:
    _client: Avacube

    def __init__(self, client: Avacube) -> None:
        self._client = client

    @cached_property
    def smart_account_address(self) -> smart_account_address.SmartAccountAddressResourceWithStreamingResponse:
        from .resources.smart_account_address import SmartAccountAddressResourceWithStreamingResponse

        return SmartAccountAddressResourceWithStreamingResponse(self._client.smart_account_address)

    @cached_property
    def tasks(self) -> tasks.TasksResourceWithStreamingResponse:
        from .resources.tasks import TasksResourceWithStreamingResponse

        return TasksResourceWithStreamingResponse(self._client.tasks)

    @cached_property
    def key(self) -> key.KeyResourceWithStreamingResponse:
        from .resources.key import KeyResourceWithStreamingResponse

        return KeyResourceWithStreamingResponse(self._client.key)


class AsyncAvacubeWithStreamedResponse:
    _client: AsyncAvacube

    def __init__(self, client: AsyncAvacube) -> None:
        self._client = client

    @cached_property
    def smart_account_address(self) -> smart_account_address.AsyncSmartAccountAddressResourceWithStreamingResponse:
        from .resources.smart_account_address import AsyncSmartAccountAddressResourceWithStreamingResponse

        return AsyncSmartAccountAddressResourceWithStreamingResponse(self._client.smart_account_address)

    @cached_property
    def tasks(self) -> tasks.AsyncTasksResourceWithStreamingResponse:
        from .resources.tasks import AsyncTasksResourceWithStreamingResponse

        return AsyncTasksResourceWithStreamingResponse(self._client.tasks)

    @cached_property
    def key(self) -> key.AsyncKeyResourceWithStreamingResponse:
        from .resources.key import AsyncKeyResourceWithStreamingResponse

        return AsyncKeyResourceWithStreamingResponse(self._client.key)


Client = Avacube

AsyncClient = AsyncAvacube
