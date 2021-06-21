import os
import librosa

def segment_audio(path):

    SR = 16000
    DURATION = 30
    sample_fit = int(DURATION*SR)

    y, sr = librosa.load(path, sr=SR)

    num_segments = int(y.shape[0]/sample_fit)

    segments = []
    for i in range(num_segments):
        start_sample = sample_fit * i
        end_sample = start_sample + sample_fit
        
        segment = y[start_sample:end_sample]
        
        segments.append(segment)

    return segments



def compute_melgram(segments):

    SR = 16000
    N_FFT = 512
    HOP_LEN = 256
    N_MELS = 96

    melgrams = []
    for segment in segments:

        melgram = librosa.feature.melspectrogram(y=segment, sr=SR, hop_length=HOP_LEN, n_fft=N_FFT, n_mels=N_MELS)
        logam = librosa.amplitude_to_db(melgram).T

        melgrams.append(logam)

    return melgrams

    