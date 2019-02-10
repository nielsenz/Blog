Title: Manipulating and Displaying National Park Service Data 
Date: 2017-08-10
Category: Analysis
Tags: visualizations, python, tableau, national park service
Summary: A data visualization project many months in the making, using tableau and python. 

**TL;DR** I used Python to expand a spreadsheet I got from the United States National Park Service in order to visualize it in with Tableau. I threw the code up [on Github](https://github.com/nielsenz/National-Parks-Expander) and the data visualization can be found [on Tableau](https://public.tableau.com/profile/zach.nielsen#!/vizhome/NationalParkServiceAttendanceAnalysis/NationalParkAttendenceAnalysis).

 My first experience with Python came when I took a data scraping class in college. From there, I ignored it for about a year until I picked up a book titled *Automate the Boring Stuff*. The book is terrific and details practical applications of programming, which my computer science degree was lacking. From there, I played around a bit with a simple script that [combines two PDF files.](https://github.com/nielsenz/pdf-Combiner) 

I then found a problem that I could practice my excel manipulation skills by programming with Python. As someone who has always loved the outdoors, I found an excel spreadsheet that has the attendance for every national park since 1904. In order to best visualize the data, I needed to manipulate the excel document so that it was in the correct format for visualization. I accomplished this by *expanding* the dataset. Initially, I looked at a spreadsheet that had the **Years** on top and the **Parks** running down the spreadsheet. However, I needed a spreadsheet with three columns: Park, Year, and Attendance. 

Overall, I had a great time writing this program. It was fun experimenting with and getting used to openpyxl and pandas. The meat of the program is in lines 13-27, with two loops to loop through each year per park and then per park.

`for parks in range(2,376):`
`	parkCode = 'B' + str(parks)`
`	parkNameCode = 'A' + str(parks)`
`	currentPark = sheet[parkCode].value`
`	currentParkName = sheet[parkNameCode].value`
`	#And then this should get all the years per park`
`	for years in range(3,115):`
`		year = sheet.cell(row=1, column=years).value`
`		attendance = sheet.cell(row=parks, column=years).value`
`		if attendance == None:`
`			attendance = 0`
`		df2 = pd.DataFrame({"Park Name" : [currentParkName],"Park": [currentPark], "Date" : [year], "Attendance" : [attendance]}, index = [coolindex])`
`		frames = [df, df2]`
`		df = pd.concat(frames)`
`		coolindex=coolindex+1`

It’s also a good sign that I now would do things differently. After my first [data science](https://www.kaggle.com/znielsen/analysis-and-prediction-of-student-performance) kernel on Kaggle, I now have more experience with Pandas and would use it exclusively. Openpyxl gave me the ability to select a cell by the row and column number, which was very useful. 

## Visualizations with Tableau
Now that I have the spreadsheet the way I like it, I can now visualize the data using Tableau. My goal is to have two graphs: one that displayed average attendance versus total attendance and a heat map of the United States showing the national park attendance. This was my first time making a heat map in Tableau and it could have not gone easier. 

### Attendance versus Average Attendance 
When I first looked at the data, I wondered how the average attendance per park differed from the overall attendance. Were there years that had a high average attendance but low overall attendance? Or as more parks were added to the national parks system, did average attendance decrease? By graphing this, there’s an intuitive way to see if the trends are the same or not. As we can see, there are slight variations but overall the trend lines are the same. 

The one design decision that was interesting to think about was if I should add dual Y axises, putting the two lines on the same graph. I decided against it, because I think that dual axises are misleading. If I tried to synchronize the axises, the average attendance is so much lower than the overall attendance it just looks like a horizontal line near zero. Although hilarious, it’s ultimately useless and that’s why I chose to stick with the two separate graphs. 

### US National Parks Heat Map
My other visualization that I wanted to create was a heat map. For those unaware, a heat map is a type of graph that colors different fields darker depending on the value. Oftentimes a heat map is applied to a spreadsheet with darker values surrounding higher values. For example, if you had a spreadsheet with monthly sales, a darker green would mean a higher value than a lighter green. 

The other place where heat maps are used are to show data on a map. By placing all of the national parks on a map of the United States, the national parks that are darker have more visitors than those which are lighter. It would be fun to look at different parts of the United States and see if there’s any correlations, as well as just see if the visitors move westward as more parks are opened in the west. 

The heat park itself was pretty easy to create. The mapping data was also provided from the park service, and I used a simple join to the data I created with the python file to associate it together in Tableau. From there, I just had one remaining design choice: should the user be allowed to select one year at a time, or should the user be allowed to select multiple years at once. 

For those that are unaware, Tableau has a bunch of ways to filter dates. The two that apply here are a singular selection [^1] or multiple date selection.[^2] Both have pros and cons, the most notable being the multiple selection is messy but more efficient and visa versa. Ultimately, I decided to go with the multiple selection, but I may transfer back to the single use if users are having trouble with the multiple selection. 

## Conclusion
It was excellent to get back into the swing of things. Instead of using SQL to manipulate the data, I can see how Python fits into a data visualization environment. I could have even graphed the data using Python; however, I wanted to practice my mapping skills in Tableau. I can’t wait to see how this graph looks and what other insights may come from this data. 

[^1]:	Meaning that the user can select one and only one year.

[^2]:	Meaning that whatever dates the user wants to select can be selected. 