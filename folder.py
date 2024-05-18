import os
import shutil

example_dir = 'Example'
os.makedirs(example_dir, exist_ok=True)

sub_dir = os.path.join(example_dir, 'subdirect')
os.makedirs(sub_dir, exist_ok=True)

#  Bu subdirectorynin içərisinə bir şəkil və bir text faylı əlavə edirk.
# Manual olaraq mövcud qovluğa əlavə etdymz faylların yolunu daxil edrk.
current_dir = os.getcwd() 
image_src = os.path.join(current_dir, 'image.jpg') 
text_file_src = os.path.join(current_dir, 'example.txt')  

if os.path.exists(image_src):
    shutil.copy(image_src, sub_dir)
else:
    print(f"Error: {image_src} faylı mövcud deyil.")

if os.path.exists(text_file_src):
    shutil.copy(text_file_src, sub_dir)
else:
    print(f"Error: {text_file_src} faylı mövcud deyil.")

for item in os.listdir(sub_dir):
    if item.endswith('.txt'):
        src_path = os.path.join(sub_dir, item)
        dest_path = os.path.join(example_dir, item)
        shutil.move(src_path, dest_path)

print("Task tamamlandı.")
