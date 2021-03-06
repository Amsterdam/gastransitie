from django.contrib.gis.db import models


class GasAfwc2017(models.Model):
    ogc_fid = models.IntegerField(blank=True, primary_key=True)
    corp = models.CharField(max_length=255, blank=True, null=True)
    corporatie = models.CharField(max_length=255, blank=True, null=True)
    bouwjaar = models.IntegerField(blank=True, null=True)
    aantal_adressen = models.IntegerField(blank=True, null=True)
    aantal_corporatie = models.IntegerField(blank=True, null=True)
    percentage_corporatie = models.IntegerField(blank=True, null=True)
    gemeente = models.CharField(max_length=255, blank=True, null=True)
    perc = models.IntegerField(blank=True, null=True)
    wkb_geometry = models.GeometryField(srid=4326, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afwc2017_clean'
        verbose_name = 'corporatie bezit - gebouw'
        verbose_name_plural = 'corporatie bezit - gebouwen'

    def __str__(self):
        return 'Corporatie bezit {} (gebouw {})'.format(self.corp, self.ogc_fid)
