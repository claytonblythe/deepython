Title: Manchester United Game Reminders with Python and Raspberry Pi
Date: 2017-9-09 13:10
Category: Other
tags: raspberry pi, python, web scraping, soccer

Suprisingly, I have found that I have a lot more free time now in the real world working than I did during undergraduate study, but that might be because I was doing things like research programs and internships on top of taking seventeen credits a semester. However, now that I have this all this free time, I have started to follow sports more, specifically the English Premier League and NCAA Football. 

My favorite team in the English Premier League is Manchester United, however I couldn't be bothered to periodically check online, find their schedule, and determine when they play next. Additionally, I thought this would be a good opportunity for me to learn more about web scraping and python. So I built a simple web
scraping script to periodically parse Manchester United's upcoming schedule and text it to my iphone every couple of days. 

I have a python script called redDevilNotify.py running every two days on my Raspberry Pi which uses a Raspian Linux Distribution as the operating system. The Raspberry Pi is running 24/7 in my apartment, but it is very efficient and doesn't use much energy. 
The script uses the beautifulsoup python library to scrape the html of Manchester United's website for upcoming games, parses the html, converts the UTC dates to EST, and then it uses the Twilio API to text a reminder SMS to my iphone. 

The following crontab scheduling command is used to run the script, and you can edit this with the bash command bash:::crontab -e

0 9 \*/2 * * /usr/bin/python3 /path/to/redDevilNotify.py 

This means that the script will run on the zeroth minute of the ninth hour every two days for every week and month of the year. 

[Github Repo](https://github.com/claytonblythe/RedDevilNotify)

Until next time,
#### Clayton Blythe | *Deep Python*
