print("Importing...")

from datetime import datetime
from face_recognition import compare_faces, face_encodings, load_image_file
from gpiozero import MotionSensor
from i2c import display_msg
from known_encodings import known_encodings
from os import system, listdir
from sms import send_sms
from time import sleep

# Locations of images for face_recognition.
known_folder = "known"
unknown_folder = "unknown"

# Motion Sensor Initialization.
pir = MotionSensor(4)

# Authenticates the captured image of the current user and
# compares it with the saved images of users who are
# allowed access.
#
# Returns True if face data matches that of a saved image,
# otherwise False.
def authenticate():
	global name
	global utc

	utc = str(datetime.utcnow())
	unknown_file = unknown_folder + utc.replace(" ", "_") + ".jpg"

	print("Please look at camera\n")
	display_msg("Please look     at camera")
	sleep(2)

	for i in range(3, 0, -1):
		print("Taking photo in " + str(i) + " second(s)")
		display_msg("Taking photo in " + str(i) + " second(s)")

	print()

	# Captures an image with camera at 640x480 resolution.
	system("raspistill -w 640 -h 480 -vf -t 1 -o " + unknown_file)

	print("Photo Taken\n")
	display_msg("Photo Taken")

	print("Processing...\n")
	display_msg("Processing...")
	
	utc = utc.split(".")
	utc = utc[0]

	if not known_encodings:
		return "auth_err"

	# The image previously captured is processed by the
	# face_recognition library and is returned as a list
	# of doubles that are used to locate the face in the image.
	unknown_encoding = face_encodings(load_image_file(unknown_file))

	if not unknown_encoding:
		return "no_enc"

	# The encodings of the previously captured image are comapred
	# to the ecnodings of the saved allowed users images. The
	# saved allowed users image encodings were previoulsy saved
	# so that processing can be much faster.
	for encoding in known_encodings:
		match = compare_faces(encoding[1], unknown_encoding[0])

		if match and match[0]:
			name = encoding[0].title()
			return True

	return False

def main():
	print("Loaded")

	sleep(0.5)
	system("clear")

	print("Face Recognition - Ready")
	display_msg("Face Recognition     Ready")

	while True:
		# If motion is detected run main authentication loop.
		if pir.motion_detected:
			system("clear")

			# Run authentication.
			auth = authenticate()

			date = "\rDate: " + utc + "\n"
			msg = None
			grant = "ACCESS GRANTED"
			deny = "ACCESS DENIED"

			if auth == "auth_err":
				print(deny)
				display_msg(deny)
				msg = date + "AUTHENTICATION ERROR\nNo known images to compare to. Access will be denied to all. Add known images to gain access."
			elif auth == "no_enc":
				print(deny)
				print("No Face Detected")
				display_msg(deny + "   No Face Detected")
			elif auth:
				print(grant)
				print("Welcome, " + name)
				display_msg(grant + "  Welcome, " + name)
				msg = date + name + " - Authenticated"
			else:
				print(deny)
				display_msg(deny)
				msg = date + "User Denied Access."

			# Send SMS with message.
			if msg:
				send_sms(text=msg)

			sleep(5)

			system("clear")

			print("Face Recognition - Ready")
			display_msg("Face Recognition     Ready")

try:
	main()
except:
	print("Face Recognition - Not Ready")
	display_msg("Face Recognition   Not Ready")
