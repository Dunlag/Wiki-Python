import cv2
import glob

images = glob.glob("./sample_images/*.jpg")

for image in images:
    img = cv2.imread(image,0)
    resized_image = cv2.resize(img,(800, 600))
    cv2.imshow("redisemsionada",resized_image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    ##poner el script en la misma carpeta que las imagenes para generar el nuevo archivo
    ##o poner la ruta completa de la imagen
    cv2.imwrite("resized"+image, resized_image)