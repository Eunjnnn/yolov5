### 연습장이에오. 그냥 연습장 이에오.


# import torch

# # Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # yolov5n - yolov5x6 official model
# #                                            'custom', 'path/to/best.pt')  # custom model

# # Images
# im = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, URL, PIL, OpenCV, numpy, list

# # Inference
# results = model(im)

# # Results
# results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

# results.xyxy[0]  # im predictions (tensor)
# results.pandas().xyxy[0]  # im predictions (pandas)
# #      xmin    ymin    xmax   ymax  confidence  class    name
# # 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# # 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# # 3  986.00  304.00  1028.0  420.0    0.286865     27     tie


print('is it working?')