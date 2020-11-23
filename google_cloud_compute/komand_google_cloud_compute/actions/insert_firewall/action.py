import komand
from .schema import InsertFirewallInput, InsertFirewallOutput

# Custom imports below
import json
import urllib2


class InsertFirewall(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="insert_firewall",
            description="Creates a firewall rule in the specified project using the data included in the request",
            input=InsertFirewallInput(),
            output=InsertFirewallOutput(),
        )

    def run(self, params={}):
        try:
            server = self.connection.server
            token = self.connection.token

            # add request path parameter
            project_id = self.connection.project_id

            # add request body parameter
            data = {}
            data["name"] = params.get("name", "")
            data["allowed"] = params.get("allowed", "")

            if params.get("id", ""):
                data["id"] = params.get("id", "")
            if params.get("kind", ""):
                data["kind"] = params.get("kind", "")
            if params.get("selfLink", ""):
                data["selfLink"] = params.get("selfLink", "")
            if params.get("description", ""):
                data["description"] = params.get("description", "")
            if params.get("network", ""):
                data["network"] = params.get("network", "")
            if params.get("sourceTags", ""):
                data["sourceTags"] = params.get("sourceTags", "")
            if params.get("sourceRanges", ""):
                data["sourceRanges"] = params.get("sourceRanges", "")
            if params.get("targetTags", ""):
                data["targetTags"] = params.get("targetTags", "")
            if params.get("creationTimestamp", ""):
                data["creationTimestamp"] = params.get("creationTimestamp", "")

            url = server + "/projects/{0}/global/firewalls".format(project_id)

            # new Request Request
            request = urllib2.Request(
                url,
                data=json.dumps(data),
                headers={"Content-Type": "application/json", "Authorization": "Bearer %s" % token},
            )

            # Call api and response data
            resp = urllib2.urlopen(request)

            # handle decoding json
            try:
                result_dic = json.loads(resp.read())
            except ValueError as e:
                self.logger.error("Decoding JSON Errors:  %s", e)
                raise ("Decoding JSON Errors")

            return result_dic
        # handle exception
        except urllib2.HTTPError, e:
            self.logger.error("HTTPError: %s for %s", str(e.code), url)
            message = json.loads(e.read())["error"]["message"]
            self.logger.error("HTTPError Reason: %s" % message)
            raise Exception(message)
        except urllib2.URLError, e:
            self.logger.error("URLError: %s for %s", str(e.reason), url)
        except Exception:
            import traceback

            self.logger.error("Generic Exception: %s", traceback.format_exc())
        raise Exception("URL Request Failed")

    def test(self):
        try:
            token = self.connection.token
            #  url test authentication
            url = "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={0}".format(token)

            # call request test authentication
            request = urllib2.Request(url, headers={"Content-Type": "application/json"})
            response = urllib2.urlopen(request)

        except urllib2.HTTPError, e:
            message = json.loads(e.read())
            raise Exception("%s (HTTP status: %s)" % (message, str(e.code)))

        return {"status_code": response.getcode()}
