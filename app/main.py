from twitter import Twitter
from send_email import Gmail
import keys


def main():
    while True:
        print("What do you want to do?\n"
              "1. Send the 5 biggest news articles to me in email\n"
              "2. Tweet the biggest headline\n"
              "3. Browse the headlines\n"
              "4. Quit")
        option = int(input("Please enter a number: "))

        match option:
            case 1:
                email_articles()
            case 2:
                tweet_headline()
            case 3:
                print_headlines()
            case 4:
                break
            case _:
                print("Please enter one of the options")
                continue
        print("Operation successful")


def email_articles(articles_dict, n=5):
    if len(articles_dict) < n:
        return None

    articles = []
    for h, text in articles_dict:
        articles.append(h + "\n" + text)

    email = input("Please enter your email: ")
    gmail = Gmail(keys.EMAIL_SENDER, keys.EMAIL_SENDER_PASSWORD)
    gmail.send(email, "\n\n".join(articles[0:n]))
    return 0


def tweet_headline(headline):
    twitter = Twitter()
    twitter.post(headline)
    return 0


def print_headlines(articles_dict):
    articles = []
    for h, text in articles_dict:
        articles.append("1. " + h + "\n" + text)
    print("\n\n".join(articles))


if __name__ == "__main__":
    main()
