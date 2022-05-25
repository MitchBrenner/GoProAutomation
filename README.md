# GoProAutomation

Link to API GitHub repo
https://github.com/KonradIT/gopro-py-api

This program contains methods to automate your GoPro Experience

## Methods:

### take_photo_transfer_delete()
* This function will take a picture, save it to your local storage and delete the photo on the go-pros memory

### timelapse(interval)
* This function will take a photo every given interval and save the image into a folder on your computer then delete the photo off of your gopro

### media_download_and_transfer_delete()
* This function will download all the GoPro's media to your computer, then delete all the files on the GoPro

### shutter_video(video_duration_in_seconds, sleep_duration_in_minutes)
* This function will take a video every given duration for a specific duration