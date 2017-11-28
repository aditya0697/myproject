import tweepy
import json
from tweepy.parsers import JSONParser
from flask import request
from flask import Flask
app = Flask(__name__)


class ResultData:
    rdCount = 0
    def __init__(self, text, user_id, user_name, user_screen_name, retweet_count, user_profile_image ):
        self.text = text
        self.user_id = user_id
        self.user_name = user_name
        self.user_screen_name = user_screen_name
        self.retweet_count = retweet_count
        self.user_profile_image = user_profile_image
        ResultData.rdCount += 1

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    
    
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

@app.route('/')
def hello_world():
    return('Adityaa')


@app.route('/search', methods=['GET', 'POST'])
def search():

    query = request.args.get('q','#redburns')
    search_number = 10
    search_result = api.search(query, rpp=search_number)
    result = []
    ii = 0
    for i in search_result:

        result.append(ResultData(i.text, i.user.id, i.user.name, i.user.screen_name, i.retweet_count, i.user.profile_image_url_https).__dict__ )
    print(result)
    result_json = json.dumps(result)
    return(result_json)

if __name__ == '__main__':
   app.run()
