import os, slackclient

SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_USER_TOKEN = os.environ.get('SLACK_USER_TOKEN')

# initialize slack client
food_slack_client = slackclient.SlackClient(SLACK_BOT_TOKEN)
fsc = slackclient.SlackClient(SLACK_USER_TOKEN)

# check if everything is alright
print(SLACK_BOT_TOKEN)
print('Dayo')
is_ok = food_slack_client.api_call("users.list").get('ok')
mem = food_slack_client.api_call("users.list").get('members')
if(is_ok):
    for user in mem:
        
        usName = user.get('name')
        if (usName == 'food_bot_ish'):
            usId = user.get('id')
            print(usName, usId)
print(is_ok)

#food_slack_client.api_call("chat.postMessage", channel="food_test", text="Dayo is the best")
#food_slack_client.api_call("chat.postMessage", channel="general", text="@channel You people of Earth, I have come to solve your miserable lives and make it rain on you bitches. Thank you!")
history = fsc.api_call("groups.history", channel="GARQ9DUKF")
arr = []
for message in history['messages']:
    print(message)
    if message['username']:
        mess = message['username'] + ': ' + message.get('text')
        arr.append(mess)
    else:
        arr.append('')

print(arr)


