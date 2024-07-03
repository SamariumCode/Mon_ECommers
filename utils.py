from kavenegar import *


from django.contrib.auth.mixins import UserPassesTestMixin


class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin


def send_otp_code(phone_number, code):

    try:
        api = KavenegarAPI(
            '59322B72626E47375365553465574C61647049555A6C43553961506748546461466132436A55445365586F3D')
        params = {'sender': '1000689696', 'receptor': '09305771212',
                  'message': '.وب سرویس پیام کوتاه کاوه نگار'}
        response = api.sms_send(params)
        onse = api.sms_send(params)
        print(onse)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
