import os


class Config:
    """API configurations"""

    APP_TITLE = os.environ.get("APP_TITLE", "Data Tracing")
    APP_DESCRIPTION = os.environ.get("APP_DESCRIPTION", "App to data tracing")
    VERSION = os.environ.get("VERSION", "0.0.0")
    OPENAPI_URL = os.environ.get("OPENAPI_URL", "/api/openapi.json")

    DB_URL = os.environ.get("DB_URL", "postgresql://data_tracking:data_tracking@localhost:5432/data_tracking")

    COOKIE_MAX_AGE = os.environ.get("COOKIE_MAX_AGE", 259200)  # 259200 [s] => 72 [h]
