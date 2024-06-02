import nibabel as nib
from visualization_4d import visualize_4d

# Load the NII file
inst = "BNI"; id = "29006"; mod = "dti"
img = nib.load(inst+'/'+id+'/session_1/'+mod+'_1/'+mod+'.nii')

# Get the image data
image_data = img.get_fdata()

# Display slices of the image
print(image_data.shape)
num_slices = image_data.shape[-2]
print(num_slices)

# Visualize using the SliceViewer class
visualize_4d(image_data)