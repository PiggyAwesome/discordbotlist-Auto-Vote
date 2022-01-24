import requests, time

auth = "" # INSERT YOU AUTH TOKEN HERE

bot_name = "dank-memer"
bot_id = 270904126974590976


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "authorization": auth,
    "content-length": "0",
    "cookie": "",
    "dnt": "1",
    "origin": "https://discordbotlist.com",
    "referer": f"https://discordbotlist.com/bots/{bot_name}/upvote",
    "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="96", "Avast Secure Browser";v="96"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36}"
    
    }

while True:
  resp = requests.post(f"https://discordbotlist.com/api/v1/bots/{bot_id}/upvote", headers=headers)

  if "message" in resp.text:
    print(f"Error: {resp.json()['message']}")
  else:
    print(f"Success: {resp.text}")
    
  print("Waiting 12 Hours")
  time.sleep(43200)
