import urllib2
from bs4 import BeautifulSoup
import smtplib, ssl

CLASS_NAME = #fill in with the class name (ex. 'CMSC420')
SECTION_NUM = #fill in with the section number that you're interested in (ex. '0101')

SENDER_EMAIL = #fill in with sender account's email addr as a string
SENDER_PASS = #fill in with sender account's password as a string

RECIPIENT_EMAIL = #fill in with recipient's email as a string

TARGET_PAGE_URL = #search for your class on testudo.umd.edu (ex. CMSC420) and paste the url of the results page here as a string
TARGET_PAGE = urllib2.urlopen(TARGET_PAGE_URL)

#parses results page for open seats
soup = BeautifulSoup(TARGET_PAGE, 'html.parser')
open_seats_spans = soup.find_all('span', attrs={'class': 'open-seats-count'})
row_index = 0
section_id_spans = soup.find_all('span', attrs={'class': 'section-id'})
for section_id_span in section_id_spans:
    section_id = section_id_span.text.strip()
    if section_id == SECTION_NUM:
        break
    row_index += 1
open_seats = open_seats_spans[row_index].text

#if there are open seats, send email to recipient
if int(open_seats) > 0:
    server = smtplib.SMTP("smtp.gmail.com",587)
    try:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SENDER_EMAIL, SENDER_PASS)
        msg = '\nHi, there are ' + open_seats + ' seats open in ' +  CLASS_NAME + ' section ' + SECTION_NUM
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg)
    except Exception as e:
        print(e)
    server.quit()

