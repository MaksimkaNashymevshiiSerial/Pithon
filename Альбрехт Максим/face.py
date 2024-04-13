import cv2
filename = 'omg season.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255,
	cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow('Image', img)
cv2.imwrite('edges_' + filename, edges)
cv2.imshow('Edges', edges)
cv2.imshow('cartoon', cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()
source = cv2 CasacadeClafsfe()
while True:
	ret, img = source.read(1,3, 5)
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y)
    if 
source.releece()
draw.text((x,y))
filenamsrtok
 im.save()
 if__name()
  



