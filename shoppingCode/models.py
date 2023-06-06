from django.db import models

from users.models import User

class ShoppingCode(models.Model):

    code    = models.IntegerField(blank=True)
    is_active   = models.BooleanField(default=True)
    #id usuario al que pertenece
    user        = models.ForeignKey(User , related_name='shoppingCode', on_delete=models.CASCADE)

    def __str__(self):
        return self.telefono