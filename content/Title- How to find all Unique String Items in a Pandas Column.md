Title: How to find all Unique String Items in a Pandas Column
Date: 2018-01-28
Category: Tech Tips
Tags: tech tips, pandas, python, analytics
Summary: A quick one liner on dealing with a unique problem

While working on some hockey analysis, I came across an interesting problem: I wanted to find all of the unique values of a certain column. While normally an easy problem by using describe(), this specific column consisted of only string variables; describe() only works for numerical variables.   
  
After researching the problem, I came across the following method:

`shot_df.Position.unique()`

Where shotdf is my dataframe and Position is the column containing the string values. This will then output any unique values from the position column. 