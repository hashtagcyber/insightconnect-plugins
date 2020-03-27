# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Monitors a list of groups for user membership changes"


class Input:
    
    GROUP_IDS = "group_ids"
    INTERVAL = "interval"
    

class Output:
    
    USERS_ADDED_FROM_GROUPS = "users_added_from_groups"
    USERS_REMOVED_FROM_GROUPS = "users_removed_from_groups"
    

class UsersAddedRemovedFromGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group_ids": {
      "type": "array",
      "title": "Group ID's",
      "description": "A list of group ID's",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "interval": {
      "type": "integer",
      "title": "Interval",
      "description": "The time in seconds between checks for changes to the groups users",
      "default": 300,
      "order": 2
    }
  },
  "required": [
    "group_ids",
    "interval"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UsersAddedRemovedFromGroupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "users_added_from_groups": {
      "type": "array",
      "title": "Additions",
      "description": "Users added to a group since the last check",
      "items": {
        "$ref": "#/definitions/user_group"
      },
      "order": 1
    },
    "users_removed_from_groups": {
      "type": "array",
      "title": "Removals",
      "description": "Users removed from a group since the last check",
      "items": {
        "$ref": "#/definitions/user_group"
      },
      "order": 2
    }
  },
  "definitions": {
    "_links": {
      "type": "object",
      "title": "_links",
      "properties": {
        "changePassword": {
          "$ref": "#/definitions/changePassword",
          "title": "ChangePassword",
          "order": 1
        },
        "changeRecoveryQuestion": {
          "$ref": "#/definitions/changePassword",
          "title": "ChangeRecoveryQuestion",
          "order": 2
        },
        "deactivate": {
          "$ref": "#/definitions/changePassword",
          "title": "Deactivate",
          "order": 3
        },
        "expirePassword": {
          "$ref": "#/definitions/changePassword",
          "title": "ExpirePassword",
          "order": 4
        },
        "forgotPassword": {
          "$ref": "#/definitions/changePassword",
          "title": "ForgotPassword",
          "order": 5
        },
        "resetFactors": {
          "$ref": "#/definitions/changePassword",
          "title": "ResetFactors",
          "order": 6
        },
        "resetPassword": {
          "$ref": "#/definitions/changePassword",
          "title": "ResetPassword",
          "order": 7
        }
      },
      "definitions": {
        "changePassword": {
          "type": "object",
          "title": "changePassword",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "order": 1
            }
          }
        }
      }
    },
    "changePassword": {
      "type": "object",
      "title": "changePassword",
      "properties": {
        "href": {
          "type": "string",
          "title": "Href",
          "order": 1
        }
      }
    },
    "credentials_input": {
      "type": "object",
      "title": "credentials_input",
      "properties": {
        "password": {
          "$ref": "#/definitions/password",
          "title": "Password",
          "order": 1
        },
        "provider": {
          "$ref": "#/definitions/provider",
          "title": "Provider",
          "order": 2
        },
        "recovery_question": {
          "$ref": "#/definitions/recovery_question",
          "title": "Recovery Question",
          "order": 3
        }
      },
      "definitions": {
        "password": {
          "type": "object",
          "title": "password",
          "properties": {
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Password value e.g. tlpWENT2m",
              "order": 1
            }
          }
        },
        "provider": {
          "type": "object",
          "title": "provider",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Provider name e.g. OKTA",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Provider type e.g. OKTA",
              "order": 1
            }
          }
        },
        "recovery_question": {
          "type": "object",
          "title": "recovery_question",
          "properties": {
            "answer": {
              "type": "string",
              "title": "Answer",
              "description": "Recovery answer e.g. Annie Oakley",
              "order": 2
            },
            "question": {
              "type": "string",
              "title": "Question",
              "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
              "order": 1
            }
          }
        }
      }
    },
    "password": {
      "type": "object",
      "title": "password",
      "properties": {
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Password value e.g. tlpWENT2m",
          "order": 1
        }
      }
    },
    "profile": {
      "type": "object",
      "title": "profile",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "order": 1
        },
        "firstName": {
          "type": "string",
          "title": "FirstName",
          "order": 3
        },
        "lastName": {
          "type": "string",
          "title": "LastName",
          "order": 4
        },
        "login": {
          "type": "string",
          "title": "Login",
          "order": 5
        },
        "mobilePhone": {
          "type": "string",
          "title": "MobilePhone",
          "order": 6
        },
        "secondEmail": {
          "type": "string",
          "title": "SecondEmail",
          "order": 2
        }
      }
    },
    "provider": {
      "type": "object",
      "title": "provider",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Provider name e.g. OKTA",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Provider type e.g. OKTA",
          "order": 1
        }
      }
    },
    "recovery_question": {
      "type": "object",
      "title": "recovery_question",
      "properties": {
        "answer": {
          "type": "string",
          "title": "Answer",
          "description": "Recovery answer e.g. Annie Oakley",
          "order": 2
        },
        "question": {
          "type": "string",
          "title": "Question",
          "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
          "order": 1
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "activated": {
          "type": "string",
          "title": "Activated",
          "order": 4
        },
        "created": {
          "type": "string",
          "title": "Created",
          "order": 3
        },
        "credentials": {
          "$ref": "#/definitions/credentials_input",
          "title": "Credentials",
          "order": 10
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        },
        "lastLogin": {
          "type": "string",
          "title": "LastLogin",
          "order": 6
        },
        "lastUpdated": {
          "type": "string",
          "title": "LastUpdated",
          "order": 7
        },
        "links": {
          "$ref": "#/definitions/_links",
          "title": "Links",
          "order": 11
        },
        "passwordChanged": {
          "type": "string",
          "title": "PasswordChanged",
          "order": 8
        },
        "profile": {
          "$ref": "#/definitions/profile",
          "title": "Profile",
          "order": 9
        },
        "status": {
          "type": "string",
          "title": "Status",
          "order": 2
        },
        "statusChanged": {
          "type": "string",
          "title": "StatusChanged",
          "order": 5
        }
      },
      "definitions": {
        "_links": {
          "type": "object",
          "title": "_links",
          "properties": {
            "changePassword": {
              "$ref": "#/definitions/changePassword",
              "title": "ChangePassword",
              "order": 1
            },
            "changeRecoveryQuestion": {
              "$ref": "#/definitions/changePassword",
              "title": "ChangeRecoveryQuestion",
              "order": 2
            },
            "deactivate": {
              "$ref": "#/definitions/changePassword",
              "title": "Deactivate",
              "order": 3
            },
            "expirePassword": {
              "$ref": "#/definitions/changePassword",
              "title": "ExpirePassword",
              "order": 4
            },
            "forgotPassword": {
              "$ref": "#/definitions/changePassword",
              "title": "ForgotPassword",
              "order": 5
            },
            "resetFactors": {
              "$ref": "#/definitions/changePassword",
              "title": "ResetFactors",
              "order": 6
            },
            "resetPassword": {
              "$ref": "#/definitions/changePassword",
              "title": "ResetPassword",
              "order": 7
            }
          },
          "definitions": {
            "changePassword": {
              "type": "object",
              "title": "changePassword",
              "properties": {
                "href": {
                  "type": "string",
                  "title": "Href",
                  "order": 1
                }
              }
            }
          }
        },
        "changePassword": {
          "type": "object",
          "title": "changePassword",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "order": 1
            }
          }
        },
        "credentials_input": {
          "type": "object",
          "title": "credentials_input",
          "properties": {
            "password": {
              "$ref": "#/definitions/password",
              "title": "Password",
              "order": 1
            },
            "provider": {
              "$ref": "#/definitions/provider",
              "title": "Provider",
              "order": 2
            },
            "recovery_question": {
              "$ref": "#/definitions/recovery_question",
              "title": "Recovery Question",
              "order": 3
            }
          },
          "definitions": {
            "password": {
              "type": "object",
              "title": "password",
              "properties": {
                "value": {
                  "type": "string",
                  "title": "Value",
                  "description": "Password value e.g. tlpWENT2m",
                  "order": 1
                }
              }
            },
            "provider": {
              "type": "object",
              "title": "provider",
              "properties": {
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Provider name e.g. OKTA",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Provider type e.g. OKTA",
                  "order": 1
                }
              }
            },
            "recovery_question": {
              "type": "object",
              "title": "recovery_question",
              "properties": {
                "answer": {
                  "type": "string",
                  "title": "Answer",
                  "description": "Recovery answer e.g. Annie Oakley",
                  "order": 2
                },
                "question": {
                  "type": "string",
                  "title": "Question",
                  "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
                  "order": 1
                }
              }
            }
          }
        },
        "password": {
          "type": "object",
          "title": "password",
          "properties": {
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Password value e.g. tlpWENT2m",
              "order": 1
            }
          }
        },
        "profile": {
          "type": "object",
          "title": "profile",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "order": 1
            },
            "firstName": {
              "type": "string",
              "title": "FirstName",
              "order": 3
            },
            "lastName": {
              "type": "string",
              "title": "LastName",
              "order": 4
            },
            "login": {
              "type": "string",
              "title": "Login",
              "order": 5
            },
            "mobilePhone": {
              "type": "string",
              "title": "MobilePhone",
              "order": 6
            },
            "secondEmail": {
              "type": "string",
              "title": "SecondEmail",
              "order": 2
            }
          }
        },
        "provider": {
          "type": "object",
          "title": "provider",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Provider name e.g. OKTA",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Provider type e.g. OKTA",
              "order": 1
            }
          }
        },
        "recovery_question": {
          "type": "object",
          "title": "recovery_question",
          "properties": {
            "answer": {
              "type": "string",
              "title": "Answer",
              "description": "Recovery answer e.g. Annie Oakley",
              "order": 2
            },
            "question": {
              "type": "string",
              "title": "Question",
              "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
              "order": 1
            }
          }
        }
      }
    },
    "user_group": {
      "type": "object",
      "title": "user_group",
      "properties": {
        "group_id": {
          "type": "string",
          "title": "Group Id",
          "order": 2
        },
        "group_name": {
          "type": "string",
          "title": "Group Name",
          "order": 1
        },
        "users": {
          "type": "array",
          "title": "Users",
          "items": {
            "$ref": "#/definitions/user"
          },
          "order": 3
        }
      },
      "definitions": {
        "_links": {
          "type": "object",
          "title": "_links",
          "properties": {
            "changePassword": {
              "$ref": "#/definitions/changePassword",
              "title": "ChangePassword",
              "order": 1
            },
            "changeRecoveryQuestion": {
              "$ref": "#/definitions/changePassword",
              "title": "ChangeRecoveryQuestion",
              "order": 2
            },
            "deactivate": {
              "$ref": "#/definitions/changePassword",
              "title": "Deactivate",
              "order": 3
            },
            "expirePassword": {
              "$ref": "#/definitions/changePassword",
              "title": "ExpirePassword",
              "order": 4
            },
            "forgotPassword": {
              "$ref": "#/definitions/changePassword",
              "title": "ForgotPassword",
              "order": 5
            },
            "resetFactors": {
              "$ref": "#/definitions/changePassword",
              "title": "ResetFactors",
              "order": 6
            },
            "resetPassword": {
              "$ref": "#/definitions/changePassword",
              "title": "ResetPassword",
              "order": 7
            }
          },
          "definitions": {
            "changePassword": {
              "type": "object",
              "title": "changePassword",
              "properties": {
                "href": {
                  "type": "string",
                  "title": "Href",
                  "order": 1
                }
              }
            }
          }
        },
        "changePassword": {
          "type": "object",
          "title": "changePassword",
          "properties": {
            "href": {
              "type": "string",
              "title": "Href",
              "order": 1
            }
          }
        },
        "credentials_input": {
          "type": "object",
          "title": "credentials_input",
          "properties": {
            "password": {
              "$ref": "#/definitions/password",
              "title": "Password",
              "order": 1
            },
            "provider": {
              "$ref": "#/definitions/provider",
              "title": "Provider",
              "order": 2
            },
            "recovery_question": {
              "$ref": "#/definitions/recovery_question",
              "title": "Recovery Question",
              "order": 3
            }
          },
          "definitions": {
            "password": {
              "type": "object",
              "title": "password",
              "properties": {
                "value": {
                  "type": "string",
                  "title": "Value",
                  "description": "Password value e.g. tlpWENT2m",
                  "order": 1
                }
              }
            },
            "provider": {
              "type": "object",
              "title": "provider",
              "properties": {
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Provider name e.g. OKTA",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Provider type e.g. OKTA",
                  "order": 1
                }
              }
            },
            "recovery_question": {
              "type": "object",
              "title": "recovery_question",
              "properties": {
                "answer": {
                  "type": "string",
                  "title": "Answer",
                  "description": "Recovery answer e.g. Annie Oakley",
                  "order": 2
                },
                "question": {
                  "type": "string",
                  "title": "Question",
                  "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
                  "order": 1
                }
              }
            }
          }
        },
        "password": {
          "type": "object",
          "title": "password",
          "properties": {
            "value": {
              "type": "string",
              "title": "Value",
              "description": "Password value e.g. tlpWENT2m",
              "order": 1
            }
          }
        },
        "profile": {
          "type": "object",
          "title": "profile",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "order": 1
            },
            "firstName": {
              "type": "string",
              "title": "FirstName",
              "order": 3
            },
            "lastName": {
              "type": "string",
              "title": "LastName",
              "order": 4
            },
            "login": {
              "type": "string",
              "title": "Login",
              "order": 5
            },
            "mobilePhone": {
              "type": "string",
              "title": "MobilePhone",
              "order": 6
            },
            "secondEmail": {
              "type": "string",
              "title": "SecondEmail",
              "order": 2
            }
          }
        },
        "provider": {
          "type": "object",
          "title": "provider",
          "properties": {
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Provider name e.g. OKTA",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Provider type e.g. OKTA",
              "order": 1
            }
          }
        },
        "recovery_question": {
          "type": "object",
          "title": "recovery_question",
          "properties": {
            "answer": {
              "type": "string",
              "title": "Answer",
              "description": "Recovery answer e.g. Annie Oakley",
              "order": 2
            },
            "question": {
              "type": "string",
              "title": "Question",
              "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
              "order": 1
            }
          }
        },
        "user": {
          "type": "object",
          "title": "user",
          "properties": {
            "activated": {
              "type": "string",
              "title": "Activated",
              "order": 4
            },
            "created": {
              "type": "string",
              "title": "Created",
              "order": 3
            },
            "credentials": {
              "$ref": "#/definitions/credentials_input",
              "title": "Credentials",
              "order": 10
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "lastLogin": {
              "type": "string",
              "title": "LastLogin",
              "order": 6
            },
            "lastUpdated": {
              "type": "string",
              "title": "LastUpdated",
              "order": 7
            },
            "links": {
              "$ref": "#/definitions/_links",
              "title": "Links",
              "order": 11
            },
            "passwordChanged": {
              "type": "string",
              "title": "PasswordChanged",
              "order": 8
            },
            "profile": {
              "$ref": "#/definitions/profile",
              "title": "Profile",
              "order": 9
            },
            "status": {
              "type": "string",
              "title": "Status",
              "order": 2
            },
            "statusChanged": {
              "type": "string",
              "title": "StatusChanged",
              "order": 5
            }
          },
          "definitions": {
            "_links": {
              "type": "object",
              "title": "_links",
              "properties": {
                "changePassword": {
                  "$ref": "#/definitions/changePassword",
                  "title": "ChangePassword",
                  "order": 1
                },
                "changeRecoveryQuestion": {
                  "$ref": "#/definitions/changePassword",
                  "title": "ChangeRecoveryQuestion",
                  "order": 2
                },
                "deactivate": {
                  "$ref": "#/definitions/changePassword",
                  "title": "Deactivate",
                  "order": 3
                },
                "expirePassword": {
                  "$ref": "#/definitions/changePassword",
                  "title": "ExpirePassword",
                  "order": 4
                },
                "forgotPassword": {
                  "$ref": "#/definitions/changePassword",
                  "title": "ForgotPassword",
                  "order": 5
                },
                "resetFactors": {
                  "$ref": "#/definitions/changePassword",
                  "title": "ResetFactors",
                  "order": 6
                },
                "resetPassword": {
                  "$ref": "#/definitions/changePassword",
                  "title": "ResetPassword",
                  "order": 7
                }
              },
              "definitions": {
                "changePassword": {
                  "type": "object",
                  "title": "changePassword",
                  "properties": {
                    "href": {
                      "type": "string",
                      "title": "Href",
                      "order": 1
                    }
                  }
                }
              }
            },
            "changePassword": {
              "type": "object",
              "title": "changePassword",
              "properties": {
                "href": {
                  "type": "string",
                  "title": "Href",
                  "order": 1
                }
              }
            },
            "credentials_input": {
              "type": "object",
              "title": "credentials_input",
              "properties": {
                "password": {
                  "$ref": "#/definitions/password",
                  "title": "Password",
                  "order": 1
                },
                "provider": {
                  "$ref": "#/definitions/provider",
                  "title": "Provider",
                  "order": 2
                },
                "recovery_question": {
                  "$ref": "#/definitions/recovery_question",
                  "title": "Recovery Question",
                  "order": 3
                }
              },
              "definitions": {
                "password": {
                  "type": "object",
                  "title": "password",
                  "properties": {
                    "value": {
                      "type": "string",
                      "title": "Value",
                      "description": "Password value e.g. tlpWENT2m",
                      "order": 1
                    }
                  }
                },
                "provider": {
                  "type": "object",
                  "title": "provider",
                  "properties": {
                    "name": {
                      "type": "string",
                      "title": "Name",
                      "description": "Provider name e.g. OKTA",
                      "order": 2
                    },
                    "type": {
                      "type": "string",
                      "title": "Type",
                      "description": "Provider type e.g. OKTA",
                      "order": 1
                    }
                  }
                },
                "recovery_question": {
                  "type": "object",
                  "title": "recovery_question",
                  "properties": {
                    "answer": {
                      "type": "string",
                      "title": "Answer",
                      "description": "Recovery answer e.g. Annie Oakley",
                      "order": 2
                    },
                    "question": {
                      "type": "string",
                      "title": "Question",
                      "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
                      "order": 1
                    }
                  }
                }
              }
            },
            "password": {
              "type": "object",
              "title": "password",
              "properties": {
                "value": {
                  "type": "string",
                  "title": "Value",
                  "description": "Password value e.g. tlpWENT2m",
                  "order": 1
                }
              }
            },
            "profile": {
              "type": "object",
              "title": "profile",
              "properties": {
                "email": {
                  "type": "string",
                  "title": "Email",
                  "order": 1
                },
                "firstName": {
                  "type": "string",
                  "title": "FirstName",
                  "order": 3
                },
                "lastName": {
                  "type": "string",
                  "title": "LastName",
                  "order": 4
                },
                "login": {
                  "type": "string",
                  "title": "Login",
                  "order": 5
                },
                "mobilePhone": {
                  "type": "string",
                  "title": "MobilePhone",
                  "order": 6
                },
                "secondEmail": {
                  "type": "string",
                  "title": "SecondEmail",
                  "order": 2
                }
              }
            },
            "provider": {
              "type": "object",
              "title": "provider",
              "properties": {
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Provider name e.g. OKTA",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Provider type e.g. OKTA",
                  "order": 1
                }
              }
            },
            "recovery_question": {
              "type": "object",
              "title": "recovery_question",
              "properties": {
                "answer": {
                  "type": "string",
                  "title": "Answer",
                  "description": "Recovery answer e.g. Annie Oakley",
                  "order": 2
                },
                "question": {
                  "type": "string",
                  "title": "Question",
                  "description": "Recovery question e.g. Who's a major player in the cowboy scene?",
                  "order": 1
                }
              }
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
