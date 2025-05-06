import cv2, time

video = cv2.VideoCapture(0) # 0 es la camara por defecto, 1 es la segunda camara, etc

a=0
while True: # bucle infinito para capturar frames
    a=a+1
    check, frame = video.read() # check es un booleano que indica si se ha podido leer el frame, frame es el frame capturado

    print(check) # True o False
    print(frame) # el frame capturado, es una matriz de 3 dimensiones (alto, ancho, canales de color)

    #time.sleep(3) # espera 3 segundos para que la camara se estabilice
    #cv2.imshow("captura",frame) # muestra el frame capturado en una ventana llamada "captura"
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convierte el frame a escala de grises
    cv2.imshow("captura",gray) # muestra el frame en escala de grises en la ventana "captura"
    key = cv2.waitKey(1) # espera a que se pulse una tecla para cerrar la ventana
    
    if (key==ord('q')):
        break # si se pulsa la tecla 'q', se sale del bucle
print(a) # imprime el numero de frames capturados
print(frame.shape) # imprime la forma del frame capturado (alto, ancho, canales de color)
video.release() # libera la camara
cv2.destroyAllWindows() # cierra todas las ventanas abiertas