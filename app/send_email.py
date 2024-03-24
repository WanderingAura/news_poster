import smtplib, ssl

SMTP_SERVER = "smtp.gmail.com"
PORT = 587

class Gmail:
    def __init__(self, email, password) -> None:
        try:
            self.email = email
            self.context = ssl.create_default_context()
            self.server = smtplib.SMTP(host=SMTP_SERVER, port=PORT)
            self.server.ehlo() #identifies the user to the server
            self.server.starttls(context=self.context)
            self.server.ehlo()
            self.server.login(email, password)
        except Exception as e:
            print(f"Failed to log into email. Error: {e}")
        finally:
            self.server.quit()

    def send(self, receiver, text):
        try:
            self.server.sendmail(self.email, receiver, text)
        except Exception as e:
            print(f"Failed to send email. Error: {e}")

        
    def quit(self):
        self.server.quit()