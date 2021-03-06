from jetpack import jetroutine
from PIL import Image
import boto3
from aws_config_local import configs

@jetroutine
async def image_handler():
    s3 = boto3.client(
        's3',
        aws_access_key_id=configs().aws_access_key,
        aws_secret_access_key=configs().aws_secret_key
    )
    
    # download image from s3
    s3.download_file(configs().bucket_name, 'original/cats.jpg', 'cats.jpg')
    print("DOWNLOADED FILE")
    # resize image
    image_resize(400, 'cats.jpg', 'cats-resized-400.jpg')
    
    # upload image to s3
    response = s3.upload_file('cats-resized-400.jpg', configs().bucket_name, 'resized/cats-resized-400.jpg')
    print(response)
    
    return f"Image resized and uploaded back to {configs().bucket_name}/resized/"



def image_resize(width, source_name, target_name):
    basewidth = width
    img = Image.open(source_name)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(target_name)

# def main():
#     image_handler()

# if __name__ == "__main__":
#     main()
