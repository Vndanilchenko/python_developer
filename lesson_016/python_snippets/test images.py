# pip install opencv-contrib-python - установка из заранее собранных пакетов

import cv2
import os
image_cv2 = cv2.imread('external_data/girl.jpg')
# Загрузка происходит не в привычном нам RGB,а в BGR!


# Добавим небольшую функцию для отображения изображений в окнах windows:
def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Возможности OpenCV:

# Ресайз слайсами:
cropped = image_cv2[250:2000, 100:1500]
viewImage(cropped, 'Cropped version')

# Процентное изменение размера:

scale_percent = 20  # Процент от изначального размера
width = int(image_cv2.shape[1] * scale_percent / 100)
height = int(image_cv2.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image_cv2, dim, interpolation=cv2.INTER_AREA)
viewImage(resized, 'Resized version')

# Изменение цветовой гаммы:

gray_image = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2GRAY)
viewImage(gray_image, 'Gray version')
# Интересно, что gray_image — это одноканальная версия изображения
# Что заметно уменьшает количество значений для обработки

# Рисование на изображениях:

image_with_line = image_cv2.copy()
cv2.line(image_with_line, (1000, 100), (1000, 2000), (0, 255, 0), 10)
# Для отрисовки линии необходимы координаты начала и конца, цвет и ширина линии
viewImage(image_with_line, 'Line')

image_with_rectangle = image_cv2.copy()
cv2.rectangle(image_with_rectangle, (100, 100), (1500, 2000), (0, 255, 255), 10)
# Для отрисовки прямоугольника необходимы координаты левого верхнего и правого нижнего углов
# + цвет линии и её ширина
viewImage(image_with_rectangle, 'Rectangle')

# И немного магии!
# Пример с распозаванием лиц:

image_path = 'external_data/girl.jpg'
face_cascade = cv2.CascadeClassifier('external_data/haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(10, 10)
)
# Рисуем квадраты вокруг лиц
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 10)
viewImage(image, 'Detected face')
