import os
from datetime import date, datetime
import zoneinfo
import tweepy

TARGET = date(2027, 12, 10)
TZ = zoneinfo.ZoneInfo("America/Argentina/Buenos_Aires")

def days_left():
    today = datetime.now(TZ).date()
    return (TARGET - today).days

def message(d):
    if d < 0:
        return "Ya se fue Milei 🎉 #ChauMilei"
    if d == 0:
        return "¡Hoy se va Milei! 🎉 #ChauMilei"
    return f"Faltan {d} días para que se vaya Milei (salvo que pase algo antes)\n#ChauMilei"

def main():
    d = days_left()
    tweet = message(d)
    client = tweepy.Client(
        consumer_key=os.environ["X_API_KEY"],
        consumer_secret=os.environ["X_API_SECRET"],
        access_token=os.environ["X_ACCESS_TOKEN"],
        access_token_secret=os.environ["X_ACCESS_SECRET"]
    )
    client.create_tweet(text=tweet)
    print("Publicado:", tweet)

if __name__ == "__main__":
    main()
