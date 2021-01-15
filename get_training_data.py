import os
import cv2


def concat(paths: list):
    if len(paths) == 1:
        return cv2.imread(paths[0])
    # read in images
    im_1 = cv2.imread(paths[0])
    im_2 = cv2.imread(paths[1])
    # minimum concat
    main = cv2.vconcat([im_1, im_2])
    # if more than two images
    if len(paths) > 2:
        for i in range(2, len(paths)):
            to_concat = cv2.imread(paths[i])
            main = cv2.vconcat([main, to_concat])
    return main


def move_rename(image, subfolder):
    # write the image to correct dir
    cv2.imwrite(f"data/ground-truth/{subfolder}.tif", image)
    txt = f"../../make_ocr/data/{subfolder[:2]}--/{subfolder}"
    # read the transcription and write to correct dir
    with open(f"{txt}/Story {subfolder}", 'r') as f:
        content = f.readlines()
    with open(f"data/ground-truth/{subfolder}.gt.txt", 'w') as f:
        f.write("\t".join(content).replace("\n", ""))
    return


def main():
    for folder in os.listdir("../../make_ocr/data"):
        for subfolder in os.listdir(f"../../make_ocr/data/{folder}"):
            if subfolder != ".DS_Store":
                images = []
                for file in os.listdir(f"../../make_ocr/data/{folder}/{subfolder}"):
                    # if file.endswith('missing'):
                    #     print(file)
                    if file.endswith('.jpg'):
                        images.append(f"../../make_ocr/data/{folder}/{subfolder}/{file}")
                try:
                    if len(images) == 1:
                        move_rename(concat(sorted(images)), subfolder)
                except:
                    print(subfolder)
    return


# if __name__ == "__main__":
main()
