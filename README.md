# Invisibility_Cloak_OpenCV
A simple program to create an Invisibility Cloak (A Red One in my case) using OpenCV.

This Repo conatins two files of which only the 'invisibilty_Cloak.py' is the one that should be run to get the desired outcome.

You only need OpenCV installed in your system and you are good to go.

There are four steps involved in this program:
1) Capture the background before hand, now we assume that the background will remain static here.
2) Start capturing frames live and then detect the red color in the frame by converting RGB to HSV (Hue-Saturation-Value) format which makes the task easier and accurate.
3) Segmenting the Red color from the frame using 'cv2.MORPH_OPEN(), cv2.MORPH_DIALATE(), cv2.morphologyEX()'. (Read OpenCV documentaion on the same to know more) They basically do the task of masking the red color objects in the frame so that they can be entirely made invisible.
4) Produce the final Output frame by using cv2.addWeighted() function. 
