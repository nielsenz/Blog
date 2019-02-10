Title: Python Data Science Tips 
Date: 2017-05-23
Category: Tech Tips
Tags: python, analysis, data science, pandas
Summary: Four **very useful ** bits of Python code

Since it’s been too long since I’ve done a #techTips post, here are some cool tricks I learned from my most recent data science adventure on Kaggle. This is from my categorizing student performance, which can be [seen here](https://www.kaggle.com/znielsen/analysis-and-prediction-of-student-performance) for a more in depth analysis. 

1. While graphing in Seaborn, a cool tip is that you can add the jitter flag which better shows the distribution of data. A graph[^1] looks like the following: `sns.stripplot(x="Class", y="raisedhands", data=df, jitter=True);`
2. To quickly see the number of observations in each section of a categorical variable, you can write something like this `print(df['SectionID'].value\_counts())`
3. In order to break a categorical variable into discrete dummy variables, you can write something like`df1 = pd.get_dummies(df['gender'])`. This automatically breaks the categorical variable apart, with correct naming and everything. A super useful one-liner in data analysis. 
4. Finally, in order to concatenate a data frame to another data frame, you can type something like this `df = pd.concat([df, df1, df2, df3], axis=1)`. This will add the columns from df, df1, df2 and df3 to one data frame. I used this trick where df1, df2, and df3 are all dummy variables that I then add to the original df. In my post I note that I’m sure there’s a better way; however, this is what made the most sense to me. 

And there you go. Four Python data science tips that will be useful to me in the future. Here’s hoping that they save the reader some work as well. 

[^1]:	After inputting seaborn as sns