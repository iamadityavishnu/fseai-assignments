import requests
from bs4 import BeautifulSoup
import pandas as pd
import click
import re


@click.command()
@click.option('--hashtag', '-h', help='Enter the hashtag you want to create dataset about')
def tweet_extractor(hashtag):
    url = 'https://mobile.twitter.com/hashtag/' + hashtag
    contents = requests.get(url)
    # need response status here
    soup = BeautifulSoup(contents.content, 'lxml')
    data_list = []
    for a in soup.find_all('div', attrs={'class': 'dir-ltr'}):
        cleaned_text = ''
        for i in a.text:
            if re.match("^[a-zA-Z0-9_ ,']*$", i):
                cleaned_text = ''.join([cleaned_text, i])
        data_list.append(cleaned_text)
    data_to_csv = pd.DataFrame(data_list)
    data_to_csv.to_csv('tweets.csv')
    click.echo(click.style('TWEETS SUCCESSFULLY SAVED TO TWEETS.CSV!', fg='green', bold=True))


if __name__ == '__main__':
    tweet_extractor()
