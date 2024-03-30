from minio import Minio
from minio.error import S3Error
from config.settings import MINIO_END_POINT, MINIO_ROOT_USER, MINIO_ROOT_PASSWORD


def connect_minio_client() -> Minio:
    minio_client = Minio(
        endpoint=MINIO_END_POINT,
        access_key='rootuser',
        secret_key='rootpassword',
        secure=False
    )
    return minio_client


def save_object_minio(file_path: str, bucket: str, obj_name: str) -> str:
    try:
        minio_client = connect_minio_client()
        if not minio_client.bucket_exists(bucket_name=bucket):
            minio_client.make_bucket(bucket_name=bucket)
        minio_client.fput_object(
            bucket_name=bucket,
            object_name=obj_name,
            file_path=file_path
        )
        url = minio_client.presigned_get_object(
            bucket_name=bucket,
            object_name=obj_name
        )
        return url
    except S3Error as ex:
        raise Exception(ex.message)
    except Exception as ex:
        raise Exception(str(ex))


def get_url_minio(obj_name: str, bucket: str) -> str | None:
    try:
        minio_client = connect_minio_client()
        minio_client.stat_object(
            bucket_name=bucket,
            object_name=obj_name
        )
        url = minio_client.presigned_get_object(
            bucket_name=bucket,
            object_name=obj_name
        )
        return url
    except S3Error as ex:
        return
    except Exception as ex:
        return


def download_object_from_minio(obj_name: str, bucket: str) -> None:
    try:
        minio_client = connect_minio_client()
        minio_client.fget_object(
            bucket_name=bucket,
            object_name=obj_name,
            file_path=obj_name
        )
    except S3Error as ex:
        raise Exception(ex.message)
    except Exception as ex:
        raise Exception(str(ex))


def delete_object_minio(obj_name: str, bucket: str) -> None:
    try:
        minio_client = connect_minio_client()
        if not minio_client.bucket_exists(bucket_name=bucket):
            minio_client.make_bucket(bucket_name=bucket)
        minio_client.stat_object(
            bucket_name=bucket,
            object_name=obj_name
        )
        minio_client.remove_object(
            bucket_name=bucket,
            object_name=obj_name
        )
    except S3Error as ex:
        raise Exception(ex.message)
    except Exception as ex:
        raise Exception(str(ex))
