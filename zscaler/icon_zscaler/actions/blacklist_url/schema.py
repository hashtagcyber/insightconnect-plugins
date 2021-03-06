# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Blacklist or unblacklist URLs"


class Input:
    BLACKLIST_STATE = "blacklist_state"
    URLS = "urls"
    

class Output:
    SUCCESS = "success"
    

class BlacklistUrlInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "blacklist_state": {
      "type": "boolean",
      "title": "Blacklist State",
      "description": "True to blacklist a URL, false to unblacklist a URL",
      "default": true,
      "order": 2
    },
    "urls": {
      "type": "array",
      "title": "URLs",
      "description": "A given set of one or more URLs or domains to update in the blacklist",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "urls"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class BlacklistUrlOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether or not the request succeeded",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
