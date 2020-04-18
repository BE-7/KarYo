import tensorflow as tf
import sys
import os
# cwd = "G:/Karyotyping"
# print(cwd)
cwd = os.getcwd()

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
sys.path.insert(1, cwd+'/Classifier/Group A Classifier')
from groupA_Classifier import groupA_Classifier
sys.path.insert(1, cwd+'/Classifier/Group B Classifier')
from groupB_Classifier import groupB_Classifier
sys.path.insert(1, cwd+'/Classifier/Group C Classifier')
from groupC_Classifier import groupC_Classifier
sys.path.insert(1, cwd+'/Classifier/Group D Classifier')
from groupD_Classifier import groupD_Classifier
sys.path.insert(1, cwd+'/Classifier/Group E Classifier')
from groupE_Classifier import groupE_Classifier
sys.path.insert(1, cwd+'/Classifier/Group F Classifier')
from groupF_Classifier import groupF_Classifier
sys.path.insert(1, cwd+'/Classifier/Group G Classifier')
from groupG_Classifier import groupG_Classifier

def TSCM_classifier(target):
	#print("works")
	imageDir = target+"/Original_after_max/"
	filename = os.listdir(imageDir)
	print(filename)
	# cwd = os.getcwd()
	# threshold = {'chr_1': 0.7005995916377785, 'chr_10': 0.4755305751011922, 'chr_11': 0.5514257906848549, 'chr_12': 0.559018386543816, 'chr_13': 0.589966843652929, 'chr_14': 0.6609391017984121, 'chr_15': 0.5838806254741473, 'chr_16': 0.5823814703358544, 'chr_17': 0.565929741686226, 'chr_18': 0.6527430527230613, 'chr_19': 0.665208366054755, 'chr_2': 0.5877262700954055, 'chr_20': 0.6467213091305178, 'chr_21': 0.8292170328080145, 'chr_22': 0.6091317460577712, 'chr_3': 0.4931755405333307, 'chr_4': 0.5620491582359004, 'chr_5': 0.5397103494431219, 'chr_6': 0.4842160374053523, 'chr_7': 0.5146558618108774, 'chr_8': 0.4306479982239135, 'chr_9': 0.5489281096991072, 'chr_x': 0.45030022453030816, 'chr_y': 0.9058650792861471}
	threshold = {'group a': 0.8444676472308345, 'group b': 0.8090349167274121, 'group c': 0.7297357970727424, 'group d': 0.8734794594034324, 'group e': 0.7846987010310184, 'group f': 0.7985919211716459, 'group g': 0.883614893560183}
	tf.reset_default_graph()

	with tf.gfile.FastGFile(cwd+"/Classifier/Group Classifier/tf_files/retrained_graph.pb", 'rb') as f:
		graph_def = tf.GraphDef()
		graph_def.ParseFromString(f.read())
		_ = tf.import_graph_def(graph_def, name='')

	predicted = {}
	unpredicted = {}
	total = 0
	groupA = []
	groupB = []
	groupC = []
	groupD = []
	groupE = []
	groupF = []
	groupG = []

	with tf.Session() as sess:
		for file in filename:
			image_path = imageDir+file
			image_data = tf.gfile.FastGFile(image_path, 'rb').read()
			label_lines = [line.rstrip() for line in tf.gfile.GFile(cwd+"/Classifier/Group Classifier/tf_files/retrained_labels.txt")]
			softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
			predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
			top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
			print(top_k)
			name = label_lines[top_k[0]]
			print(name)

			# if(name == "group a"):
			# 	value,flag = groupA_Classifier(imageDir,file)
			# 	if(flag==1):
			# 		predicted.update({file:value[file]})
			# 	else:
			# 		unpredicted.update({file:value[file]})

			if(name == "group a"):
				groupA.append(file)
			if(name == "group b"):
				groupB.append(file)
			if(name == "group c"):
				groupC.append(file)
			if(name == "group d"):
				groupD.append(file)
			if(name == "group e"):
				groupE.append(file)
			if(name == "group f"):
				groupF.append(file)
			if(name == "group g"):
				groupG.append(file)																							
			# name = name.split(" ")
			# temp = name[0]+"_"+name[1]
			# #print(name[1])
			# score = predictions[0][top_k[0]]
			# print(score)
			# print(threshold[temp])
			# if(score>=threshold[temp]):
			# 	count=count+1
			# 	predicted.update({file:temp})
			# 	print("incremented count")
			# else:
			# 	unpredicted.update({file:temp})	
			for node_id in top_k:
				human_string = label_lines[node_id]
				score = predictions[0][node_id]
				#print(node_id)
				print('%s (score = %.5f)' % (human_string, score))
	
	print("###")
	print(groupA)
	print(groupB)
	print(groupC)
	print(groupD)
	print(groupE)
	print(groupF)
	print(groupG)
	
	tf.reset_default_graph()
	print("Group A starts")
	pred, unpred, count = groupA_Classifier(imageDir,groupA)
	total = total + count
	for key,value in pred.items():
		predicted.update({key:value})
	for key,value in unpred.items():
		unpredicted.update({key:value})

	tf.reset_default_graph()
	print("Group B starts")
	pred, unpred, count = groupB_Classifier(imageDir,groupB)
	total = total + count
	for key,value in pred.items():
		predicted.update({key:value})
	for key,value in unpred.items():
		unpredicted.update({key:value})


	tf.reset_default_graph()
	print("Group C starts")
	pred, unpred, count = groupC_Classifier(imageDir,groupC)
	total = total + count
	for key,value in pred.items():
		predicted.update({key:value})
	for key,value in unpred.items():
		unpredicted.update({key:value})		

	tf.reset_default_graph()
	print("Group D starts")
	pred, unpred, count = groupD_Classifier(imageDir,groupD)
	total = total + count
	for key,value in pred.items():
		predicted.update({key:value})
	for key,value in unpred.items():
		unpredicted.update({key:value})

	tf.reset_default_graph()
	print("Group E starts")	
	pred, unpred, count = groupE_Classifier(imageDir,groupE)
	total = total + count
	for key,value in pred.items():
		predicted.update({key:value})
	for key,value in unpred.items():
		unpredicted.update({key:value})

	tf.reset_default_graph()
	print("Group F starts")
	pred, unpred, count = groupF_Classifier(imageDir,groupF)
	total = total + count
	for key,value in pred.items():
		predicted.update({key:value})
	for key,value in unpred.items():
		unpredicted.update({key:value})

	tf.reset_default_graph()
	print("Group G starts")
	pred, unpred, count = groupG_Classifier(imageDir,groupG)
	total = total + count
	for key,value in pred.items():
		predicted.update({key:value})
	for key,value in unpred.items():
		unpredicted.update({key:value})

	print("correct predictions are "+str(total))
	print("###################")
	print("Predicted Dict")
	print(predicted)
	print("###################")
	print("Unpredicted Dict")
	print(unpredicted)

	return predicted,unpredicted

# TSCM_classifier(cwd+"/chromosome_data/original 32/")