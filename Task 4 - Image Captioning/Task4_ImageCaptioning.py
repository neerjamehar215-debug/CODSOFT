from transformers import  BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import os

print("="* 50)
print("    IMAGE CAPTIONING SYSTEM")
print("=" * 50)

# Load Pretrained Model
print("Loading AI Model... Please Wait...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("Model Loaded Successfully!\n")


def generate_caption(image_path):
    try:
        # if file exists
        if not os.path.exists(image_path):
            print("Error: Image File not found!")
            return

        # open image
        image = Image.open(image_path)

        # Generator Caption
        inputs = processor(image, return_tensors="pt")

        output = model.generate(**inputs)

        caption = processor.decode(output[0], skip_special_tokens=True)

        print("\nGenerated Caption:")
        print("-" * 30)
        print(caption)
        print("-" *30)

    except Exception as e:
        print("An Error Occured:", e)

def main():
    while True:
        print("\nOptions:")
        print("1. Generate Caption")
        print("2. Exit")

        choice = input ("Enter your Choice:")

        if choice == "1":
            image_path = input("Enter Image Path:")
            generate_caption(image_path)

        elif choice ==  "2":
            print("Thank you for Usinf Image Captioning system!")
            break

        else:
            print ("Invalid Choice! Try Again.")


if __name__=="__main__":
    main()
