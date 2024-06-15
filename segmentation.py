import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
from masks_utils import extract_largest_component, save_masks, plot_image_subplot

# Load the NIFTI file
inst = "ETH"; id = "29058"; mod = "anat"
file_path = inst+'/'+id+'/session_1/'+mod+'_1'
img = sitk.ReadImage(file_path+'/'+mod+'.nii.gz')

# Specify the slice number
slice_num = 90
# Threshold parameters
wm_threshold = 0.22
gm_threshold = 0.122
csf_threshold = 0

# Min-Max-Normalize image to [0, 1]
img_data = sitk.GetArrayFromImage(img)
img_data_normalized = (img_data - np.min(img_data)) / (np.max(img_data) - np.min(img_data))
img_normalized = sitk.GetImageFromArray(img_data_normalized)
img_normalized.CopyInformation(img)

# >> Original Data <<

# Extract Sice
slice_data = sitk.GetArrayViewFromImage(img_normalized)[slice_num, :, :]

# Display the ORIGINAL slice
plt.figure(figsize=(24, 6))
plot_image_subplot((1, 5, 1), slice_data, f'Original Slice {slice_num}')

# >> White Matter <<

# White Matter - Mask
white_matter = extract_largest_component(img_normalized, wm_threshold)

# Extract mask from original slice
white_matter_data = slice_data.copy()
white_matter_data[sitk.GetArrayViewFromImage(white_matter)[slice_num, :, :] == 0] = 0

# Display slice with WHITE MATTER
title = f'White Matter (Threshold > {wm_threshold})'
plot_image_subplot((1, 5, 2), white_matter_data, title)

# >> Grey Matter <<

# Grey Matter - Mask
grey_matter = extract_largest_component(img_normalized, gm_threshold, wm_threshold)

# Extract mask from original slice
grey_matter_data = slice_data.copy()
grey_matter_data[sitk.GetArrayViewFromImage(grey_matter)[slice_num, :, :] == 0] = 0

# Display slice with GREY MATTER
title = f'Grey Matter (Threshold > {gm_threshold})'
plot_image_subplot((1, 5, 3), grey_matter_data, title)

# >> Central Spinal Fluid <<

# Central Spinal Fluid - Mask
central_spinal_fluid = extract_largest_component(img_normalized, csf_threshold, gm_threshold)

# Extract mask from original slice
csf_data = slice_data.copy()
csf_data[sitk.GetArrayViewFromImage(central_spinal_fluid)[slice_num, :, :] == 0] = 0

# Display slice with CSF
title = f'CSF (Threshold > {csf_threshold})'
plot_image_subplot((1, 5, 4), csf_data, title)

# >> Overlay <<

# Create the overlay plot
overlay_data = np.stack([slice_data] * 3, axis=-1)

# Apply colors
# White matter in red
overlay_data[..., 0][sitk.GetArrayViewFromImage(white_matter)[slice_num, :, :] > 0] = 1
# Grey matter in green
overlay_data[..., 1][sitk.GetArrayViewFromImage(grey_matter)[slice_num, :, :] > 0] = 1
# CSF in blue
overlay_data[..., 2][sitk.GetArrayViewFromImage(central_spinal_fluid)[slice_num, :, :] > 0] = 1

# Display the overlay image
title = f'CSF (Threshold > {csf_threshold})'
plot_image_subplot((1, 5, 5), overlay_data, 'Overlay of Masks')

# Show the plot
plt.tight_layout()
plt.show()

# Save masks
save_masks(white_matter, grey_matter, central_spinal_fluid, file_path)






