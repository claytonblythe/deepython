Title: redditstream-cli
Date: 2017-11-05 13:10
Category: Misc 

I have wanted to learn more about the reddit.com PRAW API, so I decided to do this project over the weekend. I sometimes find myself following interesting stories or watching a soccer game and wanting to read all the new reddit comments as they come in. However, with standard reddit in a browser that would require sorting by new and refreshing the page every few seconds. 

Instead, I developed a command line tool and interface for live streaming reddit comments from any subreddit. All you have to do is sign up for the PRAW API, clone my [github repository](https://github.com/claytonblythe/redditstream-cli), make your own credentials.json file, and launch with 

`python redditstream-cli.py -s soccer`

Here are three separate sessions running in separate windows, streaming [r/politics](http://reddit.com/r/politics) [r/soccer](http://reddit.com/r/soccer) and [r/python](http://reddit.com/r/python) respectively. They will live load new comments to the subreddits as soon as they are posted. 

![Alt Test](http://deepython.com/images/redditstream-cli-screenshot.png) 

Here is an extra demo of what it looks like in action! 

[![demo](https://asciinema.org/a/JZhJWeNvq1bTI8tG4VbaYPfJS.png)](https://asciinema.org/a/JZhJWeNvq1bTI8tG4VbaYPfJS?autoplay=1) 

If you want to help out with this project or have suggestions/requests for features let me know, or feel free to help over in the [github repo](https://github.com/claytonblythe/redditstream-cli).

I eventually want to make it more interactive, to allow you to change the subreddit or filter out certain submissions. So far I would consider this the alpha version. 

Until next time,
#### Clayton Blythe | *Deep Python*
