# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:07:45 2020

@author: Alfredo
"""

#!/usr/bin/python
#
# Copyright (c) 2018, 2019 TainiTec Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os.path
import numpy as np
from numpy import *
from initial_processes import *
import parameters
import os
import matplotlib.pyplot as plt
prm = parameters.Parameters()
import mne
import xlrd


number_of_channels = 16
sample_rate = 250.4
sample_datatype = "int16"
display_decimation = 1

"Specifiy the start time and end times here!!!!" 

start_time=11410
end_time=11470


# start_time=81700
# end_time=81800

filename="F:\\Taini_Mouse\\201215\\Ephys Taini Data\\B_VGATCre1411_KA_SeizureInduction-2020_12_22-0000.dat"
#fn="C:\\Users\\Alfredo\\Desktop\\B_VGATCre1411_KA_SeizureInduction-2020_12_18-0000.dat"

def parse_dat(filename):
    '''Load a .dat file by interpreting it as int16 and then de-interlacing the 16 channels'''

    # Load the raw (1-D) data
    dat_raw = np.fromfile(filename, dtype=sample_datatype)

    # Reshape the (2-D) per channel data
    step = number_of_channels * display_decimation
    dat_chans = [dat_raw[c::step] for c in range(number_of_channels)]

    # Build the time array
    t = np.arange(len(dat_chans[0]), dtype=float) / display_decimation

    return dat_chans, t

dat_chans, t = parse_dat(filename)  
    
data=np.array(dat_chans)
length=(len(data[0]))

del(dat_chans)

#insert here save function to save data in smaller format



n_channels=16

channel_names=['MEC_1', 'MEC_2', 'MC_ipsi_1', 'Thal_PVT_1', 'Thal_PVT_3', 
                       'HPCipsi_1', 'EMG', 'HPCipsi_2', 'MC_Contra_1', 'MC_Contra_2', 
                       'Blank', 'MS_1', 'MS_2', 'MC_ipsi_2', 'HPC_contra_1', 'HPC_contra_2']
channel_types=['eeg','eeg','eeg','eeg','eeg','eeg','emg','eeg','eeg','eeg','emg','eeg','eeg','eeg','eeg','eeg']
        
    
'This creates the info that goes with the channels, which is names, sampling rate, and channel types.'
info = mne.create_info(channel_names, sample_rate, channel_types)


'This makes the object that contains all the data and info about the channels.'
'Computations like plotting, averaging, power spectrums can be performed on this object'


#Below is an MNE function to get index from data object.
t_idx=custom_raw.time_as_index([prm.get_starttime(), prm.get_endtime()])
sub_data1, times =custom_raw[prm.get_channel_1(), t_idx[0]:t_idx[1]] #H



# time_axis, sub_data = sub_time_data(data, start_time, end_time, sample_rate) #MNE object

# sub_datatp=sub_data.transpose()

custom_raw = mne.io.RawArray(data, info)

# plot_data=custom_raw.get_data(picks=[5, 0, 15, 13, 3, 12, 8])

# for x in range(len(plot_data)):
#     standardev=statistics.stdev(plot_data[x])
# #    print(standardev)
#     medi=statistics.median(plot_data[x])
# #    print(med)
#     for n in range(len(plot_data[x])):
#         print(n)
#         if plot_data[x, n]>8*standardev:
#             plot_data[x, n-10:n+10]=medi
        
#         if plot_data[x,n]<(-500):
#             plot_data[x, n-10:n+10]=medi
            
                       
#                    
#
#
# plot_all(plot_data[0,:], prm.get_sampling_rate(),'k')
# plot_all(plot_data[1,:]-1200, prm.get_sampling_rate(),'k') #k-black
# plot_all(plot_data[2,:]-2000, prm.get_sampling_rate(),'k')
# plot_all(plot_data[3,:]-3000, prm.get_sampling_rate(),'k')
# plot_all(plot_data[4,:]-4000, prm.get_sampling_rate(),'k')
# plot_all(plot_data[5,:]-5000, prm.get_sampling_rate(),'k')
# plot_all(plot_data[6,:]-6000, prm.get_sampling_rate(),'k')
'To do a basic plot below. The following can be added for specifc order of channels order=[4, 5, 3, 0, 1, 14, 15, 16]'
colors=dict(mag='darkblue', grad='b', eeg='k', eog='k', ecg='m',
    emg='g', ref_meg='steelblue', misc='k', stim='b',
    resp='k', chpi='k')

custom_raw.plot(None, 5, 20, 11412,color = colors, scalings = "auto", order=[15, 5, 0, 15, 13, 9, 3, 12], show_options = "true" )#0,1,5,7,14,15, 8,9, 13,2, 3,4, 11,12, 6


