# Selenium Script to launch gmail compose window using my gmail login with fields pre populated 
# so I can email myself any interesting articles to read later 
# Within gmail I have a filter that applies label 'ToRead' and archives all mails such as below 
# starting with 'ToRead' in subject.

# MacOS version 
# This python script is invoked by the shell script sel-gmail-chrome-mac.sh

# Tested on / with : 
#  MacOS Ventura 13.6.1 
#  Chrome 120.0.6099.216
#  Python 3.12.1
#  selenium 4.16.0
#  setuptools 69.0.3
#  undetected-chromedriver 3.5.4

# Bugs : 
# - Worked fine in my test but may not be 100% reliable. Keystrokes may not get sent 
# - Google may totally block bot-access to gmail (Selenium). 
# - Already saw this problem on MacOS but not on windows. Hence using undetected_chromedriver on MacOS
# - Repeated bot logins may cause Google account to be suspended. You may want to use with less
# important account. 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import undetected_chromedriver as uc

import time
import os 

# config 
url = 'https://mail.google.com'
#url = 'https://web.whatsapp.com' # try if you have any Google profile loading issues 
sleeptime = 2 # pause in seconds after each step
mailto = 'myemailid@gmail.com'
subject = 'ToRead : ' 
chromedriver = r'/usr/local/bin/chromedriver'
chrome_version=120

# Start Chrome with my default profile, so I dont have to login to google 
# Google profile dir on MacOS is ~/Library/Application Support/Google/Chrome
# There is a 'Default' sub dir under above, which is supposed to be the default 
# google profile dir. But need to omit the 'Default' for Selenium 

chrome_options = uc.ChromeOptions()
# found out that ~/ doesnt work, need to be full path, hence os.path.join() below 
googleProfileSubdir = os.path.join(os.getenv('HOME'),'Library/Application Support/Google/Chrome')
chrome_options.add_argument(f"--user-data-dir={googleProfileSubdir}")

driver = uc.Chrome(options = chrome_options, use_subprocess=True, version_main = chrome_version)

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