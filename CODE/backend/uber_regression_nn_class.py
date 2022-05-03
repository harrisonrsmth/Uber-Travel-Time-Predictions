#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


# In[7]:


#Build convolutional neural network
class Uber_reg(nn.Module):
    def __init__(self):
        super(Uber_reg, self).__init__() #init Uber_reg's superclass

        #use GPU if available 
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        
        self.lin = nn.Sequential(
            nn.Linear(6, 64), #out 64 features
            # nn.BatchNorm2d(nf), 
            nn.LeakyReLU(0.01, inplace=True),
            
            nn.Linear(64, 32), #out 32
            # nn.BatchNorm2d(nf*2), #same as output channels
            nn.LeakyReLU(0.01, inplace=True),
            
            nn.Linear(32, 16), #out 16
            # nn.BatchNorm2d(nf*4),
            nn.LeakyReLU(0.01, inplace=True),
            
            nn.Linear(16, 8), #out 8
            # nn.BatchNorm2d(nf*2),
            nn.LeakyReLU(0.01, inplace=True),
            
            nn.Linear(8, 4), #out 4
            # nn.BatchNorm2d(nf),
            nn.LeakyReLU(0.01, inplace=True),

            nn.Linear(4, 2), #out 2
            nn.LeakyReLU(0.01, inplace=True),

            nn.Linear(2, 1), #out 1
            nn.LeakyReLU(0.01, inplace=True)
        )

        self.model_dir = 'checkpoints/'

        self.distance_mean = 12.210185789365196
        self.distance_max = 68.64447323801441
        self.distance_min = 0.2101942240567526
        self.day_of_week_mean = 4.051910014609448
        self.day_of_week_max = 7
        self.day_of_week_min = 1
        self.hour_bucket_mean = 1.5408693496868424
        self.hour_bucket_max = 3
        self.hour_bucket_min = 0
        self.temp_mean = 52.534307356161555
        self.temp_max = 81.5714
        self.temp_min = 24.875
        self.precip_mean = 0.013171941967445693
        self.precip_max = 0.26
        self.precip_min = 0.0
        self.wind_speed_mean = 8.918930698134712
        self.wind_speed_max = 22.25
        self.wind_speed_min = 0.0

    def forward(self, x):
        # print(1, x.shape)
        #reshape for dummy data with 1 feature
        # x = x.reshape((x.shape[0], 1))
        # print(2, x.shape)
        x = self.lin(x)
        # print(3, x.shape)
        return x

    def save_model(self):
        #saves the model state and optimizer state on the dict
        if not os.path.exists(self.model_dir):
            os.mkdir(self.model_dir)
        torch.save({
            'model_state_dict': self.state_dict(),
            'optimizer_state_dict': opt.state_dict()
        }, os.path.join(model_dir, 'checkpoint.pt'))
        print('model saved at', self.model_dir + 'checkpoint.pt')

    def load_model(self, load_optimizer=False):
        #load the model from the disk if it exists, skip if you don't need this part
        if os.path.exists(self.model_dir):
            checkpoint = torch.load(os.path.join(self.model_dir, 'checkpoint.pt'))
            self.load_state_dict(checkpoint['model_state_dict'])
            if load_optimizer:
                opt.load_state_dict(checkpoint['optimizer_state_dict'])
            print('loaded model from saved checkpoint')

    def predict_sample(self, sample):
        np_sample = np.array([sample])
        tensor_sample = torch.from_numpy(np_sample.astype(np.float32))
        prediction = self(tensor_sample.to(self.device))[0].item()
        return prediction

