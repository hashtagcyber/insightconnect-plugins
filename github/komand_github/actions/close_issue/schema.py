# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Close issue"


class Input:
    ISSUE_NUMBER = "issue_number"
    ORGANIZATION = "organization"
    REPOSITORY = "repository"
    

class Output:
    SUCCESS = "success"
    

class CloseIssueInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "issue_number": {
      "type": "number",
      "title": "Issue Number",
      "description": "Issue number",
      "order": 1
    },
    "organization": {
      "type": "string",
      "title": "Organization",
      "description": "Organizational owner of repository",
      "order": 3
    },
    "repository": {
      "type": "string",
      "title": "Repository",
      "description": "Repository to post issue",
      "order": 2
    }
  },
  "required": [
    "issue_number",
    "repository"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CloseIssueOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Returns true if the issue was closed",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
