from PIL import Image, ImageEnhance, ImageFilter
import os

path = "Images"
pathout = "Edited_Images"

if not os.path.exists(path):
    os.makedirs(path)
if not os.path.exists(pathout):
    os.makedirs(pathout)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    for filename in os.listdir(path):
    
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            img = Image.open(os.path.join(path, filename))

            sharpness_enhancer = ImageEnhance.Sharpness(img)
            img = sharpness_enhancer.enhance(1.5)  
            
            contrast_enhancer = ImageEnhance.Contrast(img)
            img = contrast_enhancer.enhance(1.2)  
            
            brightness_enhancer = ImageEnhance.Brightness(img)
            img = brightness_enhancer.enhance(1.1)  
            
            color_enhancer = ImageEnhance.Color(img)
            img = color_enhancer.enhance(1.3)  

            img = img.filter(ImageFilter.GaussianBlur(radius=0.5))

            cleanname = os.path.splitext(filename)[0]
            extension = os.path.splitext(filename)[1]

            img.save(os.path.join(pathout, f"{cleanname}_edited{extension}"))

print("Processing completed.")
