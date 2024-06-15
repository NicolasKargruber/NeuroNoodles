import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

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

def save_masks(wm_mask, gm_mask, csf_mask, file_path):
    wm_mask_path = file_path + "/white_matter_mask.nii.gz"
    gm_mask_path = file_path + "/grey_matter_mask.nii.gz"
    csf_mask_path = file_path + "/csf_mask.nii.gz"

    # Save WM mask
    sitk.WriteImage(wm_mask, wm_mask_path)
    print(f"White matter mask saved to {wm_mask_path}")

    # Save GM mask
    sitk.WriteImage(gm_mask, gm_mask_path)
    print(f"Grey matter mask saved to {gm_mask_path}")

    # Save CSF mask
    sitk.WriteImage(csf_mask, csf_mask_path)
    print(f"CSF mask saved to {csf_mask_path}")


def plot_image_subplot(position, data, title, cmap='gray', origin='lower'):
    plt.subplot(position[0], position[1], position[2])
    plt.imshow(data, cmap=cmap, origin=origin)
    plt.title(title)
    # plt.colorbar()
    plt.axis('off')