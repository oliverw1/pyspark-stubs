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

# Stubs for pyspark.sql.catalog (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Callable, Dict, List, Optional
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.session import SparkSession
from pyspark.sql.types import DataType, StructType
from collections import namedtuple

Database = namedtuple("Database", "name description locationUri")

Table = namedtuple("Table", "name database description tableType isTemporary")

Column = namedtuple("Column", "name description dataType nullable isPartition isBucket")

Function = namedtuple("Function", "name description className isTemporary")

class Catalog:
    def __init__(self, sparkSession: SparkSession) -> None: ...
    def currentDatabase(self) -> str: ...
    def setCurrentDatabase(self, dbName: str) -> None: ...
    def listDatabases(self) -> List[Database]: ...
    def listTables(self, dbName: Optional[str] = ...) -> List[Table]: ...
    def listFunctions(self, dbName: Optional[str] = ...) -> List[Function]: ...
    def listColumns(
        self, tableName: str, dbName: Optional[str] = ...
    ) -> List[Column]: ...
    def createTable(
        self,
        tableName: str,
        path: Optional[str] = ...,
        source: Optional[str] = ...,
        schema: Optional[StructType] = ...,
        **options: str
    ) -> DataFrame: ...
    def dropTempView(self, viewName: str) -> None: ...
    def dropGlobalTempView(self, viewName: str) -> None: ...
    def registerFunction(
        self, name: str, f: Callable[..., Any], returnType: DataType = ...
    ) -> None: ...
    def isCached(self, tableName: str) -> bool: ...
    def cacheTable(self, tableName: str) -> None: ...
    def uncacheTable(self, tableName: str) -> None: ...
    def clearCache(self) -> None: ...
    def refreshTable(self, tableName: str) -> None: ...
    def recoverPartitions(self, tableName: str) -> None: ...
    def refreshByPath(self, path: str) -> None: ...
