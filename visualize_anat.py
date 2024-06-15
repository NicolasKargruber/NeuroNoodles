import nibabel as nib
from visualization import visualize

# Load the NIFTI file
inst = "EMC"; id = "29916"; mod = "anat"
img = nib.load(inst+'/'+id+'/session_1/'+mod+'_1/'+mod+'.nii.gz')

# Get the image data
image_data = img.get_fdata()

# Display slices of the image
print(image_data.shape)
num_slices = image_data.shape[-1]
print(num_slices)

# Visualize using the SliceViewer class
visualize(image_data)