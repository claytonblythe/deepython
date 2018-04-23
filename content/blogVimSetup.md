Title: Blogging with Vim and Pelican
Date: 2017-9-9 13:10
Category: Other
tags: vim

I have started to learn vim, and it has been a little painful to be honest. However, I have found it to be pretty liberating in that I barely need to use a mouse to do work on my laptop, especially for things like manipulating files, writing code, and even editing/building my blog. 

I am slowly learning the tricks to quickly and efficiently navigate file structures, make changes to files, and even run normal bash commands as well. It was quit intimidating at first, but I am already finding it rewarding. Now, I have even written some custom commands and scripts to integrate my blog editing and deployment process that uses Pelican, a python utility for building sites and converting markdown text files to HTML. 

I think that it is important to be able to work as quickly and efficiently as possible, and not be hampered by menial things like taking time to open files, make changes, save them, and then see how the changes impact what you are trying to build or accomplish. The goal here is to make sure that my fingers and ability to navigate file structures aren't the limiting factors for my productivity, but rather the speed at which I can think and come up with solutions or content. 

For my blog, my workflow is as follows: I type "serve" in the command line which is a bash alias for changing to the directory of my blog, running a python/pelican development server which serves a local host replica of my blog. The blog is automatically opened in google chrome at http://localhost.com:8000 for me to browse and critique, as this 8000 port is the default for pelican. In an iterm2 terminal, I launch vim with the command "v", hit the leader key "," and shortly after "f" to open a small file browser plugin, which shows at the bottom most recently used files. There I can quickly move to different posts I had been working
on and use standard vim commands. In normal mode I type the leader key ',' and then shortly after I type 'z'. This allows me to perform edits in "focus mode", a minimalistic mode for the vim text editor that I find quite useful and aesthetically pleasing. This focus mode functionality comes from a vim plugin that comes with a vimrc repository that I will link at the bottom.

One important customization I added to vim was to make the Caps Lock serve as an escape key, so I can easily revert back to normal mode without having to reach for the escape key, which can take a lot of time if you make hundreds of small edits.

So I begin making changes, and then I write the buffer of the file onto disk with the ":w" vim command, which is connected to an autocmd hook in vim within ~/vim_runtime/my_configs.vim. This configuration calls the google chrome command line utility chrome-cli. Chrome-cli waits a little under a second for Pelican to build the static html pages, and then refreshes any tabs I have open that contain the title
of my blog,"deepython.com", in the description of the tab. 

Here is the specific autocmd added to ~/.vim_runtime/my_configs.vim file: 

autocmd BufWritePost \*.md :!sleep .69 && /Users/claytonblythe/github/version_control/scripts/reloadDeepython.sh

The script reloadDeepython.sh contains the following: 

chrome-cli list tabs | grep deepython.com | cut -c 2-4 | while read -r line; do chrome-cli reload -t "$line"; done

This assumes you have chrome-cli installed, which can be installed with "pip install chrome-cli"

Using this configuration, I can get almost instant feed back about the aesthetics and content of my posts without even having to exit vim! 

It has been a pretty valuable way for me to learn about vim, python, and bash scripting, not to mention it is saving me a lot of time as well. 

Here is a photo of what my development environment looks like. Pretty slick huh? 

![Alt Test](http://deepython.com/images/blogSetup.png) 


Here are some other links used in this post: 

* [vimrc](https://github.com/amix/vimrc) github repo
* [chrome-cli](https://github.com/claytonblythe/version_control/blob/master/scripts/reloadDeepython.sh) script
* [chrome-cli](https://github.com/prasmussen/chrome-cli) github repo

I hope that you find this useful. 

Until next time,
#### Clayton Blythe | *Deep Python*
