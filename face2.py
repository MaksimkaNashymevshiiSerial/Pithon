import cv2
filename = "ink4.jpg"

#Читаем файл в библиотеку cv2

img = cv2.imread(filename)
# Читаем фильтр
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default_xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
	gray, scaleFactor=1.1, minNeighbors=12, minSize=(10, 10))

print("Лиц обнаружено: " , len(faces))
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 5)

cv2.imwrite('face_detected_' + filename, img)
cv2.imshow('Лица', img)
cv2.waitKey()
cv2.destroyAllWindows()