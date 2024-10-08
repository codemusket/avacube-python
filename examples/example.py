#!/usr/bin/env -S rye run python

import os

from avacube import Avacube

client = Avacube(
    # This is the default and can be omitted
    auth_key=os.environ.get("AUTH_KEY"),
)
address_resp = client.smart_account_address.retrieve(
    owner="owner",
)
print(address_resp.nonce)
