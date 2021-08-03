from tortoise.models import Model
from tortoise import fields

class File(Model):
    file_name = fields.TextField(pk=True, null=False)
    file_type_extension = fields.TextField(null=False)
    description = fields.TextField(null=False)
    uploaded_by = fields.TextField(null=False)
    uploaded_at = fields.DateField(null=False, default='1992-01-01')
    file = fields.BinaryField(null=False)
    
    class Meta:
            table='Files'
            unique_together=( ("file_name", "file_type_extension") )

    def __str__(self):
        return self.name


