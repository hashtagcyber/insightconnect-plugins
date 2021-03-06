# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    SERVER = "server"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "server": {
      "type": "string",
      "title": "Server",
      "description": "ZeuS Tracker API Server",
      "default": "https://zeustracker.abuse.ch",
      "order": 1
    }
  },
  "required": [
    "server"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
