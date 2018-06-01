def merge(array):
	if len(array) > 1:
		print("Splitting", array)
		half = len(array)//2
		left = array[:half]
		#print(left)
		right = array[half:]
		#print(right)
		merge(left)
		merge(right)
		
		i = 0
		j = 0
		k = 0
		
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				array[k] = left[i]
				i+=1
			else:
				array[k] = right[j]
				j+=1
			k+=1
		while i < len(left):
			array[k] = left[i]
			i+=1
			k+=1
		while j < len(right):
			array[k] = right[j]
			j+=1
			k+=1
	print('merging', array)
array = [1,5,7,8,6,2,4,3]
merge(array)
print(array)