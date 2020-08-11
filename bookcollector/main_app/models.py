from django.db import models

RATES = (
    (1, 'Poor'),
    (2, 'Excellent'),
)

class Reader(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    
class Book(models.Model) :
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    releaseDate = models.IntegerField()
    reader = models.ManyToManyField(Reader)
    def __str__(self):
        return self.title

class Rating(models.Model):
    date = models.DateField("Rate Date")
    rate  = models.IntegerField(
        choices = RATES
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rate_display()} on {self.date}"
    class Meta:
        ordering = ['-date']    
