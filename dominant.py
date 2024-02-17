import numpy as np
import cv2
from sklearn.cluster import KMeans
import os

def get_all_dominant_colors(file_name):
    frame_names = sorted(os.listdir(f"temp/{file_name}"))
    print(len(frame_names))
    dom_colors = []

    for i in range(0, len(frame_names)):
        print(round(float(i)/float(len(frame_names))*100,2), "%")
        file_name_im = f"temp/{file_name}/frame{i}.jpg"

        image = cv2.imread(file_name_im)

        processed_image = process_image(image)

        dominant_color = get_dominant_colors(processed_image)

        dom_colors.append(dominant_color.tolist())
    
    return dom_colors


def process_image(image):
    pixels = image.reshape((-1, 3))

    pixels = np.float32(pixels)

    return pixels


def get_dominant_colors(pixels):
    kmeans = KMeans(n_clusters=1, n_init=10)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_

    return colors.astype(int)

def display_dominant_colors(dominant_colors):
    # Create a blank white image
    bar = np.zeros((50, 300, 3), dtype=np.uint8)
    startX = 0

    # For each dominant color, draw a rectangle on the blank image
    for color in dominant_colors:
        endX = startX + (300 // len(dominant_colors))
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype(int).tolist(), -1)
        startX = endX

    # Display the image
    cv2.imshow("Dominant Colors", bar)
    cv2.waitKey(0)
    cv2.destroyAllWindows()