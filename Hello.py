import tweepy
import json
from tweepy.parsers import JSONParser
from flask import Flask
from flask import request
app = Flask(__name__)

consumer_key = 'xxx'
consumer_secret = 'xxx'

access_token = 'xxx'
access_token_secret = 'xxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

@app.route('/hello')
def hello_world():
    return('Adityaa')


@app.route('/search', methods=['GET', 'POST'])
def search():
    search_text = "#porn"
    query = request.args.get('q','#redburns')
    search_number = 10
    search_result = api.search(query, rpp=search_number)
    result = []
    for i in search_result:
        result.append(i.text)
        print i.text
    result_json = json.dumps(result)
    return(result_json)

if __name__ == '__main__':
   app.run()
