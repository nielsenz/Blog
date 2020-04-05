Title: Looking at Vegas Local Restaurants
Date: 2020-04-05
Category: Projects
Slug: creating-vegas-local-restaurants

During this whole Covid-19 thing, I was trying to think of a way that I could help. Luckily I came across this project by Jeff Triplett - it's a way to highlight any major local restaurants. Luckily it's on github, so I forked the project and starting throwing in my old data. There were a few technical lessons along the way, but I'm optimistic to be putting something out there to help our small businesses in the valley. Those will be below, but I'd appreciate it if you were to go to the site and enter your favorite local restaurant, if you're a vegas local! 
  
## Vegas Local Restaurants - Technical Notes
1. Make sure all of your files are up to date: I rarely use Ruby, so the homebrew version that I was using was very much out of date. Once I had that all up and running, it was a piece of cake. 

2. I learned a ton about environmental variables. Jeff had set up a script to sync the entries from Google Sheets, and by finishing up and implementing the online google account, Sheetfu became quite helpful. 

3. The Kansas City version of this project was hosted on Github Pages, and the sync function was then hosted with a Github function. It was all very cool, but I decided that I would wait to implement that. Github had other ideas - by bringing over the Workflows folder, it then implemented the function, which would then email me whenever it would try (and fail) to run. Needless to say, that morning I woke up with ~45 emails. Luckily you can disable that functionality within the Github UI. 

Overall, it was a great side project to accomplish. It helps out local restaurants, let's me strech my Jekyll skills, and also allows me to practice hosting something again. I look forward to seeing where this goes from here. 