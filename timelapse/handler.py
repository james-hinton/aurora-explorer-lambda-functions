import imageio.v2 as imageio
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, Normalize
from scipy.ndimage import gaussian_filter
import contextily as ctx
import rasterio

colors = [
    (0, 0, 0),  # Black
    (0.05, 0, 0.1),  # Very Dark Purple
    (0.1, 0, 0.2),  # Really Dark Purple
    (0.15, 0, 0.3),  # Darker Purple
    (0.2, 0, 0.4),   # Dark Purple
    (0.25, 0, 0.5),  # Purple-ish
    (0.3, 0, 0.6),   # Medium Purple
    (0.35, 0, 0.7),  # Lighter Purple
    (0.4, 0.2, 0.8),  # Purple
    (0.2, 0.3, 0.9),  # Blue
    (0.1, 0.7, 0.9),  # Light Blue
]

n_bins = [3, 6, 12, 18, 24]
cmap = ListedColormap(colors)
norm = Normalize(vmin=2, vmax=24)


def lambda_handler(event, context):
    # TODO: This requires local storage, which is not available in the lambda. Update this to use S3.
    img_dir = event["img_dir"]
    images = []

    for filename in sorted(os.listdir(img_dir)):
        if filename.endswith(".tif"):
            file_path = os.path.join(img_dir, filename)
            img = imageio.imread(file_path)

            # Reshape the image
            half_index = img.shape[1] // 2
            img = img[:, half_index:]
            img = img[: int(img.shape[0] * 0.9), :]

            # This smooths the image
            img = gaussian_filter(img, sigma=1.5)

            img = np.where(img < 2, np.nan, img)

            rgba_img = plt.get_cmap(cmap)(norm(img))

            rgba_img[np.isnan(img), :] = 0  # Set to black

            images.append((rgba_img * 255).astype(np.uint8))

    print("Generating a gif with", len(images), "frames")
    output_path = "./aurora_timelapse_styled.gif"
    imageio.mimsave(output_path, images, loop=0, fps=3)


if __name__ == "__main__":
    # Mimic an event object
    event = {
        "img_dir": "/home/james/Projects/aurora-explorer-k8s/aurora_intensity_processor/aurora_intensity_gridded_tiffs_20240324222405454298"
    }
    lambda_handler(event, None)
