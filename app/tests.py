from django.test import TestCase
from app.models import InquirySubmission
from app.serializer import InquirySubmissionSerializer

class SerializerTestCase(TestCase):
    def test_create_with_images(self):
        data = {
            'first_name': 'firstnametest',
            'last_name': 'lastnametest',
            'email': 'email@test.com',
            'instagram': 'igtest',
            'design_type': 'CU',
            'description': 'descriptiontest',
            'date': '2024-03-07',
            'images': [
                {'image_url': 'https://www.notion.so/'},
                {'image_url': 'https://www.notion.so/'},
            ]
        }
        serializer = InquirySubmissionSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        inquiry_submission = serializer.save()
        self.assertIsInstance(inquiry_submission, InquirySubmission)
        self.assertEqual(inquiry_submission.submissionimage_set.count(), 2)