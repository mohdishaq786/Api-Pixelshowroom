from ultralytics import YOLO
from PIL import Image
import numpy as np

license_plate_detector = YOLO("license_plate_detector.pt")

def masking_license_plate(input_img):
    im = input_img.resize( [640, 640])
    pred=license_plate_detector(im,imgsz=640)

    # filler = Image.open('filler.jpg')

    data = pred[0].boxes.data.numpy()
    im=pred[0].orig_img
    for bbox in data:
        x, y, w, h, _, _ = bbox.astype(int)
        if bbox[-2] >0.6:
            im[y:h, x:w] = 0
            # im[y:h, x:w] = np.array(filler.resize(Image.fromarray(im[y:h, x:w]).size).convert('RGB'))[..., ::-1]

    output_result = im[...,::-1]
    output_result = Image.fromarray(output_result)
    return output_result
    