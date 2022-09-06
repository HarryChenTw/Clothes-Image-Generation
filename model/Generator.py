import torch
import torch.nn as nn


class Generator(nn.Module):

    # define convTrans block for generator 
    def convTransBlock(self, in_channels, out_channels, kernel_size, stride, padding):
        block = nn.Sequential(
            nn.ConvTranspose2d(
                in_channels = in_channels, 
                out_channels = out_channels, 
                kernel_size = kernel_size, 
                stride = stride,
                padding = padding,
                bias = False
            ),
            nn.BatchNorm2d(num_features = out_channels),
            nn.ReLU(inplace = True)
        )
        return block
    
    def __init__(self, generator_input_size:int=100, image_size:int=64, image_channel:int=3) -> None:
        super().__init__()
        self.generator_input_size = generator_input_size
        self.image_size = image_size
        self.image_channel = image_channel

        self.generator = nn.Sequential(

            self.convTransBlock(
                in_channels = self.generator_input_size,
                out_channels = 512,
                kernel_size = 4,
                stride = 1,
                padding = 0
            ),

            self.convTransBlock(
                in_channels = 512,
                out_channels = 256,
                kernel_size = 4,
                stride = 2,
                padding = 1
            ),

            self.convTransBlock(
                in_channels = 256,
                out_channels = 128,
                kernel_size = 4,
                stride = 2,
                padding = 1
            ),

            self.convTransBlock(
                in_channels = 128,
                out_channels = 64,
                kernel_size = 4,
                stride = 2,
                padding = 1
            ),

            self.convTransBlock(
                in_channels = 64,
                out_channels = 32,
                kernel_size = 4,
                stride = 2,
                padding = 1
            ),

            nn.ConvTranspose2d(
                in_channels = 32, 
                out_channels = self.image_channel, 
                kernel_size = 4, 
                stride = 2,
                padding = 1,
                bias = False
            ),
            nn.Tanh()
        )
        
    def forward(self,input):
        return self.generator(input)