import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Resizes an image uploaded to an S3 bucket and saves the resized version
    to another S3 bucket.
    """
    try:
        # Get the source bucket and key from the S3 event
        source_bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']

        # Define the destination bucket name
        destination_bucket_name = 'your-resized-images-bucket-name' # Replace with your bucket name

        # Get the image from the source S3 bucket
        response = s3.get_object(Bucket=source_bucket_name, Key=object_key)
        original_image_body = response['Body'].read()

        # Open the image using Pillow
        image = Image.open(io.BytesIO(original_image_body))

        # Define the desired size for the resized image
        # You can adjust these values as needed
        target_width = 200
        target_height = 200
        resized_image = image.resize((target_width, target_height))

        # Save the resized image to a BytesIO object
        buffer = io.BytesIO()
        resized_image.save(buffer, format=image.format or 'JPEG') # Use original format or default to JPEG
        buffer.seek(0)

        # Upload the resized image to the destination S3 bucket
        s3.put_object(
            Bucket=destination_bucket_name,
            Key=object_key, # You might want to modify the key for resized images
            Body=buffer,
            ContentType=f'image/{image.format.lower()}' if image.format else 'image/jpeg'
        )

        print(f"Successfully resized {object_key} from {source_bucket_name} to {destination_bucket_name}")

        return {
            'statusCode': 200,
            'body': 'Image resized successfully'
        }

    except Exception as e:
        print(f"Error processing image: {e}")
        return {
            'statusCode': 500,
            'body': f'Error resizing image: {str(e)}'
        }
