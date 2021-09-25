import torch
import torch.nn.functional as F


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
        # 476*636 -> 238*318
        self.pool1 = torch.nn.MaxPool2d()

        # 238*318 -> 236*316 -> 234*314 -> 232*312
        self.conv3 = torch.nn.Conv2d(64, 128, kernel_size=(3, 3), padding=(0, 0), stride=(1, 1))
        self.conv4 = torch.nn.Conv2d(128, 128, kernel_size=(3, 3), padding=(0, 0), stride=(1, 1))
        self.conv5 = torch.nn.Conv2d(128, 128, kernel_size=(3, 3), padding=(0, 0), stride=(1, 1))
        # 232*312 -> 116*156
        self.pool2 = torch.nn.MaxPool2d()

        # 116*156 -> 114*154 -> 112*152
        self.conv6 = torch.nn.Conv2d(128, 256, kernel_size=(3, 3), padding=(0, 0), stride=(1, 1))
        self.conv7 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), padding=(0, 0), stride=(1, 1))
        # 112*152 -> 56*76 
        self.pool3 = torch.nn.MaxPool2d()

        # 56*76 -> 54*74 -> 52*72
        self.conv8 = torch.nn.Conv2d(256, 512, kernel_size=(3, 3), padding=(0, 0), stride=(1, 1))
        self.conv9 = torch.nn.Conv2d(512, 512, kernel_size=(3, 3), padding=(0, 0), stride=(1, 1))
        # 52*72 -> 26*36 
        self.pool4 = torch.nn.MaxPool2d()

        # 26*36 -> 24*34 -> 22*32
        self.conv10 = torch.nn.Conv2d(512, 1024, kernel_size=(3, 3), padding=(0, 0), stride=(1, 1))
        self.conv11 = torch.nn.Conv2d(1024, 1024, kernel_size=(3, 3), padding=(0, 0), stride=(1, 1))

        self.up1 = torch.nn.ConvTranspose2d(1024, 512, kernel_size=(2, 2), stride=(1, 1))

        self.bn1

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.pool1(x)

        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))
        x = F.relu(self.conv5(x))
        x = self.pool2(x)

        x = F.relu(self.conv6(x))
        x = F.relu(self.conv7(x))
        x = self.pool3(x)

        x = F.relu(self.conv8(x))
        x = F.relu(self.conv9(x))
        x = self.pool4(x)

        x = F.relu(self.conv10(x))
        x = F.relu(self.conv11(x))


















