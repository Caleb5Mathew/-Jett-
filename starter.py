from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


search_eng = webdriver.Chrome()
search_eng.get("https://www.facebook.com/")
username = search_eng.find_element(By.ID, "email")
password = search_eng.find_element(By.ID, "pass")
submit = search_eng.find_element(By.NAME, "login")
username.send_keys("calebmathew2121@gmail.com")
password.send_keys("Vikkstar123")
# Step 4) Click Login
submit.click()
actions = ActionChains(search_eng)
search_bar = search_eng.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/label/input")
search_eng.execute_script("window.resizeTo(1024, 768)")
search_eng.maximize_window()

search_bar.send_keys("support group")
time.sleep(2)
#Need the timer or else it won't search (learned this after 2 days trying to find a workaround haha)

search_bar.send_keys(Keys.ENTER)
time.sleep(5)
actions.move_to_element_with_offset(search_eng.find_element(By.PARTIAL_LINK_TEXT, 'Group'), 0,0).click().perform()
actions.move_to_element_with_offset(search_eng.find_element(By.PARTIAL_LINK_TEXT, 'Group'), 0,0).click().perform()
actions.move_to_element_with_offset(search_eng.find_element(By.TAG_NAME, 'body'), 0,0)
time.sleep(2)
actions.move_by_offset(384, 48).click().perform()
actions.move_by_offset(100, 40).click().perform()
#2nd selected and listed group
#actions.move_by_offset(400, 40).click().perform()
#3rd selected and listed group

#########################THis people part doesnt gow straight to groups na dlcikcs on it instead, maybe try to find a way selenium can maximize the screen cause it works when the screen is fullscreen
time.sleep(10)
People = search_eng.find_element(By.PARTIAL_LINK_TEXT, "People")
People.click()


time.sleep(2)

#search_eng2 = webdriver.Chrome()

#search_eng.switch_to.frame("https://www.facebook.com/groups/autismparenting/members")
time.sleep(2)
#search_eng.execute_script("window.scrollBy(0,750)")
#last_height = search_eng.execute_script("return document.body.scrollHeight")
#search_eng.execute_script("window.scrollTo(0, document.body.scrollHeight);")

search_eng.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

def val_exist(variable):
    is_real = bool(variable)


num = 0
#####################While loop goes on forever i think, position the break well
for num in range(0, 60):
    string_1 = "//*[text()='Joined  minutes ago']"
    string_2 = str(num)
    beginning_substring = string_1[:19]
    ending_substring = string_1[19:]
    fstring = inserted_string = beginning_substring + string_2 + ending_substring
    try:
        val_exist(Reset_fo_da_move_thing)
    except NameError:
        dec_var = 1
    if dec_var != 1:
        break
    else:
        pass

    try:
        Reset_fo_da_move_thing = search_eng.find_element(By.XPATH, fstring)


    except:
        pass

if dec_var == 1:
    try:
        Reset_fo_da_move_thing = search_eng.find_element(By.XPATH, "//*[text()='Joined 2 hours ago']")

    except:
        pass
else:
    pass

if dec_var == 1:
    try:
        Reset_fo_da_move_thing = search_eng.find_element(By.XPATH, "//*[text()='Joined 3 hours ago']")

    except:
        pass
else:
    pass

if dec_var == 1:
    try:
        Reset_fo_da_move_thing = search_eng.find_element(By.XPATH, "//*[text()='Joined 4 hours ago']")

    except:
        pass
else:
    pass

if dec_var == 1:
    try:
        Reset_fo_da_move_thing = search_eng.find_element(By.XPATH, "//*[text()='Joined 5 hours ago']")

    except:
        pass
else:
    pass

if dec_var == 1:
    try:
        Reset_fo_da_move_thing = search_eng.find_element(By.XPATH, "//*[text()='Joined 6 hours ago']")

    except:
        pass
else:
    pass

    num += 1

splicing_for_hover = str(Reset_fo_da_move_thing.location)
x_splicing_for_hover = splicing_for_hover[6:9]
y_splicing_for_hover = splicing_for_hover[16:20]
print(x_splicing_for_hover)
print(y_splicing_for_hover)
try:
    Name1 = search_eng.find_element(By.XPATH, "//*[text()='Ian Oliver']")
    Name2 = search_eng.find_element(By.XPATH, "//*[text()='ShanTavia Janae' McDaniel']")
    Name3 = search_eng.find_element(By.XPATH, "//*[text()='Corey Richardson Sr.']")
except:
    pass
try:
    Name1 = search_eng.find_element(By.XPATH, "//*[text()='Buat Main Koin']")
    Name2 = search_eng.find_element(By.XPATH, "//*[text()='Melissa Jones']")
    Name3 = search_eng.find_element(By.XPATH, "//*[text()='Shirley Davitt Marks']")
except:
    pass


#print(Name1.location)
#print(Name2.location)
#print(Name3.location)

#329, 1710
#329, 1781
#329, 1781 + 81 (idk what that is too lazy to do it rn)

num = 5
string_1 = "window.scrollTo( , )"
string_2 = str(x_splicing_for_hover)
string_3 = str(y_splicing_for_hover)
beginning_substring_1 = string_1[:16]
mid_substring = string_1[17:18]
ending_substring_1 = string_1[19:]
fstring_1 = inserted_string = beginning_substring_1 + string_2 + mid_substring + string_3 + ending_substring_1

#search_eng.execute_script(fstring_1)


def scroll_shim(passed_in_driver, object):
    x = Reset_fo_da_move_thing.location['x']
    y = Reset_fo_da_move_thing.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    search_eng.execute_script(scroll_by_coord)

    #search_eng.execute_script(scroll_nav_out_of_way)
var = 0
def check_exists_by_xpath(xpath):
    try:
        search_eng.find_element(By.XPATH, str(xpath))
    except NoSuchElementException:
        return True
    return False


print(check_exists_by_xpath("//*[text()='Invioprosj']"))
search_eng.find_element(By.XPATH, "//*[text()='Invite']")
x = Reset_fo_da_move_thing.location['x']
y = Reset_fo_da_move_thing.location['y']
y_ne = int(y + 50)
y_new = str(y_ne)
num = 0
scroll_shim(search_eng, Reset_fo_da_move_thing)
actions.move_to_element(Reset_fo_da_move_thing).perform()
#while num < 6000:
        #actions.move_by_offset(x, y + num).click().perform()
actions.move_by_offset(0, -19).click().perform()

#if check_exists_by_xpath("//*[text()='Invite']") == False:
    #while num < 60:
        #actions.move_by_offset(0, -num).click().perform()
        #num += 1
        #print(num)
        #time.sleep(1)



#while num < 60:
    #actions.move_by_offset(0, -num).click().perform()
    #num += 1


#time.sleep(30)
#hover = actions.move_by_offset(int(x_splicing_for_hover), int(y_splicing_for_hover)).perform()
#hover.click()

time.sleep(2)
#Message_startup = search_eng.find_element(By.XPATH, "//div[@aria-label='Message']")
Message_startup = search_eng.find_element(By.XPATH, "//*[text()='Message']")
actions.move_to_element(Message_startup)
actions.click()
actions.perform()

try:
    ting = search_eng.find_element(By.XPATH, "//div[@aria-label='Message']/role='button")
    ting.click()
except:
    pass
    #tng = search_eng.find_element(By.PARTIAL_LINK_TEXT, "Friend")
    #tng.click()

Aa_messenger = search_eng.find_element(By.XPATH, "//div[@aria-label='Message']/role='textbox")
Aa_messenger.send_keys("calebmathew2121@gmail.com")