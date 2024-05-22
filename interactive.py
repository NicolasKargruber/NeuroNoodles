import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Load the NIfTI file
img = nib.load('29058/session_1/anat_1/anat_rpi_blocked_blocked.nii')
# img = nib.load('rest.nii')

# Get the image data
data = img.get_fdata()

# Create a figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Display initial slice
current_slice = data.shape[-1] // 2
img_plot = ax.imshow(data[:, :, current_slice], cmap='gray')

# Add a slider to control the slice
ax_slider = plt.axes([0.125, 0.1, 0.775, 0.03], facecolor='lightgoldenrodyellow')
slice_slider = Slider(ax_slider, 'Slice', 0, data.shape[-1] - 1, valinit=current_slice, valfmt='%d')

# Update the plot when the slider is changed
def update(val):
    current_slice = int(slice_slider.val)
    img_plot.set_data(data[:, :, current_slice])
    fig.canvas.draw_idle()

slice_slider.on_changed(update)

plt.show()