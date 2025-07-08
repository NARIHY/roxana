from rest_framework import serializers
from .models import Categorie, Materiel

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class MaterielSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer(read_only=True)
    categorie_id = serializers.PrimaryKeyRelatedField(
        queryset=Categorie.objects.all(), source='categorie', write_only=True
    )
    qr_code_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Materiel
        fields = ['id', 'uid', 'nom', 'categorie', 'categorie_id', 'description', 'date_ajout', 'qr_code_image']
