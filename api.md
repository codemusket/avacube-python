# SmartAccountAddress

Types:

```python
from avacube.types import AddressResp
```

Methods:

- <code title="post /GetSmartAccountAddress">client.smart_account_address.<a href="./src/avacube/resources/smart_account_address.py">retrieve</a>(\*\*<a href="src/avacube/types/smart_account_address_retrieve_params.py">params</a>) -> <a href="./src/avacube/types/address_resp.py">AddressResp</a></code>

# Tasks

Types:

```python
from avacube.types import BoolValue, TaskCreateResponse, TaskListResponse
```

Methods:

- <code title="post /CreateTask">client.tasks.<a href="./src/avacube/resources/tasks.py">create</a>(\*\*<a href="src/avacube/types/task_create_params.py">params</a>) -> <a href="./src/avacube/types/task_create_response.py">TaskCreateResponse</a></code>
- <code title="get /ListTasks">client.tasks.<a href="./src/avacube/resources/tasks.py">list</a>() -> <a href="./src/avacube/types/task_list_response.py">TaskListResponse</a></code>
- <code title="post /DeleteTask">client.tasks.<a href="./src/avacube/resources/tasks.py">delete</a>(\*\*<a href="src/avacube/types/task_delete_params.py">params</a>) -> <a href="./src/avacube/types/bool_value.py">BoolValue</a></code>
- <code title="post /CancelTask">client.tasks.<a href="./src/avacube/resources/tasks.py">cancel</a>(\*\*<a href="src/avacube/types/task_cancel_params.py">params</a>) -> <a href="./src/avacube/types/bool_value.py">BoolValue</a></code>

# Key

Types:

```python
from avacube.types import KeyRetrieveResponse
```

Methods:

- <code title="post /GetKey">client.key.<a href="./src/avacube/resources/key.py">retrieve</a>(\*\*<a href="src/avacube/types/key_retrieve_params.py">params</a>) -> <a href="./src/avacube/types/key_retrieve_response.py">KeyRetrieveResponse</a></code>
