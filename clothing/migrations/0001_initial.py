# Generated by Django 2.2.7 on 2019-11-21 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableColors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'available_colors',
            },
        ),
        migrations.CreateModel(
            name='AvailableParts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'available_parts',
            },
        ),
        migrations.CreateModel(
            name='AvailableSizeUnits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'available_size_units',
            },
        ),
        migrations.CreateModel(
            name='BasicProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'basic_products',
            },
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=20)),
                ('hex_code', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'colors',
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'parts',
            },
        ),
        migrations.CreateModel(
            name='SideNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side_name', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'side_names',
            },
        ),
        migrations.CreateModel(
            name='SizeUnits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_unit', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'size_units',
            },
        ),
        migrations.CreateModel(
            name='SizeFiguresForProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_figure', models.CharField(max_length=20)),
                ('basic_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.BasicProducts')),
                ('part', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.Parts')),
                ('size_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.SizeUnits')),
            ],
            options={
                'db_table': 'size_figures_for_products',
            },
        ),
        migrations.CreateModel(
            name='SideImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side_image', models.URLField(max_length=3000)),
                ('basic_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.BasicProducts')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.Colors')),
                ('side_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.SideNames')),
            ],
            options={
                'db_table': 'side_images',
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('made_of', models.CharField(max_length=20)),
                ('made_by', models.CharField(max_length=20)),
                ('made_in', models.CharField(max_length=20)),
                ('elasticity', models.CharField(max_length=20)),
                ('texture', models.CharField(max_length=20)),
                ('thickness', models.CharField(max_length=20)),
                ('care', models.CharField(max_length=500)),
                ('fitting_info', models.CharField(max_length=200)),
                ('basic_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.BasicProducts')),
            ],
            options={
                'db_table': 'product_info',
            },
        ),
        migrations.CreateModel(
            name='ModelImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_image', models.URLField(max_length=3000)),
                ('basic_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.BasicProducts')),
            ],
            options={
                'db_table': 'model_images',
            },
        ),
        migrations.AddField(
            model_name='basicproducts',
            name='available_color',
            field=models.ManyToManyField(null=True, through='clothing.AvailableColors', to='clothing.Colors'),
        ),
        migrations.AddField(
            model_name='basicproducts',
            name='available_part',
            field=models.ManyToManyField(null=True, through='clothing.AvailableParts', to='clothing.Parts'),
        ),
        migrations.AddField(
            model_name='basicproducts',
            name='available_size_unit',
            field=models.ManyToManyField(null=True, through='clothing.AvailableSizeUnits', to='clothing.SizeUnits'),
        ),
        migrations.AddField(
            model_name='basicproducts',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.Brands'),
        ),
        migrations.AddField(
            model_name='basicproducts',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.Categories'),
        ),
        migrations.AddField(
            model_name='availablesizeunits',
            name='basic_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.BasicProducts'),
        ),
        migrations.AddField(
            model_name='availablesizeunits',
            name='size_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.SizeUnits'),
        ),
        migrations.CreateModel(
            name='AvailableSideNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.Categories')),
                ('side_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.SideNames')),
            ],
            options={
                'db_table': 'available_side_names',
            },
        ),
        migrations.AddField(
            model_name='availableparts',
            name='basic_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.BasicProducts'),
        ),
        migrations.AddField(
            model_name='availableparts',
            name='part',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.Parts'),
        ),
        migrations.AddField(
            model_name='availablecolors',
            name='basic_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.BasicProducts'),
        ),
        migrations.AddField(
            model_name='availablecolors',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clothing.Colors'),
        ),
    ]
