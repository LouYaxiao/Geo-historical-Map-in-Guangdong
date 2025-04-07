import os
import geopandas as gpd
from shapely.geometry import LineString, Polygon
from svgpathtools import svg2paths


def svg_to_shapefile(svg_path, output_shapefile_path):
    # Extract paths from the SVG file
    paths, _ = svg2paths(svg_path)

    geometries = []

    # Convert each path to a shapely geometry
    for path in paths:
        for segment in path:
            if isinstance(segment, LineString):
                geometries.append(LineString([(point.real, point.imag) for point in segment]))
            elif isinstance(segment, Polygon):
                geometries.append(Polygon([(point.real, point.imag) for point in segment]))

    # Create a GeoDataFrame from the geometries
    gdf = gpd.GeoDataFrame(geometry=geometries)

    # Save to Shapefile
    gdf.to_file(output_shapefile_path)


# Paths
svg_file_path = r"D:\Python\广西.svg"
output_shapefile_path = r"D:\Python\广西.shp"

# Convert SVG to Shapefile
svg_to_shapefile(svg_file_path, output_shapefile_path)

print(f"Shapefile created at: {output_shapefile_path}")

# Convert SVG to Shapefile
svg_to_shapefile(svg_file_path, output_shapefile_path)

print(f"Shapefile created at: {output_shapefile_path}")
