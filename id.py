import requests
from json import loads


class TelegramBot:
    def __init__(self):
        token = ' ' # Write your Token here
        self.base_url = f'http://api.telegram.org/bot{token}/'

    def start(self):
        update_id = None
        while True:
            content = self.obter_msg(update_id)
            msgs = content["result"]
            if msgs:
                for msg in msgs:
                    update_id = msg['update_id']
                    chat_id = msg['message']['from']['id']
                    self.responder('Your Chat id: ', chat_id)

    def obter_msg(self, update_id):
        link_req = f'{self.base_url}getUpdates?timeout=100'
        if update_id:
            link_req = f'{link_req}&offset={update_id + 1}'
        resp = requests.get(link_req)
        return loads(resp.content)

    def responder(self, respost, chat, par=''):
        send = f'{self.base_url}sendMessage?chat_id={chat}&text={respost}{chat}'
        requests.get(send)


bot = TelegramBot()
bot.start()
