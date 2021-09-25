import torch


class SimpleNet(torch.nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        # data_depth, data_rgb, data_seg, data_u, data_v

