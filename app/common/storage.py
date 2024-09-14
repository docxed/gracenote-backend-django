from storages.backends.s3boto3 import S3Boto3Storage
from storages.utils import clean_name
from decouple import config
import uuid
import os


# Create your views here.
class MinioStorage(S3Boto3Storage):
    bucket_name = config("MINIO_BUCKET_NAME")
    default_acl = "public-read"

    def _save(self, name, content):
        # สร้างชื่อไฟล์ใหม่ให้เป็นเอกลักษณ์ด้วย UUID
        base_name, ext = os.path.splitext(name)  # ดึงนามสกุลไฟล์
        name = f"{base_name}-{uuid.uuid4()}{ext}"  # ใช้ UUID เพื่อสร้างชื่อไฟล์ใหม่
        cleaned_name = clean_name(name)
        name = self._normalize_name(cleaned_name)

        # ดำเนินการอัปโหลดไฟล์ตามปกติ
        return super()._save(name, content)
