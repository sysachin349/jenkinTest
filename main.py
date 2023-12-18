import boto3
from botocore.exceptions import ClientError

aws_access_key_id = 'AKIA2H2XH7UUDYL5OPNA'
aws_secret_access_key = '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'
aws_region = 'us-east-1'  

ses_client = boto3.client('ses', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

sender_email = 'newsletter@prohouseprojects.com'
recipient_email = 'sachiny@fecdirect.net'

subject = 'Hello from Amazon SES'
body = 'This is a test email sent using Amazon SES for testing purpose INBOX.'

message = {
    'Subject': {'Data': subject},
    'Body': {'Text': {'Data': body}}
}

try:
    response = ses_client.send_email(
        Source=sender_email,
        Destination={'ToAddresses': [recipient_email]},
        Message=message
    )
    print("Email sent! Message ID:", response['MessageId'])

except ClientError as e:
    print("Error sending email:", e.response['Error']['Message'])