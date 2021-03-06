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

from pyspark.serializers import (
    AutoBatchedSerializer as AutoBatchedSerializer,
    BatchedSerializer as BatchedSerializer,
    CompressedSerializer as CompressedSerializer,
    FlattenedValuesSerializer as FlattenedValuesSerializer,
    PickleSerializer as PickleSerializer,
)
from pyspark.util import fail_on_stopiteration as fail_on_stopiteration
from typing import Any, Optional

process: Any

def get_used_memory(): ...

MemoryBytesSpilled: int
DiskBytesSpilled: int

class Aggregator:
    createCombiner: Any = ...
    mergeValue: Any = ...
    mergeCombiners: Any = ...
    def __init__(
        self, createCombiner: Any, mergeValue: Any, mergeCombiners: Any
    ) -> None: ...

class SimpleAggregator(Aggregator):
    def __init__(self, combiner: Any): ...

class Merger:
    agg: Any = ...
    def __init__(self, aggregator: Any) -> None: ...
    def mergeValues(self, iterator: Any) -> None: ...
    def mergeCombiners(self, iterator: Any) -> None: ...
    def items(self) -> None: ...

class ExternalMerger(Merger):
    MAX_TOTAL_PARTITIONS: int = ...
    memory_limit: Any = ...
    serializer: Any = ...
    localdirs: Any = ...
    partitions: Any = ...
    batch: Any = ...
    scale: Any = ...
    data: Any = ...
    pdata: Any = ...
    spills: int = ...
    def __init__(
        self,
        aggregator: Any,
        memory_limit: int = ...,
        serializer: Optional[Any] = ...,
        localdirs: Optional[Any] = ...,
        scale: int = ...,
        partitions: int = ...,
        batch: int = ...,
    ) -> None: ...
    def mergeValues(self, iterator: Any) -> None: ...
    def mergeCombiners(self, iterator: Any, limit: Optional[Any] = ...) -> None: ...
    def items(self): ...

class ExternalSorter:
    memory_limit: Any = ...
    local_dirs: Any = ...
    serializer: Any = ...
    def __init__(self, memory_limit: Any, serializer: Optional[Any] = ...) -> None: ...
    def sorted(self, iterator: Any, key: Optional[Any] = ..., reverse: bool = ...): ...

class ExternalList:
    LIMIT: int = ...
    values: Any = ...
    count: Any = ...
    def __init__(self, values: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def append(self, value: Any) -> None: ...
    def __del__(self) -> None: ...

class ExternalListOfList(ExternalList):
    count: Any = ...
    def __init__(self, values: Any) -> None: ...
    def append(self, value: Any) -> None: ...
    def __iter__(self) -> Any: ...

class GroupByKey:
    iterator: Any = ...
    def __init__(self, iterator: Any) -> None: ...
    def __iter__(self) -> Any: ...

class ExternalGroupBy(ExternalMerger):
    SORT_KEY_LIMIT: int = ...
    def flattened_serializer(self): ...
