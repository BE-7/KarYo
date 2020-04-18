import tensorflow as tf
import sys
import os
cwd = os.getcwd()
# cwd = "G:/Karyotyping"

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

def groupA_Classifier(imageDir,filename):

	#print("works")
	# t = imagePath.split("/")
	# imageDir = t[0]+"/"+t[1]+"/"+t[2]+"/"+t[3]+"/vertical/"

	#rootdir = 'G:/Karyotyping/Classifier/images/vertical_original_32/'
	# filename = os.listdir(imageDir)
	# print(filename)

	threshold = {'chr_1': 0.8452277568861369, 'chr_2': 0.8609725153574379, 'chr_3': 0.8580233093563804}


	with tf.gfile.FastGFile(cwd+"/Classifier/Group A Classifier/tf_files/retrained_graph.pb", 'rb') as f:
		graph_def = tf.GraphDef()
		graph_def.ParseFromString(f.read())
		_ = tf.import_graph_def(graph_def, name='')

	predicted = {}
	unpredicted = {}
	count = 0

	with tf.Session() as sess:
		for file in filename:
			image_path = imageDir+file
			image_data = tf.gfile.FastGFile(image_path, 'rb').read()
			label_lines = [line.rstrip() for line in tf.gfile.GFile(cwd+"/Classifier/Group A Classifier/tf_files/retrained_labels.txt")]
			softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
			predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
			top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
			print(top_k)
			name = label_lines[top_k[0]]
			print(name)
			name = name.split(" ")
			temp = name[0]+"_"+name[1]
			#print(name[1])
			score = predictions[0][top_k[0]]
			print(score)
			print(threshold[temp])
			if(score>=threshold[temp]):
				count=count+1
				predicted.update({file:temp})
				print("incremented count")
			else:
				unpredicted.update({file:temp})	
	return predicted,unpredicted,count