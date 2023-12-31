# Generated by Django 3.2.15 on 2023-04-06 06:37

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ab_contents', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='affilates_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affreg_name', models.CharField(blank=True, max_length=200, null=True)),
                ('affvalid_from', models.CharField(blank=True, max_length=200, null=True)),
                ('affvalid_to', models.CharField(blank=True, max_length=200, null=True)),
                ('affclub', models.CharField(blank=True, max_length=250, null=True)),
                ('affrank', models.CharField(blank=True, max_length=250, null=True)),
                ('affstate', models.CharField(blank=True, max_length=250, null=True)),
                ('affdistrict', models.CharField(blank=True, max_length=250, null=True)),
                ('aff_status', models.CharField(blank=True, default=0, max_length=10)),
                ('affreg_img', models.ImageField(default='', upload_to='image/regcheck')),
            ],
        ),
        migrations.CreateModel(
            name='affiliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affiliation_img', models.ImageField(null=True, upload_to='file')),
                ('affiliation_name', models.ImageField(null=True, upload_to='file')),
            ],
        ),
        migrations.CreateModel(
            name='blackbelt_holders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bth_reg', models.CharField(max_length=25)),
                ('bth_name', models.CharField(max_length=25)),
                ('bth_desig', models.CharField(max_length=20)),
                ('bth_image', models.ImageField(null=True, upload_to='image/blackbeltholder')),
            ],
        ),
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carimage', models.ImageField(null=True, upload_to='carouselimages/')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='check_register_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_reg_name', models.CharField(max_length=25)),
                ('check_reg_gender', models.CharField(max_length=10)),
                ('check_reg_bloodg', models.CharField(max_length=10)),
                ('check_reg_dob', models.CharField(max_length=20)),
                ('check_reg_national', models.CharField(max_length=15)),
                ('check_reg_occup', models.CharField(max_length=20)),
                ('check_reg_qualific', models.CharField(max_length=20)),
                ('check_reg_phon', models.CharField(max_length=15)),
                ('check_reg_email', models.EmailField(max_length=254)),
                ('check_reg_doj', models.CharField(max_length=20)),
                ('check_reg_pgname', models.CharField(max_length=20)),
                ('check_reg_pgoccu', models.CharField(max_length=20)),
                ('check_reg_address', models.CharField(max_length=50)),
                ('check_reg_reson', models.CharField(max_length=50)),
                ('check_reg_exp', models.CharField(max_length=5)),
                ('check_reg_op', models.CharField(max_length=5)),
                ('check_status', models.CharField(max_length=10)),
                ('check_reg_img', models.ImageField(upload_to='image/regcheck')),
            ],
        ),
        migrations.CreateModel(
            name='contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_title', models.CharField(max_length=25)),
                ('con_content', models.TextField()),
                ('cont_img', models.ImageField(upload_to='image/blackbeltholder')),
            ],
        ),
        migrations.CreateModel(
            name='Enquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('contact_no', models.CharField(max_length=30)),
                ('mail_id', models.EmailField(max_length=254)),
                ('sub', models.CharField(max_length=30)),
                ('mesage', models.TextField()),
                ('enq_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='hbgimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image', models.ImageField(null=True, upload_to='image/bgimg')),
            ],
        ),
        migrations.CreateModel(
            name='HistoyrPdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('histry_img', models.ImageField(upload_to='image/blackbeltholder')),
            ],
        ),
        migrations.CreateModel(
            name='imagefolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=40)),
                ('mdesig', models.CharField(max_length=90)),
                ('mposition', models.CharField(max_length=90)),
                ('asso_image', models.ImageField(null=True, upload_to='image/blackbeltholder')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newstitle', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='pdfimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('more_img', models.ImageField(upload_to='image/blackbeltholder')),
            ],
        ),
        migrations.CreateModel(
            name='register_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_id', models.CharField(max_length=25)),
                ('reg_name', models.CharField(max_length=25)),
                ('reg_gender', models.CharField(max_length=10)),
                ('reg_bloodg', models.CharField(max_length=10)),
                ('reg_dob', models.CharField(max_length=20)),
                ('reg_national', models.CharField(max_length=15)),
                ('reg_occup', models.CharField(max_length=20)),
                ('reg_qualific', models.CharField(max_length=20)),
                ('reg_phon', models.CharField(max_length=15)),
                ('reg_email', models.EmailField(max_length=254)),
                ('reg_doj', models.CharField(max_length=20)),
                ('reg_pgname', models.CharField(max_length=20)),
                ('reg_pgoccu', models.CharField(max_length=20)),
                ('reg_address', models.CharField(max_length=150)),
                ('reg_reson', models.CharField(max_length=50)),
                ('reg_exp', models.CharField(max_length=5)),
                ('reg_op', models.CharField(max_length=5)),
                ('reg_img', models.ImageField(upload_to='image/blackbeltholder')),
            ],
        ),
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='regforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ev_subhead', models.CharField(max_length=255)),
                ('event_sub', models.TextField()),
                ('env_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karatte_org.news')),
            ],
        ),
        migrations.CreateModel(
            name='moreconts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('more_cont', models.TextField()),
                ('more_img', models.ImageField(upload_to='image/blackbeltholder')),
                ('con_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cont', to='karatte_org.contents')),
            ],
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(null=True, upload_to='folderimages/')),
                ('folder_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karatte_org.imagefolder')),
            ],
        ),
        migrations.CreateModel(
            name='eventimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('envimgpdf', models.FileField(upload_to='folderimages')),
                ('evnimg', models.ImageField(upload_to='folderimages')),
                ('envimage_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karatte_org.news')),
            ],
        ),
    ]
