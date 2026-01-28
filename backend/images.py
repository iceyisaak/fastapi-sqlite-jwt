from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    # public_key=os.getenv("IMAGE_PUBLIC_KEY"),
    # base_url=os.getenv("IMAGEKIT_URL")
)

URL_ENDPOINT=os.getenv("IMAGEKIT_URL_ENDPOINT")