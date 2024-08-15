from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.train(data='/Users/zk/workspace/yolo-learn/safe_hat.yaml', epochs=3)

model.val()
