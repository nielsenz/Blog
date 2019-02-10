Title: Dealing with NaN values in Pandas
Date: 2017-09-22
Category: Tech Tips
Tags: python, pandas, NaN values, tech tips
Summary: How to accomplish basic selections of data using Pandas.

In my continued [^1] series on Pandas, today I’m going to be writing about how to deal with NaN values.[^2] NaN values are entries in a dataframe that lack data; perhaps the column is non applicable, the data is messy, or the data is simply incomplete. Many models do not do well with NaN data, so dealing with these rows are a critical part of the data science process. Below are four examples of how to drop NaN values from a Pandas Dataframe. 

`df.dropna()     #This command drops all rows that have any NaN values
``df.dropna(how='all')     #This command drops the rows only if ALL columns are NaN
``df.dropna(thresh=2)   #This command drops the row if it does not have at least two values that are not NaN
` `df.dropna(subset=1)   #This command drops the row only if NaN is in the specific column 
`

[^1]:	yet unanticipated

[^2]:	Summarized from [this](https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-certain-columns-is-nan/13413845) Stack Overflow post. 