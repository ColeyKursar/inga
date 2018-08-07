from rest_framework.serializers import ModelSerializer
from inga.models import Methods, Chemistry, Chlorophyll, Converted, DNA, Extraction, ExtractionResultWeight, ExtrafloralNectaries, FeatureTableRawData, Field, Hairs, Herbivory, HPLCResult, LeafMassArea, Location, Nitrogen, Plant, PlantDNA, PlantPhoto, PlantSpecies, PlantVoucher, RAW, Site, Toughness, UPLCResult, PC_ID, Tyrosine, HairMeasurement, Expansion, PlantSpeciesHistorical, Herbivore


class ChemistrySerializer(ModelSerializer):
    class Meta:
        model = Chemistry
        fields = '__all__'

class MethodsSerializer(ModelSerializer):
    class Meta:
        model = Methods
        fields = '__all__'

class ChlorophyllSerializer(ModelSerializer):

    class Meta:
        model = Chlorophyll
        fields = '__all__'


class ConvertedSerializer(ModelSerializer):

    class Meta:
        model = Converted
        fields = '__all__'


class DNASerializer(ModelSerializer):

    class Meta:
        model = DNA
        fields = '__all__'


class ExtractionSerializer(ModelSerializer):

    class Meta:
        model = Extraction
        fields = '__all__'


class ExtractionResultWeightSerializer(ModelSerializer):

    class Meta:
        model = ExtractionResultWeight
        fields = '__all__'


class ExtrafloralNectariesSerializer(ModelSerializer):

    class Meta:
        model = ExtrafloralNectaries
        fields = '__all__'


class FeatureTableRawDataSerializer(ModelSerializer):

    class Meta:
        model = FeatureTableRawData
        fields = '__all__'


class FieldSerializer(ModelSerializer):

    class Meta:
        model = Field
        fields = '__all__'


class HairsSerializer(ModelSerializer):

    class Meta:
        model = Hairs
        fields = '__all__'

class HerbivoreSerializer(ModelSerializer):

    class Meta:
        model = Herbivore
        fields = '__all__'

#class HerbivoreCollectionObservationSerializer(ModelSerializer):
#
#    class Meta:
#        model = HerbivoreCollectionObservation
#        fields = '__all__'
#
#
#class HerbivoreDNASerializer(ModelSerializer):
#
#    class Meta:
#        model = HerbivoreDNA
#        fields = '__all__'
#
#
#class HerbivoreSpeciesSerializer(ModelSerializer):
#
#    class Meta:
#        model = HerbivoreSpecies
#        fields = '__all__'
#
#
#class HerbivoreCollectionSerializer(ModelSerializer):
#
#    class Meta:
#        model = HerbivoreCollection
#        fields = '__all__'


class HerbivorySerializer(ModelSerializer):

    class Meta:
        model = Herbivory
        fields = '__all__'


class HPLCResultSerializer(ModelSerializer):

    class Meta:
        model = HPLCResult
        fields = '__all__'


class LeafMassAreaSerializer(ModelSerializer):

    class Meta:
        model = LeafMassArea
        fields = '__all__'


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class NitrogenSerializer(ModelSerializer):

    class Meta:
        model = Nitrogen
        fields = '__all__'


class PlantSerializer(ModelSerializer):

    class Meta:
        model = Plant
        fields = '__all__'


class PlantDNASerializer(ModelSerializer):

    class Meta:
        model = PlantDNA
        fields = '__all__'


class PlantPhotoSerializer(ModelSerializer):

    class Meta:
        model = PlantPhoto
        fields = '__all__'


class PlantSpeciesSerializer(ModelSerializer):

    class Meta:
        model = PlantSpecies
        fields = '__all__'


class PlantVoucherSerializer(ModelSerializer):

    class Meta:
        model = PlantVoucher
        fields = '__all__'


class RAWSerializer(ModelSerializer):

    class Meta:
        model = RAW
        fields = '__all__'


class SiteSerializer(ModelSerializer):

    class Meta:
        model = Site
        fields = '__all__'


class ToughnessSerializer(ModelSerializer):

    class Meta:
        model = Toughness
        fields = '__all__'


class UPLCResultSerializer(ModelSerializer):

    class Meta:
        model = UPLCResult
        fields = '__all__'


class PC_IDSerializer(ModelSerializer):

    class Meta:
        model = PC_ID
        fields = '__all__'


class TyrosineSerializer(ModelSerializer):

    class Meta:
        model = Tyrosine
        fields = '__all__'


class ExpansionSerializer(ModelSerializer):

    class Meta:
        model = Expansion
        fields = '__all__'


class HairMeasurementSerializer(ModelSerializer):

    class Meta:
        model = HairMeasurement 
        fields = '__all__'


class PlantSpeciesHistoricalSerializer(ModelSerializer):

    class Meta:
        model = PlantSpeciesHistorical 
        fields = '__all__'
