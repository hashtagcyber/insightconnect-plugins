# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Launch a new audit in OpenVAS"


class Input:
    PROFILE = "profile"
    SCHEDULE = "schedule"
    TARGET = "target"
    

class Output:
    MESSAGE = "message"
    SCAN_ID = "scan_id"
    SUCCESS = "success"
    TARGET_ID = "target_id"
    

class LaunchScanInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "profile": {
      "type": "string",
      "title": "Profile",
      "description": "Scan profile in the OpenVAS server E.g. Full and fast",
      "order": 2
    },
    "schedule": {
      "type": "string",
      "title": "Schedule",
      "description": "Schedule id to use for the scan",
      "order": 3
    },
    "target": {
      "type": "string",
      "title": "Target IP Address or ID",
      "description": "If only one IP address is to be scanned, the IP can be passed directly through this parameter. Otherwise, a target ID can be passed from the Create Target functionality",
      "order": 1
    }
  },
  "required": [
    "profile",
    "target"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LaunchScanOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message",
      "order": 4
    },
    "scan_id": {
      "type": "string",
      "title": "Scan ID",
      "description": "Scan ID E.g. 9a849831-23a0-48ba-8e8f-a3deeaa45f7e",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 1
    },
    "target_id": {
      "type": "string",
      "title": "Target ID",
      "description": "Target ID",
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
