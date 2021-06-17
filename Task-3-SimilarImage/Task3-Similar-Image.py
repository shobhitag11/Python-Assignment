# Import packages
import cv2
import os

def compare_images(queryImage_histogram, eachImage_histogram):
    '''This function compares each of the histogram numpy array
     values of query image with each image present in a folder
     and find the total sum of absolute compared values'''
    compared_value, i = 0, 0
    while i < len(queryImage_histogram) and i < len(eachImage_histogram):
        compared_value += (queryImage_histogram[i] - eachImage_histogram[i]) ** 2
        i += 1
    compared_value = compared_value ** (1 / 2)
    return compared_value

def main(query_image, directory_path):
    '''computes the most visually similar to the query image'''
    query_image = cv2.imread(query_image)

    # Convert Query image to grayscale
    queryImage_grayscale = cv2.cvtColor(query_image, cv2.COLOR_BGR2GRAY)

    # finding the histogram, since we ger overall idea about the
    # intensity distribution of an image, also, since there are max (0, 255)
    # So taking points as 256.
    queryImage_histogram = cv2.calcHist([queryImage_grayscale], [0], None, [256], [0, 256])

    filename_with_computedValue = {}# Stores compared pixel values with filename as the key.

    # Traverse the complete directory.
    for file in os.listdir(directory_path):
        image = cv2.imread(os.path.join(directory_path, file))
        eachImage_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        eachImage_histogram = cv2.calcHist([eachImage_grayscale], [0], None, [256], [0, 256])

        computed_value = compare_images(queryImage_histogram, eachImage_histogram)
        filename_with_computedValue[file] = computed_value

    # Best visually matching image should have the minimum compared value between pixels.
    best_matching_image = min(filename_with_computedValue, key=filename_with_computedValue.get)

    # print(best_matching_image)
    return best_matching_image

# Running the code directly
if __name__ == "__main__":

    query_image = 'query.jpg'
    directory_path = 'dataBase/'

    print("The most similar image is {}".format(main(query_image, directory_path)))