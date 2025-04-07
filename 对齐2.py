import geopandas as gpd
from shapely.ops import nearest_points

# Load the GeoJSON file
geojson_file = r"C:\Users\Lou13\Desktop\mygeodata\-.geojson"
geojson_data = gpd.read_file(geojson_file)

# Load the QGIS file (assuming it's exported as a shapefile from the QGIS project)
qgis_file = r"C:\Users\Lou13\Desktop\广西进士.shp"  # Replace this with the actual file from the QGIS project
qgis_data = gpd.read_file(qgis_file)

# Ensure both datasets use the same CRS
assert geojson_data.crs == qgis_data.crs, "CRS does not match between datasets."

# Function to find the nearest point from QGIS to a point in the GeoJSON
def snap_to_nearest(point, qgis_geom):
    nearest_geom = nearest_points(point, qgis_geom.unary_union)[1]
    return nearest_geom

# Apply the snapping function to each point in the GeoJSON data
geojson_data['geometry'] = geojson_data['geometry'].apply(lambda geom: snap_to_nearest(geom, qgis_data))

# Save the adjusted GeoJSON
adjusted_geojson_file = r"C:/Users/Lou13/Desktop/adjusted_geojson_output.geojson"
geojson_data.to_file(adjusted_geojson_file, driver='GeoJSON')

print(f"Adjusted GeoJSON saved to {adjusted_geojson_file}")
