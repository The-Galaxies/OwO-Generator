import time
import requests
import random
from data.cogs import start_gen

tokens = [""] # tokens (add more than one token for faster gen)
channelid = ""  # add channel id for msges to be posted
times = 0
print('''

________    ___________________ _______    ____   ____________  
\_____  \  /  _____/\_   _____/ \      \   \   \ /   /\_____  \ 
 /   |   \/   \  ___ |    __)_  /   |   \   \   Y   /  /  ____/ 
/    |    \    \_\  \|        \/    |    \   \     /  /       \ 
\_______  /\______  /_______  /\____|__  /    \___/   \_______ \\


''')


def msg(msg):
  global times
  times += 1

  for token in tokens:
    payload = {"content": msg}
    header = {"authorization": token}
    response = requests.get("https://discord.com/api/users/@me",
                            headers=header)

    if response.status_code == 200:
      data = response.json()
      account_name = f"{data['username']}#{data['discriminator']}"
    else:
      account_name = "**You have not set tokens properly**"
    url = f"https://discord.com/api/v9/channels/{channelid}/messages"
    r = requests.post(url, data=payload, headers=header)
    if r.status_code == 200:
      print(f"#{times} Sent {msg} succesfully in id {account_name}")
    else:
      print(f"Error in sending {msg} in user {account_name}")




if __name__ == "__main__":
  start_gen(tokens)
  total_time = 0
  while True:
  
     start = time.time()
  
     # Start Cooldown
     common_time = random.randint(1, 10)
     print("Common time =", common_time)
     time.sleep(common_time)
  
     # Mid Cooldown
     mid = random.randint(1, 20)
     print("Mid Time =", mid)
     print('Both of them will take =', mid + common_time)
     time.sleep(mid)
  
  
     # Execution
     msg('owo h)
   
     stop = time.time()
     time_1 = stop - start
  
     total_time += time_1
  
     print("Time =", time_1)
     print("Total time =", total_time)
     print()

     final_time = 0
     if total_time > 600:
         print('Reached the limit, Shutting Down')
         
         second_break = random.randint(3600, 7200)
         
         print("Going to break!\nBreak time is around:", second_break//60, "mins")
         time.sleep(second_break)
         final_time += total_time
         total_time = 0
         print()
  
     if final_time > 1500:
         print("Enough For today!")
         print("Total Time Taken =",  total_time)
         break
