# Data-conversion-necessary-for-.lg-object-in-PPGNet-and-clipping-of-image

Conversion of digitized shapefiles into pixel coordinates that are suitable to be used as inputs in the PPGNet linegraph.py submodule for conversion to .lg objects.
The digitized shapefiles are of roofs which are mostly single standing buildings with simple roof. The shapefile is converted to GeoJSON file in QGIS and this is used in the code. 
The image is a 10000x10000 tif file consisting of multiple roofs in one image. 

The order of execution is as follows:

  -> Run the 'coordinates.py' followed by 'pixel.py' to obtain the original coordinates from GeoJSON file and the converted pixel coordinates respectively. 
  
  -> Run 'visualizeLineAndJunctions.py' to visualize the junctions and line segments on the image.
  
  -> Run 'boundingBox.py' to obtain the bounding box with 20 pixel buffer which is used both for clipping images and obtaining pixels for clipped images.
  
  -> Run 'visualizeBoundingBox.py' to visualize the bounding boxes on the image.
  
  -> Run 'individualLineSegment.py' to obtain pixel coordinates of line segment for each clipped image of roof. This is the first input to the 'linegraph.py' submodule of PPGNet.
  
  -> Run 'clipAndSave.py' to clip and save the individual roofs in the designated folder. These images are the second input which is used for training the network.

One image 'kriti.tif' can be found in the drive link https://drive.google.com/drive/u/1/folders/1ZTM_Y4iM9nNJLNKkZMlwxgXsoHepS63W and one GeoJSON file of the digitized shapefile 'Kriti_456_5748.geojson' is also provided for visualization and testing.

# Acknowledgement

Gratitude to Mr. Simon Hensel https://github.com/SimonHensel for his invaluable guidance and support throughout the project. 

# References

Original Work: https://github.com/svip-lab/PPGNet
Images and .lg objects for training: https://github.com/SimonHensel/Vectorization-Roof-Data-Set
