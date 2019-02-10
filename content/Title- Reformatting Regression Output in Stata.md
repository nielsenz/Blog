Title: Reformatting Regression Output in Stata
Date: 2017-01-05
Category: Tech Tips
Tags: tech tips, stata, regressions
Slug: reformatting-regression-output-stata
Summary: New Year new way to view regression output. 

One of the most time intensive parts of data analysis isn't completing the regression, but making the results of that regression more attractive to view. In the program Stata, this can be done using the block of code below. 

`ssc install outreg `
`regress yx+z`
`outreg using cleanRegResults.doc, replace`
`regress ya+x+z`
`outreg using cleanRegResults.doc, merge `

Where a, x, y, and z are regression variables

The code block will first install the plugin necessary. The third line then creates a new .doc file[^1] that has the regression output displayed in column form. Lines four and five are not necessary, but are useful if the regression has multiple forms or if I want to compare the results of two different regressions.

[^1]:	titled cleanRegResults