import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class SliceViewer:
    def __init__(self, image):
        self.image_array = image
        self.num_slices = self.image_array.shape[2]
        self.slice_index = self.num_slices // 2

        self.fig, self.ax = plt.subplots(1, 1)
        plt.subplots_adjust(bottom=0.25)  # Adjust the bottom to fit the slider

        # Create the slider axis and the Slider object
        ax_slider = plt.axes([0.125, 0.1, 0.775, 0.03], facecolor='lightgoldenrodyellow')
        self.slice_slider = Slider(ax_slider, 'Slice', 0, self.num_slices - 1, valinit=self.slice_index, valfmt='%d')

        # Connect the slider to the update function
        self.slice_slider.on_changed(self.update_slider)

        self.fig.canvas.mpl_connect('scroll_event', self.on_scroll)
        self.update_slice()

    def update_slice(self):
        self.ax.clear()
        self.ax.imshow(self.image_array[:, :, self.slice_index], cmap='gray')
        self.ax.set_title(f"Slice {self.slice_index + 1} / {self.num_slices}")
        plt.draw()

    def on_scroll(self, event):
        if event.button == 'up':
            self.slice_index = (self.slice_index + 1) % self.num_slices
        elif event.button == 'down':
            self.slice_index = (self.slice_index - 1) % self.num_slices
        self.update_slice()
        self.slice_slider.set_val(self.slice_index)

    def update_slider(self, val):
        self.slice_index = int(self.slice_slider.val)
        self.update_slice()

def visualize(image):
    print("Preparing visualization...")
    viewer = SliceViewer(image)
    plt.show()
    viewer.update_slice()