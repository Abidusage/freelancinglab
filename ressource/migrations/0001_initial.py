# Generated by Django 4.2.2 on 2023-11-06 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formation', models.CharField(choices=[('HTML et CSS', 'HTML et CSS'), ('JAVASCRIPT', 'JAVASCRIPT'), ('PYTHON', 'PYTHON'), ('DJANGO', 'DJANGO'), ('REACT', 'REACT'), ('BOOTSTRAP', 'BOOTSTRAP'), ('SQL', 'SQL'), ('PHP', 'PHP'), ('iOS', 'iOS'), ('Flutter', 'Flutter'), ('Xamarin', 'Xamarin'), ('Ionic', 'Ionic'), ('Apache Cordova', 'Apache Cordova'), ('React Native', 'React Native'), (' Android', ' Android'), (' Analyse et suivi des performances SEO', ' Analyse et suivi des performances SEO'), (' SEO local', ' SEO local'), (' SEO technique', ' SEO technique'), (' Link building', ' Link building'), (' Rédaction SEO', ' Rédaction SEO'), (' Optimisation du contenu', ' Optimisation du contenu'), (' Recherche de mots-clés', ' Recherche de mots-clés'), (' Fondamentaux du SEO', ' Fondamentaux du SEO'), (' Link building', ' Link building'), ("Marketing d'influence", "Marketing d'influence"), (' Gestion des crises et modération des communautés', ' Gestion des crises et modération des communautés'), (' Gestion de la réputation en ligne', ' Gestion de la réputation en ligne'), (' Analyse des performances et des métriques', ' Analyse des performances et des métriques'), (' Publicité sur les réseaux sociaux', ' Publicité sur les réseaux sociaux'), (' Stratégie de communication en ligne', ' Stratégie de communication en ligne'), (' Création de contenu engageant', 'Création de contenu engageant'), (' Gestion des réseaux sociaux', '   Gestion des réseaux sociaux'), ("Coaching d'équipe", "Coaching d'équipe"), (' Coaching sportif', '   Coaching sportif'), (' Coaching en développement personnel', '   Coaching en développement personnel'), (' Coaching en gestion du temps et des priorités', '   Coaching en gestion du temps et des priorités'), (' Coaching en développement personnel', '   Coaching de carrière'), (' Coaching de leadership', '   Coaching de leadership'), (' Gestion des réseaux sociaux', '   Gestion des réseaux sociaux'), (' Coaching professionnel', '   Coaching professionnel'), (' Coaching de vie', '   Coaching de vie'), (' UX Web Design', 'UX Web Design'), (' Les bases de la conception UX – Adobe XD', 'Les bases de la conception UX – Adobe XD'), (' UX Design for Mobile ', 'UX Design for Mobile '), (' Techniques de base en photographie', 'Techniques de base en photographie '), (' Photographie de paysage', 'Photographie de paysage'), (' Photographie de portrait', 'Photographie de portrait'), (" Photographie d'Photographie de rue", "Photographie d'Photographie de rue"), (' Photographie de mariage', 'Photographie de mariage'), (' Photographie de mode', 'Photographie de mode'), (' Photographie de produits', 'Photographie de produits'), (' Photographie de nuit et astrophotographie', 'Photographie de nuit et astrophotographie'), (' Photographie culinaire', 'Photographie culinaire'), (' Photographie de sport', 'Photographie de sport'), (' Photographie documentaire et reportage', 'Photographie documentaire et reportage'), (' Photographie de produits', 'Photographie en noir et blanc'), (' Photographie en noir et blanc', 'Photographie de produits'), (' Retouche photo et post-production', 'Retouche photo et post-production'), (' Gestion des couleurs et impression', 'Gestion des couleurs et impression'), (' Design graphique de base', 'Design graphique de base'), (' Adobe Photoshop', 'Adobe Photoshop'), (' Adobe Illustrator', 'Adobe Illustrator'), (' Adobe InDesign', 'Adobe InDesign'), (' Adobe Illustrator', 'Adobe Illustrator'), (' Conception de logo', 'Conception de logo'), (' Typographie', 'Typographie'), (" Conception d'affiches", "Conception d'affiches"), (" Conception d'emballages", "Conception d'emballages"), (' Conception de sites web', 'Conception de sites web'), (" Conception d'interfaces utilisateur (UI)", "Conception d'interfaces utilisateur (UI)"), (" Conception d'expérience utilisateur (UX)", "Conception d'expérience utilisateur (UX)"), (' Illustration numérique', 'Illustration numérique'), (' CoConception de motion graphics', 'Conception de motion graphics'), (" Conception de marque et d'identité", "Conception de marque et d'identité"), (' Conception éditoriale', 'Conception éditoriale'), (" Conception d'interfaces utilisateur (UI)", "Conception d'interfaces utilisateur (UI)"), (" Conception d'interfaces utilisateur (UI)", "Conception d'interfaces utilisateur (UI)")], max_length=200, null=True)),
                ('langue', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
                ('liens', models.CharField(max_length=300, null=True)),
            ],
            options={
                'verbose_name_plural': 'Ressource',
            },
        ),
    ]
