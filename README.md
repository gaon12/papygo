> You can also read this README in [English](./README_EN.md)!

# papygo
## 소개
`papygo`는 [네이버 파파고](https://papago.naver.com)를 더 쉽게 사용할 수 있도록 만든 라이브러리입니다. 네이버 공식 API 문서를 바탕으로 코드를 작성했습니다.

## 설치
`pip`로 쉽게 설치할 수 있습니다.

```
pip install papygo
```

## 사용 방법
```python
from papygo.translator import Translator

# 실제 client_id와 client_secret으로 바꿔야 합니다.
client_id = 'your_client_id'
client_secret = 'your_client_secret'
# 네이버 클라우드에서 발급받은 경우 'naver_cloud'를, 네이버 클라우드 플랫폼 공공기관용에서 발급받은 경우 'naver_cloud_gov'를 입력합니다.
papago_type = 'naver_cloud'

# 번역 인스턴스 생성
translator = Translator(client_id, client_secret, papago_type)

# text 변수에 번역을 하고 싶은 문장을 입력합니다.
text = "Hello, world!"

# 이 예제에서는 text 변수값을 영어에서 한국어로 번역합니다.
try:
    translated_text = translator.translate(text, "en", "ko")
    print("Translated Text:", translated_text)

# 오류 발생 시 오류 내용이 출력됩니다.
except Exception as e:
    print(f"An error occurred: {e}")
```

## API 키 등록
네이버 클라우드, 네이버 클라우드 공공기관용 모두 발급 방법이 다르므로, 공식 문서를 읽으시기 바랍니다.

* 네이버 클라우드: [https://guide.ncloud-docs.com/docs/papagotranslation-use-apis](https://guide.ncloud-docs.com/docs/papagotranslation-use-apis)
* 네이버 클라우드 공공기관용: [https://guide-gov.ncloud-docs.com/docs/papagotranslation-use-apis](https://guide-gov.ncloud-docs.com/docs/papagotranslation-use-apis)

## 한계점
* 네이버 개발자 센터에서 파파고 API 지원 종료로 인해 라이브러리 개발 단계에서 빠졌습니다. 파파고 API 지원 종료 안내와 관련한 자세한 내용은 [네이버 개발자 센터 공지사항 - 파파고 API 지원 종료 안내](https://developers.naver.com/notice/article/14501) 문서를 확인하세요!
* 문서 번역(Papago Doc Translation API), 웹사이트 번역(Papago Website Translation API), 언어 인식(Papago Language Detection API)은 본 라이브러리에서 지원하지 않습니다.
* Papago Text Translation 사용 시 번역 결과 화면 내 브랜드 가이드라인에 따라 반드시 Papago 저작권 표기를 해야 한다고 합니다. 자세한 내용은 [네이버 클라우드 플랫폼 - Papago Translation 저작권 표기 정책](https://guide.ncloud-docs.com/docs/naveropenapiv3-translation-copyright) 문서를 확인하시기 바랍니다.

## 기여
본 프로젝트를 지원할 수 있습니다. `issue` 등록 또는 `Pull Request(PR)`은 언제나 환영입니다!

## 라이선스
[MIT 라이선스](./LICENSE)로 배포됩니다.