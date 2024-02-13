from django.db import models


class DeskModuleType(models.Model):
    module_type = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.module_type


class DeskModule(models.Model):
    title = models.CharField(max_length=150)
    icon = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    list_definition_id = models.IntegerField(
        blank=True, null=True
    )  # TODO can we just use the form ID or URL for this?
    form_id = models.IntegerField(
        blank=True, null=True
    )  # TODO how to import from kobo in bahis 3, as a URL?, also - how to handle offline forms?
    external_url = models.URLField(
        blank=True, null=True
    )  # TODO if this is also a URL can we simplify all three into one field?
    module_type = models.ForeignKey(DeskModuleType, on_delete=models.CASCADE)
    parent_module_id = models.ForeignKey("DeskModule", on_delete=models.SET_NULL, blank=True, null=True)
    sort_order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(list_definition_id__isnull=True, form_id__isnull=True, external_url__isnull=True)
                | models.Q(list_definition_id__isnull=False, form_id__isnull=True, external_url__isnull=True)
                | models.Q(list_definition_id__isnull=True, form_id__isnull=False, external_url__isnull=True)
                | models.Q(list_definition_id__isnull=True, form_id__isnull=True, external_url__isnull=False),
                name="check a maximum of one endpoint option is filled in",
            )
        ]
