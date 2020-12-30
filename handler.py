import json
import boto3

translate_api = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)

def translate(event, context):
    request_body = json.loads(event['body'])
    
    text = request_body['text']
    source_language = request_body['source_language']
    target_language = request_body['target_language']

    result = translate_api.translate_text(Text=text, 
            SourceLanguageCode=source_language, TargetLanguageCode=target_language)
    
    body = {
        "text": result.get('TranslatedText')
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response