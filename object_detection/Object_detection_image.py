######## Image Object Detection Using Tensorflow-trained Classifier #########
# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util

def detection(imagePath, target):

	# Name of the directory containing the object detection module we're using
	MODEL_NAME = 'inference_graph'
	IMAGE_NAME = imagePath

	# Grab path to current working directory
	CWD_PATH = os.getcwd()
	CWD_PATH = CWD_PATH+"/object_detection"
	# Path to frozen detection graph .pb file, which contains the model that is used
	# for object detection.
	PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

	# Path to label map file
	PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')

	# Path to image
	PATH_TO_IMAGE = imagePath
	# Number of classes the object detector can identify
	NUM_CLASSES = 6

	# Load the label map.
	# Label maps map indices to category names, so that when our convolution
	# network predicts `5`, we know that this corresponds to `king`.
	# Here we use internal utility functions, but anything that returns a
	# dictionary mapping integers to appropriate string labels would be fine
	label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
	categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
	category_index = label_map_util.create_category_index(categories)

	# Load the Tensorflow model into memory.
	detection_graph = tf.Graph()
	with detection_graph.as_default():
	    od_graph_def = tf.GraphDef()
	    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
	        serialized_graph = fid.read()
	        od_graph_def.ParseFromString(serialized_graph)
	        tf.import_graph_def(od_graph_def, name='')

	    sess = tf.Session(graph=detection_graph)

	# Define input and output tensors (i.e. data) for the object detection classifier

	# Input tensor is the image
	image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

	# Output tensors are the detection boxes, scores, and classes
	# Each box represents a part of the image where a particular object was detected
	detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

	# Each score represents level of confidence for each of the objects.
	# The score is shown on the result image, together with the class label.
	detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
	detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

	# Number of objects detected
	num_detections = detection_graph.get_tensor_by_name('num_detections:0')
	#print("number of detections are ",num_detections)

	# Load image using OpenCV and
	# expand image dimensions to have shape: [1, None, None, 3]
	# i.e. a single-column array, where each item in the column has the pixel RGB value
	image = cv2.imread(PATH_TO_IMAGE)
	image_expanded = np.expand_dims(image, axis=0)

	# Perform the actual detection by running the model with the image as input
	(boxes, scores, classes, num) = sess.run(
	    [detection_boxes, detection_scores, detection_classes, num_detections],
	    feed_dict={image_tensor: image_expanded})

	coordinates = vis_util.return_coordinates(
	                        image,
	                        np.squeeze(boxes),
	                        np.squeeze(classes).astype(np.int32),
	                        np.squeeze(scores),
	                        category_index,
	                        use_normalized_coordinates=True,
	                        line_thickness=2,
	                        min_score_thresh=0.60)

	z = 1

	# if not os.path.exists("images/validation_result/"+b):
	# 	os.mkdir("images/validation_result/"+b)

	if not os.path.exists(target+"/cropped"):
		os.mkdir(target+"/cropped")

	for coordinate in coordinates:
	            (y1, y2, x1, x2, acc) = coordinate
	            height = y2-y1
	            width = x2-x1
	            crop = image[y1:y1+height, x1:x1+width]
	            cv2.imwrite(target+"/cropped/"+str(z)+".jpg",crop)
	            z=z+1 

	# Draw the results of the detection (aka 'visualize the results')

	vis_util.visualize_boxes_and_labels_on_image_array(
	    image,
	    np.squeeze(boxes),
	    np.squeeze(classes).astype(np.int32),
	    np.squeeze(scores),
	    category_index,
	    use_normalized_coordinates=True,
	    line_thickness=2,
	    min_score_thresh=0.60)

	# All the results have been drawn on image. Now display the image.


	temp = imagePath.split("/")
	cv2.imwrite(target+"/"+"detected_"+temp[-1],image)


# Uncomment the below line to test the module independently and comment line 23 ie CWD_PATH
# detection("G:/Karyotyping/chromosome_data/original 32/original 32.jpg","G:/Karyotyping/chromosome_data/original 32")