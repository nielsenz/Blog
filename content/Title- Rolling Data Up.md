Title: Rolling Data Up
Date: 2016-09-15
Category: Tech Tips
Tags: data, sql, coding
Slug: rolling-data-up
Summary: We're not talking about a fruit rollup here. 

A common problem I run into while writing SQL code is the idea of rolling up data to a higher level. This just means taking a set of data, and making it less granular in some way. This is commonly done to speed up calculations, at the expense of the ability to drill down into that data. A common example is taking day level data and turning it into month level data. Here, obviously you lose the ability to drill down to sales per day (for example), but it can potentially speed up SQL procedures tremendously.

The way I do that currently in Microsoft SQL is by using the dateadd(datediff()) method, along with a group by. Say you have a table with Sales, Product, and day level date, and you want to turn that into month level data. So, you'd do something that looks like this:

`SELECT Sales = SUM(Sales), Product, DATEADD(DATEDIFF(DateField)) FROM #ExampleTable. GROUP BY PRODUCT, DATEADD(DATEDIFF(DateField)`

That will take your data, sum the sales per product per month, and group it by product and month. Definitely useful, although I will be waiting for the day until this is built in.