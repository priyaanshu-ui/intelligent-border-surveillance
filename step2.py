from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.track(source="video.mp4", show=True, save=True,
            tracker="bytetrack.yaml")
