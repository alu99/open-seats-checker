#!/home/myuser/bin/python

import urllib2
from bs4 import BeautifulSoup
import smtplib, ssl

target_page_url = 'https://app.testudo.umd.edu/soc/search?courseId=CMSC420&sectionId=&termId=201908&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on'
target_page = urllib2.urlopen(target_page_url)

soup = BeautifulSoup(target_page, 'html.parser')
open_seats_spans = soup.find_all('span', attrs={'class': 'open-seats-count'})
row_index = 0
section_id_spans = soup.find_all('span', attrs={'class': 'section-id'})
for section_id_span in section_id_spans:
    section_id = section_id_span.text.strip()
    if section_id == '0101':
        break
    row_index += 1
open_seats = open_seats_spans[row_index].text

if int(open_seats) > 0:
    server = smtplib.SMTP("smtp.gmail.com",587)
    try:
        server.ehlo() # Can be omitted
        server.starttls() # Secure the connection
        server.ehlo() # Can be omitted
        server.login('filerobot99@gmail.com', 'integralwasabi')
        msg = '\nHi Andrew, there are ' + open_seats + ' seats open in CMSC420 section 0101'
        server.sendmail('filerobot99@gmail.com', ['andrew.lu99@gmail.com', 'alu12345@terpmail.umd.edu'], msg)
    except Exception as e:
        print(e)
    server.quit()

