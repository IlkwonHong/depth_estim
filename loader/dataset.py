import cv2
from torch.utils.data import Dataset


class TrainDatasetPtD(Dataset):
    def __init__(self, file_list):
        self.file_list = file_list
        # self.mode = mode

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        data_path = self.file_list[idx]
        data_depth = cv2.imread(data_path + 'depth.png')
        data_rgb = cv2.imread(data_path + 'rgb.png')
        data_gray = cv2.cvtColor(data_rgb, cv2.COLOR_BGR2GRAY)
        data_seg = cv2.imread(data_path + 'rgb_dp_segm.png')
        data_u = cv2.imread(data_path + 'rgb_dp_u.png')
        data_v = cv2.imread(data_path + 'rgb_dp_v.png')

        return data_depth, data_gray, data_seg, data_u, data_v
