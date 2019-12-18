import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# --
from commander.commander import Commander
from vk_bot import VkBot
# --


def write_msg(user_id, message,keyboard):
    if keyboard:
        vk.method("messages.send", {"user_id":event.user_id, "message": message, "random_id":random.randint(0,2048), "keyboard": keyboard})
    else:
        vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-ключ
token = "eba3fbbbd3b9704498ee312a5c72002ca17dfad7fca8efe5afaee007a800a2a0c912554647b48295daa01"

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

commander = Commander()
print("Server started")

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            print(f'New message from {event.user_id}', end='')

            bot = VkBot(event.user_id)
            if event.text[0] == "/":
                print(bot._get_time)
                write_msg(event.user_id, commander.do(event.text[1::]),bot.get_keyboard(event.text))
            else:
                print(str(bot._get_time))
                write_msg(event.user_id, bot.new_message(event.text),bot.get_keyboard(event.text))

            print('Text: ', event.text)
            print("-------------------")
