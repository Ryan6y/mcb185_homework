import random
import time

def random_names(n, k):
	klist = list()
	kset = set()
	for _ in range(n):
		kmer = ''.join(random.choices('ACGT', k=k))
		klist.append(kmer)
		kset.add(kmer)
	return klist, kset

for size in range(1000, 10000, 1000):

	list1, set1 = random_names(size, 10)
	list2, set2 = random_names(size, 10)

	t0 = time.time()
	for name1 in list1:
		if name1 in list2: pass
	t1 = time.time()
	list_time = t1 - t0

	t0 = time.time()
	for name1 in list1:
		if name1 in set2: pass
	t1 = time.time()
	set_time = t1 - t0

	print(list_time, set_time, list_time/set_time)