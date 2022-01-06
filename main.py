import random
import smtplib
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()
month = now.month
my_email = 'python.chinwe@gmail.com'
pwd = 'pyt@#chinwe'


if weekday == 3 and month == 1:
    with open("quotes.txt") as quote_file:
        quote_list = quote_file.readlines()
        quote = random.choice(quote_list)
        quote_only = quote[0:quote.find('-')]
        quote_author = quote[quote.find('-'):len(quote) - 1]

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as connection:
        connection.starttls()
        connection.login(my_email, pwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='chinwej.obiageri@gmail.com',
            msg=f"Subject:Motivational Quote"
                f"\n\n{quote_only}\n\n{quote_author}"
        )