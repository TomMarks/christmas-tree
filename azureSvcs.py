import wave
import torch
import torchaudio
import torchaudio.utils.ffmpeg_utils
import silero_vad_utils
import time

# Callback function for audio stream
""" def audio_callback(in_data, frame_count, time_info, status):
    global incoming_audio

    incoming_audio.append((in_data, frame_count, time_info, status))
    return (in_data, pyaudio.paContinue)

 """# Torchaudio microphone stream



# Setup channel info
FORMAT = torch.int16 # data type formate
FORMAT_STR = "s16p"
CHANNELS = 1 # Adjust to your number of channels
RATE = 16000 # Sample Rate
CHUNK = 1024 # Block Size
FRAMES_PER_CHUNK = 4000
RECORD_SECONDS = 5 # Record time
WAVE_OUTPUT_FILENAME = "file.wav"
USB_CARD_NUM = "3"
SOURCE_HW = "plughw:" + USB_CARD_NUM + "," + "0"

in_speech = False
incoming_audio = []

# Startup pyaudio instance
streamer = torchaudio.io.StreamReader(
    src=SOURCE_HW, # should select default microphone
    format="alsa"
    )

# configure the audio stream output
streamer.add_basic_audio_stream(frames_per_chunk=FRAMES_PER_CHUNK, sample_rate=RATE, format=FORMAT_STR, stream_index=0, num_channels=CHANNELS)
print("The number of source streams:", streamer.num_src_streams)
print(streamer.get_src_stream_info(0))
print(streamer.get_out_stream_info(0))

# start Recording
print("Stream opened...")

# aquisition loop
stream = streamer.stream(timeout=-1, backoff=1.0)
while 1:
    #print("Checking for audio...")
    buf = next(stream)
    if buf is not None:
        aud = silero_vad_utils.speech_in_audio(buf)
        if aud is not None:
            if in_speech == False:
                # print the current time
                in_speech = True
                print("Start of speech detected at %hh:mm:ss" % os.time())
        else:
            if in_speech == True:
                in_speech = False
                print("End of speech detected at %hh:mm:ss" % os.time())
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