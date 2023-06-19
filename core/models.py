from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ('title', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()

    image = models.ImageField(upload_to='item_images', blank=True, null=True)    
    is_sold = models.BooleanField(default=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class StrategyCard(models.Model):
    title = models.CharField(max_length=200)
    # is_fulfilled = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class StrategyDeck(models.Model):
    title = models.CharField(max_length=200)
    strategies = models.ManyToManyField(StrategyCard, related_name='deck_strategies', blank=True)
    def __str__(self):
        return self.title
    
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    # transaction_series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
    ACTION_CHOICES = (('buy', 'buy'),
                    ('sell', 'sell'))

    actionType = models.CharField(choices=ACTION_CHOICES, max_length=200, default='buy')
    fulfilled_strategies = models.ManyToManyField(StrategyCard, related_name='fulfilled_series', blank=True)
    annotation = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)




    class Meta:
        pass
        # ordering = ['-updated', '-created', 'like_count', 'message_count']
    def __str__(self):
        return self.annotation


class TransactionSeries(models.Model):
# investor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
# adopted_deck = models.ForeignKey(StrategyDeck, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    adoptedStrategyCard = models.ManyToManyField(StrategyCard, related_name='strategy_series', blank=True)
    adoptedStrategyDeck = models.ManyToManyField(StrategyDeck, related_name='strategy_series', blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
