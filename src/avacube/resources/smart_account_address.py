# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import smart_account_address_retrieve_params
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
from ..types.address_resp import AddressResp

__all__ = ["SmartAccountAddressResource", "AsyncSmartAccountAddressResource"]


class SmartAccountAddressResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SmartAccountAddressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/codemusket/avacube-python#accessing-raw-response-data-eg-headers
        """
        return SmartAccountAddressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SmartAccountAddressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/codemusket/avacube-python#with_streaming_response
        """
        return SmartAccountAddressResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressResp:
        """
        Retrieve Smart Account Address

        Args:
          owner: The hex address of the account owner whose smart wallet address is being
              requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/GetSmartAccountAddress",
            body=maybe_transform(
                {"owner": owner}, smart_account_address_retrieve_params.SmartAccountAddressRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressResp,
        )


class AsyncSmartAccountAddressResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSmartAccountAddressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/codemusket/avacube-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSmartAccountAddressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSmartAccountAddressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/codemusket/avacube-python#with_streaming_response
        """
        return AsyncSmartAccountAddressResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressResp:
        """
        Retrieve Smart Account Address

        Args:
          owner: The hex address of the account owner whose smart wallet address is being
              requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/GetSmartAccountAddress",
            body=await async_maybe_transform(
                {"owner": owner}, smart_account_address_retrieve_params.SmartAccountAddressRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressResp,
        )


class SmartAccountAddressResourceWithRawResponse:
    def __init__(self, smart_account_address: SmartAccountAddressResource) -> None:
        self._smart_account_address = smart_account_address

        self.retrieve = to_raw_response_wrapper(
            smart_account_address.retrieve,
        )


class AsyncSmartAccountAddressResourceWithRawResponse:
    def __init__(self, smart_account_address: AsyncSmartAccountAddressResource) -> None:
        self._smart_account_address = smart_account_address

        self.retrieve = async_to_raw_response_wrapper(
            smart_account_address.retrieve,
        )


class SmartAccountAddressResourceWithStreamingResponse:
    def __init__(self, smart_account_address: SmartAccountAddressResource) -> None:
        self._smart_account_address = smart_account_address

        self.retrieve = to_streamed_response_wrapper(
            smart_account_address.retrieve,
        )


class AsyncSmartAccountAddressResourceWithStreamingResponse:
    def __init__(self, smart_account_address: AsyncSmartAccountAddressResource) -> None:
        self._smart_account_address = smart_account_address

        self.retrieve = async_to_streamed_response_wrapper(
            smart_account_address.retrieve,
        )
