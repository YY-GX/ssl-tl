from PIL import Image
import os
import os.path
import random
import torch.utils.data as data
from scipy.io import loadmat



class Flower102(data.Dataset):


    def __init__(self, root_dir, label_file='imagelabels.mat', mode = 'train', data_split='setid.mat', transforms=None):


        self.all_labels = loadmat(os.path.join(root_dir,label_file))['labels'][0]
        mapping = {'train':'trnid','val':'valid','test':'tstid'}
        self.split = loadmat(os.path.join(root_dir,data_split))[mapping[mode]][0]
        self.root = os.path.join(root_dir,'jpg')
        self.images = [os.path.join(self.root,'image_{:05d}.jpg'.format(id))for id in self.split]
        self.labels = [self.all_labels[id-1]-1 for id in self.split]


        self.transforms = transforms

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):
        """
        Args:
            index (int): Index
        Returns:
            tuple: (image, target) where target is index of the target class.
        """

        img = Image.open(self.images[index]).convert('RGB')
        target = self.labels[index]

        if self.transforms:
            img = self.transforms(img)

        return img, target

if __name__ == '__main__':
    Flower102('../../../../../../datasets/target/flower_data/')