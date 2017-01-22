# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
#test atom push
def frequency(o,n):
    return 440*2**((o-4)+(n-10)/12.)

os=np.arange(0,11)
ns=np.arange(1,13)

frecuencies=np.zeros((len(os),len(ns)))

for i in range(len(ns)):
    frecuencies[:,i]=frequency(os,ns[i])


frecuencies_flat=frecuencies.flatten()


notes_name=['DO','DO#','RE','RE#','MI','FA','FA#','SOL','SOL#','LA','LA#','SI']

def find_note(freq):
    print (freq)
    of=np.argmin(np.abs(frecuencies-freq))/frecuencies.shape[-1]
    nf=np.argmin(np.abs(frecuencies-freq))%frecuencies.shape[-1]
    print ('octave:', of)
    print ('note:', nf, notes_name[nf])
    print (frecuencies[of,nf])


def find_nearest_vector_index(array, value):
    n = np.array([abs(i-value) for i in array])
    nindex=np.apply_along_axis(np.argmin,0,n)

    return nindex

#%%
fs=44100

import time
s=time.time()
duration = 2 # seconds
myrecording = sd.rec(duration * fs, samplerate=fs, channels=1)
time.sleep(duration)

e=time.time()
print (e-s)

#%%
sd.play(myrecording,fs)


#%%

#x=np.linspace(0,100,10000)

#myrecording=np.sin(30*x)+0.5*np.cos(x)
#%%

while True:
    duration = 1 # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=1)
    time.sleep(duration)
    if myrecording.ndim==1:
        sound_array=np.copy(myrecording[:])
    if myrecording.ndim==2:
        sound_array=np.copy(myrecording[:,0])

#    fig=plt.figure()
#    bx=plt.subplot(312)
#    cx=plt.subplot(313)

#    ax=plt.subplot(311)

#    ax.plot(sound_array)
    transform=np.fft.fft(sound_array)

    freqs = np.fft.fftfreq(transform.shape[-1])*fs
    freqs=freqs[:len(freqs)/2]
    transform=transform[:len(transform)/2]
    #positions=np.arange(-len(transform)/2,len(transform)/2,1)
#    bx.plot(freqs,transform.real,freqs,transform.imag)
    transform_abs=np.sqrt(transform.real**2+transform.imag**2)
#    cx.plot(freqs,transform_abs,'bo')
    notes=4
    freq_detected=np.zeros(4)
    for i in range(notes):
        freq_detected[i]=np.abs(freqs[np.argmax(transform_abs)])

    freq=np.abs(freqs[np.argmax(transform_abs)])

    find_note(freq)

#%%

duration = 2 # seconds
myrecording = sd.rec(duration * fs, samplerate=fs, channels=1)

time.sleep(duration)
if myrecording.ndim==1:
    sound_array=np.copy(myrecording[:])
if myrecording.ndim==2:
    sound_array=np.copy(myrecording[:,0])

sound_array[:20000]=0
t=np.linspace(0,len(sound_array)/float(fs),len(sound_array) )
fig=plt.figure()
bx=plt.subplot(312)
cx=plt.subplot(313)

ax=plt.subplot(311)

ax.plot(sound_array)
transform=np.fft.fft(sound_array)

freqs = np.fft.fftfreq(transform.shape[-1])*fs
freqs=freqs[:len(freqs)/2]
transform=transform[:len(transform)/2]
#positions=np.arange(-len(transform)/2,len(transform)/2,1)`
bx.plot(freqs,transform.real,freqs,transform.imag)
transform_abs=np.sqrt(transform.real**2+transform.imag**2)
#notes=4
#freq_detected=np.zeros(4)
#for i in range(notes):
#    freq_detected[i]=np.abs(freqs[np.argmax(transform_abs)])

transform_abs[freqs<frecuencies[0,-1]]=0
freq=np.abs(freqs[np.argmax(transform_abs)])


find_note(freq)

index_freq=find_nearest_vector_index(frecuencies_flat,freq)
cut_up=frecuencies_flat[index_freq+1]#-frecuencies_flat[index_freq]
cut_down=frecuencies_flat[index_freq-1]#frecuencies_flat[index_freq]-
cx.plot(freqs,transform_abs)
cx.set_xscale('log')
#
#a=freqs<cut_up
#b=freqs>cut_down
#transform_abs[a*b]=0
#freq=np.abs(freqs[np.argmax(transform_abs)])
#cx.plot(freqs,transform_abs,'ro')

sd.play(myrecording,fs)
print ('second note')
find_note(freq)

#plt.figure()


sub_arrays=[sound_array[i*fs/10:(i+1)*fs/10] for i in range(len(sound_array)/(fs/10))]

grid_freqs=np.zeros((len(sub_arrays),len(sub_arrays[0])/2))
i=0
for array in sub_arrays:
    sub_transform=np.fft.fft(array)



    sub_freqs = np.fft.fftfreq(sub_transform.shape[-1])*fs
    sub_freqs=sub_freqs[:len(sub_freqs)/2]
    sub_transform=sub_transform[:len(sub_transform)/2]
    sub_transform_abs=np.sqrt(sub_transform.real**2+sub_transform.imag**2)
    sub_transform_abs[sub_freqs<frecuencies[0,-1]]=0
    sub_transform_abs[sub_freqs<200]=0

    sub_freq=np.abs(sub_freqs[np.argmax(sub_transform_abs)])

    find_note(sub_freq)

    grid_freqs[i,:]=sub_transform_abs[:]
    i=i+1

#sub_freqs


t_sub=[1./10*(i+1) for i in range(len(sound_array)/(fs/10))]
#%%
from matplotlib.colors import LogNorm
plt.figure()
#plt.contourf(grid_freqs.T,levels=[1e-3,1e-2,1e-1,1,1e1,1e2,1e3],cmap=plt.cm.viridis,norm = LogNorm())
log_freqs=np.log(sub_freqs)
log_freqs[0]=log_freqs[1]
X,Y=np.meshgrid(t_sub,log_freqs)
plt.contourf(X,Y,grid_freqs.T,cmap=plt.cm.viridis)
plt.colorbar()

#plt.xscale('log')
#plt.colorbar()
#%%
for i in range(grid_freqs.shape[0]):
    print (i)
    plt.plot(sub_freqs,grid_freqs[4,:])
    plt.xscale('log')
#    plt.yscale('log')
