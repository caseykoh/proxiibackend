from rest_framework import serializers
from . models import *

class SubmissionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionImage
        fields = ('image_url',)

class InquirySubmissionSerializer(serializers.ModelSerializer):
    images = SubmissionImageSerializer(many=True, required=False)

    class Meta:
        model = InquirySubmission
        fields = ('first_name', 'last_name', 'email', 'instagram', 'design_type', 'description', 'date', 'images',)
    
    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        submission = InquirySubmission.objects.create(**validated_data)
        for image_data in images_data:
            SubmissionImage.objects.create(submission=submission, **image_data)
        return submission

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ('date', 'start_time', 'end_time')