import boto3
import json
import uuid

# S3 bucket where MP3 files will be stored
BUCKET_NAME = "tts-bucket-11022026"

# Initialize AWS clients
polly = boto3.client('polly')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Parse incoming JSON
        body = json.loads(event['body'])
        text = body.get('text', '')
        voice = body.get('voice', 'Joanna')  # default voice

        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Text cannot be empty'})
            }

        # Generate speech using Polly
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId=voice
        )

        audio_stream = response['AudioStream'].read()
        file_name = f"{str(uuid.uuid4())}.mp3"

        # Save to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=audio_stream,
            ContentType='audio/mpeg'
        )

        # Generate pre-signed URL (valid 1 hour)
        url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET_NAME, 'Key': file_name},
            ExpiresIn=3600
        )

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'audio_url': url})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
