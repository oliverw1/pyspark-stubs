#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from typing import Any, Optional

class ExecutorResourceRequest:
    def __init__(
        self,
        resourceName: Any,
        amount: Any,
        discoveryScript: str = ...,
        vendor: str = ...,
    ) -> None: ...
    @property
    def resourceName(self): ...
    @property
    def amount(self): ...
    @property
    def discoveryScript(self): ...
    @property
    def vendor(self): ...

class ExecutorResourceRequests:
    def __init__(
        self, _jvm: Optional[Any] = ..., _requests: Optional[Any] = ...
    ) -> None: ...
    def memory(self, amount: Any): ...
    def memoryOverhead(self, amount: Any): ...
    def pysparkMemory(self, amount: Any): ...
    def cores(self, amount: Any): ...
    def resource(
        self,
        resourceName: Any,
        amount: Any,
        discoveryScript: str = ...,
        vendor: str = ...,
    ): ...
    @property
    def requests(self): ...

class TaskResourceRequest:
    def __init__(self, resourceName: Any, amount: Any) -> None: ...
    @property
    def resourceName(self): ...
    @property
    def amount(self): ...

class TaskResourceRequests:
    def __init__(
        self, _jvm: Optional[Any] = ..., _requests: Optional[Any] = ...
    ) -> None: ...
    def cpus(self, amount: Any): ...
    def resource(self, resourceName: Any, amount: Any): ...
    @property
    def requests(self): ...
