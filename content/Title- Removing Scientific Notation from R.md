Title: Removing Scientific Notation from R
Date: 2016-09-03
Category: Tech Tips
Tags: tech tips, r
Slug: remove-scientific-notation-from-r
Summary: Scientific Notation in R getting ya down? Well no more! 

As someone who uses R for data analysis, I've run into the feature of R displaying results in scientific notation. For the numbers I'm usually dealing with, scientific notation is not needed. So, after googling around, I found this [Stack Overflow](http://stackoverflow.com/questions/5352099/how-to-disable-scientific-notation-in-r "Disable Scientific Notation in R") post that said to append the following line to the top of the code:

`options(scipen=999)`

Now, these results shall be displayed in the more common format, adding clarity to the analysis. 
