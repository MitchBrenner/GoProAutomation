from goprocam import GoProCamera, constants
import shutil  # shutil allows for you to move specific folders
import time  # used for delay

# Link to API GitHub repo
# https://github.com/KonradIT/gopro-py-api

go_pro = GoProCamera.GoPro()  # creating gopro object

# go_pro.listMedia(True)
# go_pro.delete('all')
# go_pro.video_settings(fps="60", res="4k") to change video settings
# go_pro.shoot_video(duration=5)
# go_pro.downloadLastMedia(custom_filename="video.MP4")


def take_photo_transfer_delete():
    go_pro.take_photo(timer=5)
    go_pro.downloadLastMedia(custom_filename="selfie.JPG")
    go_pro.delete("last")


def timelapse(interval):
    i = 0
    while True:
        go_pro.downloadLastMedia(go_pro.take_photo(timer=interval), custom_filename="photo" + str(i) + '.JPG')
        shutil.move('./photo' + str(i) + '.JPG', './images/photo' + str(i) + '.JPG')
        i += 1


def media_download_and_transfer_delete():
    media = go_pro.downloadAll()
    for i in media:
        shutil.move('./101GOPRO-{}'.format(i), './images/101GOPRO-{}'.format(i))
    go_pro.delete('all')


def shutter_video(video_duration_in_seconds, sleep_duration_in_minutes):
    if type(video_duration_in_seconds) != int or type(sleep_duration_in_minutes) != int:
        print("Arguments must be integers")
        return

    while True:
        go_pro.mode("0")  # switches mode to video
        go_pro.shutter("1")  # turns on video
        time.sleep(video_duration_in_seconds)
        go_pro.shutter("0")  # turns off video
        time.sleep(sleep_duration_in_minutes * 60)

