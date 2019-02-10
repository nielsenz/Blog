Title: SQL-Like Selection in Pandas
Date: 2017-09-22
Category: Tech Tips
Tags: python, pandas, sql
Summary: How to accomplish basic selections of data using Pandas.

Coming from a SQL background, I was struggling to understand how to select a subsection of entries from a Pandas dataframe. Recently I came across [this post](http://devarea.com/pandas-for-sql-users/) that is the Rosetta Stone between the two, showing a SQL command and showing how to obtain that same result with Pandas.[^1] 

As an example, here are some select statements translated into a Pandas command:

`Select * from df where Age > 12`
`df[df['Age']>10]`
Here, the goal is to make a dataframe from a dataframe where age is greater than 10. Pretty straightforward. 

`Select Name, Country  from df where Age > 12`
`dfdf['Age'>10]['Name','Country']
`Here, we’re selecting two fields from a dataframe. The first one part is setting the condition (where age is greater than 10) and the second bit shows the fields that we want. 

Something to note is that logical connectors work inside the dataframe, meaning that you can have something like the following: 

`df[(df['Age']>12) | (df['Height'] > 130)]`

Overall, these Pandas tips will make information selection much more efficient. Python really can be used throughout the data science pipeline, and I look forward to further experimentations with it. 

[^1]:	While doing research for this post, I didn’t realize is that Pandas has a similar section in their [documentation](https://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html)!