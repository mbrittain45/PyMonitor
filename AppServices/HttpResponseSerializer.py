

import pickle

from requests.models import Response

from requests.structures import CaseInsensitiveDict

from datetime import datetime


#
# HttpResponseSerializer - write a reqeusts Response to a file and read it back out when needed
#
class HttpResponseSerializer:

    # serialize to a file
    @staticmethod
    def writeResponseToFile( filePath: str, response: Response ):

        now = datetime.now()

        data = {
            'current_time': now.isoformat(),
            'status_code': response.status_code,
            'headers': response.headers,
            'content': response.content,
            'url': response.url,
            'encoding': response.encoding,
            'reason': response.reason
        }

        with open( filePath, 'wb' ) as file:
            pickle.dump( data, file )



    # read a Response serialized to a file
    @staticmethod
    def readResponseFromFile( filePath: str ) -> tuple[ Response, datetime ]:
   
        with open( filePath, 'rb') as file:
            data = pickle.load(file)

            # Create a new Response object
            reconstructed_response = Response()

            # Manually set the attributes
            datetime_string = data['current_time']
            reconstructed_response.status_code = data['status_code']
            reconstructed_response.headers = CaseInsensitiveDict(data['headers'])
            reconstructed_response._content = data['content'] # Use internal attribute
            reconstructed_response.url = data['url']
            reconstructed_response.encoding = data['encoding']
            reconstructed_response.reason = data['reason']
    
            recovered_datetime = datetime.fromisoformat(datetime_string)

            return reconstructed_response, recovered_datetime

        return None

