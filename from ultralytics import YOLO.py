# Complete YOLOv8 detection script

from ultralytics import YOLO
import cv2

# Load a pretrained YOLOv8 model (Nano version is fastest; you can change to yolov8s.pt, yolov8m.pt, etc.)
model = YOLO('yolov8n.pt')

# --- IMAGE DETECTION ---

def detect_image(image_path):
    results = model(image_path, show=True, save=True)
    print(f"Results for image {image_path}:")
    for result in results:
        print(result)

# Example: detect_image("test.jpg")


# --- VIDEO DETECTION ---

def detect_video(video_path):
    results = model.predict(source=video_path, show=True, save=True)
    print(f"Detection completed for video {video_path}")

# Example: detect_video("test_video.mp4")


# --- WEBCAM DETECTION ---

def detect_webcam():
    cap = cv2.VideoCapture(0)  # 0 for default webcam
    if not cap.isOpened():
        print("Cannot open webcam")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(source=frame, save=False, stream=True)

        for result in results:
            frame = result.plot()  # overlay detections on the frame

        cv2.imshow('YOLOv8 Webcam Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example: detect_webcam()


# --- MAIN ---

if __name__ == "__main__":
    # Choose one of the following:

    # Run on an image
    # detect_image("test.jpg")

    # Run on a video file
    # detect_video("test_video.mp4")

    # Run on live webcam
    detect_webcam()
