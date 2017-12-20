# Face Recognition for Raspberry Pi

### Idea from [Raspberry Pi Facial Recognition by Anton](https://www.hackster.io/gr1m/raspberry-pi-facial-recognition-16e34e)

### This project uses:
* [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
* [face_recognition Library](https://github.com/ageitgey/face_recognition)
* [Newhaven Display](http://www.newhavendisplay.com/nhd0216k3zflgbwv3-p-5738.html)
* [PIR Motion Sensor](https://www.amazon.com/EMY-HC-SR501-Pyroelectric-Infrared-Detector/dp/B00FDPO9B8)
* [Rapberry Pi Camera Module V2](https://www.raspberrypi.org/products/camera-module-v2/)
* [Twilio for SMS](https://www.twilio.com/)

### [Installation instructions](https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65) for [face_recognition](https://github.com/ageitgey/face_recognition) on Raspberry Pi.

#### [Raspberry Pi 3 Model B GPIO Layout](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png)
#### [Newhaven Display NHD-0216K3Z-FL-GBW-V3 Manual](https://www.newhavendisplay.com/specs/NHD-0216K3Z-FL-GBW.pdf)
#### [Twilio Python Helper Library](https://www.twilio.com/docs/libraries/python)

## Notes

#### face_recognition Library
* The face_recognition library installation will take about 2 hours to complete.

#### I2C Display
* I2C commands for display will work with Newhaven Display NHD-0216K3Z-FL-GBW-V3 but may not work for other displays.

#### Known Encodings
* To make processing faster this project creates all encodings for saved known images beforehand.
* Save known images to folder "known" and then run "get-known-encodings.py" to create the python file "known-encodings.py".

#### Image Size
* The image resolution used when taking a photo is 640x480, this is to make processing faster and does not seem to affect facial recognition ability.

#### Twilio
* sms.py requires [account information](https://www.twilio.com/docs/libraries/python) from Twilio account to successfully send a text message.
* If you want to send an image over MMS with Twilio you must make the image HTTP accessible.
