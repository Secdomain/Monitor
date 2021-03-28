# Imports
import sys
import requests

# Parsing receive data
Received = sys.argv
print(Received)
fields = {'token': Received[1], 'Chat_id': Received[2], 'Autor': Received[3], 'Pull_title': Received[4], 'Link_Pull': Received[5], 'Repo_link': Received[6]}

# Clean to the repo_link
parser = fields['Repo_link']
parser = parser.split(':')
parser[0] = 'https:'
fields['Repo_link'] = ''.join(parser)

# The text to send a message on Telegram
text = f'New Pull request:\n {"=-"*25}\nAuthor: {fields["Autor"]} \nRepository name: {fields["Pull_title"]} \n{"-="*25}\nPull request link: {fields["Link_Pull"]}\n \nRepository link: {fields["Repo_link"]}'
print(text)
# Send message
link_req = f'https://api.telegram.org/bot{fields["token"]}/sendMessage?chat_id={fields["Chat_id"]}&text={text}'
requests.get(link_req)
