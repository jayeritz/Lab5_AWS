import boto3
from botocore.exceptions import ClientError
import logging

s3_resource = boto3.resource('s3')

class HtmlDocument:
    def __init__(self, my_code):
        self.my_code= my_code
      
    def __str__(self):
        return f"CODE: {self.my_code}"


class HtmlManager:
    def __init__(self):
        self.my_document = None

    def create_html(self):
        
        my_code = """<html>
        <head></head>
        <body><br><p style="font-weight: bold; color:#FF69B4; font-size:32px">All I want to do is be better.</p><br>
        <p>
        <figure><img src="https://ih1.redbubble.net/image.994972411.5295/poster,840x830,f8f8f8-pad,1000x1000,f8f8f8.jpg" alt="Keep an Open Mind Girl!" width="500"
         height="500">
         <figcaption>Keep an Open Mind Girl!</figcaption>
         </figure>
         </p>
         </body>
        </html>"""

        new_doc = HtmlDocument(my_code)
        self.my_document = new_doc
        

    def save_my_file (self):
        with open("jamilahtmlcode.html", "w") as file:
            file.write(self.my_document.my_code)

class AWSManager:
    def __init__(self):
        pass
       # self.s3 = boto3.resource('s3')

    def upload_to_s3(self):
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file('jamilahtmlcode.html', 'lmtd-class', 'jamilahtmlcode.html')
            print(response)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def in_the_s3_bucket():
        bucket = boto3.resource('s3').Object('lmtd-class', '')
        contents = json.load(bucket.get()['Body']) 
        print(contents)   




manager = HtmlManager()

manager.create_html()
manager.save_my_file()

awsmanager = AWSManager()
#awsmanager.upload_to_s3()
awsmanager.in_the_s3_bucket()

