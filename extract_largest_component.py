import SimpleITK as sitk
import numpy as np

def extract_largest_component(image, lower, upper):
    # Apply binary thresholding to create a mask for white matter
    binary_mask = sitk.BinaryThreshold(image, lowerThreshold=lower, upperThreshold=upper)
    binary_mask_np = sitk.GetArrayViewFromImage(binary_mask)

    # Convert into image
    binary_image = sitk.GetImageFromArray(binary_mask_np.astype(np.uint8))
    # Convert into (labeled) connected component image
    component_image = sitk.ConnectedComponent(binary_image)
    # Sorted according to size
    sorted_component_image = sitk.RelabelComponent(component_image, sortByObjectSize=True)
    # Get largest connected component
    return sorted_component_image == 1