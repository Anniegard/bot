import bs4 as bs4
import requests
import random
import codecs

def change_time(time,change):
    str_time = [int(time[0]+time[1]),int(time[3]+time[4]),int(time[6]+time[7])]
    str_time[0]+= change
    if str_time[0]<0:
                str_time[0]+=24
    if str_time[0]>=24:
                str_time[0]-=24
    time=str(str_time[0])+':'+str(str_time[1])+':'+str(str_time[2])
    return time

def count_lines(filename, chunk_size=1<<13):
    file = codecs.open( "pred.txt", "r", "utf_8_sig" )
    return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))
class VkBot:

    def __init__(self, user_id):
        print("\nСоздан объект бота!")

        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ["ПРИВЕТ", "ВРЕМЯ", "ПОКА", 'НАСТАВЛЕНИЕ','ФРАНЦИЯ','ИСПАНИЯ','США(ЧИКАГО)','КИТАЙ','ИТАЛИЯ','МЕКСИКА','ВЕЛИКОБРИТАНИЯ','ТУРЦИЯ','ГЕРМАНИЯ','ТАИЛАНД','СПБ','УФА','НАЧАТЬ']

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    def new_message(self, message):

        # Привет
        if message.upper() == self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}!\n Чем займемся?)"

        # Время
        elif message.upper() == self._COMMANDS[1]:
            return 'Выберите город!'

        # Пока
        elif message.upper() == self._COMMANDS[2]:
            return f"Пока-пока, {self._USERNAME}!"
        
        # Предсказание
        elif message.upper() == self._COMMANDS[3]:
            return self._get_pred()
        
        elif message.upper() == self._COMMANDS[4]:
            return change_time(self._get_time(),-2)

        elif message.upper() == self._COMMANDS[5]:
            return change_time(self._get_time(),-2)

        elif message.upper() == self._COMMANDS[6]:
            return change_time(self._get_time(),-9)

        elif message.upper() == self._COMMANDS[7]:
            return change_time(self._get_time(),5)

        elif message.upper() == self._COMMANDS[8]:
            return change_time(self._get_time(),-2)

        elif message.upper() == self._COMMANDS[9]:
            return change_time(self._get_time(),-10)

        elif message.upper() == self._COMMANDS[10]:
            return change_time(self._get_time(),-3)

        elif message.upper() == self._COMMANDS[11]:
            time = self._get_time()
            return time

        elif message.upper() == self._COMMANDS[12]:
            return change_time(self._get_time(),-2)

        elif message.upper() == self._COMMANDS[13]:
            return change_time(self._get_time(),-4)

        elif message.upper() == self._COMMANDS[14]:
            time = self._get_time()
            return time

        elif message.upper() == self._COMMANDS[15]:
            return change_time(self._get_time(),2)
        
        elif message.upper() == self._COMMANDS[16]:
            return f"С чего начнём, {self._USERNAME}?"
        #Если не нашёл команду
        else:
            return "Не понимаю о чем вы..."

    def _get_time(self):
        request = requests.get("https://my-calend.ru/date-and-time-today")
        b = bs4.BeautifulSoup(request.text, "html.parser")
        time=self._clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]
        if time[1]==':':
            time='0'+time
        return time

    def _get_pred(self):
        f = codecs.open( "pred.txt", "r", "utf_8_sig" )
        st = random.randrange(1, count_lines('pred.txt'), 1)
        k = 1
        for line in f:
            k+=1
            if k == st:
                st=line
        return st

    @staticmethod
    def _clean_all_tag_from_str(string_line):

        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """

        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result

    def get_keyboard(self,message):
        if message.upper() == self._COMMANDS[0]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        # Время
        elif message.upper() == self._COMMANDS[1]:
            keyboard = open("city.json","r", encoding="utf-8").read()
            return keyboard

        # Пока
        elif message.upper() == self._COMMANDS[2]:
            return False
        
        # Предсказание
        elif message.upper() == self._COMMANDS[3]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard
        
        elif message.upper() == self._COMMANDS[4]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        elif message.upper() == self._COMMANDS[5]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        elif message.upper() == self._COMMANDS[6]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        elif message.upper() == self._COMMANDS[7]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        elif message.upper() == self._COMMANDS[8]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        elif message.upper() == self._COMMANDS[9]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        elif message.upper() == self._COMMANDS[10]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        elif message.upper() == self._COMMANDS[11]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        elif message.upper() == self._COMMANDS[12]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        elif message.upper() == self._COMMANDS[13]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        elif message.upper() == self._COMMANDS[14]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard

        elif message.upper() == self._COMMANDS[15]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard
        elif message.upper() == self._COMMANDS[16]:
            keyboard = open("start.json","r", encoding="utf-8").read()
            return keyboard
        #Если не нашёл команду
        else:
            return open("start.json","r", encoding="utf-8").read()
