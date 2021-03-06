# Generated by Django 2.0.9 on 2019-01-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0041_auto_20190108_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zaaktype',
            name='handeling_initiator',
            field=models.CharField(help_text="Werkwoord dat hoort bij de handeling die de initiator verricht bij dit zaaktype. Meestal 'aanvragen', 'indienen' of 'melden'. Zie ook het IOB model op https://www.gemmaonline.nl/index.php/Imztc_2.1/doc/attribuutsoort/zaaktype.handeling_initiator", max_length=20, verbose_name='handeling initiator'),
        ),
    ]
