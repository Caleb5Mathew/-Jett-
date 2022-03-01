# -Jett-
This Repository is a tool used to auto-send messages and also a tool to find people who share certain similiar qualities. For example, "people who suffer from Blastocystis parasites" or "people who suffer from bipolar disorder" or "Parent of kids with autistic children.
```diff
! \/ Scroll for Pre-Reqs \/ !
 
This auto-messenger started out while putting together a gift for a friend. There was a group of people that I found through 
tiktok that helped me make this project and sent me tips and selenium interpretation and to that I want to say thank you. 
Most of the people that helped me probably won't see this, but doing something that kind for a stranger is something straight 
out of a superhero book so thank you. 

-Background-
Jett is a 12 year old kid with a intestine parasite. He was one of my teacher's kids and she told us about how he couldn't do 
stuff with friends and now becuase of that parasite his life had been so much harder. The reason I picked up this project
was because of a image that my teacher painted in our heads. She talked about one night where she just held jett and they both 
cried together and he was saying "I don't want to keep doing this." This reminded me of a friend I had 2 years ago during the 
summer of my 8th grade. He had appendicitis and I watched my best friend, previously radiating joy and hope, turn down a path of
paralyzing hopelessness and thinking about Jett doing the same thing prompted me to start this project. I face-timed my friend 
and we brainstormed a plan to help him through it and provide a few segments of encouragement. My friend shared his experiences,
and the biggest wish he had during his condition: a person to relate to, and a community. That's what I based my words of 
encouragement and project off of- a compassionate community. 

-The Project-
The project is composed of a puzzle-like painting. Every puzzle piece/pieces represent a person that is standing with Jett, 
and the whole painting represents the beautiful piece that Jett is. The main takeaway we hoped that he would get from this 
was that he was a precious sculpture, a priceless work of art that is made up and supported by people in his community. We 
conveyed this sense of community by adding letters from friends, classmates of mine, and people on facebook that went through
the same scenario. I figured this was what my friend meant when he wished for people who could relate, and also figured that
these people would be the most compassionate and open to help. I made this bot to scour facebook for these people. And came 
up with 2 before the bot broke. Attached as the starter.py is the working model but using it too much got me banned on facebook.
Haven't gotten around to making burner accounts and keep messaging, felt like that was just immoral to do haha. But if anybody 
is interested in pursuing this project into places that I didn't, I would suggest to automate the bot to use a 
if (you get banned) statement to make a new gmail account, store it into a variable, and then use that to make a new facebook
account and keep going

!Recommended to run on PyCharm!
-Pre-Reqs-
  -edit the username and password val (look for "edit_here!") and fill in with your username and password
  -edit the key word to look up the group name
  -adjust the meter on where to click for the group
  -replace message with your own text inside and adjust the %s variables as needed
-imports-
  -from selenium import webdriver
  -from selenium.webdriver.common.by import By
  -from selenium.webdriver.common.keys import Keys
  -import time
  -from selenium.webdriver.common.action_chains import ActionChains
  -from selenium.common.exceptions import NoSuchElementException


