import nibabel as nib
from visualization import visualize

# Load the NIfTI file
img = nib.load('29058/session_1/rest_1/rest.nii')

# Get the image data
image_data = img.get_fdata()

# Display slices of the image
num_slices = image_data.shape[-2]
print(image_data.shape)
print(num_slices)

# Visualize using the SliceViewer class
visualize(image_data[:,:,:,0])