Title: Asynchronously Scraping deepython.com
Date: 2017-10-26 13:10
Category: Misc 

I wanted to learn more about how to do asynchronous web scraping in python3 using the asyncio and aiohttp libraries. Let's assume I have a large number of urls that I want to scrape, and they are all contained in a list, say 10,000 elements long. In synchronous scraping, the client running the python script will send a requst to url of the server hosting the html content, wait for a response containing this html content, proceed to the next url, send another request and so on. 

In contrast, asynchronous scraping with the asyncio and aiohttp libraries will create a queue of scraping tasks, and while a particular task is waiting for the web content to arrive from the server, it will go ahead and request content from other web pages while waiting. This allows for making requests and receiving content concurrently instead of in a sequential fashion, enabling a large number of web requests to be completed in a short time. 

In [this github repo](https://github.com/claytonblythe/async_examples/blob/master/notebooks/deepython_requests.ipynb) I show that scraping the html content from the home page of my website [deepython.com](http://deepython.com) (served from my raspberry pi) 10,000 times only takes about twenty seconds, compared to several minutes in the sequential example. 

This difference would only be exacerbated if you have urls and web servers that take a wide range of time to respond. So here this can give speedups for web scraping of 10x or 100x+ if you are lucky! I think that there are some interesting applications for this, doing large scale scraping of websites. 

Next it is useful to use some type of proxies and random user agents, to make it more difficult for websites to tell that you are sending an unnatural number of requests. 


Until next time,
#### Clayton Blythe | *Deep Python*
