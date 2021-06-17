# Import desired packages
import numpy as np
import cv2

def main(originalImage, maskImage, destination_path):
    '''
    This function process originalImage and maskImage
    and create the resultant image at destination_path.
    '''
    common_size = (2000, 3000)#any size chosen

    originalImage = cv2.imread(originalImage)
    originalImage = cv2.resize(originalImage, common_size)

    maskImage = cv2.imread(maskImage, cv2.IMREAD_GRAYSCALE)
    maskImage = cv2.resize(maskImage, common_size)

    resultImage = cv2.bitwise_and(originalImage, originalImage, mask=maskImage)
    resultImage[np.where((resultImage == [0, 0, 0]).all(axis=2))] = [0, 0, 255]

    # Resize Image as described for result.jpg i.e. 4480*5170
    resultImage = cv2.resize(resultImage, (4480, 5170))

    # Saves the resultImage at the destination_path
    cv2.imwrite(destination_path, resultImage)

# Running the code directly
if __name__ == "__main__":

    originalImage = 'images/input.jpg'
    maskImage = 'images/mask.png'
    destination_path = 'images/result.jpg'
    main(originalImage, maskImage, destination_path)
