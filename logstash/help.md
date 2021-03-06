# Description

[Logstash](https://www.elastic.co/products/logstash) is an open source, server-side data processing pipeline that ingests data from a multitude of sources simultaneously, transforms it, and then sends it to your favorite "stash." This plugin uses the [Logstash API](https://www.elastic.co/guide/en/logstash/current/event-api.html) to retrieve metadata about your Logstash instance.

# Key Features

* Retrieve information about your Logstash instance
* Retrieve hot threads from your Logstash instance
* Retrieve Logstash node information and statistics
* Retrieve information about plugins installed in your Logstash instance

# Requirements

* Logstash Server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Host URL, E.g. http://192.168.33.10:9600|None|

## Technical Details

### Actions

#### General Info

This action is used to retrieve general information about the Logstash instance, including the host and version.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|Response|

Example output:

```
```

#### Node Info

This action is used to retrieve information about the node.

##### Input

|Name|Type|Default|Required|Description| Enum
|----|----|--------|-----------|-------|----------------------------------------|
|types|string|None|False|Comma-separated list of types of node info to return.| ['pipeline', 'os', 'jvm']

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### Plugins

This action is used to get information about all Logstash plugins that are currently installed

#### Input

This action does not take any inputs

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### Node Stats

This action is used to retrieve runtime stats about Logstash.

##### Input

|Name|Type|Default|Required|Description| Enum
|----|----|--------|-----------|-------|--------------------------------------|
|types|string|None|False|Comma-separated list of types of node info to return.|
['pipeline', 'os', 'jvm', 'reloads', 'process']

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### Hot Threads

This action is used to get the current hot threads for Logstash. A hot thread is a Java thread that has high CPU usage and executes for a longer than normal period of time

#### Input

|Name|Type|Default|Required|Description|
|----|----|--------|-----------|-------|
|threads|integer|3|False|The number of hot threads to return|
|human|boolean|false|False|If true, returns plain text instead of JSON format.|
|ignore_idle_threads|boolean|true|False|If true, does not return idle threads|

The `human` input parameter returns raw text as response. This raw text response is mapped to the `text` key in the result node of the response object.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Logstash monitoring API](https://www.elastic.co/guide/en/logstash/current/monitoring-logstash.html).
* [Logstash](https://www.elastic.co/products/logstash)
