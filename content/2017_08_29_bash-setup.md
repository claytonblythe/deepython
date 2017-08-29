Title: Docker 101
Date: 2017-8-18 22:34
Category: Other
status: draft

testing
## Understanding Bash Startup Files

In order to do efficient work in a unix/linux environment, it is important to get a personalized environment setup to use various aliases, default directories, and to get your proper path environment setup. This article is meant to summarize the difference between .bashrc .bash_profile .profile and what I think the best setup is regarding these files. It is standard for these files to be srotred in the home directory ~ which is described by [Tilde Expansion](http://www.gnu.org/software/bash/manual/bashref.html#Tilde-Expansion). 

It is helpful to think about how Bash chronologically behaves when it is invoked as a interactive login session. When Bash is invoked as an interactive login shell, it first reads from the file /etc/profile if that file exists. After reading that file, it will look for a file at ~/.bash_profile, ~/.bash_login, and ~/.profile in that order. It will execute commands from the first one that is available if it exists, and will not proceed unless explicitly told so. 

If Bash is invoked as an interactive non-login session, then Bash reads and executes commands from ~/.bashrc, if that file exists. Therefore it is common to include the following commands in ~/.bash_profile, as it is often desired to ensure that ~/.bashrc is executed regardless of whether Bash is executed in a login or non-login session.  


:::bash
if [ -f ~/.bashrc ]; then
   source ~/.bashrc
fi

So here in ~/.bashrc you can put all various starting configurations like your PATH and you can source a file containing aliases like ~/.aliases every time you have a terminal session, whether it is a login session or simply another window. 


Just to specify, for remote shell logins, like an ssh login, Bash will read /etc/profile and then one of ~/.bash_profile or ~/.profile. 

For more reading, you can visit the bash manual and user guide [here](http://www.gnu.org/software/bash/manual/bashref.html#Introduction) or another helpful guide [here](http://mywiki.wooledge.org/DotFiles)

I think my setup will most likely include a sourcing of aliases from ~/.aliases within my ~/.bashrc file which is sourced for every terminal session, either login or non-login sessions. This seems to be a good setup for keeping things tidy and organized. I am open to suggestions and advice if anyone reads this post!


Until next time,
#### Clayton Blythe | *Deep Python*
