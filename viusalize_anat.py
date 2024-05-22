import nibabel as nib
import matplotlib.pyplot as plt

# Load the NIfTI file
img = nib.load('29058/session_1/anat_1/anat_rpi_blocked_blocked.nii')

# Get the image data
data = img.get_fdata()

# Display slices of the image
num_slices = data.shape[-1]
print(data.shape)
print(num_slices)

# Visualize middle slices in the axial, sagittal, and coronal planes
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Axial plane (z-axis)
axes[0].imshow(data[:, :, num_slices // 2], cmap='gray')
axes[0].set_title('Axial')
axes[0].axis('off')

# Sagittal plane (x-axis)
axes[1].imshow(data[:, num_slices // 2, :], cmap='gray')
axes[1].set_title('Sagittal')
axes[1].axis('off')

# Coronal plane (y-axis)
axes[2].imshow(data[num_slices // 2, :, :].T, cmap='gray', origin='lower')
axes[2].set_title('Coronal')
axes[2].axis('off')

plt.show()