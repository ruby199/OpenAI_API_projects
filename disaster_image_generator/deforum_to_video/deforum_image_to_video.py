import os
import imageio

print(os.getcwd())  # prints the current working directory

# directory_name = "natural_disaster_fire"
directory_name = "natural_disaster_fire_2"


image_folder = fr"C:\Users\yscho73\Documents\OpenAPI_projects\OpenAPI_projects\disaster_image_generator\deforum_to_video\{directory_name}"
output_file = r"C:\Users\yscho73\Documents\OpenAPI_projects\OpenAPI_projects\disaster_image_generator\deforum_to_video\output.gif"




images = []
for filename in sorted(os.listdir(image_folder)):
    if filename.endswith(".png"):
        file_path = os.path.join(image_folder, filename)
        images.append(imageio.imread(file_path))
        
imageio.mimsave(output_file, images, duration=0.1)

