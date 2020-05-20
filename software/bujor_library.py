import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundcard as sc
from scipy.io import wavfile


def mySine(A,f,theta0,t):
    return(A*np.sin(2*np.pi*f*t)+theta0)

def myCosine(A,f,theta0,t):
    return(A*np.cos(2*np.pi*f*t)+theta0)

def myRamp(A,t1,t):
    return(A*(t>=t1))

def myBox(A,t1,t2,t):
    return(A*((t>=t1)&(t<t2)))

def myChirp(A,f,t):
    return(A*np.sin(2*np.pi*(f-alpha*t)*t))

def myWhiteNoise(A,t):
    n=np.random.rand(np.size(t))
    return(2*A*(n-n.mean()))

def myDFT(x):
    N=np.size(x)
    X=np.zeros(N,dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k]=X[k]+x[n]*np.exp(-2j*np.pi*k*n/N)
    return(X)

def plotInTime(x,fs):
    t=np.arange(0,np.size(x,0)/fs,1/fs)
    plt.plot(t,x)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

def plotInTimeAndSave(x,fs, path_for_save):
    t=np.arange(0,np.size(x,0)/fs,1/fs)
    plt.plot(t,x)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.savefig(path_for_save)
    
def plotInFrequency(x,fs):
    N=int(np.size(x,0)/2)
    if np.size(x,0)==1:
        X=np.fft.fft(x,axis=1)
    else:
        X=np.fft.fft(x,axis=0)
    X=np.abs(X)
    X=X[:N]
    f=np.arange(0,fs/2,fs/2/N)
    plt.plot(f,X)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)   

def plotInFrequencyAndSave(x,fs, path_for_save):
    N=int(np.size(x,0)/2)
    if np.size(x,0)==1:
        X=np.fft.fft(x,axis=1)
    else:
        X=np.fft.fft(x,axis=0)
    X=np.abs(X)
    X=X[:N]
    f=np.arange(0,fs/2,fs/2/N)
    plt.plot(f,X)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)   
    plt.savefig(path_for_save)


def freqResp(f,H):
    plt.figure()
    plt.plot(f,abs(H))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.title('Frequency response')
    plt.grid(True) 
    
def play(x,fs):
    sd.play(x, fs)

def record(t,fs):
    mike = sc.default_microphone()
    samples=fs*t
    x=mike.record(samples,fs)
    return(x)
    
def readWav(fileName):
    # this returns sampling frequency and signal: fs,y = readWav(s)
    return(wavfile.read(fileName))
    
def fadeIn(x,fs,dt):
    nSamples=dt*fs
    effect=np.linspace(0,1,nSamples)
    effect=np.stack((effect,effect),axis=0).T
    nTotalSamples=len(x)
#    y=x
    if nSamples<nTotalSamples:
        y=x[:nSamples]*effect
        y=np.concatenate((y,x[nSamples:,:]),axis=0)   
    else:
        y=x*effect[:nTotalSamples]
    return(y.astype('int16'))    
    
    