from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ZONA(models.Model):
    ZON_ID = models.AutoField(('Id zona'), primary_key=True)
    ZON_NOMBRE = models.CharField(('Nombre zona'), max_length=40, null=True, blank=True)

    class  Meta:
        db_table = "ZONA"

    def __str__(self):
        return self.ZON_NOMBRE
        

class ESTADO(models.Model):
    EST_ID = models.AutoField(('Id estado'), primary_key=True)
    EST_NOMBRE = models.CharField(('Nombre de estado'), max_length=100, null=True, blank=True)

    class Meta:
        db_table = "ESTADO"

    def __str__(self):
        return self.EST_NOMBRE


class TRANSPORTE(models.Model):
    TRA_ID = models.AutoField(('Id transporte'), primary_key=True)
    TRA_NOMBRESERVICIO = models.CharField(('Nombre servicio de transporte'), max_length=40, null=True, blank=True)
    TRA_HORARIO = models.CharField(('Horario del transporte'), max_length=50, null=True, blank=True)
    TRA_VEHICULO = models.CharField(('Vehiculo de transporte'), max_length=50, null=True, blank=True)
    TRA_CONDUCTOR = models.CharField(('Nombre conductor'), max_length=100, null=True, blank=True)
    TRA_VALOR = models.IntegerField(('Valor del transporte'), null=True, blank=True)

    class Meta: 
        db_table = "TRANSPORTE"

    def __str__(self):
        return self.TRA_NOMBRESERVICIO


class TOUR(models.Model):
    TOU_ID = models.AutoField(('Id servicio de tour'), primary_key=True)
    ZON_ID = models.ForeignKey(ZONA, verbose_name="Zona", on_delete=models.PROTECT)
    TOU_NOMBRE = models.CharField(('Nombre de tour'), max_length=100, null=True, blank=True)
    TOU_DESCRIPCION = models.CharField(('Descripción del tour'), max_length=255, null=True, blank=True)
    TOU_VALOR = models.IntegerField(('Valor del tour'), null=True, blank=True)

    class Meta:
        db_table = "TOUR"

    def __str__(self):
        return self.TOU_NOMBRE + ' - ' + str(self.ZON_ID)


class DEPARTAMENTO(models.Model):
    DEP_ID = models.AutoField(('Id departamento'), primary_key=True)
    DEP_NOMBRE = models.CharField(('Nombre de departamento'), max_length=100, null=True, blank=True)
    EST_ID = models.ForeignKey(ESTADO, verbose_name="Estado", on_delete=models.PROTECT)
    DEP_DESCRIPCION = models.CharField(('Descripción de departamento'), max_length=255, null=True, blank=True)
    DEP_CANTIDADHABITACIONES = models.IntegerField(('Cantidad de habitaciones'), null=True, blank=True)
    DEP_CANTIDADCAMAS = models.IntegerField(('Cantidad de camas'), null=True, blank=True)
    DEP_CANTIDADBANOS = models.IntegerField(('Cantidad de baños'), null=True, blank=True)
    DEP_CANTIDADPERSONAS = models.IntegerField(('Cantidad de personas'), null=True, blank=True)
    DEP_DIRECCION = models.CharField(('Direccion departamento'), max_length=100, null=True, blank=True)    
    ZON_ID = models.ForeignKey(ZONA, verbose_name="Zona", on_delete=models.PROTECT)
    DEP_VALOR_DIA = models.IntegerField(('Valor arriendo por dia'), null=True, blank=True)
    DEP_IMAGEN1 = models.ImageField(upload_to='departamentos', null=True)
    DEP_IMAGEN2 = models.ImageField(upload_to='departamentos', null=True)
    DEP_IMAGEN3 = models.ImageField(upload_to='departamentos', null=True)
    TOU_ID1 = models.ForeignKey(TOUR, related_name="Tour_asociado_1", verbose_name="Tour asociado", on_delete=models.PROTECT)
    TOU_ID2 = models.ForeignKey(TOUR, related_name="Tour_asociado_2", verbose_name="Tour 2 asociado", on_delete=models.PROTECT)
    TOU_ID3 = models.ForeignKey(TOUR, related_name="Tour_asociado_3", verbose_name="Tour 3 asociado", on_delete=models.PROTECT)

    class  Meta:
        db_table = "DEPARTAMENTO"

    def __str__(self):
        return self.DEP_NOMBRE #+ ' - ' + self.DEP_DIRECCION + ' - ' + str(self.ZON_ID)


class INVENTARIO(models.Model):
    INV_ID = models.AutoField(('Id inventario'), primary_key=True)
    INV_DEPARTAMENTO = models.OneToOneField(DEPARTAMENTO, on_delete= models.CASCADE, null=False, blank=False, related_name='inventario_depto')
    INV_MICROONDAS = models.BooleanField(('Microondas'), default=False)
    INV_HORNOELECTRICO = models.BooleanField(('Horno Electrico'), default=False)

    class Meta:
        db_table = "INVENTARIO"

    def __str__(self):
        return str(self.INV_ID)




class RESERVA(models.Model):
    RES_ID = models.AutoField(('ID Reserva'), primary_key=True)
    RES_USER = models.ForeignKey(User, on_delete=models.CASCADE)
    RES_DEPARTAMENTO = models.ForeignKey(DEPARTAMENTO, on_delete=models.CASCADE)
    RES_FECHA_INGRESO = models.DateField(('Fecha de ingreso'),null=True, blank=True)
    RES_FECHA_SALIDA = models.DateField(('Fecha de salida'),null=True, blank=True)
    RES_CANTIDAD_DIAS = models.IntegerField(('Cantidad de dias'),null=True, blank=True)
    RES_ASISTENTES = models.TextField(('Asistentes'),null=True, blank=True, help_text="Ingrese nombre y rut de los asistentes a la reserva")
    RES_VALOR_RESERVA = models.IntegerField(('Valor de la reserva'),null=True, blank=True)

    class Meta:
        db_table = "RESERVA"
    
    def __str__(self):
        return f"Reserva '{self.RES_DEPARTAMENTO}' efectuada por '{self.RES_USER}', entre {self.RES_FECHA_INGRESO} - {self.RES_FECHA_SALIDA}"


# RES_DESEA_TOUR = models.BooleanField(('Desea tour'), default=False, null=True, blank=True)
# RES_TOUR_1 = models.IntegerField(('Tour 1'),null=True, blank=True)
# RES_TOUR_2 = models.IntegerField(('Tour 2'),null=True, blank=True)
# RES_TOUR_3 = models.IntegerField(('Tour 3'),null=True, blank=True)
# RES_DESEA_TRANSPORTE = models.BooleanField(('Desea transporte'), default=False, null=True, blank=True)
# RES_TRANSPORTE_1 = models.IntegerField(('Transporte ida'),null=True, blank=True)
# RES_TRANSPORTE_2 = models.IntegerField(('Transporte vuelta'),null=True, blank=True)


# class CHECKLIST(models.Model):
#     CLIST_ID = models.AutoField(('ID Checklist'), primary_key=True)
#     CLIST_DEPARTAMENTO = models.ForeignKey(DEPARTAMENTO, on_delete=models.CASCADE)
    
#     CLIST_ULTIMA_MODIFICACION = models.DateField(('Fecha última modificación'),null=True, blank=True, auto_now=True)


# class CHECKIN(models.Model):
#     CIN_ID = models.AutoField(('ID Check In'), primary_key=True)


# class CHECKOUT(models.Model):
#     COUT_ID = models.AutoField(('ID Check Out'), primary_key=True)