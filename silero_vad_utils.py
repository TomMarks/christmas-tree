import datetime
import torch
import torchaudio

SAMPLING_RATE = 16000
USE_ONNX = False # change this to True if you want to test onnx model

# need to pip install soundfile or you will get "no backend" error from torch
from pprint import pprint

# download example
# torch.hub.download_url_to_file('https://models.silero.ai/vad_models/en.wav', 'en_example.wav')

# if USE_ONNX:
#     !pip install -q onnxruntime

# Local model
model, utils = torch.hub.load(
    repo_or_dir='silero-vad',
    source='local',
    model='silero_vad',
    force_reload=True,
    onnx=USE_ONNX)

# Repo model
""" model, utils = torch.hub.load(repo_or_dir='snakers4/silero-vad',
                              model='silero_vad',
                              force_reload=True,
                              onnx=USE_ONNX)
 """
(get_speech_timestamps,
 save_audio,
 read_audio,
 VADIterator,
 collect_chunks) = utils

# Used to step through audio chunks
vad_iterator = VADIterator(model)

# *** Import Ends / Code Begins ***

def speech_in_audio(audio_tensor_list):
    """
    Extracts speech chunks from audio data using a voice activity detection (VAD) model.

    Args:
        audio_data (list): The audio data as a list of samples.

    Returns:
        tensor: A tensor object containing only the speech.

    Raises:
        None.

    """
    #try:
    print(f"Audio tensor shape: {audio_tensor_list[0].shape}")
    speech_timestamps = get_speech_timestamps(audio_tensor_list[0].data, model, sampling_rate=SAMPLING_RATE)
    pprint(speech_timestamps)
    # Remove speechless chunks
    chunks = collect_chunks(speech_timestamps, wav)
    return torch.tensor(chunks)
    #except:
    #    return None

def speech_in_audio_streaming(audio_data):
    """
    Extracts speech chunks from audio data using a voice activity detection (VAD) model.

    Args:
        audio_data (list): The audio data as a list of samples.

    Returns:
        tensor: A tensor object containing only the speech.

    Raises:
        None.

    """
    try:
        wav = torch.tensor(audio_data)
        speech_timestamps = get_speech_timestamps(wav, model, sampling_rate=SAMPLING_RATE)
        pprint(speech_timestamps)
        # Remove speechless chunks
        chunks = collect_chunks(speech_timestamps, wav)
        return torch.tensor(chunks)
    except:
        return None
# (in_data, frame_count, time_info, status)

# Take audio from the microphone, get speech timestamps, and save speech chunks to file

""" with torch.no_grad():
    vad_stream = VADIterator()
    for i, chunk in enumerate(vad_stream(wav)):
        save_audio(f'chunk_{i}.wav', [chunk], SAMPLING_RATE)
        if i > 10:
            break
        print(f'Processed chunk {i}')
        print(chunk.shape)
 """
