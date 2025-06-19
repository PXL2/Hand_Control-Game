import cv2
import mediapipe as mp
#inicializar a captura de vídeo usanco OpenCV
captura = cv2.VideoCapture(0);
if not captura.isOpened():
    print("Não foi possível acessar a câmera!")
    exit();
while(True):
    #Ler um quadro da câmera
    ret,quadro = captura.read();
    if not ret:
        print('Não foi possível ler o quadro da câmera!')
        break;
    #Exibição do quadro
    cv2.imshow('Câmera' , quadro)
    #Sair do looping se a tecla q for pressionada.
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break;

 
captura.release()
cv2.destroyAllWindows()
