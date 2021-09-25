import torch
import torch.nn as nn
import torch.nn.functional as F


class SHNet(nn.Module):
    def __init__(self):
        super(SHNet, self).__init__()

        # 4채널 : data_rgb, data_seg, data_u, data_v

        # 640*480
        # (640-8+4)/4 = 159 * 119
        self.conv1 = nn.Conv2d(6, 16, kernel_size=(8, 8), padding=(2, 2), stride=(4, 4))
        # (159+2-5)/2 = 78 * 58
        self.conv2 = nn.Conv2d(16, 32, kernel_size=(5, 5), padding=(1, 1), stride=(2, 2))
        # 38*28
        self.conv3 = nn.Conv2d(32, 64, kernel_size=(4, 4), padding=(1, 1), stride=(2, 2))
        # 18*13
        self.conv4 = nn.Conv2d(64, 128, kernel_size=(4, 4), padding=(1, 1), stride=(2, 2))

        self.pool1 = nn.MaxPool2d()

        self.bn1



