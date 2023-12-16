import wave
import torch
import torchaudio
import pyaudio
import silero_vad_utils
import time

# Callback function for audio stream
def audio_callback(in_data, frame_count, time_info, status):
    global audio_buffer

    # Add to the list as a tuple in case we need any of this
    audio_buffer.append((in_data, frame_count, time_info, status))
    return (in_data, pyaudio.paContinue)
# end audio_callback

# Initialize globals
in_speech = False
audio_buffer = []

# Setup channel info
FORMAT = pyaudio.paInt16 # data type formate
CHANNELS = 1 # Adjust to your number of channels
RATE = 16000 # Sample Rate
CHUNK = 2000 # Block Size
FRAMES_PER_CHUNK = 4000

# start Recording
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
    frames_per_buffer=CHUNK, stream_callback=audio_callback)
print("Stream opened...")

# aquisition loop
while 1:
    if audio_buffer is not None and audio_buffer.count > 0:
        aud = silero_vad_utils.speech_in_audio(audio_buffer)
        if aud is not None:
            if in_speech == False:
                # print the current time
                in_speech = True
                print(f"Start of speech detected at {os.time(): %x}")
        else:
            if in_speech == True:
                in_speech = False
                print("End of speech detected at %x" % os.time())
    else:
        time.sleep(0.1)
    


""" # If the VAD is not detecting speech, mark the start time and set the in_speech variable to True
if in_speech == False:
    in_speech = True
    print("Start of speech detected at %hh:mm:ss" % os.time())

# Append the data to the frames array for saving later
frames.append(in_data)

# If the VAD is detecting speech, mark the end time and set the in_speech variable to False
if in_speech == True:
    in_speech = False
    print("End of speech detected at %hh:mm:ss" % os.time())


# Record for RECORD_SECONDS
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

aud = silero_vad_utils.speech_in_audio(frames)

if aud is not None:
    if in_speech == False:
        
        # print the current time
        in_speech = True
        print("Start of speech detected at %hh:mm:ss" % os.time())
    print(aud.shape)
 """
# Stop Recording
streamer.remove_stream(0)

# Write your new .wav file with built in Python 3 Wave module
""" waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close() """