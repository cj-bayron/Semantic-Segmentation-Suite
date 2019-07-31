'''splitter
'''
import glob
import shutil
import random

def split(train_dir, train_label_dir, val_dir, val_label_dir, num_val):
    '''split data into training/validation sets
    '''
    # move all to training directories
    for im in glob.glob(val_dir + '/*'):
        shutil.move(im, train_dir)

    for im in glob.glob(val_label_dir + '/*'):
        shutil.move(im, train_label_dir)

    inputs = glob.glob(train_dir + '/*')
    labels = glob.glob(train_label_dir + '/*')

    inputs.sort()
    labels.sort()
    assert(len(inputs) == len(labels))

    val_indices = random.sample(range(len(inputs)), num_val)

    val_inputs, val_labels = [], []
    for idx in val_indices:
        shutil.move(inputs[idx], val_dir)
        shutil.move(labels[idx], val_label_dir)


if __name__ == "__main__":
    split(train_dir='train', train_label_dir='train_labels',
          val_dir='val', val_label_dir='val_labels', num_val=100)