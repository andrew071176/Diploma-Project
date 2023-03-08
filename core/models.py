from django.db import models
from django.core.validators import RegexValidator


# phone validator(if +380 == True: pass)
phone_validator = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[ -]?){7}$', message='Error phone number')


# "Hero" Section Model
class Hero(models.Model):
    video = models.URLField()

    def __str__(self):
        return "Hero Section"
    
    def save(self, *args, **kwargs):
        if not self.pk and Hero.objects.exists():
            raise ValueError('There is can be only one Hero instance')
        return super(Hero, self).save(*args, **kwargs)


# "About" Section Model
class About(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=500, null=True)
    photo = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValueError('There is can be only one About instance')
        return super(About, self).save(*args, **kwargs)



# "Why Us" Section Model
class WhyUs(models.Model):
    title = models.CharField(max_length=20)
    position = models.SmallIntegerField(unique=True)
    description = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.title


# "Menu" Section Models
    #1 For dish categories(spicy, soup & etc.)
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('position',)

    #2 For dish item
class Dish(models.Model):
    title = models.CharField(max_length=120, unique=True, db_index=True)
    ingredients = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/%Y-%m-%d', blank=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    
    # for "Specials" category
    is_special = models.BooleanField(default=False) # if true: display in specials 
    position = models.SmallIntegerField(unique=True) # if 1: active item after page update

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('category', 'position')


# "Events" Section Model
class Event(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True) # if 1: active item after page update
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='events/%Y-%m-%d', default=None)

    def __str__(self):
        return self.title


# "Reservation" Section Model
class Reservation(models.Model):

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    persons = models.SmallIntegerField()
    message = models.TextField(max_length=250, blank=True)

    date = models.DateField(auto_now_add=True)
    date_processing = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ': ' + self.phone

    class Meta:
        ordering = ('-date', )


# "Staff" Section Model
class Staff(models.Model):
    photo = models.ImageField(default=None)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name


# "Gallery" Section Model
class Gallery(models.Model):
    photo = models.ImageField(default=None)
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title 


# "Testimonial" Section Model
class Testimonial(models.Model):
    photo = models.ImageField(default=None)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    rating = models.IntegerField()
    testimonial = models.TextField()

    def __str__(self):
        return self.name


# "Contact Us" Section Model
    #1 For information to contact restaraunt
class Contacts(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=24)
    zipcode = models.PositiveIntegerField()
    phone = models.CharField(max_length=20, validators=[phone_validator])
    email = models.EmailField()

    def __str__(self):
        return "Restaraunt contacts"
    
    def save(self, *args, **kwargs):
        if not self.pk and Contacts.objects.exists():
            raise ValueError('There is can be only one Contact instance')
        return super(Contacts, self).save(*args, **kwargs)

    
    #2 For "Contact Us" form
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    topic = models.CharField(max_length=250, blank=False)
    message = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.name + " " + self.email