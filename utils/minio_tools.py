from minio import Minio
from minio.error import S3Error
from config.settings import MINIO_END_POINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY


def connect_minio_client() -> Minio:
    minio_client = Minio(
        endpoint=MINIO_END_POINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=False
    )
    return minio_client
