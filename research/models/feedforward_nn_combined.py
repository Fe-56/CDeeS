import torch
import torch.nn as nn
import math

class NeuralNetworkCombined(nn.Module):
    def __init__(self, input_size, output_size=2, dropout_prob=0.0):
        super(NeuralNetworkCombined, self).__init__()

        self.hidden_size = math.ceil((input_size**0.5) * 1.5)
        self.p = dropout_prob

        self.layers = nn.Sequential(
            nn.Linear(input_size, self.hidden_size),
            nn.ReLU(),
            # nn.Dropout(self.p),
            nn.Linear(self.hidden_size, self.hidden_size),
            nn.ReLU(),
            # nn.Dropout(self.p),
            nn.Linear(self.hidden_size, self.hidden_size),
            nn.ReLU(),
            # nn.Dropout(self.p),
            nn.Linear(self.hidden_size, self.hidden_size),
            nn.ReLU(),
            # nn.Dropout(self.p),
            nn.Linear(self.hidden_size, self.hidden_size),
            nn.ReLU(),
            # nn.Dropout(self.p),
            nn.Linear(self.hidden_size, output_size)
        )

    def forward(self, x):
        return self.layers(x)
    