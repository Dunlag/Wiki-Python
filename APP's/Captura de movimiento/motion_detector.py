import cv2, time

first_frame = None

video = cv2.VideoCapture("./People Walking Free Stock Footage, Royalty-Free No Copyright Content.mp4")

# Espera y descarta los primeros frames para evitar el frame negro
#time.sleep(2)
for i in range(1):
    check, frame = video.read()

while True: 
    check, frame = video.read() 
    if not check or frame is None:
        break  # Sale del bucle si no hay más frames (fin del video o error)
    status = 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if first_frame is None:
        first_frame = gray
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]    
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    
    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  
    
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
    cv2.imshow("captura en gris", gray)
    cv2.imshow("diferencia", delta_frame)
    cv2.imshow("diferencia umbral", thresh_frame)
    cv2.imshow("Color frame", frame)

    #para videos 
    key = cv2.waitKey(30)
    #para la camara
    #key = cv2.waitKey(1)

    
    if key == ord('q'):
        break
    
    print(status)

video.release() 
cv2.destroyAllWindows()