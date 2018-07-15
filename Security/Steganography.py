from Security.LSBSteg import LSBSteg
import cv2
import os


def encode(img_path, video):
    steg = LSBSteg(cv2.imread(img_path))
    img_encoded = steg.encode_text(video.get_secret_code())

    output_path = os.path.dirname(img_path) + "/output.png"
    cv2.imwrite(output_path, img_encoded)
    os.remove(img_path)
    os.rename(output_path, img_path[:-3] + "png")


def decode():
    # decoding
    im = cv2.imread("output.png")
    steg = LSBSteg(im)
    print("Text value:", steg.decode_text())

