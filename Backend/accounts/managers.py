from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self,email,password,first_name,last_name,**kwargs):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")
        
        user=self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password,first_name,last_name,**kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_active',True)
        kwargs.setdefault('is_superuser',False)
        return self._create_user(email,password,first_name,last_name,**kwargs)
    
    def create_superuser(self,email,password,first_name,last_name,**kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_active',True)
        kwargs.setdefault('is_superuser',True)
        return self._create_user(email,password,first_name,last_name,**kwargs)