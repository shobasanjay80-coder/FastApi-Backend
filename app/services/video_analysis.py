import cv2
import mediapipe as mp


mp_face_mesh = mp.solutions.face_mesh
mp_pose = mp.solutions.pose


def analyze_video(video_path):

    cap = cv2.VideoCapture(video_path)

    face_mesh = mp_face_mesh.FaceMesh(
        static_image_mode=False,
        max_num_faces=1,
        refine_landmarks=True
    )

    pose = mp_pose.Pose()

    total_frames = 0
    eye_contact_frames = 0
    posture_frames = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        total_frames += 1

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_results = face_mesh.process(rgb)

        if face_results.multi_face_landmarks:

            eye_contact_frames += 1

        pose_results = pose.process(rgb)

        if pose_results.pose_landmarks:

            posture_frames += 1

    cap.release()

    if total_frames == 0:
        return {
            "confidence_score": 0,
            "body_language_score": 0
        }

    eye_contact_score = (eye_contact_frames / total_frames) * 100
    posture_score = (posture_frames / total_frames) * 100

    confidence_score = (eye_contact_score + posture_score) / 2

    return {
        "confidence_score": round(confidence_score, 2),
        "body_language_score": round(posture_score, 2)
    }