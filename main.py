from fbchat import Client
from fbchat.models import *
import json
#import commands 
import Cmd.Chatbot as chat
import Cmd.NTR as h


class MesBot(Client):
    def onMessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        try:
            msg = str(message_object).split(', ')[15][14:-1]
            print(msg)
            if ("//video.xx.fbcdn" in msg):
                msg = msg
            else:
                msg = str(message_object).split(', ')[19][20:-1]
        except:
            try:
                msg = str(message_object.text).lower()
                print(msg)
            except:
                pass

        if (author_id != self.uid):
            if "!" in msg:
                if "hentai" in msg:
                	title = h.RandomSeries()
                	img_location = str(h.download(title))
                	if "Cmd" not in img_location:
                		self.sendMsg(img_location, thread_id, thread_type)
                	else:
                		self.sendImg(img_location, title, thread_id, thread_type)
#                		link = f"https://hentai2read.com/hentai-list/search/{title}"
#                		self.sendMsg(link, thread_id, thread_type)
		else:
			reply = chat.ChatBot(msg)
			self.sendMsg(reply, thread_id, thread_type)

    def sendMsg(self, reply, thread_id, thread_type):
        self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
        
    def sendImg(self, image_path, reply, thread_id, thread_type):
    	self.sendLocalImage(image_path, message=Message(text=reply), thread_id=thread_id, thread_type=thread_type)

try:
	with open("Cookies.json", 'r') as file:
		session_cookies = json.load(file)
#		session_cookies = {
#		"sb": "'',
#		"fr": "",
#		"c_user": "",
#		"datr":"",
#		"xs": ""
#		}
except FileNotFoundError:
	print("Please make sure there is a Cookies.json file")
	exit()
	
bot = MesBot('EMAIL', 'PASSWORD', session_cookies=session_cookies)
print(bot.isLoggedIn())

try:
    bot.listen()
except:
    bot.listen()
