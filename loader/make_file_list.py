from glob import glob
import pickle

# Data File Path
train_data_path = 'A:\\test_data\\data\\data\\train'
test_data_path = 'A:\\test_data\\data\\data\\test'


def make_file_list(path):
    list_dir = glob(path + '\\*')
    file_list = list()
    for folder_idx in list_dir:
        folder_path = glob(folder_idx+'\\*_depth.png')

        for file_idx in folder_path:
            file_idx = file_idx.replace('_depth.png', '_')
            file_list.append(file_idx)

    return file_list


if __name__ == '__main__':
    train_file_list = make_file_list(train_data_path)
    test_file_list = make_file_list(test_data_path)

    with open('train_file_list.pickle', 'wb') as f:
        pickle.dump(train_file_list, f, pickle.HIGHEST_PROTOCOL)
    with open('test_file_list.pickle', 'wb') as f:
        pickle.dump(test_file_list, f, pickle.HIGHEST_PROTOCOL)

    # with open('test_file_list.pickle', 'rb') as f:
    #     data = pickle.load(f)