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

# Stubs for pyspark.sql.group (Python 3.5)
#

from typing import overload
from typing import Any, Callable, Dict, List, Optional

from pyspark.sql._typing import LiteralType
from pyspark.sql.pandas._typing import GroupedMapPandasUserDefinedFunction
from pyspark.sql.context import SQLContext
from pyspark.sql.column import Column
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.pandas.group_ops import PandasGroupedOpsMixin
from pyspark.sql.types import *
from py4j.java_gateway import JavaObject  # type: ignore[import]

class GroupedData(PandasGroupedOpsMixin):
    sql_ctx: SQLContext
    def __init__(self, jgd: JavaObject, df: DataFrame) -> None: ...
    @overload
    def agg(self, *exprs: Column) -> DataFrame: ...
    @overload
    def agg(self, __exprs: Dict[str, str]) -> DataFrame: ...
    def count(self) -> DataFrame: ...
    def mean(self, *cols: str) -> DataFrame: ...
    def avg(self, *cols: str) -> DataFrame: ...
    def max(self, *cols: str) -> DataFrame: ...
    def min(self, *cols: str) -> DataFrame: ...
    def sum(self, *cols: str) -> DataFrame: ...
    def pivot(
        self, pivot_col: str, values: Optional[List[LiteralType]] = ...
    ) -> GroupedData: ...
