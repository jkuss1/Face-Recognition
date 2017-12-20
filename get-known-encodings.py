from face_recognition import face_encodings, load_image_file
from os import listdir

# Folder location to save processed images.
folder = "known"
encodings = []

# Finds all saved images of allowed users and uses
# face_recogntion to find their face encodings.
for f in listdir(folder):
	print("Processing: " + f)
	encodings.append((f.split(".")[0], face_encodings(load_image_file(folder + f))))

# Writes processed encodings to python file for
# use in authentication.
output = open("known_encodings.py", "w")
output.write("from array import array\n\n")
output.write("# List of encodings produced from saved images of allowed users.\n")
output.write("known_encodings = " + str(encodings).replace("array(", "array('d', "))
output.close()
