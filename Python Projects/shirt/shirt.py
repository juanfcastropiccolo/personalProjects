import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    valid_extensions = [".jpg", ".jpeg", ".png"]

    if not any(sys.argv[1].endswith(ext) for ext in valid_extensions):
        print("Invalid input")
        sys.exit(1)

    input1_valid = any(sys.argv[1].endswith(ext) for ext in valid_extensions)
    input2_valid = any(sys.argv[2].endswith(ext) for ext in valid_extensions)

    if not input1_valid or not input2_valid or sys.argv[1].split('.')[-1] != sys.argv[2].split('.')[-1]:
        print("Input and output have different extensions")
        sys.exit(1)

    shirt_converter(sys.argv[1])

def shirt_converter(input_image):
    try:
        shirt_image = Image.open("shirt.png")
        with Image.open(input_image) as input:
            fitted_image = ImageOps.fit(input, (600, 600))
            fitted_image.paste(shirt_image, shirt_image)
            fitted_image.save(sys.argv[2])

    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()
