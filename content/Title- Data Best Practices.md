Title: Data Best Practices
Date: 2017-01-10
Category: Guides
Tags: data, best practices, guides
Slug: data-best-practices
Summary: Before the fun stuff starts, it's crucial to do the less fun stuff. 

I thought I'd write down some best practices for whenever I get a new set of data. Getting and playing with data is one of the tenets of being a data scientist/economist. However, it is difficult to know how to proceed an open, entirely new CSV. Below is a checklist for me (and all of, truly) to follow in order to maintain scientific integrity:

1. Have a hypothesis to test
	Whenever I have a new dataset, my immediate desire is to start running regressions on any combination of variables. However, I now realize that is the wrong way to begin. I should first have a hypothesis that I want to test, and then find data that can help me find a solution. The scientific method that everyone learned in middle school is actually useful, who would have thought?
2.  Look for any outliers
	Now that you have a hypothesis and data that can be used to determine if the hypothesis is true, the next step would be to examine the data and make sure it is relatively sound. Normally this can be accomplished by noting any outliers, and seeing if they can be removed or not. [^1] In addition, I like to check the spread of the data, establishing a baseline for each variable in my head. Does the mean of variable x seem higher than normal? That is worth examining in closer detail.
3. Run the regression
	After noting the hypothesis and eliminating any possible outliers, it is now time to run the actual regression. If the results are statistically significant, then the mission is complete On the other hand, if the results are less than spectacular then it is time to change your hypothesis. What could be better? Is there any information that can be added/removed that would lead to a working conclusion? After a new hypothesis is made, the cycle can start over.

As I stated before, whenever I receive new data, I have a tendency to run regressions without a thought as to what the results mean or the quality of the results. Following this list will allow me to approach the problem in a more scientific way, leading to better analysis and more interesting results.  

[^1]:	I was in a statistics class one time, and the professor asks us if we knew when it was acceptable to remove outliers. After staring in silence for a bit, the professor remarked that it is when another piece of data contradicts the outlier itself.

	As an example, getting the age of all the students in the classroom, the mean would be around 21. However, say there was an outlier of 67. Delving deeper into that entry, we find out that is actually the teacher's age. Then it would be permissible to remove that entry. However, that entry could also be legal, if that was a returning student. This explanation continues to be the best way to determine outliers.