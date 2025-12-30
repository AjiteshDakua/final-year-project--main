import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

camera = cv2.VideoCapture(0)

scan_active = False
scan_completed = False
palm_detected = False
confidence = 0


def reset_scan():
    global scan_active, scan_completed, palm_detected, confidence
    scan_active = False
    scan_completed = False
    palm_detected = False
    confidence = 0


def start_scan():
    global scan_active, scan_completed, palm_detected, confidence
    scan_active = True
    scan_completed = False
    palm_detected = False
    confidence = 0


def gen_frames():
    global scan_active, scan_completed, palm_detected, confidence

    while True:
        if not scan_active:
            time.sleep(0.05)
            continue

        success, frame = camera.read()
        if not success:
            continue

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            palm_detected = True
            confidence += 2
            confidence = min(confidence, 100)

            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # ✅ STOP SCAN (NOT CAMERA)
            if confidence >= 100:
                scan_completed = True
                scan_active = False  # camera stays ON
                break

        _, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()

        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
