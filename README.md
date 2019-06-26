# open-seats-checker
Script that checks for and emails user when a seat opens up in a class at the University of Maryland on `testudo.umd.edu`. Scrapes the class search results page to check for open seats.

The email used to send the notifications must be a Gmail.

In order to let our app interact with the sender's Gmail account, you must allow less secure apps to access that account. That is why I recommend creating a new Gmail account to send the notifications. The recipient's email can just be your everyday email account.

I recommend scheduling this script using crontab or launchd to have it run in the background of your system.

How to allow access to less secure apps: https://support.google.com/accounts/answer/6010255?hl=en
