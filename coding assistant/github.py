import requests
import re,random
from tkinter import Text,Tk,END

def getCodes(query):
    query = "-".join(query.split())
    link = "https://api.github.com/search/repositories?q="+query

    response = requests.get(link)

    json = response.json()


    print(json['total_count'])

    results = json['total_count']

    chooserandom = random.choice(json['items'])

    print(chooserandom['name'])

    print(chooserandom['branches_url'])

    regexp = "\{([^{}]+)\}"

    branches =re.sub(regexp,"",chooserandom['branches_url'])

    print(branches)

    brancheslist = requests.get(branches)

    # print(brancheslist.json())

    branchurls = []

    for i in brancheslist.json():
        branchurls.append(i['commit']['url'])

    files = []

    for i in range(len(branchurls)):
        files.append(requests.get(branchurls[i]).json()['files'])

    raw_urls = []

    for i in range(len(files[0])):
        raw_urls.append(files[0][i]['raw_url'])

    print(raw_urls)

    codes = [requests.get(raw_urls[i]).text for i in range(len(raw_urls))]

    return "\n".join(codes)

if __name__ == "__main__":

    win = Tk()

    t = Text(win)
    t.pack()

    t.insert(END,getCodes("Hello world in python"))

    win.mainloop()