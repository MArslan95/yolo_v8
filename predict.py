from ultralytics import YOLO

model=YOLO("yolov8m.pt")

# model.predict(source='1.jpg', save=True, save_txt=True)
model.predict(source='street.mp4', save=True, conf=0.5, show=True)