# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Provides a list of IP network ranges with WHOIS records that match a specific query"


class Input:
    COUNTRY = "country"
    INCLUDE_TOTAL_COUNT = "include_total_count"
    IP = "ip"
    PAGE = "page"
    QUERY = "query"
    SERVER = "server"
    

class Output:
    RESPONSE = "response"
    

class ReverseIpWhoisInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "country": {
      "type": "string",
      "title": "Country",
      "description": "Limits results to IP addresses allocated to an entity with a particular country",
      "order": 3
    },
    "include_total_count": {
      "type": "boolean",
      "title": "Include Total Count",
      "description": "Returns the total number of results for a query",
      "default": false,
      "order": 5
    },
    "ip": {
      "type": "string",
      "title": "IP",
      "description": "Required for single IP result",
      "order": 1
    },
    "page": {
      "type": "string",
      "title": "Page",
      "description": "Providing the page number allows access to additional pages of data",
      "order": 6
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "A space separated list of free text query terms",
      "order": 2
    },
    "server": {
      "type": "string",
      "title": "Server",
      "description": "Limits results to ranges from a particular WHOIS server",
      "order": 4
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ReverseIpWhoisOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/reverse_ip_whois_response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "reverse_ip_whois_response": {
      "type": "object",
      "title": "reverse_ip_whois_response",
      "properties": {
        "country": {
          "type": "string",
          "title": "Country",
          "order": 1
        },
        "ip_from": {
          "type": "string",
          "title": "IP From",
          "order": 2
        },
        "ip_from_alloc": {
          "type": "string",
          "title": "IP From Alloc",
          "order": 3
        },
        "ip_to": {
          "type": "string",
          "title": "IP To",
          "order": 4
        },
        "ip_to_alloc": {
          "type": "string",
          "title": "IP To Alloc",
          "order": 5
        },
        "organization": {
          "type": "string",
          "title": "Organization",
          "order": 6
        },
        "range": {
          "type": "string",
          "title": "Range",
          "order": 7
        },
        "record_date": {
          "type": "string",
          "title": "Record Date",
          "order": 8
        },
        "record_ip": {
          "type": "string",
          "title": "Record IP",
          "order": 9
        },
        "server": {
          "type": "string",
          "title": "Server",
          "order": 10
        },
        "whois_record": {
          "type": "string",
          "title": "Whois Record",
          "order": 11
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
