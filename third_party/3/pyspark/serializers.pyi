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

basestring = str
unicode = str
xrange = range

class SpecialLengths:
    END_OF_DATA_SECTION: int = ...
    PYTHON_EXCEPTION_THROWN: int = ...
    TIMING_DATA: int = ...
    END_OF_STREAM: int = ...
    NULL: int = ...
    START_ARROW_STREAM: int = ...

class Serializer:
    def dump_stream(self, iterator: Any, stream: Any) -> None: ...
    def load_stream(self, stream: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

class FramedSerializer(Serializer):
    def __init__(self) -> None: ...
    def dump_stream(self, iterator: Any, stream: Any) -> None: ...
    def load_stream(self, stream: Any) -> None: ...
    def dumps(self, obj: Any) -> None: ...
    def loads(self, obj: Any) -> None: ...

class BatchedSerializer(Serializer):
    UNLIMITED_BATCH_SIZE: int = ...
    UNKNOWN_BATCH_SIZE: int = ...
    serializer: Any = ...
    batchSize: Any = ...
    def __init__(self, serializer: Any, batchSize: Any = ...) -> None: ...
    def dump_stream(self, iterator: Any, stream: Any) -> None: ...
    def load_stream(self, stream: Any): ...

class FlattenedValuesSerializer(BatchedSerializer):
    def __init__(self, serializer: Any, batchSize: int = ...) -> None: ...
    def load_stream(self, stream: Any): ...

class AutoBatchedSerializer(BatchedSerializer):
    bestSize: Any = ...
    def __init__(self, serializer: Any, bestSize: Any = ...) -> None: ...
    def dump_stream(self, iterator: Any, stream: Any) -> None: ...

class CartesianDeserializer(Serializer):
    key_ser: Any = ...
    val_ser: Any = ...
    def __init__(self, key_ser: Any, val_ser: Any) -> None: ...
    def load_stream(self, stream: Any): ...

class PairDeserializer(Serializer):
    key_ser: Any = ...
    val_ser: Any = ...
    def __init__(self, key_ser: Any, val_ser: Any) -> None: ...
    def load_stream(self, stream: Any): ...

class NoOpSerializer(FramedSerializer):
    def loads(self, obj: Any): ...
    def dumps(self, obj: Any): ...

class PickleSerializer(FramedSerializer):
    def dumps(self, obj: Any): ...
    def loads(self, obj: Any, encoding: str = ...): ...

class CloudPickleSerializer(PickleSerializer):
    def dumps(self, obj: Any): ...

class MarshalSerializer(FramedSerializer):
    def dumps(self, obj: Any): ...
    def loads(self, obj: Any): ...

class AutoSerializer(FramedSerializer):
    def __init__(self) -> None: ...
    def dumps(self, obj: Any): ...
    def loads(self, obj: Any): ...

class CompressedSerializer(FramedSerializer):
    serializer: Any = ...
    def __init__(self, serializer: Any) -> None: ...
    def dumps(self, obj: Any): ...
    def loads(self, obj: Any): ...

class UTF8Deserializer(Serializer):
    use_unicode: Any = ...
    def __init__(self, use_unicode: bool = ...) -> None: ...
    def loads(self, stream: Any): ...
    def load_stream(self, stream: Any) -> None: ...

class ChunkedStream:
    buffer_size: Any = ...
    buffer: Any = ...
    current_pos: int = ...
    wrapped: Any = ...
    def __init__(self, wrapped: Any, buffer_size: Any) -> None: ...
    def write(self, bytes: Any) -> None: ...
    def close(self) -> None: ...
    @property
    def closed(self): ...

def read_int(stream): ...
def write_int(value, stream): ...
