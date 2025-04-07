
import geopandas as gpd
from shapely.geometry import Point

# Load the GeoJSON file
geojson_file = r"C:\Users\Lou13\Desktop\mygeodata\-.geojson"
geojson_data = gpd.read_file(geojson_file)

# Load the QGIS file (assuming it's exported as a shapefile from the QGIS project)
qgis_file = r"C:\Users\Lou13\Desktop\广西进士.shp"  # Replace with the correct path if exported
qgis_data = gpd.read_file(qgis_file)

# Check if the 'properties' field in GeoJSON contains a matching column like '姓名'
# Assuming 'Name' or '姓名' is present within the 'properties' dictionary

common_column_qgis = '姓名'  # Column in QGIS file
common_column_geojson = 'Name'  # Adjust based on GeoJSON 'properties'

# Safely extract the name from the properties in GeoJSON, handling None values
def extract_name_from_properties(prop):
    if prop is not None:
        return prop.get(common_column_geojson, None)
    return None  # Return None if 'properties' is None

# Apply the function to create the 'matched_name' column in GeoJSON
geojson_data['matched_name'] = geojson_data['properties'].apply(extract_name_from_properties)

# Create a dictionary of coordinates from the QGIS file based on the '姓名' (Name) column
qgis_coords = qgis_data.set_index(common_column_qgis)[['geometry']]

# Function to update the coordinates in the GeoJSON file to match those in the QGIS file
def update_coordinates(row, qgis_coords):
    try:
        # Find the matching row in the QGIS data
        qgis_point = qgis_coords.loc[row['matched_name']].geometry
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
adjusted_geojson_file = r"C:\Users\Lou13\Desktop\adjusted_geojson_output.geojson3"
geojson_data.to_file(adjusted_geojson_file, driver='GeoJSON')

print(f"Adjusted GeoJSON file saved as: {adjusted_geojson_file}")