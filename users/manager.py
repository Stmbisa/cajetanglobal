from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations: True

    def create_user(self, email, first_name, last_name,phone,gender, country_of_orgin,country_of_destiantion, nationality, 
    next_of_kin, next_of_kin_phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('Email Required')
        email=self.normalize_email(email)
        user = self.model(email=email,first_name=first_name, last_name=last_name, gender=gender, phone=phone, 
        country_of_orgin=country_of_orgin, country_of_destiantion=country_of_destiantion, nationality=nationality,
        next_of_kin=next_of_kin, next_of_kin_phone_number=next_of_kin_phone_number,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name,gender,password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must be is_staff=True'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must be is_superuser=True'))
        
        return self.create_user(email,first_name, last_name,gender, password, **extra_fields)


