import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

# Path to 1st & 2nd Patient
inst = "EMC"; id1 = "29889"; id2 = "29917"; mod = "anat"
person1_path = inst+'/'+id1+'/session_1/'+mod+'_1'
person2_path = inst+'/'+id2+'/session_1/'+mod+'_1'

# Load images for the 1st person
anat_img1 = sitk.ReadImage(f"{person1_path}/anat.nii.gz")
wm_mask1 = sitk.ReadImage(f"{person1_path}/white_matter_mask.nii.gz")
gm_mask1 = sitk.ReadImage(f"{person1_path}/grey_matter_mask.nii.gz")
csf_mask1 = sitk.ReadImage(f"{person1_path}/csf_mask.nii.gz")

# Load images for the 2nd person
anat_img2 = sitk.ReadImage(f"{person2_path}/anat.nii.gz")
wm_mask2 = sitk.ReadImage(f"{person2_path}/white_matter_mask.nii.gz")
gm_mask2 = sitk.ReadImage(f"{person2_path}/grey_matter_mask.nii.gz")
csf_mask2 = sitk.ReadImage(f"{person2_path}/csf_mask.nii.gz")

# Slice numbers
slice_num1 = 143
slice_num2 = 135

# Convert images to numpy arrays
anat_data1 = sitk.GetArrayViewFromImage(anat_img1)[slice_num1, :, :]
anat_data2 = sitk.GetArrayViewFromImage(anat_img2)[slice_num2, :, :]

wm_data1 = sitk.GetArrayViewFromImage(wm_mask1)[slice_num1, :, :]
gm_data1 = sitk.GetArrayViewFromImage(gm_mask1)[slice_num1, :, :]
csf_data1 = sitk.GetArrayViewFromImage(csf_mask1)[slice_num1, :, :]

wm_data2 = sitk.GetArrayViewFromImage(wm_mask2)[slice_num2, :, :]
gm_data2 = sitk.GetArrayViewFromImage(gm_mask2)[slice_num2, :, :]
csf_data2 = sitk.GetArrayViewFromImage(csf_mask2)[slice_num2, :, :]

# Define transparency for overlay (alpha value)
alpha = 0.2

# Create figure
plt.figure(figsize=(18, 12))

# Plot for white matter
plt.subplot(1, 3, 1)
plt.imshow(anat_data1, cmap='gray', origin='lower')
plt.imshow(wm_data1, cmap='Reds', origin='lower', alpha=0.2)
plt.imshow(wm_data2, cmap='Blues', origin='lower', alpha=alpha)
plt.title('White Matter Comparison')
plt.colorbar()
plt.axis('off')

# Plot for grey matter
plt.subplot(1, 3, 2)
plt.imshow(anat_data1, cmap='gray', origin='lower')
plt.imshow(gm_data1, cmap='Reds', origin='lower', alpha=0.2)
plt.imshow(gm_data2, cmap='Blues', origin='lower', alpha=alpha)
plt.title('Grey Matter Comparison')
plt.colorbar()
plt.axis('off')

# Plot for CSF
plt.subplot(1, 3, 3)
plt.imshow(anat_data1, cmap='gray', origin='lower')
plt.imshow(csf_data1, cmap='Reds', origin='lower', alpha=0.1)
plt.imshow(csf_data2, cmap='Blues', origin='lower', alpha=alpha)
plt.title('CSF Comparison')
plt.colorbar()
plt.axis('off')

# Show the plots
plt.tight_layout()
plt.show()
