# Generated by Django 5.0.2 on 2024-02-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('past_experience', models.IntegerField()),
                ('skills_score', models.IntegerField()),
                ('technology_known', models.PositiveIntegerField(null=True)),
                ('employee_level', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'employees',
            },
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('scope', models.IntegerField(default=1, help_text='Scope of the project (1-10)')),
                ('complexity', models.IntegerField(default=1, help_text='Technical complexity of the project (1-10)')),
                ('knowledge', models.IntegerField(default=1, help_text='Domain knowledge required for the project (1-10)')),
                ('time_effort', models.IntegerField(default=1, help_text='Time and effort required for the project (1-10)')),
                ('resources', models.IntegerField(default=1, help_text='Resource requirements for the project (1-10)')),
                ('risk', models.IntegerField(default=1, help_text='Risk and uncertainty associated with the project (1-10)')),
                ('project_complexity', models.CharField(blank=True, help_text='Project complexity (Easy, Intermediate, Advanced)', max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'projects',
            },
        ),
        migrations.CreateModel(
            name='technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('python', models.BooleanField(default=False)),
                ('c', models.BooleanField(default=False)),
                ('java', models.BooleanField(default=False)),
                ('javascript', models.BooleanField(default=False)),
                ('nodejs', models.BooleanField(default=False)),
                ('git_github', models.BooleanField(default=False)),
                ('php', models.BooleanField(default=False)),
                ('react', models.BooleanField(default=False)),
                ('bootstrap', models.BooleanField(default=False)),
                ('nginx', models.BooleanField(default=False)),
                ('typescript', models.BooleanField(default=False)),
                ('angularjs', models.BooleanField(default=False)),
                ('frontend', models.BooleanField(default=False)),
                ('backend', models.BooleanField(default=False)),
                ('mongodb', models.BooleanField(default=False)),
                ('mysql', models.BooleanField(default=False)),
                ('docker', models.BooleanField(default=False)),
                ('azure', models.BooleanField(default=False)),
                ('django', models.BooleanField(default=False)),
                ('postgresql', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'technologies',
            },
        ),
    ]
