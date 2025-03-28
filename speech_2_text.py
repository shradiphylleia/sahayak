import io
import torch
import torchaudio
import numpy as np
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq

MODEL_ID = "erax-ai/EraX-WoW-Turbo-V1.0"
try:
    PROCESSOR = AutoProcessor.from_pretrained(MODEL_ID)
    MODEL = AutoModelForSpeechSeq2Seq.from_pretrained(MODEL_ID)
except Exception as e:
    print(f"Error initializing model: {e}")
    PROCESSOR = None
    MODEL = None

def speech_text(audio_input):
    """
    transcribe streamlit audio input to text using the pre-initialized model.
    
    Args:
        audio_input:BytesIO object
    
    Returns:
        str:text from the audio
    """
    if PROCESSOR is None or MODEL is None:
        raise RuntimeError("Model was not properly initialized")

    try:
        if not isinstance(audio_input, io.BytesIO):
            audio_input = io.BytesIO(audio_input)

        waveform, sample_rate = torchaudio.load(audio_input)

        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
            waveform = resampler(waveform)

        waveform = waveform.numpy().squeeze()
        inputs = PROCESSOR(waveform, sampling_rate=16000, return_tensors="pt")

        with torch.no_grad():
            generated_ids = MODEL.generate(**inputs)
        
        transcription = PROCESSOR.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        return transcription
    
    except Exception as e:
        print(f"Error during audio transcription: {e}")
        return "" 