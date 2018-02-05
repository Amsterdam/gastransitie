# Generated by Django 2.0.2 on 2018-02-05 14:20

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BagBuurt',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3)),
                ('vollcode', models.CharField(max_length=4)),
                ('naam', models.CharField(max_length=40)),
                ('vervallen', models.NullBooleanField()),
                ('ingang_cyclus', models.DateField(blank=True, null=True)),
                ('brondocument_naam', models.CharField(blank=True, max_length=100, null=True)),
                ('brondocument_datum', models.DateField(blank=True, null=True)),
                ('stadsdeel_id', models.CharField(max_length=14)),
                ('buurtcombinatie_id', models.CharField(blank=True, max_length=14, null=True)),
                ('date_modified', models.DateTimeField()),
                ('begin_geldigheid', models.DateField(blank=True, null=True)),
                ('einde_geldigheid', models.DateField(blank=True, null=True)),
                ('geometrie', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=28992)),
            ],
            options={
                'db_table': 'bag_buurt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CBSBuurt',
            fields=[
                ('ogc_fid', models.AutoField(primary_key=True, serialize=False)),
                ('bu_code', models.CharField(blank=True, max_length=10, null=True)),
                ('bu_naam', models.CharField(blank=True, max_length=60, null=True)),
                ('wk_code', models.CharField(blank=True, max_length=8, null=True)),
                ('gm_code', models.CharField(blank=True, max_length=6, null=True)),
                ('gm_naam', models.CharField(blank=True, max_length=60, null=True)),
                ('ind_wbi', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('water', models.CharField(blank=True, max_length=4, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('dek_perc', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('oad', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('sted', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('aant_inw', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('aant_man', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('aant_vrouw', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_00_14_jr', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_15_24_jr', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_25_44_jr', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_45_64_jr', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_65_eo_jr', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_ongehuwd', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_gehuwd', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_gescheid', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_verweduw', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('bev_dichth', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('aantal_hh', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_eenp_hh', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_hh_z_k', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_hh_m_k', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('gem_hh_gr', models.DecimalField(blank=True, decimal_places=1, max_digits=11, null=True)),
                ('p_west_al', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_n_w_al', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_marokko', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_ant_aru', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_surinam', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_turkije', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('p_over_nw', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('opp_tot', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('opp_land', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('opp_water', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'verbose_name': 'CBS buurt',
                'verbose_name_plural': 'CBS buurten',
                'db_table': 'gas_cbs_buurt_2017_raw',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EnergieLabel',
            fields=[
                ('ogc_fid', models.AutoField(primary_key=True, serialize=False)),
                ('energielabel', models.CharField(blank=True, max_length=1, null=True)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'energie_labels_clean',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GasAfwc2017',
            fields=[
                ('ogc_fid', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('corp', models.CharField(blank=True, max_length=255, null=True)),
                ('corporatie', models.CharField(blank=True, max_length=255, null=True)),
                ('bouwjaar', models.IntegerField(blank=True, null=True)),
                ('aantal_adressen', models.IntegerField(blank=True, null=True)),
                ('aantal_corporatie', models.IntegerField(blank=True, null=True)),
                ('percentage_corporatie', models.IntegerField(blank=True, null=True)),
                ('gemeente', models.CharField(blank=True, max_length=255, null=True)),
                ('perc', models.IntegerField(blank=True, null=True)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'verbose_name': 'corporatie bezit - gebouw',
                'verbose_name_plural': 'corporatie bezit - gebouwen',
                'db_table': 'afwc2017_clean',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mip2016',
            fields=[
                ('ogc_fid', models.IntegerField(primary_key=True, serialize=False)),
                ('datum', models.CharField(blank=True, max_length=255, null=True)),
                ('organisatie', models.CharField(blank=True, max_length=255, null=True)),
                ('opdrachtgever', models.CharField(blank=True, max_length=255, null=True)),
                ('nummer', models.CharField(blank=True, max_length=255, null=True)),
                ('omschrijving', models.CharField(blank=True, max_length=255, null=True)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'mip2016_clean',
                'managed': False,
            },
        ),
    ]
