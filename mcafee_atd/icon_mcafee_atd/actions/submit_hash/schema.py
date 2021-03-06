# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Check if a MD5 hash is blacklisted or whitelisted"


class Input:
    HASH = "hash"
    

class Output:
    RESULTS = "results"
    SUCCESS = "success"
    

class SubmitHashInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "MD5 Hash",
      "description": "MD5 Hash to submit",
      "order": 1
    }
  },
  "required": [
    "hash"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SubmitHashOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "object",
      "title": "Results",
      "description": "Return information about given MD5 Hash",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success status of submit Hash request",
      "order": 1
    }
  },
  "required": [
    "results",
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
