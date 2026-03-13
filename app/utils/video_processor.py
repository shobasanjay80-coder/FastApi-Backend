import os
import cv2
import subprocess
from app.config.settings import settings


def extract_audio_from_video(video_path: str):

    audio_dir = settings.AUDIO_UPLOAD_DIR
    os.makedirs(audio_dir, exist_ok=True)

    filename = os.path.basename(video_path).split(".")[0]
    audio_path = os.path.join(audio_dir, f"{filename}.wav")

    command = [
        "ffmpeg",
        "-i", video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        audio_path
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return audio_path


def get_video_duration(video_path: str):

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    cap.release()

    if fps == 0:
        return 0

    duration = frame_count / fps

    return duration


def extract_frames(video_path: str, interval=30):

    frames = []

    cap = cv2.VideoCapture(video_path)

    count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        if count % interval == 0:
            frames.append(frame)

        count += 1

    cap.release()

    return frames