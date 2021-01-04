# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    AUTO_REFERRALS = "auto_referrals"
    HOST = "host"
    PORT = "port"
    USE_SSL = "use_ssl"
    USERNAME_PASSWORD = "username_password"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "auto_referrals": {
      "type": "boolean",
      "title": "Auto Referrals",
      "description": "Allows the plugin to follow referrals from the specified Active Directory server to other Active Directory servers",
      "default": true,
      "order": 5
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Server Host, e.g. example.com",
      "order": 1
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Port, e.g. 389",
      "default": 389,
      "order": 2
    },
    "use_ssl": {
      "type": "boolean",
      "title": "Use SSL",
      "description": "Use SSL?",
      "order": 3
    },
    "username_password": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Username and Password",
      "description": "Username and password",
      "order": 4
    }
  },
  "required": [
    "auto_referrals",
    "host",
    "port",
    "use_ssl",
    "username_password"
  ],
  "definitions": {
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password",
          "order": 2
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with",
          "order": 1
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
