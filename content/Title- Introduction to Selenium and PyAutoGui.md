Title: Introduction to Selenium and PyAutoGui
Date: 2018-02-02
Category: Guides
Tags: guides, python, selenium, pyautogui, automation
Summary: A great introduction on how to get more out of your computer by using python. 

While looking for more ways to automate my computer using python, I found [this video](https://www.youtube.com/watch?v=dZLyfbSQPXI&t=673s) from PyBay2016 very informative. Presented by Al Sweigart, this video is a no nonsense look on how to get started with some basic automation. 
## Selenium
Selenium is used in testing web apps; however, it can also be used to automate any online activity. His selenium example looks like the following:

`from selenium import webdriver`
`browser = webdriver.Firefox()`
`brower.get('theurl.com’)`
`element = browser.find_element_by_css_selector(the css selector)`
`element.text` 
`element.click()`
`browser.quit()`

This example opens a web browser and navigates to a web page. From there, it finds a specific element, grabs the text and then clicks on that element. Selenium is useful because it can handle the minutiae that comes with navigating the web. 

Starting from the top, a simple `import selenium` does not work, the key is to import the web driver from selenium. Lines 2 and 3 start a browser on screen and navigates to the inputted URL.

Line 4 is where the magic happens. Instead of trying to follow the CSS chain, I can inspect an element on screen [^1], and then copy the selector path directly from the developer tools. 

Other useful methods can be used to send keys, submit, and refresh a web page. 
## PyAutoGUI
PyAutoGUI is a package that is more useful with automating tasks on screen.[^2] This module can be installed by using pip which looks like the following:  `pip install pyautogui`. 

In order to be useful, PyAutoGUI needs the pixel coordinates of where to click. To solve this problem, there is a useful function called `displayMousePosition()`. By running this function, the program will give a real time position for where the mouse is on the screen. This is a great way to plan out where the mouse needs to be in order to click the desired targets.

In addition, there’s several other useful functions: `click(), typewrite(), hotkey('ctrl','o')` are three of the most useful. Typewrite() is used to send text to the active program.  `moveTo()` and `moveRel()` will move the cursor to a specific point or in relation to where it is currently. Finally, there’s a `locateOnScreen()` method to match a screenshot with something on screen. 

The [documentation ](https://pyautogui.readthedocs.io/en/latest/introduction.html) online is well written and contains all of the methods that can be implemented with PyAutoGUI

## Conclusion 
Automation is clearly the area where I am slacking the most. These tools have great potential to simplify the daily computing process and I look forward to trying them. 

[^1]:	Right click, inspect element

[^2]:	Which can be gathered by the GUI part of the name.