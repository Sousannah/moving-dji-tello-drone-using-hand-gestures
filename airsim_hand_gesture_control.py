import cv2
import mediapipe as mp
import airsim

# Initialize AirSim client
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)
client.takeoffAsync().join()

# Initialize Mediapipe Hand module
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize OpenCV webcam capture
cap = cv2.VideoCapture(0)

# Initialize Hand module
with mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect hand landmarks
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                # Calculate finger states
                thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

                finger_states = [index_tip, middle_tip, ring_tip, pinky_tip]
                up_fingers = sum(1 for tip in finger_states if tip.y < thumb_tip.y)
                finger_count = min(up_fingers + 1, 5)

                label = ""
                if finger_count == 1:
                    label = "stop"
                elif finger_count == 2:
                    label = "Up"
                    # Move up in AirSim
                    client.moveByVelocityAsync(0, 0, -1, duration=0.1)
                elif finger_count == 3:
                    label = "Down"
                    # Move down in AirSim
                    client.moveByVelocityAsync(0, 0, 1, duration=0.1)
                elif finger_count == 4:
                    label = "Left"
                    # Move left in AirSim
                    client.moveByVelocityAsync(0, -1, 0, duration=0.1)
                elif finger_count == 5:
                    label = "Right"
                    # Move right in AirSim
                    client.moveByVelocityAsync(0, 1, 0, duration=0.1)

                # Draw landmarks on the frame
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

                # Display the finger count
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, f'Label: {label}', (20, 40), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('Finger Count', frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

cap.release()
cv2.destroyAllWindows()

# Release control
client.armDisarm(False)
client.enableApiControl(False)
