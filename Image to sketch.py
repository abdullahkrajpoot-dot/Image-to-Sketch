import cv2
def make_sketch(image_path):
    # 1. Image load karna
    img = cv2.imread(image_path)
    
    # 2. Image ko Black & White (Grey) karna
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 3. Image ko ulta (Invert) karna
    inverted_img = cv2.bitwise_not(grey_img)
    
    # 4. Blur karna taake edges soft ho jayein
    blurred = cv2.GaussianBlur(inverted_img, (21, 21), 0)
    
    # 5. Sketch effect create karna (Dodge blend)
    inverted_blurred = cv2.bitwise_not(blurred)
    sketch = cv2.divide(grey_img, inverted_blurred, scale=256.0)
    
    # 6. Result save karna
    cv2.imwrite('my_sketch.jpg', sketch)
    print("Success! Sketch saved as my_sketch.jpg")

# Test karne ke liye apni image ka naam yahan likhein
make_sketch('input.jpg')