from googletrans import Translator

# Initialize the Google Translate API translator
translator = Translator()

def translate_text(text, src='en', dest='te'):
    try:
        # Translate text
        translation = translator.translate(text, src=src, dest=dest)
        return translation.text
    except Exception as e:
        raise ValueError(f"Translation error: {e}")
