Title: My Git Workflow
Date: 2017-9-2 13:10
Category: Other
tags: git, version control, bash

## Working Efficiently (a.k.a. Lazily)

I think it is very important to reduce the amount of typing that one has to do to keep track of projects, experiments, and working with version control, especially across multiple devices. As such, I have developed a sytem that I think works pretty well, specifically for managing Github respositories and projects directly from the command line. Though it is heavily personalized to my own Github profile and there are other tools out there like Hub, I decided to build my own. 

First off, I made a bash script called newRepo.sh  which will create a new repository named after the first argument that I provide after the "newRepo" command. So if I type "newRepo pytorchTutorials", I will create a new github project called pytorchTutorials that resides in my Github repositories in the cloud. This allows me to quickly create new repos and projects from the command line without having to go to the Github website, create a repository, and then clone it through the command line. The newRepo script uses the Github API to create and
clone that newly made repository as well as add a predefined project directory structure for data, notebooks, figures, and scripts. 

The script is still a work in progress, and I am looking to make other scripts/aliases that will allow for creating private repositories and deleting them as well. 

Other useful git tools that I have made are aliases for cloning, commiting, and pushing changes to the remote repository. I have 'git status' as gs, 'git add --all' as gaa, and gcp "message here" as an alias to commit all the added changes with a provided commit message, and then push the changes. 

This tends to speed up my workflow greatly, and I hope you can find them useful! 

Most of the aliases can be found in my [dotfiles repository](https://github.com/claytonblythe/dotfiles) and the newRepo script can be found in my [version_control](https://github.com/claytonblythe/version_control) repository.

Until next time,
#### Clayton Blythe | *Deep Python*
