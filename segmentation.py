import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
from extract_largest_component import extract_largest_component

# Load the NIFTI file
inst = "ETH"; id = "29058"; mod = "anat"
img = sitk.ReadImage(inst+'/'+id+'/session_1/'+mod+'_1/'+mod+'.nii.gz')

# Specify the slice number (slice 90 in this case)
slice_num = 90
slice_data = sitk.GetArrayViewFromImage(img)[slice_num, :, :]

# Display the original slice
plt.figure(figsize=(24, 6))
plt.subplot(1, 5, 1)
plt.imshow(slice_data, cmap='gray', origin='lower')
plt.title('Original Slice 90')
plt.colorbar()
plt.axis('off')

# Threshold parameters
wm_threshold = 1200
gm_threshold = 690
csf_threshold = 0

# Determine the maximum intensity value in the entire image
img_data = sitk.GetArrayFromImage(img)
max_intensity = float(np.max(img_data)) # to Double
print(f"Maximum intensity value: {max_intensity}")

# Get largest connected component for white matter
largest_component_binary_image_wm = extract_largest_component(img, wm_threshold, max_intensity)

# Apply the mask to extract white matter
white_matter_data = slice_data.copy()
white_matter_data[sitk.GetArrayViewFromImage(largest_component_binary_image_wm)[slice_num, :, :] == 0] = 0

# Display the modified slice with white matter highlighted
plt.subplot(1, 5, 2)
plt.imshow(white_matter_data, cmap='gray', origin='lower')
plt.title(f'White Matter (Threshold > {wm_threshold})')
plt.colorbar()
plt.axis('off')

# Get largest connected component for grey matter
largest_component_binary_image_gm = extract_largest_component(img, gm_threshold, wm_threshold)

# Apply the mask to extract grey matter
grey_matter_data = slice_data.copy()
grey_matter_data[sitk.GetArrayViewFromImage(largest_component_binary_image_gm)[slice_num, :, :] == 0] = 0

# Display the modified slice with grey matter highlighted
plt.subplot(1, 5, 3)
plt.imshow(grey_matter_data, cmap='gray', origin='lower')
plt.title(f'Grey Matter (Threshold > {gm_threshold})')
plt.colorbar()
plt.axis('off')

# Get largest connected component for CSF
largest_component_binary_image_csf = extract_largest_component(img, csf_threshold, 600)

# Apply the mask to extract CSF
csf_data = slice_data.copy()
csf_data[sitk.GetArrayViewFromImage(largest_component_binary_image_csf)[slice_num, :, :] == 0] = 0

# Display the modified slice with CSF highlighted
plt.subplot(1, 5, 4)
plt.imshow(csf_data, cmap='gray', origin='lower')
plt.title(f'CSF (Threshold > {csf_threshold})')
plt.colorbar()
plt.axis('off')

# Create the overlay plot
overlay_data = np.stack([slice_data] * 3, axis=-1)

# Apply colors to the masks
# White matter in red
overlay_data[..., 0][sitk.GetArrayViewFromImage(largest_component_binary_image_wm)[slice_num, :, :] > 0] = max_intensity
# Grey matter in green
overlay_data[..., 1][sitk.GetArrayViewFromImage(largest_component_binary_image_gm)[slice_num, :, :] > 0] = max_intensity
# CSF in blue
overlay_data[..., 2][sitk.GetArrayViewFromImage(largest_component_binary_image_csf)[slice_num, :, :] > 0] = max_intensity

# Display the overlay image
plt.subplot(1, 5, 5)
plt.imshow(overlay_data / max_intensity, origin='lower')  # Normalize the image to range [0, 1] for display
plt.title('Overlay of Masks')
plt.axis('off')

# Show the plot
plt.tight_layout()
plt.show()







