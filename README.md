# Work-Ambassador-FLL-UTEP-Scoreboard
Python software I personally composed and deployed to handle scoring and leaderboards during the official El Paso FIRST® LEGO® League Explore Festival. This festival was held at UTEP in January 2025 and the software granted logistical support for over 300 students in over 20+ robotics teams. Granted logistical support for over 300 students in over 20+ robotics teams. [🚩] 

<p align="center">
<img src="https://github.com/Azaze7/Work-Ambassador-FLL-UTEP-Scoreboard/blob/main/ReadMeAssets/UTEP_FLL_Scoreboard_Setup.jpg" height="375px"> 
</p>

## 🔎 Table of Contents.

1. What is the FLL-UTEP-Scoreboard? How does it work?
2. Running Instructions.
3. What Files are Enclosed Here?
4. Closing Thoughts.

## ❓ What is the FLL-UTEP-Scoreboard? How does it work?
* This software was used during the FLL-Challenge, a robotics league sponsered by The University of Texas at El Paso.
* https://www.utep.edu/engineering/k12/robotics/fll-challenge.html
* It was run on a computer used for scoring that was hooked up to a large T.V. screen via hdmi. It allowed students and coaches to look at their current standings in the tournament without asking the judges or scorekeepers directly.
* Since it was based on the existing excel sheet used for scoring, we were able to automate the process and not require an additional redundant system to showcase standings.
<p align="center">
<img src="https://github.com/Azaze7/Work-Ambassador-FLL-UTEP-Scoreboard/blob/main/ReadMeAssets/UTEP_FLL_Table_Setup.jpg" height="200px">
</p> 

## 🧱 Running Instructions.

* To get it working, simply make a folder named "LegoScorer" and download all files on this repo and place them inside of it.
* Then place this "LegoScorer" folder in your "Downloads" folder.
* Open the .xlsm file that keeps scores and log some teams.
* Then Click the shortcut named *Run Me!*
* Assuming that you already have Python installed on your computer, the scoreboard will open and begin scrolling, automatically populating based on the scores that are logged on the excel document!

## 🗂️ What Files are Enclosed Here?

| Filename | Type | Description | 
| --------------- | --------------- | --------------- |
| ReadMeAssets | 🗂️ | Contains pictures, gifs, and other assets to make this README! |
| First Lego League Scoreboard | .bat | Windows .bat file that opens the software when the *Run Me!* shortcut is opened. |
| First Lego League Scoreboard | .text | Contains the path information the software is looking for. (Place all files in a folder named LegoScorer in the Downloads Directory, see Running Instructions Section.)
| README | .md | All of the text that you are currently reading. |
| Run Me! - First Lego League Scoreboard | .lnk | A simple, clickable shorcut that runs the First Leo League Scoreboard.bat file. This was made to make it easy to run for anyone unfamiliar with a command line interface, so it just opens like any other app. |
| UTEP_Flat_Logo_Orange | .png | A UTEP logo, taken from UTEP's official assets. Used so that it would be of high quality and follow guidelines on the software. |
| fd_fll_submerged_challenge_social_template_tw_post_619278859 | .png | A First Lego League Logo, taken from the organization's official assets. Used so that it would be of high quality and follow guidlines on the software. |
| fll-challenge-submerged-robot-game-excel-scorer | .xlsm | Excel File used to keep score by the judging team. Since we were already provided this, the python code was made to display all the results on the various boards. |
| score | .py | The custom code file that is run when *Run Me!* is clicked. It uses the open .xlsm file to build and display the results as a scrolling table, using openpyxl, pandas, & tkinter.  |

## 🚪 Closing Thoughts.
> "The success of using this software during the event brings myself great pride. As always, I loved my job helping the next generation become passionate and interested in engineering, and am very pleased with how smoothly it all ran. A highlight of my curretly *short* career that I hope to build upon!" -Gilbert Guzman

**Here's a final picture of myself at one of our events! I consider the upload of this code to be the closing page for my time as an Engineering Ambassador.**
<p align="center">
<img src="https://github.com/Azaze7/Work-Ambassador-FLL-UTEP-Scoreboard/blob/main/ReadMeAssets/UTEP_Blue_Origin_Selfie.jpg" height="150px">
</p> 

Thank You for reading about this little software. I hope it was interesting!
