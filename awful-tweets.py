import twint
import pandas

if __name__ == "__main__":

    users = ["doncicthegoat", "bussydouche"]
    tweet_files = ["dump/" + user + ".csv" for user in users]

    for index, user in enumerate(users):
        config = twint.Config()
        config.Username = user
        config.Since = "2020-04-12 00:00:00"
        config.Store_csv = True
        config.Custom["tweet"] = ["tweet"]
        config.Output = tweet_files[index]
        twint.run.Search(config)

    combined_tweets = pandas.concat([pandas.read_csv(f) for f in tweet_files])
    combined_tweets.to_csv("tweets", index=False)


