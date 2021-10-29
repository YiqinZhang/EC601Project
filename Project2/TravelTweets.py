from TwitterSearch.TwitterSearch import *
import time
import os

if not os.path.exists("result"):
    os.mkdir("result")

f = open("USCities.txt", "r")
cities = f.read().splitlines()  # read all lines into cities
for city in cities:
    try:
        tso = TwitterSearchOrder()
        tso.set_keywords(["#travel", "#holiday", "#vacation"], or_operator=True)
        tso.add_keyword(city)  # add the city name as one of the search keywords
        tso.set_language("en")  # we want to see English tweets only
        tso.set_count(100)  # search for 100 pages of tweets
        tso.set_result_type("mixed")  # search for both the popular and real-time tweets
        tso.set_include_entities(False)

        ts = TwitterSearch(
            consumer_key="********************",
            consumer_secret="*****************",
            access_token="********************",
            access_token_secret="*************",
        )

        def my_callback_closure(
            current_ts_instance,
        ):  # accepts ONE argument: an instance of TwitterSearch
            queries, tweets_seen = current_ts_instance.get_statistics()
            if queries > 0 and (queries % 5) == 0:  # trigger delay every 5th query
                time.sleep(60)  # sleep for 60 seconds

        filename = city + ".txt"
        f = open("./result/" + filename, "w")
        for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):
            if "RT @" not in tweet["text"]:
                f = open("./result/" + filename, "a")
                f.writelines(["\n", tweet["text"]])
                f.close()

    except TwitterSearchException as e:
        print(e)
