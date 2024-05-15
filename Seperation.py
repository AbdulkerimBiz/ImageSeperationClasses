import os
import shutil
from sklearn.model_selection import train_test_split

#The souce
source_folder = 'Train'
#destination
destination_folder = 'Train'

# Train, Test ve Validation rates
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# creation directories
for split in ['train', 'test', 'validation']:
    os.makedirs(os.path.join(destination_folder, split), exist_ok=True)

# determine to class names A_001 B_001 the images names like that
classes = set()
for filename in os.listdir(source_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        class_name = filename.split('_')[0]
        classes.add(class_name)

# create directory for each classes
for class_name in classes:
    for split in ['train', 'test', 'validation']:
        os.makedirs(os.path.join(destination_folder, split, class_name), exist_ok=True)

# seperate folder and copy 
for class_name in classes:
    files = [f for f in os.listdir(source_folder) if f.startswith(class_name)]
    train_files, temp_files = train_test_split(files, test_size=(1 - train_ratio))
    val_files, test_files = train_test_split(temp_files, test_size=(test_ratio / (val_ratio + test_ratio)))

    for file in train_files:
        shutil.copy(os.path.join(source_folder, file), os.path.join(destination_folder, 'train', class_name, file))

    for file in val_files:
        shutil.copy(os.path.join(source_folder, file), os.path.join(destination_folder, 'validation', class_name, file))

    for file in test_files:
        shutil.copy(os.path.join(source_folder, file), os.path.join(destination_folder, 'test', class_name, file))

print("Dataset split completed.")
