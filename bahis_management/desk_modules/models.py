from django.db import models


class DeskModuleType(models.Model):
    module_type = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.module_type


class DeskModule(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    url = models.URLField()
    module_type = models.ForeignKey(DeskModuleType, on_delete=models.CASCADE)
    parent_module_id = models.ForeignKey("DeskModule", on_delete=models.SET_NULL, null=True)
    sort_order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
