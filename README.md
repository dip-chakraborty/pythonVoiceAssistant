# pythonVoiceAssistant
**This is a python based voice assistant program/bot which can perform some digital tasks based on the user's preferences.**

----------------------------------------------------------------------------------------------------------------------------

**Tasks this bot can perform:**

**(1)** Wikipedia search

**(2)** Google search

**(3)** Playing something on Youtube

**(4)** Opening some softwares recognized by windows, ex: notepad, calculator etc.

**(5)** Saying weather of a current city

**(6)** Saying date, time

**(7)** Send email

----------------------------------------------------------------------------------------------------------------------------

**How run the assistant:**
Copy the files from the repository. Just run the **main.py**

----------------------------------------------------------------------------------------------------------------------------

**How to configure the assistant:**
The configuration and interaction of he voice assistant works in two different ways - **(1)** Initial interation with the user. **(2)** Non-initial interactions with the users.

**(1) Initial interaction with the user:** At the very initial interaction with the user there should be no **assistanceloader.json** file in the code path 
(Please delete from your directory if already copied from this repository). If this is the first interaction, the voice assistant will ask to type your name, gender and the name using which 
you/user want(s) to call the assistant. Once you supply the values, assistanceloader.json file will get automatically created in your code directory.
If you supply your name - 'XYZ', gender - 'male', assistant name - 'ABC', then you can all your assistant by 'ABC' and 'ABC' will call you 'sir' from then. 


**(2) Non-initial interactions with the users** For recurring usage, the above values gets called from **assistanceloader.json** file and interaction starts. If you have supplied the values
same as above at the time of the initial usage, the assistant will declare herself as 'ABC' and you as 'sir'!

----------------------------------------------------------------------------------------------------------------------------
**Usage of individual modules:**

**main.py:** Main run module of the project. It uses speech recognition module to always access the voice provided by the user

**assistanceloader.json:** _readme file edit in progress_

**assistantLoader.py:** _readme file edit in progress_

**runAndSplitTasks.py:** _readme file edit in progress_

**interactiveModule.py:** _readme file edit in progress_

**openSoftware.py:** _readme file edit in progress_

**playOnYoutube.py:** _readme file edit in progress_

**searchInternet.py:** _readme file edit in progress_

**sendEmail.py:** _readme file edit in progress_
