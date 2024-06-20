import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import time
from masks_utils import plot_image_subplot

# Load the NIFTI file and segmentations
inst = "EMC"; id = "29917"; mod = "anat"
file_path = inst+'/'+id+'/session_1/'+mod+'_1'

# Load the original image
img = sitk.ReadImage(file_path+'/'+mod+'.nii.gz')

# Load the saved masks
white_matter = sitk.ReadImage(file_path + '/white_matter_mask.nii.gz')
grey_matter = sitk.ReadImage(file_path + '/grey_matter_mask.nii.gz')
csf = sitk.ReadImage(file_path + '/csf_mask.nii.gz')

# Get the number of slices
num_slices = white_matter.GetSize()[2]

# Specify the display speed (seconds per frame)
display_speed = 1/8

# Function to update the plot
def update_plot(slice_num):
    # Extract the specified slice from the original image and each mask
    original_slice = sitk.GetArrayViewFromImage(img)[slice_num, :, :]
    white_matter_slice = sitk.GetArrayViewFromImage(white_matter)[slice_num, :, :]
    grey_matter_slice = sitk.GetArrayViewFromImage(grey_matter)[slice_num, :, :]
    csf_slice = sitk.GetArrayViewFromImage(csf)[slice_num, :, :]

    # Create the overlay plot
    overlay_data = np.zeros((white_matter_slice.shape[0], white_matter_slice.shape[1], 3))

    # Apply colors
    overlay_data[..., 0][white_matter_slice > 0] = 1 # Red
    overlay_data[..., 1][grey_matter_slice > 0] = 1 # Green
    overlay_data[..., 2][csf_slice > 0] = 1 # Blue

     # Display the original slice and overlay image side by side
    plt.clf()    
    plot_image_subplot((1, 2, 1), original_slice, f'Patient {id} - Original')

    # Display the overlay image
    plot_image_subplot((1, 2, 2), overlay_data, f'Overlay of Masks - Slice {slice_num}')
    plt.draw()

# Create a figure
plt.figure(figsize=(10, 8))

start_slice = 60
end_slice = 210
# Loop through all slices
for slice_num in range(start_slice, end_slice):
    update_plot(slice_num)
    plt.pause(display_speed)

# Show the final plot
plt.show()

