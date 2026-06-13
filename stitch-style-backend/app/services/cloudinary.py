import cloudinary
import cloudinary.uploader
from app.config.settings import settings

cloudinary.config(url=settings.CLOUDINARY_URL)

def upload_image(file_data):
    return cloudinary.uploader.upload(file_data)
