Problems installing pyaudio:

https://raspberrypi.stackexchange.com/questions/84666/problem-on-installing-pyaudio-on-raspberry-pi#:~:text=To%20install%20pyaudio%20in%20Raspberry%20Pi%20OS%20%28for,or%20not%2C%20check%20with%20a%20pip3%20list%20command.

If your system is not "broken", you may be successful with this sequence:

1. sudo apt-get update 
2. sudo apt-get upgrade 
3. sudo apt-get install portaudio19-dev 
4. sudo pip install pyaudio
In general: 1. updates the package list on your system, and 2. upgrades all installed packages. These two steps should usually be done before you install any new packages.

If your system still complains of broken packages and such, try this sequence:

1. sudo apt-get update 
2. sudo apt-get upgrade 
3. sudo apt-get dist-upgrade
4. sudo apt-get install portaudio19-dev 
5. sudo pip install pyaudio
Briefly, the difference between step 2 and step 3 is this:

sudo apt-get dist-upgrade will add & remove packages if necessary, and attempts to deal "intelligently" with changed dependencies.

sudo apt-get upgrade under no circumstances are currently installed packages removed, or packages not already installed retrieved and installed. This may be considered "safer" than dist-upgrade, but not as effective in all cases.