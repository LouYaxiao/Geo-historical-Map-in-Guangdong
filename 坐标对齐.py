import geopandas as gpd
from pyproj import Transformer

# Load the GeoJSON file
geojson_data = gpd.read_file(r"C:\Users\Lou13\Desktop\mygeodata\-.geojson")

# Assuming the QGIS file (shapefile) is exported separately from QGIS
shapefile_data = gpd.read_file(r"C:\Users\Lou13\Desktop\广西进士.shp")  # Adjust to match your file

# Check the CRS of both datasets
print("GeoJSON CRS:", geojson_data.crs)
print("Shapefile CRS:", shapefile_data.crs)

# If CRS is different, transform one to match the other
if geojson_data.crs != shapefile_data.crs:
    transformer = Transformer.from_crs(geojson_data.crs, shapefile_data.crs, always_xy=True)

    # Apply the transformation to latitude and longitude columns in GeoJSON
    geojson_data['geometry'] = geojson_data['geometry'].apply(
        lambda geom: geom.apply(lambda x, y: transformer.transform(x, y)))

# Save the adjusted GeoJSON
geojson_data.to_file(r"C:\Users\Lou13\Desktop\mygeodata\file.geojson", driver="GeoJSON")
