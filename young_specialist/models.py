from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    """Модель организации"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SystemUser(models.Model):
    """Модель пользователя"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class YoungSpecialistIndicators(models.Model):
    """Модель формы 1"""

    id = models.AutoField(primary_key=True)
    article_name = models.CharField(max_length=255)
    relevant_until = models.DateField()
    order = models.IntegerField()
    last_modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_name


class MonthlyFormHeader(models.Model):
    """Модель формы 2"""

    id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.organization.name


class MonthlyFormLine(models.Model):
    """Модель формы 3"""

    id = models.AutoField(primary_key=True)
    indicator = models.ForeignKey(YoungSpecialistIndicators, on_delete=models.CASCADE)
    header = models.ForeignKey(MonthlyFormHeader, on_delete=models.CASCADE)
    distribution_count = models.IntegerField()
    target_distribution_count = models.IntegerField()
    last_modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.header} - {self.indicator}"
