import os
import cv2

DATA_DIR = './dataset'

# results folder
RESULTS_DIR = './preprocessing/results'

# takes in image path and saves cropped face
def crop_face(path, name, target_size=(128, 128)):
    img = cv2.imread(path) 
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml') 
    
    # convert to grayscale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # detect faces 
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    cv2.imshow("Original image", img)
    
    for (x, y, w, h) in faces: 
        # calc center of region and define top left and bottom right corners of new image
        cx, cy = x + w // 2, y + h // 2
        
        nx, ny = cx - int(target_size[0] / 2), cy - int(target_size[1] / 2)
        nx2, ny2 = cx + int(target_size[0] / 2), cy + int(target_size[1] / 2)

        img_height, img_width = img.shape[:2]

        # adjust corners if they go out of bounds
        nx, ny = max(0, nx), max(0, ny)
        nx2, ny2 = min(img_width, nx2), min(img_height, ny2)

        # crop the face
        cropped_face = img[ny:ny2, nx:nx2]

        cv2.imshow("Cropped face", cropped_face) 
        cv2.imwrite(RESULTS_DIR + '/cropped-' + name, cropped_face) 

def preprocess_image(image_path, image_name):
    crop_face(image_path, image_name)

if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)

for i, image_name in enumerate(os.listdir(DATA_DIR)):
    image_path = os.path.join(DATA_DIR, image_name)
    preprocess_image(image_path, image_name)
