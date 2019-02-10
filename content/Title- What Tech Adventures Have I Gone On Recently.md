Title: What Tech Adventures Have I Gone On Recently
Date: 2017-04-15
Category: Tech Tips
Tags: tech tips, python, sublime text
Summary: Recent tech upgrades now makes me more productive. Read and see! 

Finals week has had me unable to write much, but I have been coding more frequently. Below are some miscellaneous tech tips that I’ve used in the past week that are worth writing down. 
## How to get to the desktop in python3
I’ve been programming my way through [Automate the Boring Stuff](https://automatetheboringstuff.com), a book about how to use python to make the computer more productive. In order to do so, I often have to change directories in my python program to find the files to manipulate in the first place! To do so, I have a little bit of code that will help with that.
	import os
Thing to import that’s used to change directories
	os.getcwd()
Displays the current working directory. I’m still trying to figure out where everything is located on my Mac, and this is a useful debugging tool. 
	os.chdir(“Desktop”)
Method to change the directory. Pretty self explanatory. I often set the files I’m currently working with on my desktop, so this would be how I could change to that directory 
## Getting Subl to work on my Mac in the terminal 
I also started to use Sublime Text to write my programs with and I’ve been researching different tips and tricks that make it more useful. I recently found some code that will let me write “subl” in the terminal and have the file pop up in Sublime Text. For example, I could write 
	subl program.py
And program.py pops up in Sublime Text. Super useful. You could also use commands like 
	subl *
And everything in the current directory will pop up in sublime text, which is crazy. The below code worked for me to get it up and running, but I do recommend Stackoverflow if it’s not working.
	sudo rm /usr/local/bin/subl
	sudo ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl