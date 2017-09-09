Title: Blogging with Vim and Pelican
Date: 2017-9-9 13:10
Category: Misc 

I have started to learn vim, it is a little painful process, but I have found it to be pretty liberating that I can barely need to use a mouse at all to do work on my laptop, manipulating files, writing code, and even editing/building my blog. 

I am slowly learning the tricks to quickly and efficiently navigate file structures, make changes to files, and even run normal bash commands as well. It has beeen a bit intimidating at first, but I am already finding it rewarding. I have written some custom commands and scripts to integrate it with my blog editing and building process with Pelican, a python utility for writing blogs in markdown format and converting to HTML. 

My workflow is as follows: I type "serve" in the command line which is a bash alias for changing to the directory of my blog and running a pelican development server which serves as a local host for my blog which is automatically opened in google chrome at http://localhost.com:8000. I then launch vim with the command "v", hit the leader key "," + "f" to open a small file browser on the bottom to show my most recently used files. There I can quickly move to different posts I had been working
on and enter view/edit mode in vim. Then, in normal mode in vim, I prefer to edit in "focus mode" which comes from a vim plugin that I will link at the bottom. I begin making changes, and can write the buffer of the file onto disk with the ":w" command, which is connected to an autocmd hook in vim to use the google chrome command line utility chrome-cli. Chrome-cli waits a little under a second for the static html pages to be built, then reloads any tabs I have open that have the title
of my blog "deepython.com" in the description of the tab. 

I use this autocmd added to ~/.vim_runtime/my_configs.vim file: 

autocmd BufWritePost \*.md :!sleep .69 && /Users/claytonblythe/github/version_control/scripts/reloadDeepython.sh

The script reloadDeepython.sh is as follows: 
chrome-cli list tabs | grep deepython.com | cut -c 2-4 | while read -r line; do chrome-cli reload -t "$line"; done

This assumes you have chrome-cli installed, which can be installed with "pip install chrome-cli"


Using this configuration, I can almost instantly get feed back about the aesthetics and content of my post without even having to exit vim! 

It has been a pretty valuable way for me to learn about vim, python, and bash scripting. 

Here is a photo of what my development environment looks like. Pretty slick huh? 

![Alt Test](http://deepython.com.s3-website.us-east-2.amazonaws.com/images/blogSetup.png) 


Here are some other links used in this post: 

* [Vimrc](https://github.com/amix/vimrc) Github Repo
* [Chrome-cli](http://github.com/claytonblythe/version_control/scripts/reloadDeepython.sh) script
* [Chrome-cli](https://github.com/prasmussen/chrome-cli) Github Repo


Until next time,
#### Clayton Blythe | *Deep Python*
