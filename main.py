from PIL import Image
from psd_tools import PSDImage
import os

LOCAL_PATH = os.getcwd()

def psd_to_pdf(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files with .psd extension in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".psd"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace(".psd", ".pdf"))

            # Open PSD file using psd-tools
            psd_image = PSDImage.open(input_path)
            
            # Convert to RGB mode
            rgb_image = psd_image.compose()
            rgb_image = rgb_image.convert("RGB")
            
            # Save the image as PDF
            rgb_image.save(output_path, "PDF", resolution=100.0)


if __name__ == "__main__":
    input_folder = f"{LOCAL_PATH}/input"
    output_folder = f"{LOCAL_PATH}/output"
    psd_to_pdf(input_folder, output_folder)