import komand
from .schema import DiskListInput, DiskListOutput
# Custom imports below
import json
import urllib2
import urllib


class DiskList(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='disk_list',
                description='Retrieves a list of persistent disks contained within the specified zone',
                input=DiskListInput(),
                output=DiskListOutput())

    def run(self, params={}):
        try:
          server  = self.connection.server
          token   = self.connection.token

          # get path parameter
          project_id = self.connection.project_id
          zone = params.get("zone")

          # Check and add parameter in dictionnary
          data = {}
          if params.get('filter', ""):
            data["filter"] = params.get('filter')

          if params.get('maxResults', ""):
            data["maxResults"] = params.get('maxResults')

          if params.get('orderBy', ""):
            data["orderBy"] = params.get('orderBy')

          if params.get('pageToken', ""):
            data["pageToken"] = params.get('pageToken')

          # encode data
          url_values = urllib.urlencode(data)
          url = server + '/projects/'+ project_id +'/zones/'+zone+'/disks?' + url_values
          
          # Call API
          request = urllib2.Request(url, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s'%token})   
          resp = urllib2.urlopen(request)
          
          # handle decoding json
          try:
            result_dic = json.loads(resp.read())
          except ValueError as e:
            self.logger.error('Decoding JSON Errors:  %s', e)
            raise('Decoding JSON Errors')
          
          return result_dic
        # handle exception
        except urllib2.HTTPError, e:
          self.logger.error('HTTPError: %s for %s', str(e.code), url)
        except urllib2.URLError, e:
          self.logger.error('URLError: %s for %s', str(e.reason), url)
        except Exception:
          import traceback
          self.logger.error('Generic Exception: %s', traceback.format_exc())
        raise Exception('URL Request Failed')

    def test(self):
        try:
          token   = self.connection.token
          #  url test authentication
          url = "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={0}".format(token)
          
          # call request test authentication
          request = urllib2.Request(url, headers={'Content-Type': 'application/json'})   
          response = urllib2.urlopen(request)
          
        except urllib2.HTTPError, e:
          message = json.loads(e.read())
          raise Exception('%s (HTTP status: %s)' % (message, str(e.code)))

        return {'status_code': response.getcode()}
