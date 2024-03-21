> You can also read this README in [English](./README_EN.md)!

# papygo
## �Ұ�
`papygo`�� [���̹� ���İ�](https://papago.naver.com)�� �� ���� ����� �� �ֵ��� ���� ���̺귯���Դϴ�. ���̹� ���� API ������ �������� �ڵ带 �ۼ��߽��ϴ�.

## ��ġ
`pip`�� ���� ��ġ�� �� �ֽ��ϴ�.

```
pip install papygo
```

## ��� ���
```python
from papygo.translator import Translator

# ���� client_id�� client_secret���� �ٲ�� �մϴ�.
client_id = 'your_client_id'
client_secret = 'your_client_secret'
# ���̹� Ŭ���忡�� �߱޹��� ��� 'naver_cloud'��, ���̹� Ŭ���� �÷��� ��������뿡�� �߱޹��� ��� 'naver_cloud_gov'�� �Է��մϴ�.
papago_type = 'naver_cloud'

# ���� �ν��Ͻ� ����
translator = Translator(client_id, client_secret, papago_type)

# text ������ ������ �ϰ� ���� ������ �Է��մϴ�.
text = "Hello, world!"

# �� ���������� text �������� ����� �ѱ���� �����մϴ�.
try:
    translated_text = translator.translate(text, "en", "ko")
    print("Translated Text:", translated_text)

# ���� �߻� �� ���� ������ ��µ˴ϴ�.
except Exception as e:
    print(f"An error occurred: {e}")
```

## API Ű ���
���̹� Ŭ����, ���̹� Ŭ���� ��������� ��� �߱� ����� �ٸ��Ƿ�, ���� ������ �����ñ� �ٶ��ϴ�.

* ���̹� Ŭ����: [https://guide.ncloud-docs.com/docs/papagotranslation-use-apis](https://guide.ncloud-docs.com/docs/papagotranslation-use-apis)
* ���̹� Ŭ���� ���������: [https://guide-gov.ncloud-docs.com/docs/papagotranslation-use-apis](https://guide-gov.ncloud-docs.com/docs/papagotranslation-use-apis)

## �Ѱ���
* ���̹� ������ ���Ϳ��� ���İ� API ���� ����� ���� ���̺귯�� ���� �ܰ迡�� �������ϴ�. ���İ� API ���� ���� �ȳ��� ������ �ڼ��� ������ [���̹� ������ ���� �������� - ���İ� API ���� ���� �ȳ�](https://developers.naver.com/notice/article/14501) ������ Ȯ���ϼ���!
* ���� ����(Papago Doc Translation API), ������Ʈ ����(Papago Website Translation API), ��� �ν�(Papago Language Detection API)�� �� ���̺귯������ �������� �ʽ��ϴ�.
* Papago Text Translation ��� �� ���� ��� ȭ�� �� �귣�� ���̵���ο� ���� �ݵ�� Papago ���۱� ǥ�⸦ �ؾ� �Ѵٰ� �մϴ�. �ڼ��� ������ [���̹� Ŭ���� �÷��� - Papago Translation ���۱� ǥ�� ��å](https://guide.ncloud-docs.com/docs/naveropenapiv3-translation-copyright) ������ Ȯ���Ͻñ� �ٶ��ϴ�.

## �⿩
�� ������Ʈ�� ������ �� �ֽ��ϴ�. `issue` ��� �Ǵ� `Pull Request(PR)`�� ������ ȯ���Դϴ�!

## ���̼���
[MIT ���̼���](./LICENSE)�� �����˴ϴ�.