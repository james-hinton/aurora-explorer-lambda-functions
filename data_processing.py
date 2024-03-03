# Due to the size of these libaries, we are not able to use them in the lambda function, so this will be moved to EKS.

# from datetime import datetime
# import numpy as np
# from scipy.interpolate import griddata
# from rasterio.transform import from_origin
# from rasterio.io import MemoryFile

# def process_aurora_data(aurora_data):
#     """
#     # Mock data
#     {"Observation Time": "2024-03-02T19:22:00Z", "Forecast Time": "2024-03-02T20:52:00Z", "Data Format": "[Longitude, Latitude, Aurora]", "coordinates": [[0, -90, 6], [0, -89, 0], [0, -88, 7], [0, -87, 8], [0, -86, 9], [0, -85, 9], [0, -84, 8], [0, -83, 8], [0, -82, 8], [0, -81, 7], [0, -80, 7], [0, -79, 6], [0, -78, 6], [0, -77, 5], [0, -76, 4], [0, -75, 4], [0, -74, 3], [0, -73, 3], [0, -72, 2], [0, -71, 2], [0, -70, 1], [0, -69, 1], [0, -68, 1], [0, -67, 0], [0, -66, 0], [0, -65, 0], [0, -64, 0], [0, -63, 0], [0, -62, 0], [0, -61, 0], [0, -60, 0], [0, -59, 0], [0, -58, 0], [0, -57, 0], [0, -56, 0], [0, -55, 0], [0, -54, 0], [0, -53, 0], [0, -52, 0], [0, -51, 0], [0, -50, 0]], "type": "MultiPoint"}
#     """

#     # Filter out coordinates with aurora intensity of 0
#     filtered_coordinates = [coord for coord in aurora_data["coordinates"] if coord[2] > 0]
    
#     points = np.array([(coord[0], coord[1]) for coord in filtered_coordinates])  # Longitude, Latitude
#     values = np.array([coord[2] for coord in filtered_coordinates])  # Aurora intensity

#     # Define grid
#     grid_x, grid_y = np.mgrid[-180:180:360j, -90:90:180j] 

#     # Perform interpolation
#     grid_z = griddata(points, values, (grid_x, grid_y), method='linear')

#     # Define the spatial resolution and transform for the output raster
#     transform = from_origin(-180, 90, 1, 1)

#     # We need to transfrom this as its currently vertical, we need it horizontal
#     grid_z = np.rot90(grid_z)

#     memory_file = MemoryFile()

#     # Create a new GeoTIFF file
#     with memory_file.open(
#         driver='GTiff',
#         height=grid_z.shape[0], width=grid_z.shape[1],
#         count=1, dtype=str(grid_z.dtype),
#         crs='+proj=latlong',
#         transform=transform
#     ) as memfile:
#         memfile.write(grid_z[::-1], 1)
    
#     return memory_file

# def process_hpi_data(hpi_data):
#     return True
