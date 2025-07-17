import cv2

# Load image
image = cv2.imread("cat.jpg")

# Draw rectangle: (x1, y1), (x2, y2), color(B,G,R), thickness
cv2.rectangle(image, (50, 50), (300, 300), (0, 255, 0), 3)

# Add text: image, text, position, font, font size, color, thickness
cv2.putText(image, "My Cat", (60, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Save the image with rectangle and text
cv2.imwrite("cat_with_box.jpg", image)

print("✅ Image saved successfully!")
# Old code (already in your file)
cv2.imwrite("cat_with_box.jpg", image)
print("✅ Image saved successfully!")

# 🆕 NEW CODE STARTS HERE
# Load the image
image = cv2.imread("cat.jpg")

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("cat_gray.jpg", gray_image)

# Convert to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imwrite("cat_hsv.jpg", hsv_image)

# Convert to LAB
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imwrite("cat_lab.jpg", lab_image)

print("✅ All color conversions done and saved!")

# === FLIP, ROTATE, CROP ===

# Load image again
image = cv2.imread("cat.jpg")

# 1. Flip the image (1 = horizontal)
flipped_image = cv2.flip(image, 1)
cv2.imwrite("cat_flipped.jpg", flipped_image)

# 2. Rotate 90 degrees clockwise
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite("cat_rotated.jpg", rotated_image)

# 3. Crop a small part of the image [rows, columns]
cropped_image = image[50:250, 100:300]
cv2.imwrite("cat_cropped.jpg", cropped_image)

print("✅ Flipped, rotated, and cropped images saved!")
