import requests

def ChatBot(user_input):
	url = f"http://api.brainshop.ai/get?bid=179628&key=MAJ9ZidCz2flXlaJ&uid=123&msg={user_input}"
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		chat = data["cnt"]
		return chat
	elif response.status_code == 401:
		return "Change the Api"
	else:
		return f"Error: {response.status_code}"