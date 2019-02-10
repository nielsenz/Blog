Title: The Tools of a Business Analyst
Date: 2017-05-18
Category: Guides
Tags: python, analysis, business, tableau 
Summary: Oftentimes I hear people worry about what tools to use. They should instead focus on the right way to think. 

Today’s post is on the technical part of being a business analyst. In my experiences, I have found that being a business analyst requires you to be able to do three things: 

- import/manage the data
- manipulate the data 
- visualize the data. 

The tools you use to do that depend on both the company and what you are familiar with. For example, if the company is using SQL to store their data, it definitely makes sense to learn SQL. 

Besides that, there is a ton of inherent flexibility with choosing your tools. The most important thing is to be able to accomplish those three tasks that I listed above. Below I'll list some examples of how these tools can fit together, if you’re unsure of what to learn first:

- Say you're just on your own and want to create a simple heat map with the data already in excel. You're pretty savvy with coding in Visual Basic, so all you have to do is google heat map excel and you're off to the races. Checking off the three categories, you can manage, manipulate, and visualize the data all in excel. Easy peazy. 
- Now let’s expand the above example: maybe you have to get and transform hundreds of observations from 36 different excel sheets. Doable yes, but difficult. Here, it makes sense to use a different, more capable tool. After reading reviews, you decide to download python and use pandas to manage your data (with the terrific read\_csv function). The same three categories are covered, but in different ways. Importing the data is accomplished with read\_csv, pandas is terrific with manipulating the data, and python has several libraries that let one visualize the data. 
- Finally, we can look at a bigger organization. Say that you are working at a company with a SQL backend that prefers their graphs in Tableau. I’m sure there’s a python package that lets you Connect to a SQL Database and then import the data into pandas similar to the second example. However, the data may be changed daily. Instead of having to run the same python script every night, the most practical method here may be to build a new table in SQL and then connect to that table directly in Tableau. Here the steps are somewhat out of order; you manipulate the data in SQL, and then import it and visualize it in Tableau. 

The point here is that there are several different tools available for becoming a business analyst, each having their own positives and negatives. What matters more here is the ability to pick the tool that applies best in the situation. SQL and tableau is a great one-two punch, but if you need to do serious statistical transformations it is best to learn Python. 

If I had to give a recommendation on what people should learn, I would suggest Tableau. Practice finding data in excel spreadsheets and then importing them into Tableau. Once you run into the limitations of Tableau [^1], I would recommend moving onto Python; it’s the tool that easiest to manage as one person.[^2] However, if you are committed to entering the business world, learning SQL may be critical.   

If the idea of learning all these different tools is slightly terrifying, do not worry. The positive note is that these skills are similar and easily transferable. Dealing with a dataframe in Python with Pandas is similar to manipulating a data set in SQL. Graphing follows from this trend; the skills are similar regardless of what tool that you use. It is more important to learn the meta-skills of dealing with data analysis: what’s the best way to graph this, what am I looking to achieve here. The tools are the easy part, it’s the thinking that’s important. 

[^1]:	Or if cost is an issue

[^2]:	And the free cost isn’t terrible either. 