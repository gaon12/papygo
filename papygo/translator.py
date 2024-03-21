import urllib.request
import urllib.parse
import json

class PapagoTranslationError(Exception):
    """Custom exception for translation errors."""
    pass

class Translator:
    def __init__(self, client_id, client_secret, papago_type='naver_cloud'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = self._get_base_url(papago_type)
        
    def _get_base_url(self, papago_type):
        """Returns the base URL based on the Papago API type."""
        if papago_type == 'naver_cloud':
            return "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
        elif papago_type == 'naver_cloud_gov':
            return "https://naveropenapi.apigw.gov-ntruss.com/nmt/v1/translation"
        else:
            raise ValueError("Invalid Papago API type specified.")
            
    def translate(self, text, source, target):
        """Translates text from the source language to the target language."""
        if not text or not source or not target:
            raise ValueError("Text, source, and target languages must be provided.")
        
        enc_text = urllib.parse.quote(text)
        data = f"source={source}&target={target}&text={enc_text}"
        request = urllib.request.Request(self.base_url)
        request.add_header("X-NCP-APIGW-API-KEY-ID", self.client_id)
        request.add_header("X-NCP-APIGW-API-KEY", self.client_secret)
        
        try:
            response = urllib.request.urlopen(request, data=data.encode("utf-8"))
            rescode = response.getcode()
            if rescode == 200:
                response_body = response.read()
                return json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
            else:
                raise PapagoTranslationError(f"Error Code: {rescode}")
        except urllib.error.URLError as e:
            raise PapagoTranslationError(f"URL Error: {e.reason}")
        except urllib.error.HTTPError as e:
            raise PapagoTranslationError(f"HTTP Error: {e.code} - {e.reason}")
        except json.JSONDecodeError:
            raise PapagoTranslationError("Failed to parse response.")
