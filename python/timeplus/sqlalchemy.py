from sqlalchemy.engine import default
from sqlalchemy import types, util

type_map = {
    "uint32": types.BigInteger,
    "int32": types.BigInteger,
    "int64": types.BigInteger,
    "int": types.BigInteger,
    "float32": types.Float,
    "float64": types.Float,
    "float": types.Float,
    "decimal(10, 2)": types.Float,
    "string": types.String,
    "bool": types.Boolean,
    "datetime64(3)": types.TIMESTAMP,
    "datetime64(3, 'UTC')": types.TIMESTAMP,
}


# the interface refer to
# https://github.com/sqlalchemy/sqlalchemy/blob/main/lib/sqlalchemy/engine/interfaces.py#L640
class TimeplusDialect(default.DefaultDialect):

    name = "timeplus"
    driver = "rest"
    scheme = "https"
    user = None
    password = None
    dialect_description = "timeplus sqlalchemy driver"
    default_schema_name = "default"
    supports_alter = False
    supports_pk_autoincrement = False
    supports_default_values = False
    supports_default_metavalue = False
    supports_empty_insert = False
    supports_unicode_statements = True
    supports_unicode_binds = True
    supports_statement_cache = True
    supports_multivalues_insert = False
    insert_executemany_returning = False
    update_executemany_returning = False
    delete_executemany_returning = False
    insert_returning = False
    update_returning = False
    update_returning_multifrom = False
    supports_sequences = False
    supports_native_enum = False
    delete_returning = False
    delete_returning_multifrom = False
    supports_identity_columns = False
    cte_follows_insert = False
    use_insertmanyvalues = False
    returns_unicode_strings = True
    supports_comments = False
    description_encoding = None
    supports_native_boolean = True
    supports_native_uuid = False
    returns_native_bytes = False

    supports_sane_rowcount = False
    supports_sane_multi_rowcount = False

    def __init__(self, context=None, *args, **kwargs):
        super(TimeplusDialect, self).__init__(*args, **kwargs)
        self.context = context or {}

    @classmethod
    def dbapi(cls):
        import timeplus

        return timeplus

    @classmethod
    def import_dbapi(cls):
        import timeplus

        return timeplus

    def create_connect_args(self, url):
        kwargs = {
            "host": url.host,
            "port": url.port or 8082,
            "user": url.username or None,
            "password": url.password or None,
            "path": url.database,
            "scheme": self.scheme,
            "context": self.context,
            "header": url.query.get("header") == "true",
        }
        return ([], kwargs)

    def do_ping(self, dbapi_connection) -> bool:
        """
        Return if the database can be reached.
        """
        try:
            dbapi_connection.execute("SELECT 1")
        except Exception:
            return False

        return True

    def do_execute(
        self,
        cursor,
        statement,
        parameters,
        context,
    ):
        return cursor.execute(statement, parameters)

    def do_close(self, dbapi_connection):
        return dbapi_connection.close()

    def get_schema_names(self, connection, **kw):
        return ["default"]

    def has_table(self, connection, table_name, schema=None):
        api_connection = connection._dbapi_connection.connection
        return api_connection._exist(table_name)

    def get_columns(self, connection, table_name, schema=None, **kwargs):
        api_connection = connection._dbapi_connection.connection
        table = api_connection._get_table(table_name)
        metadata = table.metadata()

        return [
            {
                "name": col.name,
                "type": self._map_type(col),
                "nullable": col.nullable,
                "default": col.default,
            }
            for col in metadata.columns
        ]

    def get_pk_constraint(self, connection, table_name, schema=None, **kwargs):
        return {"constrained_columns": [], "name": None}

    def get_foreign_keys(self, connection, table_name, schema=None, **kwargs):
        return []

    def get_check_constraints(self, connection, table_name, schema=None, **kwargs):
        return []

    def get_table_comment(self, connection, table_name, schema=None, **kwargs):
        return {"text": ""}

    def get_indexes(self, connection, table_name, schema=None, **kwargs):
        return []

    def get_unique_constraints(self, connection, table_name, schema=None, **kwargs):
        return []

    def get_view_definition(self, connection, view_name, schema=None, **kwargs):
        pass

    def do_rollback(self, dbapi_connection):
        pass

    def _map_type(self, col):
        if col.type in type_map:
            return type_map[col.type]
        util.warn(
            "Failed to map column {col.name} with raw type {col.type}".format(col=col)
        )
        return types.NullType
