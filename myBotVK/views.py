import random
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import vk
import dataBase

vk_api = vk.API(
    access_token="vk1.a.rM7wFZsPRGX1BcdbcQFkQX_uf-PaFELGMUMu9n7D1BLzxr30uf3Vq2Krj5lzv_7XC7p2jnYY8JAMxSfaQ6o_M3FkiNS_fKFaLz0vybV1HHS2ifgvNQdhr3hZmnbPYPZ4HCBxeLsP31yfpCNmVc099HNtSevhhRU6jNtBRmpq79IJtmsiG0V8H2heYKbRsCxrYdH5q7NNmz4tH6AGkCeM8g")


@csrf_exempt
def init(request):
    body = json.loads(request.body)
    return HttpResponse("cb0161cf")
    # ngrok http 8000


@csrf_exempt
def talk(request):
    body = json.loads(request.body)
    print(body)

    if body['type'] == 'message_new':
        data = dataBase.get_db()
        user_id = body['object']['message']['from_id']
        unknown1 = 'Я не понимаю вас'
        unknown2 = 'Напиши мне пару сообщение/ответ, если хочешь добавить новую фразу. Не забудь разделить знаком /.'

        if body['object']['message']['text'].find("/") != -1:
            asd = body['object']['message']['text'].split("/")
            dataBase.insert_db(asd[0], asd[1])
            saved = 'Я сохранил новую сообщение/ответ'
            vk_api.messages.send(user_id=user_id, message=saved,
                                 random_id=random.randint(1, 5000000000000000000000000000000000000000), v=5.103)
        else:
            for i in data:
                if i[1] == body['object']['message']['text']:
                    messages = i[2]
                    vk_api.messages.send(user_id=user_id, message=messages,
                                         random_id=random.randint(1, 5000000000000000000000000000000000000000), v=5.103)

                elif i == data[-1] and i[1] != body['object']['message']['text']:
                    vk_api.messages.send(user_id=user_id, message=unknown1,
                                         random_id=random.randint(1, 5000000000000000000000000000000000000000), v=5.103)
                    vk_api.messages.send(user_id=user_id, message=unknown2,
                                         random_id=random.randint(1, 5000000000000000000000000000000000000000), v=5.103)
                    return HttpResponse('ok')
        return HttpResponse('ok')


@csrf_exempt
def get_message(request):
    body = json.loads(request.body)
    print(body)
    if body["type"] == 'message_new':
        if "payload" in body["object"]["message"]:
            if body["object"]["message"]["payload"] == '{"command":"start"}':
                start(request)
        else:
            talk(request)
    return HttpResponse("ok")


def start(request):
    body = json.loads(request.body)
    user_id = body["object"]["message"]["from_id"]
    message = "Hello! это твое первое сообщение!"
    keyboard = {
        "one_time": True,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": '{"command":"friends"}',
                    "label": "Друзя",
                },
                "color": "primary"
            },
                {"action": {
                    "type": "text",
                    "payload": '{"command":"classmates"}',
                    "label": "Дноклассники",
                },
                    "color": "primary"
                }, {"action": {
                    "type": "text",
                    "payload": '{"command":"programmers"}',
                    "label": "Программисты",
            },
                "color": "primary"
                }
            ]
        ]
    }
    vk_api.messages.send(user_id=user_id, message=message, keyboard=json.dumps(keyboard), random_id=random.randint(1, 5000000000000000000000000000000000000000), v=5.103)
