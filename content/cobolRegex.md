Title: Regex to the Rescue
Date: 2017-9-8 15:10
Category: Other
tags: cobol, regex, python

For a project at work, I had to parse archaic mainframe flat files produced with Job Control Language (JCL) and COBOL, popular programming languages from decades ago. The difficulty is that for a given record or observation, there was no set way of distinguishing different fields, with no delimiters present. The bytes were squished up next to each other, with a specific record structure determined by various COBOL Copy Books is what they are called. 

So the task was to generate a relational data structure out of these variable length records, and within each record there are various segments, each with different fields of different lengths in bytes. As you can see, this quickly got complicated. 

However we can bring regular expressions to the rescue!

![Alt Test](https://imgs.xkcd.com/comics/regular_expressions.png) 

(Source: https://imgs.xkcd.com/comics/regular_expressions.png)

So I ended up looking for strings of text that start with a certain length of bytes for a key, followed by one of various segment indicators. Then I can use simple string splicing in Python with the shema specified by each segment's COBOL Copy Book to get the individual fields. 

[Github Repo](https://github.com/claytonblythe/cobolRegex)

Until next time,
#### Clayton Blythe | *Deep Python*
