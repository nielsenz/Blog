Title: Finding percentile breaks in Stata
Date: 2017-01-25
Category: Tech Tips
Tags: tech tips, stata
Slug: finding-percentile-breaks-in-stata
Summary: A pretty easy way to find percentile breaks in Stata. 

A fun little Stata trick that I recently discovered is a way to find the percentiles breaks of a variable in Stata. So say you have a variable describing income and want to see what constitutes the values for each percentile in 10% incriminates. In Stata, one could write the following to find that information:

`sum income, detail`

This is a good command to find out what the data looks like in more detail. And it's just cool. 