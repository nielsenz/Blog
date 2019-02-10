Title: How to fix a S3 RequestTimeTooSkewed bug
Date: 2017-07-03
Category: Tech Tips
Tags: python, analysis, data science, pandas
Summary: *Time* for another Tech Tips post! 

While uploading a recent blog post to the cloud, I came across a strange S3 error:

`ERROR: S3 error: 403 (RequestTimeTooSkewed): The difference between the request time and the current time is too large.`

I’ve never encountered this error before. At first I thought my S3 instance had a weird time bug. After doing some debugging,[^1] I saw that the time on my machine was off by several days. After logging into system preferences and updating the time, everything was back to normal.

[^1]:	Googling