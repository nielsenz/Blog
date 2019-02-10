Title: Clearing the console and environment in R
Date: 2016-09-13
Category: Tech Tips
Tags: tech tips, r
Slug: clearing-the-console-and-environment-in-r
Summary: New Year New R Studio environment 

## Clearing the console
Two things that I find myself wondering while working with R is how to clear the console, and how to clear the environment. The console is the terminal-like area where you can see the command (or commands) that are executing. For me, it oftentimes is easier to clear the console so I can better see any new error messages that occur. Also, another benefit is simply reducing the lines and lines of old, already executed code. In order to do so, you simply press `CTRL + L` on a Windows machine, and that will take clear the console for you. 

## Clearing the environment
R Studio also saves the exact environment that you're working with when you exit out of the program, such as the values of certain variables. However, sometimes I want to clear the entire environment, giving myself a fresh environment to start out with. To do that, all I have to do is type `rm(list=ls())` into the console. This is a good command to run right before putting any code into production.