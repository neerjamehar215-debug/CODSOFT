## Image Captioning System
The Image Captioning System is Artificial Intelligence project that automatically generates descriptives captions for images. It uses a BLIP (Bootstraping Language-Image pretraining) model from Hugging Face Transformers to analyze image content and generate meaningful text descriptions.
## Objectives
- To develop an AI-based Image Captioning System.
- To generates meaningful captions from image automatically.
- To apply Computer Vision and Deep Learning techniques.
- To use the BLIP model for image understanding.
- To gain practical experience in Artificial Intelligence and Machine Learning.
## Features
- Automatic image caption generation
- Supports JPG, JPEG, and PNG image formats
- User-friendly command-line interface
- Generates human readable captions
- AI-powered image understanding
## Working Principle
- The user provides an image as input.
- The AI model analyzes objects and features present in the image.
- The image is processed using the BLIP pre-trained model.
- The model generates a meaningful textual discription (caption).
- The generated caption displayed to the user.
## Algorithm
1. Start the program.
2. Load the BLIP pre-trained image captioning model.
3. Accept the image path from the user.
4. Check whether the image file exists.
5. Open and process the image.
6. Extract the image features using the BLIP processor.
7. Generate a caption using trained model .
8. Display the generated caption to the user.
9. Exit the program.
10. End the program.
## Technology used
- Python
- Transformers Library
- Hugging Face BLIP model
- pyTorch
- Pillow (PIL)
## Installation
Install the required libraries:
pip install transformers torch pillow
## How to run
1. Open the terminal.
2. Navigate to the project folder.
3. Run the Python file:
python Task4_ImageCaptioning.py
4. Select option 1 (Generate Caption).
5. Enter the Image file name or image path.
Example: Airplane.jpg
6. The system will generate and display a caption for the image.
7. Select option 2 to exit the program.
## Sample Output
==================================================
    IMAGE CAPTIONING SYSTEM
==================================================
Loading AI Model... Please Wait...
Model Loaded Successfully!

Options:
1. Generate Caption
2. Exit
Enter your Choice:1
Enter Image Path:Airplane.jpg
Generated Caption:
------------------------------
a large passenger jet sitting on top of an airport tar
------------------------------
Options:
1. Generate Caption
2. Exit
Enter your Choice:2
Thank you for Usinf Image Captioning system!
## Learning Outcomes
- Understood the basics of Image captioning using AI.
- Gained hands-on experience with hugging Face Transformers library.
- Improved Knowledge of Python libraries such as PIL or Pytorch.
- Develpoed Problem-solving and Debugging skills during project implementation. 
- Learned how pre-trained models like BLIP work for image understanding.
## Future Enhancements
- Support for multiple languages in caption generation.
- Development of a Graphical User Interface (GUI).
- Real-time image captioning usin webcam input.
- Batch processing for multiple images at once.
- voice output for generated caption.
## Author
Neerja Mehar
## Internship
CODSOFT AI Internship 
Task 4 - Image Captioning 