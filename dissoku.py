import requests
count = 1

while True:
	r = requests.get(f"https://app.dissoku.net/api/guilds/?page={count}", headers={'content-type': 'application/json','user-agent': 'Mozilla/5.0 Chrome/109.0.0.0 Safari/537.36'}).json()
	try:
		if r["detail"]: break
	except KeyError:
		for server in r["results"]:
			print(server["invitelink"])
		count += 1
