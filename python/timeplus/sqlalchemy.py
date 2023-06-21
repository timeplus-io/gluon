from sqlalchemy.engine import default


# the interface refer to
# https://github.com/sqlalchemy/sqlalchemy/blob/main/lib/sqlalchemy/engine/interfaces.py#L640
class TimeplusDialect(default.DefaultDialect):

    name = "timeplus"
    driver = "rest"
    scheme = "https"
    user = None
    password = None
    dialect_description = "timeplus sqlalchemy driver"
    supports_alter = False
    supports_pk_autoincrement = False
    supports_default_values = False
    supports_empty_insert = False
    supports_unicode_statements = True
    supports_unicode_binds = True
    returns_unicode_strings = True
    description_encoding = None
    supports_native_boolean = True

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
