Title: Manchester United Game Reminders with Python, Raspberry Pi, Beautiful Soup, and Twilio
Date: 2017-9-09 13:10
Category: Other
tags: raspberry pi, python, web scraping, soccer

Suprisingly, I have found that I have a lot more free time now in the real world working than I did during undergraduate study, but that might be because I was doing things like research programs and internships on top of classes. However, now that I have this free time, I have started to follow sports more, specifically the English Premier League and NCAA Football. 

My favorite team in the English Premier League is Manchester United, however I didn't want to have to periodically check online when they play next. So I built a simple web
scraping service with python to parse Manchester United's upcoming schedule and text it to my iphone every couple of days. 

I have the python script redDevilNotify.py running every two days on my Raspberry Pi which uses a Raspian Linux Distribution for the operating system. The Raspberry Pi is powered on 24/7 in my apartment, but it is very efficient and doesn't use much energy. 
The script uses the beautifulsoup python library to scrape Manchester United's website for upcoming games, parses them, converts the dates to EST and then uses the Twilio API to text me a reminder message. 

Crontab scheduling is used to run the script as follows, and you can edit this with the command bash:::crontab -e

0 9 \*/2 * * /usr/bin/python3 /path/to/redDevilNotify.py 

This means that the script will run on the zeroth minute of the ninth hour every two days for every week and month. 

[Github Repo](https://github.com/claytonblythe/RedDevilNotify)

Until next time,
#### Clayton Blythe | *Deep Python*
