import boto3

translate_api = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)

def translate(event, context):
    text = event['text']
    source_language, target_language = event['sourceLang'], event['targetLang']

    result = translate_api.translate_text(Text=text, 
            SourceLanguageCode=source_language, TargetLanguageCode=target_language)
    
    return {
        "text": result.get('TranslatedText')
    }