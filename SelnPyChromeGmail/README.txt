When I find interesting articles, I like to email the links to myself. I suppose one could just add to browser bookmarks or whatsapp it to oneself,
but I like gmailing it, with a specific word in the subject line ToRead which I then archive to a special gmail folder(label) using an automatic
filter. Using gmail allows me to add my comments etc and I can reply to that mail later with further links or comments. I also get the power of gmail
search. [Basically I do everything I can to curate and archive the article links without actually reading the bloomin' article :) ]

But I was so lazy that, on desktop I wanted an automated way to launch chrome with me logged in to gmail and launch 'compose' window with to:(myself)
and subject starting with 'ToRead :' already populated. All with just a single control key or 2-letter command from shell.

Used python with selenium to achieve this. In retrospect, probably not a good way at all. The approach is basically a hack/kludge but it was fun
doing it and it works !

-) But may not be 100% reliable. Keystrokes may not get sent. Behaviour was erratic few times but with a small sleep in between the steps it seems to
be ok.

-) Also Google may totally block bot-access (Selenium) to gmail . I faced this problem for some reason only on MacOS. The idea is : when you fire up
chrome manually and login to gmail, you can make it remember your login profile so gmail does not ask you to login again when you launch chrome (your
device is considered trusted). The way to do this in automation is to load the user's chrome profile.

On MacOS this was not working. Gmail forced me to always sign in. But I observed that my profile icon did appear correctly next to the 3 dots on top
right, it was the google account that was forcing me to login. I confirmed this by visiting a different URL - Whatsapp Web : web.whatsapp.com. On
this url, the automated launch of chrome remembered my whatsapp session, so this confirmed that it was not a chrome profile loading issue, but an
issue with Google account.

After a lot of time on Google and stackoverflow and trying out faking the user-agent etc, finally I stumbled upon the python package
"undetected_chromedriver" that did the trick ! But since it looks like a server side (gmail) issue, why did the problem occur only on MacOS and not
on Windows ? Heaven knows.

-) Repeated bot logins may cause Google account to be suspended. You may want to use with less important account. But still a fun exercise.

The specific versions of python, selenium, chrome and other libraries are documented inside the py script. Who knows when this will stop working ?
Perhaps with the next chrome update.

===========================================================
Windows steps :

CMD> pip3 install selenium
Download chromedriver-win64.zip link under 'Stable' from https://googlechromelabs.github.io/chrome-for-testing/#stable
As of Jan 2024 this is https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win64/chromedriver-win64.zip
Unzip to C:\webdrivers\chromedriver.exe

Copy sel-gmail-chrome-win.bat, sel-gmail-chrome-win.py to %USERPROFILE%\OneDrive\bin
double click on sel-gmail-chrome-win.bat or set up a shortcut to the batch file and a ctrl-key to launch it

===========================================================
MacOS steps :

Uninstalled Chrome completely from Macbook using steps in
https://superuser.com/questions/318186/how-do-i-uninstall-google-chrome-completely-from-my-mac
 rm -r /Applications/Google\ Chrome.app/
 rm -r ~/Library/Application\ Support/Google/Chrome/
 rm ~/Library/Application\ Support/CrashReporter/Google\ Chrome*
 rm ~/Library/Preferences/com.google.Chrome*
 rm ~/Library/Preferences/Google\ Chrome*
 rm -r ~/Library/Caches/com.google.Chrome*
 rm -r ~/Library/Saved\ Application\ State/com.google.Chrome.savedState/
 rm ~/Library/Google/GoogleSoftwareUpdate/Actives/com.google.Chrome
 rm ~/Library/Google/Google\ Chrome*
 rm -r ~/Library/Speech/Speakable\ Items/Application\ Speakable\ Items/Google\ Chrome/

Install chrome and chromedriver using brew

$ brew install --cask google-chrome
$ brew install --cask chromedriver

In Finder, Right click on /usr/local/bin/chromedriver and open it once

$ pyenv global 3.12.1
$ pyenv versions
$ python -V

$ pip install selenium

$ pip install undetected_chromedriver  # This was required as mentioned above.
If you get any error, try :
$ pip install --upgrade setuptools

In gmail, enable the keystrokes for Compose etc. On MacOS they were disabled by default. Press ? in gmail to see this.

Copy sel-gmail-chrome-win.sh, sel-gmail-chrome-win.py to ~/OneDrive/bin
Have an alias in ~/.zshrc such as cm='sh ~/Onedrive/bin/sel-gmail-chrome-mac.sh'
Start a new Terminal (shell). Type cm and press enter to launch the automation
