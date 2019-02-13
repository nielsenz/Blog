Title: Submodules in Github
Date: 2019-02-12
Category: Micro
Slug: submodules-in-github

While following my annual tradition of redesigning my blog, I realized that I want continuous deployment - the easiest way to do that seems to be with Netify. 

One aspect of that is uploading all of my files to Github. From there, Netify will grab that and then trigger a redeployment. Pretty easy. 

Except I kept getting this error, regarding my .gitmodule file. After digging in, I realized that I had copied over the pelican-themes and pelican-plugins folders from other github accounts - I had to make sure that they were listed properly. After more fiddling, I removed them and then added them back in. Once that happened, it ended up working perfectly. 

Something that helped me out was removing it, using the below code and then adding it back in: 

`rm -rf .gitmodules`
`git rm --cached c3-pro-ios-framework`
`git submodule add https://github.com/chb/c3-pro-ios-framework.git`

Overall, the `git status` command also helps notifiy what isn't getting sent to Github and what isn't. Another super awesome command! 