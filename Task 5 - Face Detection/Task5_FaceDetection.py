import cv2

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalFace_default.xml"
)

# Load Image 
image = cv2.imread("person.jpg")

# Covert Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect Faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(100,100)
)

print("Faces Detected:" , len(faces))
print(faces)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Show output
cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
    