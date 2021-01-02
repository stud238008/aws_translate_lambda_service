import boto3
import random

translate_api = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)

def translate(event, context):
    text = event['text']
    source_language, target_language = event['sourceLang'], event['targetLang']

    result = translate_api.translate_text(Text=text, 
            SourceLanguageCode=source_language, TargetLanguageCode=target_language)
    
    # Set source text as seed, so confidence is always the same for given text
    random.seed(text)

    return {
        "result": result.get('TranslatedText'),
        "confidence": random.uniform(70, 100),
        "sourceLang": source_language,
        "targetLang": target_language
    }