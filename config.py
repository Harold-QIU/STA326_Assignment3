# dataset name 
dataset = 'ml-1m'
assert dataset in ['ml-1m', 'pinterest-20']

# paths
main_path = 'Data/'

train_rating = main_path + '{}.train.rating'.format(dataset)
test_rating = main_path + '{}.test.rating'.format(dataset)
test_negative = main_path + '{}.test.negative'.format(dataset)
