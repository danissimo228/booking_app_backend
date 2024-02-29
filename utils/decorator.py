import logging
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, serializers
import functools
from django.http.response import HttpResponse
from utils.application_exception import ApplicationException


def normalize_data_to_log(data: dict):
    normalized_data = {}
    for key, value in data.items():
        if key in ('password', 'login', 'confirmPassword', 'username', 'email', 'confirmation_password'):
            normalized_data[key] = '********************'
        else:
            normalized_data[key] = value

    return normalized_data


def log_viewset_action(logger: logging.Logger):
    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(self, *args, **kwargs):
            request: Request = args[0]
            payload = {
                'kwargs': kwargs,
                'query_params': request.query_params,
                'data': normalize_data_to_log(request.data)
            }
            logger.info(
                f"{request.method} | {request.user} | {self.__class__.__name__} |{func.__name__} payload={payload}"
            )
            try:
                response: Response = func(self, *args, **kwargs)
            except serializers.ValidationError as ex:
                logger.info(
                    f"Error | {request.method} | {request.user} | "
                    f"{self.__class__.__name__} | {func.__name__} exception={str(ex)}"
                )
                return Response(
                    data={
                        'body': None,
                        'status': {
                            'message': ex.__dict__,
                            'code': status.HTTP_400_BAD_REQUEST
                        }
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            except ApplicationException as ex:
                logger.info(
                    f"Error | {request.method} |  {request.user} | "
                    f"{self.__class__.__name__} | {func.__name__} exception={str(ex)}"
                )
                return Response(
                    data={
                        'body': None,
                        'status': {
                            'message': f'{ex.message}',
                            'code': ex.code
                        }
                    },
                    status=ex.code
                )
            except Exception as ex:
                logger.info(
                    f"Error | {request.method} |  {request.user} | "
                    f"{self.__class__.__name__} | {func.__name__} exception={str(ex)}"
                )
                return Response(
                    data={
                        'body': None,
                        'status': {
                            'message': f'{ex}',
                            'code': status.HTTP_400_BAD_REQUEST
                        }
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            if isinstance(response, HttpResponse):
                res_data = response.data
                if 'meta' in response.data:
                    res_data = res_data['meta']
                if 'body' in response.data:
                    if 'meta' in response.data['body']:
                        res_data = res_data['body']['meta']
                logger.info(
                    f"{request.method} |  {request.user} | {self.__class__.__name__} | {func.__name__} "
                    f"response={normalize_data_to_log(res_data)}")
            return response
        return _wrapper
    return _decorator
