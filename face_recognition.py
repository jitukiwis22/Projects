import face_recognition
import matplotlib.pyplot as plt 
#import cv2
#img=cv2.imread('kane1.jpg')
image=face_recognition.load_image_file('jitendrap_photo.jpg')
try:
	face_loc=face_recognition.face_locations(image)
except:
	print('[-] Face Not Detected')
#plt.imshow(img)
#plt.show()
#print(face_loc)
try:
	train_enc=face_recognition.face_encodings(image)[0]
except:
	print('[-] No Face Encoding')
#print(kane_enc)
#print(kane_enc[0])

test_image=face_recognition.load_image_file('myaadhar.png')
try:
	test_loc=face_recognition.face_locations(test_image)
	#print(test_loc)
	test_enc=face_recognition.face_encodings(test_image)[0]
	#print(test_enc)
except:
	print('[-] No Face Detected')
try:
	result=face_recognition.compare_faces([train_enc],test_enc)
	print(result)
	if result[0]:
 		print('[+] Match')
	else:
		print('[-] Not Match')
except:
	print('[-] No Match Possible')
