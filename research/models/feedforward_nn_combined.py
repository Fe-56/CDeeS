import torch
import torch.nn as nn
import math

class NeuralNetworkCombined(nn.Module):
    def __init__(self, input_size):
        super(NeuralNetworkCombined, self).__init__()
        self.num_of_units = math.ceil((input_size**0.5) * 1.5)
        self.layers = nn.Sequential(
            nn.Linear(input_size, self.num_of_units),
            nn.ReLU(),
            nn.Linear(self.num_of_units, self.num_of_units),
            nn.ReLU(),
            nn.Linear(self.num_of_units, self.num_of_units),
            nn.ReLU(),
            nn.Linear(self.num_of_units, self.num_of_units),
            nn.ReLU(),
            nn.Linear(self.num_of_units, self.num_of_units),
            nn.ReLU(),
            nn.Linear(self.num_of_units, 2)
        )

    def forward(self, x):
        return self.layers(x)
    