# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Returns the job history of a specified saved search"


class Input:
    SAVED_SEARCH_NAME = "saved_search_name"
    

class Output:
    JOB_HISTORY = "job_history"
    

class GetSavedSearchJobHistoryInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "saved_search_name": {
      "type": "string",
      "title": "Saved Search Name",
      "description": "Name of a saved search",
      "order": 1
    }
  },
  "required": [
    "saved_search_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSavedSearchJobHistoryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "job_history": {
      "type": "array",
      "title": "Job History",
      "description": "Job history belonging to a saved search",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
