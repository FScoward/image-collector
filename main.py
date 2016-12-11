# -*- coding: utf-8 -*-

import tweepy
import yaml
import json


def read_config():
    """Read config file"""
    with open('config.yaml') as reader:
        y = reader.read()
        r = yaml.load(y)
        return r


def initialize_client(consumerKey, consumerSecret, accessToken, accessTokenSecret):
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    return tweepy.API(auth, parser=tweepy.parsers.JSONParser())


def main():
    config = read_config()
    client = initialize_client(config["consumer_key"], config["consumer_secret"], config["access_token"], config["access_token_secret"])
    results = client.search("白石麻衣")
    for status in results["statuses"]:
        if "media" in status["entities"]:
            for media in status["entities"]["media"]:
                print(media["media_url"])

if __name__ == '__main__':
    """Twitterから画像の収集を行う"""
    main()
