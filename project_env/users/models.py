from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import  PhoneNumberField 


class UserManager(BaseUserManager):
    def _create_user(self, username,email , password, **extra_fields):
        """
        create and save and return user with given fields
        """
        if not username or not email or not password:
            raise ValueError("Fill the required fields")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, password , email, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    age_choice = [('14', 14), ('15', 15), ('16', 16), ('17', 17), ('18', 18), ('19', 19),
                  ('20', 20), ('21', 21), ('22', 22), ('23', 23), ('24', 24), ('25', 25), ('26', 26),
                  ('27', 27), ('28', 28), ('29', 29), ('30', 30), ('31', 31), ('32', 32), ('33', 33),
                  ('34', 34), ('35', 35), ('36', 36), ('37', 37), ('38', 38), ('39', 39), ('40', 40),
                  ('41', 41), ('42', 42), ('43', 43), ('44', 44), ('45', 45), ('46', 46), ('47', 47),
                  ('48', 48), ('49', 49), ('50', 50), ('51', 51), ('52', 52), ('53', 53), ('54', 54), 
                  ('55', 55), ('56', 56), ('57', 57), ('58', 58), ('59', 59), ('60', 60), ('61', 61),
                  ('62', 62), ('63', 63), ('64', 64), ('65', 65), ('66', 66), ('67', 67), ('68', 68),
                  ('69', 69)]
    """
    age_list = list(range(14, 70))
    age_choice = []
    for i in age_list:
        age_choice.append((str(i), i))
    """
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    age = models.CharField(
        max_length=2,
        choices=age_choice,
        default=18
    )
    profile_picture = models.ImageField(null=True, blank=True)
    phonenumber_field = models.CharField(max_length=12, default="no number")
    is_author = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.username