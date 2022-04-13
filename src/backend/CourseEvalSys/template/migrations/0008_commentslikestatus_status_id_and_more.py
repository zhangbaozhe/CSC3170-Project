# Generated by Django 4.0.3 on 2022-04-13 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0007_alter_courses_course_name_alter_users_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentslikestatus',
            name='Status_ID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commentslikestatus',
            name='CommentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ID_of_Comment', to='template.comments'),
        ),
        migrations.AddConstraint(
            model_name='commentslikestatus',
            constraint=models.UniqueConstraint(fields=('User_ID', 'CommentID'), name='like_id'),
        ),
    ]
