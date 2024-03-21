> 한국어로 이 문서를 읽을 수 있습니다. [README.md](./README.md) 를 확인하세요!

# papygo
## Introduction
`papygo` is a library designed to make it easier to use [NAVER Papago](https://papago.naver.com). The code is based on NAVER's official API documentation.

## Installation
You can easily install it with `pip`.

```
pip install papygo
```

## How to use it
```python
from papygo.translator import Translator

# Make sure to replace client_id and client_secret with your actual client_id and client_secret.
client_id = 'your_client_id'
client_secret = 'your_client_secret'
# Enter 'naver_cloud' if it was issued by NAVER CLOUD PLATFORM, or 'naver_cloud_gov' if it was issued by NAVER CLOUD PLATFORM for Government.
papago_type = 'naver_cloud'

# Create a translation instance
translator = Translator(client_id, client_secret, papago_type)

# Enter the sentence you want to translate in the text variable.
text = "Hello, world!"

# This example translates the value of the text variable from English to Korean.
try:
    translated_text = translator.translate(text, "en", "ko")
    print("Translated Text:", translated_text)

# If an error occurs, the error is printed.
except Exception as e:
    print(f"An error occurred: {e}")
```

## Register API key
NAVER CLOUD PLATFORM and NAVER CLOUD PLATFORM for public institutions have different issuance methods, so please read the official documentation.

* NAVER CLOUD PLATFORM: [https://guide.ncloud-docs.com/docs/papagotranslation-use-apis](https://guide.ncloud-docs.com/docs/papagotranslation-use-apis)
* NAVER CLOUD PLATFORM for Government: [https://guide-gov.ncloud-docs.com/docs/papagotranslation-use-apis](https://guide-gov.ncloud-docs.com/docs/papagotranslation-use-apis)

## Limitations.
* The library has been removed from the development stage due to the end of Papago API support by NAVER DEVELOPER CENTER. For more information about the end of Papago API support, please refer to [NAVER DEVELOPER CENTER Announcement - Papago API support end](https://developers.naver.com/notice/article/14501)!
* Document translation (Papago Doc Translation API), website translation (Papago Website Translation API), and language detection (Papago Language Detection API) are not supported by this library.
* When using Papago Text Translation, Papago copyright notices must be displayed according to the brand guidelines in the translation result screen. For more information, please refer to [NAVER CLOUD PLATFORM - Papago Translation Copyright Notices Policy](https://guide.ncloud-docs.com/docs/naveropenapiv3-translation-copyright).

## Contribute
You can support this project. Registering an `issue` or submitting a `Pull Request(PR)` is always welcome!

## License
Distributed under the [MIT License] (./LICENSE).