from rest_framework import serializers


class TokenErrorSerializer(serializers.Serializer):
    detail = serializers.CharField()


class StatusSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    message = serializers.CharField()


class DictSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    value = serializers.CharField()
    code = serializers.CharField()


class MetaSerializer(serializers.Serializer):
    objects_count = serializers.IntegerField()
    objects_total = serializers.IntegerField()
    pages_count = serializers.IntegerField()
    page_number = serializers.IntegerField()


class NormalAnswerSerializer(serializers.Serializer):
    status = StatusSerializer()


class PaginationSerializer(NormalAnswerSerializer):
    meta = MetaSerializer()


class GetEhdAnswerSerializer(serializers.Serializer):
    req_id = serializers.CharField()
    doc_id = serializers.CharField()
