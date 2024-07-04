from django.utils import timezone
from datetime import timedelta
from celery import shared_task

from accounts.models import OtpCode


@shared_task
def remove_expired_otp_codes():
    expired_time = timezone.now() - timedelta(minutes=2)
    deleted_count, _ = OtpCode.objects.filter(
        created__lte=expired_time).delete()
