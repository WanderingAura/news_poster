from twitter import Twitter
from send_email import Gmail
import keys


def main():
    print("What do you want to do?\n"
          "1. Send the 5 biggest news articles to me in email\n"
          "2. Tweet the biggest headline\n"
          "3. Browse the headlines\n"
          "4. Quit\n")
    option = input("Please enter a number: ")

    options_dict = {"1": email_articles}


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


if __name__ == "__main__":
    main()
