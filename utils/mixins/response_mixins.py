from typing import Union
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..application_exception import ApplicationException


class ResponseMixin:
    @staticmethod
    def __make_response(
            code: int = status.HTTP_200_OK,
            message: str = "OK",
            body: Union[dict, list, bool] = None,
    ):
        return Response(
            data={
                "body": body if body else [] if isinstance(body, list) else {},
                "status": {"code": code, "message": message},
            },
            status=code,
        )

    def success_response(self, body: Union[dict, list, bool] = None):
        return self.__make_response(body=body)

    def error_response(self, code: int, message: str, body=None):
        raise ApplicationException(code=code, message=message)


class ResponseModelViewSetMixin(ResponseMixin, ModelViewSet):
    request_serializer = None

    def serialize_request(self, serializer_class, request_data) -> dict:
        self.request_serializer = serializer_class
        request_serializer = self.request_serializer(data=request_data)
        if not request_serializer.is_valid():
            raise Exception(request_serializer.errors)
        return request_serializer.validated_data
