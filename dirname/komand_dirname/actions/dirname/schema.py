# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get the directory name of a path"


class Input:
    PATH = "path"
    

class Output:
    DIRNAME = "dirname"
    

class DirnameInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "path": {
      "type": "string",
      "title": "Path",
      "description": "URL or file path",
      "order": 1
    }
  },
  "required": [
    "path"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DirnameOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "dirname": {
      "type": "string",
      "title": "Dirname",
      "description": "Directory name of a path",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
