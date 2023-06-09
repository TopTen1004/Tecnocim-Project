# Generated by Django 3.2.16 on 2022-12-12 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equivalencias', '0003_alter_producto_tipo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['tipo']},
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(choices=[('anticipo facturas', 'ANTICIPO-FACTURAS'), ('anticipo pagos domiciliados', 'ANTICIPO-DOMICILIADOS'), ('anticipo recibos', 'ANTICIPO-RECIBOS'), ('aval', 'AVAL'), ('click', 'CLICK - PAGO PROVEEDORES'), ('confirming estandar', 'CONFIRMING'), ('confirming pronto pago', 'CONFIRMING-PRONTO PAGO'), ('documentario exportaciones', 'DOCUMENTARIO-EXPORTACIONES'), ('documentario importaciones', 'DOCUMENTARIO-IMPORTACIONES'), ('descuento pagares', 'DESCUENTO-PAGARÉS'), ('descuento pagares no orden', 'DESCUENTO-PAGARÉS NO ORDEN'), ('factoring con recurso', 'FACTORING CON RECURSO'), ('factoring sin recurso', 'FACTORING SIN RECURSO'), ('financiacion importaciones', 'FINANCIACIÓN IMPORTACIONES'), ('hipoteca', 'HIPOTECA INMOBILIARIA'), ('leasing', 'LEASING'), ('multilinea', 'MULTILÍNEA'), ('poliza', 'PÓLIZA DE CRÉDITO'), ('prestamo', 'PRÉSTAMO'), ('tarjeta', 'TARJETAS'), ('excepcion', 'EXCEPCIÓN'), ('sin', 'SIN CLASIFICACIÓN')], max_length=50, primary_key=True, serialize=False, verbose_name='Producto'),
        ),
    ]
