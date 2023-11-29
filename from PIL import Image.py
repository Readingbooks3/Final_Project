from PIL import Image

def open_and_display_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)

        # Display the image
        img.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    image_path = "C:/Users/dulgu/OneDrive/Documents/class/path/to/input/image.jpg"

    # Open and display the image
    open_and_display_image(image_path)
