from time import sleep
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
from datetime import datetime as dt

URLS = ["https://www.youtube.com/watch?v=F_CHgwCQgQ4", "https://www.youtube.com/watch?v=tO6FtUzHEME", "https://www.youtube.com/watch?v=isn2EtF5jY0"]

session = HTMLSession() 
results = [str]

def GetMostPopularURLs() -> list:
    pass

def GetDescription(url) -> str:
    startTime = dt.now()
    response = session.get(url)
    response.html.render(sleep=1)
    
    soup = bs(response.html.html, "html.parser")
    
    
    result = soup.find("meta", itemprop="description")['content']
    
    elapsedTime = (dt.now() - startTime).total_seconds()
    print("Elapsed Time: " + str(elapsedTime) + " seconds")
    
    return result
    
    
def GetTrendingVideos() -> list[str]:
    url = "https://www.youtube.com/feed/trending"
    
    response = session.get(url)
    response.html.render(sleep=1)
    
    soup = bs(response.html.html, "html.parser")
    # soup.prettify()
    
    results = soup.findAll("a", href=True)
    links = []
    for result in results:
        result = result["href"]
        if "watch" in result and links.__contains__("https://www.youtube.com" + result) == False:
            links.append("https://www.youtube.com" + result)
            
    # for x in links:
    #     print(x)
    print("Found " + str(len(links)) + " links")
    return links
    
links = GetTrendingVideos()

sponsored_videos = []
index = 0
for link in links:
    desc = GetDescription(link).lower()
    if "sponser" in desc or "sponsor" in desc:
        sponsored_videos.append(desc)
        print(desc)
        index += 1
        if index > 3:
            break
    else:
        print(desc[:50])
        
    sleep(10)

for x in sponsored_videos:
    print(x)
    
print("Sponsers found: " + str(len(sponsored_videos)))

session.close()