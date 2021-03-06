# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a new list of ports to scan in the OpenVAS server"


class Input:
    NAME = "name"
    PORT_LIST_TCP = "port_list_TCP"
    PORT_LIST_UDP = "port_list_UDP"
    

class Output:
    MESSAGE = "message"
    PORT_LIST_ID = "port_list_id"
    SUCCESS = "success"
    

class CreatePortListInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Port List Name",
      "description": "Port list name",
      "order": 1
    },
    "port_list_TCP": {
      "type": "array",
      "title": "TCP Port List",
      "description": "Target Port List for TCP ports, in the form of a JSON array for each port or list of ports. For example, the following would be a valid list: ['22', '80', '443-445']",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "port_list_UDP": {
      "type": "array",
      "title": "UDP Port List",
      "description": "Target Port List for UDP ports, in the form of a JSON array for each port or list of ports. For example, the following would be a valid list: ['53', '6881-6890']",
      "items": {
        "type": "string"
      },
      "order": 3
    }
  },
  "required": [
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreatePortListOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message",
      "order": 3
    },
    "port_list_id": {
      "type": "string",
      "title": "Port List ID",
      "description": "Port list ID's",
      "order": 1
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
