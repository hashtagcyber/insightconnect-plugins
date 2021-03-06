# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CREDENTIALS = "credentials"
    MAX_PAGES = "max_pages"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "API key from account e.g. YYDHZKByMaDTMmY4ZC12MmUxLTkyTTBtY2UxUzkxNjbbYWI2OMzLYjATHjABZ9x3MUhyVUEzMWF1N0E5QThDOEhsQTRrMW1GVDZWUGVaDnA9",
      "order": 1
    },
    "max_pages": {
      "type": "integer",
      "title": "Max Pages",
      "description": "Max pages returned, default 100",
      "default": 100,
      "order": 2
    }
  },
  "required": [
    "credentials"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
