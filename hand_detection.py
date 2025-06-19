import cv2
import mediapipe as mp

# Inicializa o modulo Hands do MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils # Desenha os marcos na imagem

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro: Não foi possível abrir a câmera.")
    exit()

print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Inverte a imagem horizontalmente para que a mão espelhada pareça natural
    frame = cv2.flip(frame, 1)

    # Converte o frame BGR para RGB (MediaPipe exige RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa o frame para encontrar as mãos
    results = hands.process(frame_rgb)

    # Verifica se alguma mão foi detectada
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Desenha os marcos da mão e as conexões no frame original
            # fazendo as linhas que conectam os porntos para vizualização de mão
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            h, w, c = frame.shape
            x_index_tip = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * w)
            y_index_tip = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * h)
            cv2.circle(frame, (x_index_tip, y_index_tip), 10, (255, 0, 255), cv2.FILLED)
            cv2.putText(frame, f'X: {x_index_tip}, Y: {y_index_tip}', (x_index_tip + 20, y_index_tip),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow('Hand Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#fechar tudo
cap.release()
cv2.destroyAllWindows()
hands.close()