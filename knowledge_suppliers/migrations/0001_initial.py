# Generated by Django 5.1.5 on 2025-02-25 12:23

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeSupplier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=100, unique=True)),
                ('addres', models.TextField(max_length=100)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.course')),
            ],
            options={
                'verbose_name': 'knowledge_sipplier',
                'verbose_name_plural': 'knowledge_sippliers',
                'db_table': 'knowledge_supplier',
            },
        ),
    ]
