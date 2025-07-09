from rest_framework import serializers
from .models import Categorie, Materiel, Status

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'nom']
        
class MaterielSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer(read_only=True)
    categorie_id = serializers.PrimaryKeyRelatedField(
        queryset=Categorie.objects.all(), source='categorie', write_only=True
    )
    
    status = StatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(), source='status', write_only=True
    )

    qr_code_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Materiel
        fields = [
            'id', 'uid', 'nom',
            'categorie', 'categorie_id',
            'status', 'status_id',
            'description', 'date_ajout',
            'qr_code_image'
        ]
