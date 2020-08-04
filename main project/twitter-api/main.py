import tweepy
import pandas as pd
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(debug=True)

origins = [
    "http://localhost",
    "http://localhost:8080",
	"https://adityavishnu.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# class HashTag(BaseModel):
    # hashtag: str


@app.post("/twitter/{keyword}")
async def fetch_tweets(keyword: str):
    api_key = 'FZaHjMkqbFeahslgStHhZO8J4'
    api_key_secret = 'xiEyxkWCPsUmycgHPODN6f68trh0LSvLXgdpkWc37oj785FmKU'

    access_token = '722034106825965569-fJbvpQPEGHFjn1heMmwVAz0MoqHLdZN'
    access_token_secret = 'ockPa2LtuL6tjDotHied3yQU3tPxxY1428uxYDUqJQytI'

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweets = api.search(q=keyword, lang="en", count=100)

    data_list = []

    for tweet in tweets:
        # print(tweet.text)
        data_list.append(tweet.text)
        data_to_csv = pd.DataFrame(data_list)
        data_to_csv.to_csv('tweets.csv')

    print("Tweets Saved successfully!")
    return {"message": data_list}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
