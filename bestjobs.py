import requests
from bs4 import BeautifulSoup

# User Agent -> Search it : " My User Agent "
    # Something like > ""Mozilla/5.0 (Macintosh; Intel Mac OS X 9_12_4) AppleWebKit/531.34 (KHTML, like Gecko) Chrome/80.0.4044.113 Safari/539.36"
headers_param = {"User-Agent":" Your User Agent "}

# Getting Web Page
glassdor = requests.get("https://www.glassdoor.com/List/Best-Jobs-in-America-2019-LST_KQ0,25.htm",headers=headers_param)

# Getting Content
jobs = glassdor.content

# Parsing the Content
soup = BeautifulSoup(jobs,"html.parser")

# Wanted Data From Content
                        # ("html tag"), {"class":"class name"}
all_jobs = soup.find_all("p",{"class":"h2 m-0 entryWinner pb-std pb-md-0"})

# Let's Write Data To .txt File
index = 0
with open('data.txt','w', encoding='UTF-8') as file: 
    for job_name in all_jobs:
        file.write(f"{index + 1}-{job_name.a.text}" + "\n")
        index += 1
