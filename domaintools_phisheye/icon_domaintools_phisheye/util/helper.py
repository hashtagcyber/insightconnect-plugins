from domaintools.exceptions import (
    NotAuthorizedException, ServiceUnavailableException,
    BadRequestException, NotFoundException, InternalServerErrorException
)
from komand.exceptions import PluginException


class Helper:
    @staticmethod
    def make_request(action, *args, **kwargs):
        try:
            response = action(*args, **kwargs)
            return response.data()
        except BadRequestException as e:
            cause = "DomainToolsAPI: Bad Request:"
            assistance = f"code {e.code}, reason {e.code}"
        except ServiceUnavailableException as e:
            cause = "DomainToolsAPI: Service Unavailable:"
            assistance = f"code {e.code}, reason {e.code}"
        except NotAuthorizedException as e:
            cause = "DomainToolsAPI: Authorization Failed:"
            assistance = f"code {e.code}, reason {e.code}"
        except NotFoundException as e:
            cause = "DomainToolsAPI: Action Not Found:"
            assistance = f"code {e.code}, reason {e.code}"
        except InternalServerErrorException as e:
            cause = "DomainToolsAPI: Internal Server Error:"
            assistance = f"code {e.code}, reason {e.code}"

        action.logger.error(f"DomainToolsAPI: {cause} {assistance}")
        raise PluginException(cause=cause, assistance=assistance)
