import tensorflow as tf
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf


rootdir = 'F:/dbit/sem 7/BE Project/Classifier/2 Level Classification/test/test_images_Group G'

for subdir, dirs, files in os.walk(rootdir): 
	#getting all folder names       
    a = dirs.copy()
    break

#creating a dictionary which is initiaized to 0
predicted = {new_list: 0 for new_list in a} 
print(predicted)
total = {new_list: 0 for new_list in a} 
print(total)
individual_acc = {new_list: 0 for new_list in a} 
print(individual_acc)
threshold_score = {new_list: 0 for new_list in a} 
print(threshold_score)
avg_threshold_score = {new_list: 0 for new_list in a} 
print(avg_threshold_score)


chr_21 = {new_list: 0 for new_list in a} 
#print(avg_threshold_score)
chr_22 = {new_list: 0 for new_list in a} 
#print(avg_threshold_score)
chr_y = {new_list: 0 for new_list in a} 
#print(avg_threshold_score)



with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

count = 0
with tf.Session() as sess:
	for subdir, dirs, files in os.walk(rootdir): 
		for file in files:

			lname = file.split('_')
			#print(name)        #['karyotype 105', '19.1.jpg']
			lname1 = lname[1].split('.')
			print(lname1)       #['19', '1', 'jpg']

			a = os.path.join(subdir,file)
			#print(a)
			b = a.split("\\")
			print(b)
			file_name = file
			image_path = a
			print(image_path)
			image_data = tf.gfile.FastGFile(image_path, 'rb').read()
			label_lines = [line.rstrip() for line in tf.gfile.GFile("tf_files/retrained_labels.txt")]
			softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
			predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
			top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
			print(top_k)
			name = label_lines[top_k[0]]
			name = name.split(" ")
			print(name[1])

			temp = file_name.split(".")
			print(temp)
			temp = temp[0].split("_")
			print(temp[1])


			total["chr_"+lname1[0]] += 1

			if(lname1[0]=="21"):
				chr_21["chr_"+name[1]] += 1
			if(lname1[0]=="22"):
				chr_22["chr_"+name[1]] += 1
			if(lname1[0]=="y"):
				chr_y["chr_"+name[1]] += 1


			if(lname1[0] != "" and temp[1]==name[1]):         
				score = predictions[0][top_k[0]]
				threshold_score["chr_"+lname1[0]] += score
				#increment 
				#print("chr_"+name1[0])
				predicted["chr_"+lname1[0]] += 1

			for node_id in top_k:
			    human_string = label_lines[node_id]
			    score = predictions[0][node_id]
			    #print(node_id)
			    print('%s (score = %.5f)' % (human_string, score))
	        

print("Number of Correct Predictions")
print(predicted)
print("####################################")
print("Total Number of Images")
print(total)
print("####################################")
print("Sum of Scores")
print(threshold_score)
print("####################################")

for key in avg_threshold_score:
	a = threshold_score[key]
	b = predicted[key]
	acc = (a/b)
	avg_threshold_score[key] = acc
print("Avg of Scores")
print(avg_threshold_score)
print("####################################")


for key in individual_acc:
	a = predicted[key]
	b = total[key]
	acc = (a/b)*100
	individual_acc[key] = acc
print("Individual class acc")
print(individual_acc)
print("####################################")


a = sum(predicted.values())
b = sum(total.values())
acc = (a/b)*100
print("Total accuracy is "+ str(acc))


print("chr_21 ")
print(chr_21)
print("chr_22 ")
print(chr_22)
print("chr_y ")
print(chr_y)




#print("correct predictions are "+str(count))

# name = "32"
# filename = os.listdir(name)
# print(filename)


# # for file in filename:
# # image_path = "karyotype 40_20.2_28.jpg"
# # #image_path = "32/"+file
# # image_data = tf.gfile.FastGFile(image_path, 'rb').read()
# # label_lines = [line.rstrip() for line
# #                    in tf.gfile.GFile("tf_files/retrained_labels.txt")]

# with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
#     graph_def = tf.GraphDef()
#     graph_def.ParseFromString(f.read())
#     _ = tf.import_graph_def(graph_def, name='')


# count = 0
# with tf.Session() as sess:
# 	for file in filename:
# 		#image_path = "karyotype 40_20.2_28.jpg"
# 		image_path = "32/"+file
# 		image_data = tf.gfile.FastGFile(image_path, 'rb').read()
# 		label_lines = [line.rstrip() for line in tf.gfile.GFile("tf_files/retrained_labels.txt")]
# 		softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
# 		predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
# 		top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
# 		print(top_k)
# 		name = label_lines[top_k[0]]
# 		name = name.split(" ")
# 		print(name[1])

# 		temp = image_path.split(".")
# 		print(temp)
# 		temp = temp[0].split("_")
# 		print(temp[1])

# 		if(temp[1]==name[1]):
# 			count=count+1
# 		for node_id in top_k:
# 		    human_string = label_lines[node_id]
# 		    score = predictions[0][node_id]
# 		    #print(node_id)
# 		    print('%s (score = %.5f)' % (human_string, score))
# print("correct predictions are "+str(count))