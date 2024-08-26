from gtts import gTTS
from pydub import AudioSegment
import io

def text_to_speech(text, lang):
    try:
        # Convert text to speech using gTTS
        tts = gTTS(text=text, lang=lang)
        audio_file = io.BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        
        # Enhance audio quality with pydub
        audio_segment = AudioSegment.from_mp3(audio_file)
        audio_segment = audio_segment.set_frame_rate(44100)  # Set a higher sample rate
        enhanced_audio_file = io.BytesIO()
        audio_segment.export(enhanced_audio_file, format="mp3")
        enhanced_audio_file.seek(0)
        
        return enhanced_audio_file
    except ValueError as e:
        raise ValueError(f"Error in text_to_speech: {e}")
