#24accuracy.py by Zhiying He

def accuracy(tp, fp, tn, fn):
	precision = tp/(tp+fp)
	recall = tp/(tp+fn)
	F1 = 2*precision*recall/(precision+recall)
	acy = (tp+tn)/(tp+fn+tn+fp)
	return acy, F1

print(accuracy(1, 2, 3, 4))
print(accuracy(1, 3, 5, 7))
