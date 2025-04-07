import geopandas as gpd
from shapely.geometry import Point

# Load the GeoJSON file
geojson_file = r"C:\Users\Lou13\Desktop\mygeodata\-.geojson"
geojson_data = gpd.read_file(geojson_file)

# Load the QGIS file (assuming it's exported as a shapefile from the QGIS project)
qgis_file = r"C:\Users\Lou13\Desktop\广西进士.shp"  # Replace with the correct path if exported
qgis_data = gpd.read_file(qgis_file)

# Print the columns to identify the correct one
print("GeoJSON Columns:", geojson_data.columns)
print("QGIS Columns:", qgis_data.columns)

# Now that you know the column names, you can adjust this part of the code accordingly
# For example, if the matching column is '姓名' in QGIS and 'Name' in GeoJSON:
common_column_qgis = '姓名'  # Adjust based on the QGIS data
common_column_geojson = 'Name'  # Adjust based on the GeoJSON data

# Create a dictionary of coordinates from the QGIS file based on the common column
qgis_coords = qgis_data.set_index(common_column_qgis)[['geometry']]

# Function to update the coordinates in the GeoJSON file to match those in the QGIS file
def update_coordinates(row, qgis_coords):
    try:
        # Find the matching row in the QGIS data
        qgis_point = qgis_coords.loc[row[common_column_geojson]].geometry
        if isinstance(qgis_point, Point):
            # Update the geometry in GeoJSON with QGIS point coordinates
            return Point(qgis_point.x, qgis_point.y)
        else:
            return row.geometry  # If not a Point geometry, keep original
    except KeyError:
        # If no match is found, keep the original coordinates
        return row.geometry

# Apply the function to update coordinates in the GeoJSON file
geojson_data['geometry'] = geojson_data.apply(lambda row: update_coordinates(row, qgis_coords), axis=1)

# Save the adjusted GeoJSON file
adjusted_geojson_file = r"C:\Users\Lou13\Desktop\adjusted_geojson_output.geojson2"
geojson_data.to_file(adjusted_geojson_file, driver='GeoJSON')

print(f"Adjusted GeoJSON file saved as: {adjusted_geojson_file}")