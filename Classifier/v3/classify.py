import tensorflow as tf
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

def classify(target):
	#print("works")
	# t = imagePath.split("/")
	imageDir = target+"/Original_after_max/"

	#rootdir = 'G:/Karyotyping/Classifier/images/vertical_original_32/'
	filename = os.listdir(imageDir)
	print(filename)

	#Preprocessed threshold v1
	threshold = {'chr_1': 0.7005995916377785, 'chr_10': 0.4755305751011922, 'chr_11': 0.5514257906848549, 'chr_12': 0.559018386543816, 'chr_13': 0.589966843652929, 'chr_14': 0.6609391017984121, 'chr_15': 0.5838806254741473, 'chr_16': 0.5823814703358544, 'chr_17': 0.565929741686226, 'chr_18': 0.6527430527230613, 'chr_19': 0.665208366054755, 'chr_2': 0.5877262700954055, 'chr_20': 0.6467213091305178, 'chr_21': 0.8292170328080145, 'chr_22': 0.6091317460577712, 'chr_3': 0.4931755405333307, 'chr_4': 0.5620491582359004, 'chr_5': 0.5397103494431219, 'chr_6': 0.4842160374053523, 'chr_7': 0.5146558618108774, 'chr_8': 0.4306479982239135, 'chr_9': 0.5489281096991072, 'chr_x': 0.45030022453030816, 'chr_y': 0.9058650792861471}

	#original v3

	#threshold = {'chr_1': 0.803957915204203, 'chr_10': 0.5570297315079942, 'chr_11': 0.6024215206121787, 'chr_12': 0.6064632267524035, 'chr_13': 0.665047234768032, 'chr_14': 0.7009146782832268, 'chr_15': 0.597115438654382, 'chr_16': 0.6088642810399716, 'chr_17': 0.64755075934351, 'chr_18': 0.7068196094443655, 'chr_19': 0.7466864669297495, 'chr_2': 0.6707555519209968, 'chr_20': 0.7282319354832681, 'chr_21': 0.8366824455368214, 'chr_22': 0.6959972287981938, 'chr_3': 0.605148667581061, 'chr_4': 0.6297150880225704, 'chr_5': 0.6339215661725427, 'chr_6': 0.5512259033245918, 'chr_7': 0.5744991477835795, 'chr_8': 0.5128731890561733, 'chr_9': 0.5911184790286612, 'chr_x': 0.5657781128488157, 'chr_y': 0.8702845123349404}
	cwd = os.getcwd()
	print(cwd)
	#augmented v1
	#threshold = {'chr_1': 0.5806173143539837, 'chr_10': 0.34987123754214156, 'chr_11': 0.42290421320206445, 'chr_12': 0.3792356686467786, 'chr_13': 0.41879855452336856, 'chr_14': 0.43299127109973123, 'chr_15': 0.40641172406105125, 'chr_16': 0.4172314604484411, 'chr_17': 0.3973610919157538, 'chr_18': 0.422630432035393, 'chr_19': 0.5325401555410171, 'chr_2': 0.47840787656605244, 'chr_20': 0.4519088038660843, 'chr_21': 0.692927679962161, 'chr_22': 0.541962638970732, 'chr_3': 0.4333399000412707, 'chr_4': 0.4188196397672343, 'chr_5': 0.39296304677246197, 'chr_6': 0.37549690291575505, 'chr_7': 0.377889743914048, 'chr_8': 0.34770567460042057, 'chr_9': 0.3895080423768545, 'chr_x': 0.3659903903152476, 'chr_y': 0.7586935225408524}
	tf.reset_default_graph()
	with tf.gfile.FastGFile(cwd+"/Classifier/v3/tf_files/retrained_graph.pb", 'rb') as f:
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
			label_lines = [line.rstrip() for line in tf.gfile.GFile(cwd+"/Classifier/v3/tf_files/retrained_labels.txt")]
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
			for node_id in top_k:
				human_string = label_lines[node_id]
				score = predictions[0][node_id]
				#print(node_id)
				print('%s (score = %.5f)' % (human_string, score))

	print("correct predictions are "+str(count))
	print("###################")
	print("Predicted Dict")
	print(predicted)
	print("###################")
	print("Unpredicted Dict")
	print(unpredicted)

	return predicted,unpredicted