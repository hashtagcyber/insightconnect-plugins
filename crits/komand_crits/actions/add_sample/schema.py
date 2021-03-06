# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Creates a new sample"


class Input:
    FILE = "file"
    PARAMS = "params"
    SOURCE = "source"
    TYPE = "type"
    

class Output:
    RESPONSE = "response"
    

class AddSampleInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file": {
      "$ref": "#/definitions/file",
      "title": "File",
      "description": "The actual file data",
      "order": 3
    },
    "params": {
      "type": "object",
      "title": "Parameters",
      "description": "Object containing related data or metadata",
      "order": 4
    },
    "source": {
      "type": "string",
      "title": "Source",
      "description": "Name of the source which provided this information",
      "order": 2
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Upload type",
      "enum": [
        "metadata",
        "file"
      ],
      "order": 1
    }
  },
  "required": [
    "file",
    "source",
    "type"
  ],
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddSampleOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/post_response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "post_response": {
      "type": "object",
      "title": "post_response",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "order": 1
        },
        "message": {
          "type": "string",
          "title": "Message",
          "order": 2
        },
        "return_code": {
          "type": "integer",
          "title": "Return Code",
          "description": "The return_code is usually 0 for success, 1 for failure",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The TLO type of the TLO that created or updated",
          "order": 3
        },
        "url": {
          "type": "string",
          "title": "URL",
          "order": 5
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
