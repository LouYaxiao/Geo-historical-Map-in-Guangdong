import geojson
from svgpathtools import svg2paths
from shapely.geometry import LineString, mapping


def svg_path_to_geojson(svg_file, geojson_file):
    # Read the SVG paths
    paths, attributes = svg2paths(svg_file)

    # List to store GeoJSON features
    features = []

    for path in paths:
        # Convert the SVG path to a list of tuples (coordinates)
        coords = []
        for segment in path:
            coords.append((segment.start.real, segment.start.imag))  # Extract start point coordinates

        # Create a Shapely LineString from the coordinates
        line = LineString(coords)

        # Create a GeoJSON feature from the LineString
        feature = geojson.Feature(geometry=mapping(line))
        features.append(feature)

    # Create a GeoJSON FeatureCollection
    feature_collection = geojson.FeatureCollection(features)

    # Write to a GeoJSON file
    with open(geojson_file, 'w') as f:
        geojson.dump(feature_collection, f)

    print(f"GeoJSON file saved as {geojson_file}")


# Example usage
svg_path = "your_file.svg"  # Replace with your SVG file path
geojson_path = "output.geojson"  # Replace with your desired output GeoJSON file path
svg_path_to_geojson(svg_path, geojson_path)
