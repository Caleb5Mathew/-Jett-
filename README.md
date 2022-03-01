# -Jett-
This Repository is a tool used to auto-send messages and also a tool to find people who share certain similiar qualities. For example, "people who suffer from Blastocystis parasites" or "people who suffer from bipolar disorder" or "Parent of kids with autistic children.

```diff
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


