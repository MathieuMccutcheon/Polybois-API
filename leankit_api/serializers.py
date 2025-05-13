# leankit_api/serializers.py
from rest_framework import serializers

class BoardSerializer(serializers.Serializer):
    id    = serializers.CharField()
    title = serializers.CharField()

class CardSerializer(serializers.Serializer):
    id             = serializers.CharField()
    title          = serializers.CharField()
    lane_id        = serializers.CharField(source='laneId')
    is_done        = serializers.BooleanField(source='isDone')
    planned_start  = serializers.CharField(source='plannedStart', default=None)
    planned_finish = serializers.CharField(source='plannedFinish', default=None)
    updated_on     = serializers.DateTimeField(source='updatedOn')
