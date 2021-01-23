# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Request used to list all logs for an account"


class Input:
    pass

class Output:
    LOGS = "logs"
    

class GetAllLogsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAllLogsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "logs": {
      "$ref": "#/definitions/logsets_info",
      "title": "Logs",
      "description": "All logs",
      "order": 1
    }
  },
  "required": [
    "logs"
  ],
  "definitions": {
    "links": {
      "type": "object",
      "title": "links",
      "properties": {
        "href": {
          "type": "string",
          "title": "HREF",
          "description": "HREF",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "REL",
          "description": "REL",
          "order": 2
        }
      }
    },
    "logsets_info": {
      "type": "object",
      "title": "logsets_info",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Links",
          "items": {
            "$ref": "#/definitions/links"
          },
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 3
        },
        "rrn": {
          "type": "string",
          "title": "RRN",
          "description": "RRN",
          "order": 4
        },
        "user_data": {
          "$ref": "#/definitions/user_data",
          "title": "User Data",
          "description": "User data",
          "order": 5
        }
      },
      "definitions": {
        "links": {
          "type": "object",
          "title": "links",
          "properties": {
            "href": {
              "type": "string",
              "title": "HREF",
              "description": "HREF",
              "order": 1
            },
            "rel": {
              "type": "string",
              "title": "REL",
              "description": "REL",
              "order": 2
            }
          }
        },
        "user_data": {
          "type": "object",
          "title": "user_data",
          "properties": {
            "platform_managed": {
              "type": "string",
              "title": "Platform Managed",
              "description": "Platform managed",
              "order": 1
            }
          }
        }
      }
    },
    "user_data": {
      "type": "object",
      "title": "user_data",
      "properties": {
        "platform_managed": {
          "type": "string",
          "title": "Platform Managed",
          "description": "Platform managed",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
