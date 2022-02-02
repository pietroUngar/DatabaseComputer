from django.db import models


class Element(models.Model):

    position = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    broken = models.BooleanField()

    @property
    def identifier(self):
        return str(self)

    def __str__(self):

        return "SERG-{0:015d}".format(self.pk)


class Computer(Element):

    type = "Computer"
    MAC_number = models.CharField(max_length=100)
    processor_type = models.CharField(max_length=100)
    core_number = models.IntegerField()
    ram_dimension = models.IntegerField()
    disk_dimension = models.IntegerField()
    video_card = models.CharField(max_length=100)


class Display(Element):

    type = "Display"
    model = models.CharField(max_length=100)
    width_resolution = models.IntegerField()
    height_resolution = models.IntegerField()


class Peripheral(Element):

    connector = models.CharField(max_length=100)
    wireless = models.BooleanField()


class Cable(Element):

    connector_from = models.CharField(max_length=100)
    connector_to = models.CharField(max_length=100)
