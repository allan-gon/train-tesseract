import cv2
import pytesseract
from pytesseract import Output

if __name__ == "__main__":
    img = cv2.imread("./data/ground-truth/3101.tif")
    blur = cv2.GaussianBlur(img, (3,3), 0)

    # convert to hsv and get saturation channel
    sat = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)[:,:,1]

    # threshold saturation channel
    thresh = cv2.threshold(sat, 50, 255, cv2.THRESH_BINARY)[1]

    # apply morphology close and open to make mask
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
    mask = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel, iterations=1)

    # do OTSU threshold to get circuit image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

    # write black to otsu image where mask is black
    otsu_result = otsu.copy()
    otsu_result[mask==0] = 0

    d = pytesseract.image_to_data(otsu, output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(otsu, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', otsu)
    cv2.waitKey()

    # cv2.imshow('img', otsu)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # text = dict()
    # text["processed"] = pytesseract.image_to_string(otsu)
    # text["original"] = pytesseract.image_to_string(img)
    # with open("./data/ground-truth/3101.gt.txt", "r") as f:
    #     text["truth"] = f.read()
    # for key in text:
    #     print(f"{key}:\n{text[key]}")
