# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CATALOG = "catalog"
    HOST = "host"
    POLL_INTERVAL = "poll_interval"
    PORT = "port"
    SCHEMA = "schema"
    SOURCE = "source"
    USERNAME = "username"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "catalog": {
      "type": "string",
      "title": "Catalog",
      "description": "Catalog name",
      "default": "hive",
      "order": 4
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Host to connect to. Do not include http/https prefix",
      "order": 1
    },
    "poll_interval": {
      "type": "integer",
      "title": "Poll Interval",
      "description": "How often to ask the Presto REST interface for a progress update, defaults to a second",
      "default": 1,
      "order": 6
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Port",
      "default": 8080,
      "order": 2
    },
    "schema": {
      "type": "string",
      "title": "Schema",
      "description": "Database name",
      "default": "default",
      "order": 5
    },
    "source": {
      "type": "string",
      "title": "Source",
      "description": "Arbitrary identifier (shows up in the Presto monitoring page)",
      "default": "pyhive",
      "order": 7
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "Username",
      "order": 3
    }
  },
  "required": [
    "host"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
