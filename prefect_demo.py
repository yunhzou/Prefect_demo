import cv2
import numpy as np
from prefect import flow


@flow
def show_text_image(text):
    # Create a white image
    width, height = 200, 100
    image = np.ones((height, width, 3), np.uint8) * 255

    # Define the text and font
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (0, 0, 0)
    font_thickness = 2

    # Get the text size
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

    # Calculate the center position
    text_x = (image.shape[1] - text_size[0]) // 2
    text_y = (image.shape[0] + text_size[1]) // 2

    # Add text to the image
    cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, font_thickness)

    # Display the image
    cv2.imshow('Image', image)

    # Wait for 2 seconds
    cv2.waitKey(2000)

    # Close the image window
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Example usage
    show_text_image("Hello")
