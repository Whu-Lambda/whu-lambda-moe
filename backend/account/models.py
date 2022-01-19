from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin,
)
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self,  email, password):
        """Create and return a `User` with an email, username and password."""

        if email is None:
            raise TypeError('Users must have an email address.')

        if password is None:
            raise TypeError('Users must have a password.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,  email, password):
        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        user = self.create_user(email, password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    """
    This is a custom User model, some fields are dropped.
    You can see AbstractBaseUser for more details.
    """

    username = models.CharField(
        max_length=150, unique=True, default=uuid.uuid4)
    avatar = models.URLField(default='avatar/default.jpg')
    bio = models.CharField(max_length=64, null=True, blank=True)
    reputation = models.IntegerField(default=0)
    email = models.EmailField(db_index=True, unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case, we want that to be the email field.
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    # custom UserManager
    objects = UserManager()

    class Meta:
        db_table = 'accounts'
