#pip install opencv-python
import cv2
filename = "ink.jpg"
#Читаем файл в библиотеку cv2
img = cv2.imread(filename)
#Готовим в серрм цвете
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Контур (Параметр - нечетный)
gray = cv2.medianBlur(gray, 3)
# Маска
edges = cv2.adaptiveThreshold(gray, 255, 
	cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9, 250, 250)
# Готовим карандашный рисунок
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Показ рисунка
cv2.imshow("Image", img)
# Сохраняем и показывем обводку
cv2.imwrite("edges3_" + filename, edges)
cv2.imshow("Edges", edges)

cv2.imwrite("cartoon3_" + filename, cartoon)
cv2.imshow("cartoon", cartoon)
# Ждем нажатие кнопок и закрываем
cv2.waitKey(0)
cv2.destroyAllWindows()
