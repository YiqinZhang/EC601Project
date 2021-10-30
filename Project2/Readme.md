# Project2 TwitterAPI

## Run our code
Firstly, open TravelTweets.py. Replace the consumer_key, consumer_secret, access_token, access_token_secret with your own keys;

```
consumer_key ='Your API key/consumer key'
consumer_secret = 'Your secret API key/ consumer key'
access_token = 'Your access token'
access_token_secret = 'Your secret access token'
```

Run ``` $ python TravelTweets.py;```

Set up Google environment and install Google API(https://github.com/googleapis/google-api-python-client);

Wait for the process to be done. You should see a new folder named "result" created containing 25 text files titled with city names;

After the folder is successfully created, run ```$ python NLP.py;```

Finally, you will get a text file named "result.txt" containing a list of 10 cities.


## Product Mission

This project aims to get the most welcome cities in the US for a short trip by analyzing the tweets. I list cities ranked from the most positive to the least in the overall sentiment of all related text tweet content.


