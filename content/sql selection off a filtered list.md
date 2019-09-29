Title: Filtering based off a prefiltered list in SQL
Date: 2019-09-28
Category: Tech Tips
Slug: sql-selection-based-off-filtered-list

Having been able to write more SQL in the past week, I came across a great piece of code that I want to save for future use. 

I wanted to find all transactions that was part of a specific list in order to do market basket analysis from those specific entries.

One easy way to do that is to grab all of the transaction IDs into a temp table, and then use that temp table in a Where clause, selecting from the original data set. 

So it would look something like this:

`Select TransIDs`
`into #transactions`
`From table where _conditions_`

`select transaction_members`
`from table`
`where transIDs in #transactions`

Pretty quick way to find your all items where one needs to be from a filtered list. 

