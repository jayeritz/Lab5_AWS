import boto3

# to connect to the s3 resource
s3_resource = boto3.resource('s3')

class HtmlDocument:
    def __init__(self, my_code):
        self.my_code= my_code
      
    def __str__(self):
    return f"CODE: {self.my_code}"


class HtmlManager:
    def create_html(self):
        
        my_code = """<html>
        <head><style type='text/css'>
        .pink { color: #FF69B4; }
        </style></head>
        <body><p>All I want to do is be better.</p>
        <p><img src="https://ih1.redbubble.net/image.994972411.5295/poster,840x830,f8f8f8-pad,1000x1000,f8f8f8.jpg" alt="Keep an Open Mind Girl!" width="500"
         height="500"></p></body>
        </html>"""
        
        with open("jamilahtmlcode.html", "w") as file:
            file.write(my_code)

    def save_my_file (self):



class AWSManager
pass