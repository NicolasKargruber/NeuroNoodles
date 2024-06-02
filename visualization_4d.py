import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class SliceViewer4D:
    def __init__(self, image):
        self.image_array = image
        self.num_slices = self.image_array.shape[2]
        self.num_timepoints = self.image_array.shape[3]
        self.slice_index = self.num_slices // 2
        self.time_index = self.num_timepoints // 2

        self.fig, self.ax = plt.subplots(1, 1)
        plt.subplots_adjust(bottom=0.25, left=0.1, right=0.9, top=0.9)  # Adjust to fit both sliders

        # Create the slice slider axis and the Slider object
        ax_slice_slider = plt.axes([0.125, 0.15, 0.775, 0.03], facecolor='lightgoldenrodyellow')
        self.slice_slider = Slider(ax_slice_slider, 'Slice', 0, self.num_slices - 1, valinit=self.slice_index, valfmt='%d')

        # Create the time slider axis and the Slider object
        ax_time_slider = plt.axes([0.125, 0.05, 0.775, 0.03], facecolor='lightblue')
        self.time_slider = Slider(ax_time_slider, 'Time', 0, self.num_timepoints - 1, valinit=self.time_index, valfmt='%d')

        # Connect the sliders to the update functions
        self.slice_slider.on_changed(self.update_slider)
        self.time_slider.on_changed(self.update_time_slider)

        self.fig.canvas.mpl_connect('scroll_event', self.on_scroll)
        self.update_slice()

    def update_slice(self):
        self.ax.clear()
        self.ax.imshow(self.image_array[:, :, self.slice_index, self.time_index], cmap='gray')
        self.ax.set_title(f"Slice {self.slice_index + 1} / {self.num_slices}, Time {self.time_index + 1} / {self.num_timepoints}")
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

    def update_time_slider(self, val):
        self.time_index = int(self.time_slider.val)
        self.update_slice()

def visualize_4d(image):
    print("Preparing visualization...")
    viewer = SliceViewer4D(image)
    plt.show()
    viewer.update_slice()
