# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import key_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.key_retrieve_response import KeyRetrieveResponse

__all__ = ["KeyResource", "AsyncKeyResource"]


class KeyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/codemusket/avacube-python#accessing-raw-response-data-eg-headers
        """
        return KeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/codemusket/avacube-python#with_streaming_response
        """
        return KeyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        expired_at: int,
        owner: str,
        signature: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyRetrieveResponse:
        """
        Exchange for an Auth Token

        Args:
          expired_at: The epoch time when your key will expire.

          owner: Your wallet address.

          signature: Signature of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/GetKey",
            body=maybe_transform(
                {
                    "expired_at": expired_at,
                    "owner": owner,
                    "signature": signature,
                },
                key_retrieve_params.KeyRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyRetrieveResponse,
        )


class AsyncKeyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/codemusket/avacube-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/codemusket/avacube-python#with_streaming_response
        """
        return AsyncKeyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        expired_at: int,
        owner: str,
        signature: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeyRetrieveResponse:
        """
        Exchange for an Auth Token

        Args:
          expired_at: The epoch time when your key will expire.

          owner: Your wallet address.

          signature: Signature of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/GetKey",
            body=await async_maybe_transform(
                {
                    "expired_at": expired_at,
                    "owner": owner,
                    "signature": signature,
                },
                key_retrieve_params.KeyRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyRetrieveResponse,
        )


class KeyResourceWithRawResponse:
    def __init__(self, key: KeyResource) -> None:
        self._key = key

        self.retrieve = to_raw_response_wrapper(
            key.retrieve,
        )


class AsyncKeyResourceWithRawResponse:
    def __init__(self, key: AsyncKeyResource) -> None:
        self._key = key

        self.retrieve = async_to_raw_response_wrapper(
            key.retrieve,
        )


class KeyResourceWithStreamingResponse:
    def __init__(self, key: KeyResource) -> None:
        self._key = key

        self.retrieve = to_streamed_response_wrapper(
            key.retrieve,
        )


class AsyncKeyResourceWithStreamingResponse:
    def __init__(self, key: AsyncKeyResource) -> None:
        self._key = key

        self.retrieve = async_to_streamed_response_wrapper(
            key.retrieve,
        )
