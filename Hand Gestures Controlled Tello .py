from djitellopy import tello
import time 
import mediapipe as mp
import cv2


drone = tello.Tello()
drone.connect()
drone.streamon()
drone.takeoff()

next_detection_time = time.time() + 5  # Initialize the next detection time with a 5-second delay
# Initialize Mediapipe Hand module
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
counter = [0,0,0,0,0,0]
with mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5) as hands:
    while True:
        img = drone.get_frame_read().frame
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Convert BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect hand landmarks
        results = hands.process(rgb_frame)

        if time.time() >= next_detection_time:

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


                    if counter[finger_count] < 5:
                        if finger_count == 1:
                             # Move up
                            print("up")
                            drone.send_rc_control(0, 0, 20, 0)  # Move up
                            counter[1]+=1
                        elif finger_count == 2:
                            label = "Down"
                            drone.send_rc_control(0, 0, -20, 0)  # Move down
                            print("dowm")
                            counter[2]+=1
                        elif finger_count == 3:
                            label = "Left"
                            drone.send_rc_control(-20, 0, 0, 0)  # Move left
                            print("left")
                            counter[3]+=1
                        elif finger_count == 4:
                            label = "Right"
                            drone.send_rc_control(20, 0, 0, 0)  # Move right
                            print("right")
                        elif finger_count == 5:
                            print("stop")
                            drone.land
                            counter[5]+=1
                        else:
                            drone.send_rc_control(0,0,0,0)

                    # Draw landmarks on the frame
                    mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

                    # Display the finger count
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(frame, f'Label: {label}', (20, 40), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    # Reset the next detection time
                    next_detection_time = time.time() + 5
        cv2.imshow("Hand Tracking", frame)

cv2.destroyAllWindows()
drone.end()
print(counter[0],counter[1],counter[2],counter[3],counter[4])  