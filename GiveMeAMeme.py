'''A Useless Function'''

import requests
import webbrowser

def getmeme():
    r = requests.get("https://meme-api.herokuapp.com/gimme")
    obj = r.json()['preview']
    webbrowser.open(r.json()['preview'][len(obj)-1])

if __name__ == "__main__":
    getmeme()
