import torch
import torch.nn as nn

class Discriminator(nn.Module):

    # define Conv block for discriminator 
    def convBlock(self, in_channels, out_channels, kernel_size, stride, padding, bachnorm=True):
        if bachnorm:
            block = nn.Sequential(
                nn.Conv2d(
                    in_channels = in_channels,
                    out_channels = out_channels, 
                    kernel_size = kernel_size,
                    stride = stride,
                    padding = padding, 
                    bias = False
                ),
                nn.BatchNorm2d(out_channels),
                nn.LeakyReLU(0.2, inplace=True),
            )
        else:
            block = nn.Sequential(
                nn.Conv2d(
                    in_channels = in_channels,
                    out_channels = out_channels, 
                    kernel_size = kernel_size,
                    stride = stride,
                    padding = padding, 
                    bias = False
                ),
                nn.LeakyReLU(0.2, inplace=True),
            )
        return block
    def __init__(self, image_channel:int=3) -> None:
        super().__init__()
        self.image_channel = image_channel
        self.discriminator = nn.Sequential(

            self.convBlock(
                in_channels = self.image_channel,
                out_channels = 64, 
                kernel_size = 4,
                stride = 2,
                padding = 1, 
                bachnorm=False
            ),
            
            self.convBlock(
                in_channels = 64,
                out_channels = 128, 
                kernel_size = 4,
                stride = 2,
                padding = 1, 
                bachnorm=True
            ),

            self.convBlock(
                in_channels = 128,
                out_channels = 256, 
                kernel_size = 4,
                stride = 2,
                padding = 1, 
                bachnorm=True
            ),

            self.convBlock(
                in_channels = 256,
                out_channels = 512, 
                kernel_size = 4,
                stride = 2,
                padding = 1, 
                bachnorm=True
            ),

            nn.Conv2d(
                in_channels = 512,
                out_channels = 1, 
                kernel_size = 4,
                stride = 1,
                padding = 0, 
                bias = False
            ),
            nn.Sigmoid()
        )
    
    def forward(self, input):
        return self.discriminator(input)
