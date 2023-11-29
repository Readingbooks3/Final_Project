import cv2
import matplotlib.pyplot as plt

def image_processing(input_path, output_path):
    # Read the original image from the input path
    original_image = cv2.imread(input_path)

    if original_image is None:
        print(f"Error: Unable to read the image from {input_path}")
        return

    # Display the original image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    # Add your image processing operations here
    # Example: Convert the image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Save the processed image to the output path
    cv2.imwrite(output_path, gray_image)
    print(f"Image processed and saved to {output_path}")

    # Display the processed image
    plt.subplot(1, 2, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Processed Image')

    plt.show()

if __name__ == "__main__":
    # Example usage
    input_image_path = "C:/Users/dulgu/OneDrive/Documents/class/path/to/input/image.jpg"
    output_image_path = "C:/Users/dulgu/OneDrive/Documents/class/path/to/output/processed_image.jpg"

    # Perform image processing
    image_processing(input_image_path, output_image_path)
