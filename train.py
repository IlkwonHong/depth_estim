from loader import dataset
import pickle
from torch.utils import data

if __name__ == '__main__':
    with open('train_file_list.pickle', 'rb') as f:
        file_list = pickle.load(f)

    train_dataset = dataset.TrainDatasetPtD(file_list)
    train_dataloader = data.DataLoader(train_dataset, batch_size=256, shuffle=True)

    i = 0

    for data in train_dataloader:
        print('hi')
        i = i + 1
        # data_depth, data_rgb, data_seg, data_u, data_v

    print(i)