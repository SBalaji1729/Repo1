
# Bourne shell script to invoke python script sel-gmail-chrome-mac.py
# Invoke with : sh sel-gmail-chrome-mac.sh
# An alias cm='sh ~/Onedrive/bin/sel-gmail-chrome-mac.sh' can be created in ~/.zshrc for quick-laumching the shell script 

# Tested with python 3.12.1, therefore save current py version, switch to 3.12.1 and restore saved version

target_py_version=3.12.1
saved_py_version=`pyenv versions | egrep -e '^\*'  | awk '{print $2;}'`
echo Current python version is ${saved_py_version} 

if [ "${saved_py_version}" != "${target_py_version}" ]; then 
   echo Setting python to version ${target_py_version} ...
   pyenv global ${target_py_version}
   echo "Current python version now is `python -V 2>&1`"
fi 

echo Launching sel-gmail-chrome-mac.py ...
cd  ~/OneDrive/bin
python sel-gmail-chrome-mac.py 

if [ "${saved_py_version}" != "${target_py_version}" ]; then 
   echo restoring python back to ${saved_py_version} ...
   pyenv global ${saved_py_version}
   echo "Current python version now is `python -V 2>&1`"
fi 

