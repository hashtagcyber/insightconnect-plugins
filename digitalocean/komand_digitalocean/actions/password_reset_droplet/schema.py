# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Performs a password reset on the droplet"


class Input:
    DROPLET_ID = "droplet_id"
    

class Output:
    SUCCESS = "success"
    

class PasswordResetDropletInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "droplet_id": {
      "type": "string",
      "title": "Droplet ID",
      "description": "ID of the droplet",
      "order": 1
    }
  },
  "required": [
    "droplet_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PasswordResetDropletOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Successful",
      "description": "Reset status. True if successful, false otherwise",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
