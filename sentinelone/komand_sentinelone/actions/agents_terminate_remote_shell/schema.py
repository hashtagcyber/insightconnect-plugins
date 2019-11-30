# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "User updates about remote shell termination for an agent"


class Input:
    CHANNEL_ID = "channel_id"
    FILTER = "filter"
    

class Output:
    AFFECTED = "affected"
    

class AgentsTerminateRemoteShellInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "channel_id": {
      "type": "string",
      "title": "Channel ID",
      "description": "The channel the user is closing",
      "order": 1
    },
    "filter": {
      "type": "object",
      "title": "Filter JSON",
      "description": "Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents",
      "order": 2
    }
  },
  "required": [
    "channel_id",
    "filter"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AgentsTerminateRemoteShellOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)