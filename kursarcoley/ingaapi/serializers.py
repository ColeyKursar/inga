from rest_framework.serializers import HyperlinkedModelSerializer
from inga.models import Chemistry, Chlorophyll, Converted, DNA, Extraction, ExtractionResultWeight, ExtrafloralNectaries, FeatureTableRawData, Field, Hairs, HerbivoreCollectionObservation, HerbivoreDNA, HerbivoreSpecies, HerbivoreCollection, Herbivory, HPLCResult, LeafMassArea, Location, Nitrogen, Plant, PlantDNA, PlantPhoto, PlantSpecies, PlantVoucher, RAW, Site, Toughness, UPLCResult, PC_ID, Tyrosine


class ChemistrySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Chemistry
        fields = '__all__'


class ChlorophyllSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Chlorophyll
        fields = '__all__'


class ConvertedSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Converted
        fields = '__all__'


class DNASerializer(HyperlinkedModelSerializer):

    class Meta:
        model = DNA
        fields = '__all__'


class ExtractionSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Extraction
        fields = '__all__'


class ExtractionResultWeightSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = ExtractionResultWeight
        fields = '__all__'


class ExtrafloralNectariesSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = ExtrafloralNectaries
        fields = '__all__'


class FeatureTableRawDataSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = FeatureTableRawData
        fields = '__all__'


class FieldSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Field
        fields = '__all__'


class HairsSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Hairs
        fields = '__all__'


class HerbivoreCollectionObservationSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = HerbivoreCollectionObservation
        fields = '__all__'


class HerbivoreDNASerializer(HyperlinkedModelSerializer):

    class Meta:
        model = HerbivoreDNA
        fields = '__all__'


class HerbivoreSpeciesSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = HerbivoreSpecies
        fields = '__all__'


class HerbivoreCollectionSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = HerbivoreCollection
        fields = '__all__'


class HerbivorySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Herbivory
        fields = '__all__'


class HPLCResultSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = HPLCResult
        fields = '__all__'


class LeafMassAreaSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = LeafMassArea
        fields = '__all__'


class LocationSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class NitrogenSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Nitrogen
        fields = '__all__'


class PlantSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Plant
        fields = '__all__'


class PlantDNASerializer(HyperlinkedModelSerializer):

    class Meta:
        model = PlantDNA
        fields = '__all__'


class PlantPhotoSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = PlantPhoto
        fields = '__all__'


class PlantSpeciesSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = PlantSpecies
        fields = '__all__'


class PlantVoucherSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = PlantVoucher
        fields = '__all__'


class RAWSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = RAW
        fields = '__all__'


class SiteSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Site
        fields = '__all__'


class ToughnessSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Toughness
        fields = '__all__'


class UPLCResultSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = UPLCResult
        fields = '__all__'


class PC_IDSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = PC_ID
        fields = '__all__'


class TyrosineSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Tyrosine
        fields = '__all__'
