Title: O(n) for data scientists
Date: 2016-09-20
Category: Explanatory
Tags: data, complexity, sql, coding
Slug: o-for-data-scientists
Summary: Coding just got less complex. 

Something that gets studied a lot in computer science is the idea of big O Notation. This basically signifies the complexity of the code that the computer is running. For example, if you give the computer some random data (call it  n random data), how many operations does the computer have to do to the data. This is measured as a function of n.
  
For example, if one wanted to sort data, the fastest sort that can be completed has a big O notation of O(nlog(n)). This says that the maximum number of times it touches the data is nlog(n), for any n amount of data. Therefore, a lot of time is spent trying to reduce the complexity for any algorithm, aka how many operations the computer has to do to each bit of code. The problem we're trying to solve is how can we make an algorithm go faster and implement fewer computations on the data

## Big O for data scientists 
This idea is something that data scientists can use in their own field, especially when writing SQL code. A lot of the code I run into is poorly written, and can be reordered in order to speed up the entire process. 

For example, say I have 1 million entries that have to be standardized as well as rolled up, so that there are only 2000 groups. Now, one may think that standardizing and then rolling the data up is the best way to do that. That would lead to 1 million entries being standardized, and then that standardized data being rolled up.

However, if the process was reversed, as in the roll up occurs first and then the data standardized, that 1 million standardization operations that have to be performed gets brought down to 2000 (give or take). The query runs a lot faster, and you are able to be more productive while doing so. 

In other words, the rollup has to be performed regardless. However, by standardizing the data after the rollup instead of before, fewer total entries need to be standardized, thus speeding up the entire procedure. 

## Takeaways:
The main thing to remember is to think through the entire query, and then try to minimize the operations you do to the data. Can the rollup come first? Does the order matter? How can you reduce the stress on the machine? The difference between a good programmer and a great programmer is being able to write a faster procedure that solves the same problem.