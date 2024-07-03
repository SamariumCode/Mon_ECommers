from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from accounts.models import OtpCode


class Command(BaseCommand):
    help = "Remove all expired OTP codes"

    def handle(self, *args, **options):
        expired_time = timezone.now() - timedelta(minutes=2)
        deleted_count, _ = OtpCode.objects.filter(
            created__lte=expired_time).delete()
        self.stdout.write(f"Successfully removed {deleted_count} OTP code(s)")
