

import requests
import os

usersub = input('Enter subreddit name: ')

URL = f'http://reddit.com/r/{usersub}/top.json'
params = {'t' : 'today'}
headers = {'User-Agent' : 'Test Meme Downloader'}

resp = requests.get(URL, params=params, headers=headers)

resp.raise_for_status()

resp_json = resp.json()

data = resp_json['data']

for child in data['children']:
    meme_url = child['data']['url']

    if 'jpg' not in meme_url and 'png' not in meme_url and 'gif' not in meme_url:
        print('Sorry, only direct links to pics are supported')
        continue
    else:

        meme_file_type = meme_url.split('.')
        meme_file_type.reverse()
        filename = child['data']['title'] + '.' + meme_file_type[0]

        filename = os.path.join('memes', filename)
        resp = requests.get(meme_url, stream=True)



        with open(filename, 'wb') as file:
            for chunk in resp:
                file.write(chunk)


        print(f'File {filename} downloaded!')

print(resp)