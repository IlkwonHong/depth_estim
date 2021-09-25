import torch


class SimpleNet(torch.nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        # data_depth, data_rgb, data_seg, data_u, data_v
        # 4채널 : data_rgb, data_seg, data_u, data_v

        relu = torch.nn.ReLU()
        

        # conv2d(in_channels, out_channels, kernel_size, stride,..)
        # 480*640 -> 478*638 -> 476*636
        self.conv1 = torch.nn.Conv2d(4, 64, kernel_size=(3, 3), padding=(0, 0), stride=(1, 1))
        self.conv2 = torch.nn.Conv2d(64, 64, kernel_size=(3, 3), padding=(0, 0), stride=(1, 1))

        # contracting step
        # maxpool2d(kernel_size, stride, padding=0, dilation=1, return_indices=False, ceil_mode=False)
        self.pool1 = torch.nn.MaxPool2d()

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