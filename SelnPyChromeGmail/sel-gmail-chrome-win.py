# Selenium Script to launch gmail compose window using my gmail login with fields pre populated 
# so I can email myself any interesting articles to read later 
# Within gmail I have a filter that applies label 'ToRead' and archives all mails such as below 
# starting with 'ToRead' in subject.

# Windows version 
# This python script is invoked by the batch script sel-gmail-chrome-win.bat

# Tested on / with : 
#  Windows 11 Home OS Build 22621.3007
#  Chrome 120.0.6099.217
#  Python 3.12.1
#  selenium 4.16.0

# Bugs : 
# - Worked fine in my test but may not be 100% reliable. Keystrokes may not get sent 
# - Google may totally block bot-access to gmail (Selenium). Already saw this problem on MacOS
#   but not on windows. 
# - Repeated bot logins may cause Google account to be suspended. You may want to use with less
# important account. 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time
import os 

# config 
url = 'https://mail.google.com'
#url = 'https://web.whatsapp.com' # try if you have any Google profile loading issues 
sleeptime = 2 # pause in seconds after each step
mailto = 'myemailid@gmail.com'
subject = 'ToRead : ' 
chromedriver = 'C:\\webdrivers\\chromedriver.exe'

# Start Chrome with my default profile, so I dont have to login to google 
# Google profile dir on Windows is C:\Users\<username>\AppData\Local\Google\Chrome\User Data
# There is a 'Default' sub dir under above, which is supposed to be the default 
# google profile dir. But need to omit the 'Default' for Selenium 

service = Service(executable_path=chromedriver)
options = webdriver.ChromeOptions()
googleProfileSubdir = os.path.join(os.getenv('LOCALAPPDATA'), "Google\\Chrome\\User Data")
options.add_argument(f"--user-data-dir={googleProfileSubdir}")

driver = webdriver.Chrome(service=service, options=options)

# Launch google chrome with the above url 
driver.get(url)
time.sleep(sleeptime)

# Send the key strokes without needing to specify a specific element in the html form 
# Press c to launch compose mail window 
actions = ActionChains(driver)
actions.send_keys('c')
actions.perform()
time.sleep(sleeptime)

# need a backspace for some reason since the 'c' above appears in the mailto field 
# thats why this approach is a hack / kludge 
actions.send_keys(Keys.BACK_SPACE + mailto + Keys.TAB )
actions.send_keys(Keys.TAB )
actions.perform()
time.sleep(sleeptime)

actions.send_keys(subject + Keys.TAB)
actions.perform()

# If you exit now, browser also vanishes. The experimental detach may be a solution but did not 
# work when I tried, hence just wait till user presses ^C 
try : 
   while True:
     print("Press Ctrl-C to exit ...")
     time.sleep(60);
except KeyboardInterrupt:
   print("Exiting. Goodbye !")