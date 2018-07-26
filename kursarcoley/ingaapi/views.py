from rest_framework.viewsets import ModelViewSet
from ingaapi.serializers import MethodsSerializer, ChemistrySerializer, ChlorophyllSerializer, ConvertedSerializer, DNASerializer, ExtractionSerializer, ExtractionResultWeightSerializer, ExtrafloralNectariesSerializer, FeatureTableRawDataSerializer, FieldSerializer, HairsSerializer, HerbivoreCollectionObservationSerializer, HerbivoreDNASerializer, HerbivoreSpeciesSerializer, HerbivoreCollectionSerializer, HerbivorySerializer, HPLCResultSerializer, LeafMassAreaSerializer, LocationSerializer, NitrogenSerializer, PlantSerializer, PlantDNASerializer, PlantPhotoSerializer, PlantSpeciesSerializer, PlantVoucherSerializer, RAWSerializer, SiteSerializer, ToughnessSerializer, UPLCResultSerializer, PC_IDSerializer, TyrosineSerializer, ExpansionSerializer, PlantSpeciesHistoricalSerializer, HairMeasurementSerializer 
from inga.models import Methods, Chemistry, Chlorophyll, Converted, DNA, Extraction, ExtractionResultWeight, ExtrafloralNectaries, FeatureTableRawData, Field, Hairs, HerbivoreCollectionObservation, HerbivoreDNA, HerbivoreSpecies, HerbivoreCollection, Herbivory, HPLCResult, LeafMassArea, Location, Nitrogen, Plant, PlantDNA, PlantPhoto, PlantSpecies, PlantVoucher, RAW, Site, Toughness, UPLCResult, PC_ID, Tyrosine, PlantSpeciesHistorical, Expansion, HairMeasurement


class ChemistryViewSet(ModelViewSet):
    queryset = Chemistry.objects.all()
    serializer_class = ChemistrySerializer
    filter_fields = "__all__"


class ChlorophyllViewSet(ModelViewSet):
    queryset = Chlorophyll.objects.all()
    serializer_class = ChlorophyllSerializer
    filter_fields = "__all__"


class ConvertedViewSet(ModelViewSet):
    queryset = Converted.objects.all()
    serializer_class = ConvertedSerializer
    filter_fields = "__all__"


class DNAViewSet(ModelViewSet):
    queryset = DNA.objects.all()
    serializer_class = DNASerializer
    filter_fields = "__all__"

class ExtractionViewSet(ModelViewSet):
    queryset = Extraction.objects.all()
    serializer_class = ExtractionSerializer
    filter_fields = "__all__"


class ExtractionResultWeightViewSet(ModelViewSet):
    queryset = ExtractionResultWeight.objects.all()
    serializer_class = ExtractionResultWeightSerializer
    filter_fields = "__all__"


class ExtrafloralNectariesViewSet(ModelViewSet):
    queryset = ExtrafloralNectaries.objects.all()
    serializer_class = ExtrafloralNectariesSerializer
    filter_fields = "__all__"


class FeatureTableRawDataViewSet(ModelViewSet):
    queryset = FeatureTableRawData.objects.all()
    serializer_class = FeatureTableRawDataSerializer
    filter_fields = "__all__"


class FieldViewSet(ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    filter_fields = "__all__"


class HairsViewSet(ModelViewSet):
    queryset = Hairs.objects.all()
    serializer_class = HairsSerializer
    filter_fields = "__all__"


class HerbivoreCollectionObservationViewSet(ModelViewSet):
    queryset = HerbivoreCollectionObservation.objects.all()
    serializer_class = HerbivoreCollectionObservationSerializer
    filter_fields = "__all__"


class HerbivoreDNAViewSet(ModelViewSet):
    queryset = HerbivoreDNA.objects.all()
    serializer_class = HerbivoreDNASerializer
    filter_fields = "__all__"


class HerbivoreSpeciesViewSet(ModelViewSet):
    queryset = HerbivoreSpecies.objects.all()
    serializer_class = HerbivoreSpeciesSerializer
    filter_fields = "__all__"


class HerbivoreCollectionViewSet(ModelViewSet):
    queryset = HerbivoreCollection.objects.all()
    serializer_class = HerbivoreCollectionSerializer
    filter_fields = "__all__"


class HerbivoryViewSet(ModelViewSet):
    queryset = Herbivory.objects.all()
    serializer_class = HerbivorySerializer
    filter_fields = "__all__"


class HPLCResultViewSet(ModelViewSet):
    queryset = HPLCResult.objects.all()
    serializer_class = HPLCResultSerializer
    filter_fields = "__all__"


class LeafMassAreaViewSet(ModelViewSet):
    queryset = LeafMassArea.objects.all()
    serializer_class = LeafMassAreaSerializer
    filter_fields = "__all__"


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_fields = "__all__"

class MethodsViewSet(ModelViewSet):
    queryset = Methods.objects.all()
    serializer_class = MethodsSerializer
    filter_fields = "__all__"

class NitrogenViewSet(ModelViewSet):
    queryset = Nitrogen.objects.all()
    serializer_class = NitrogenSerializer
    filter_fields = "__all__"


class PlantViewSet(ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    filter_fields = "__all__"


class PlantDNAViewSet(ModelViewSet):
    queryset = PlantDNA.objects.all()
    serializer_class = PlantDNASerializer
    filter_fields = "__all__"


class PlantPhotoViewSet(ModelViewSet):
    queryset = PlantPhoto.objects.all()
    serializer_class = PlantPhotoSerializer
    filter_fields = "__all__"


class PlantSpeciesViewSet(ModelViewSet):
    queryset = PlantSpecies.objects.all()
    serializer_class = PlantSpeciesSerializer
    filter_fields = "__all__"


class PlantVoucherViewSet(ModelViewSet):
    queryset = PlantVoucher.objects.all()
    serializer_class = PlantVoucherSerializer
    filter_fields = "__all__"


class RAWViewSet(ModelViewSet):
    queryset = RAW.objects.all()
    serializer_class = RAWSerializer
    filter_fields = "__all__"


class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filter_fields = "__all__"


class ToughnessViewSet(ModelViewSet):
    queryset = Toughness.objects.all()
    serializer_class = ToughnessSerializer
    filter_fields = "__all__"


class UPLCResultViewSet(ModelViewSet):
    queryset = UPLCResult.objects.all()
    serializer_class = UPLCResultSerializer
    filter_fields = "__all__"


class PC_IDViewSet(ModelViewSet):
    queryset = PC_ID.objects.all()
    serializer_class = PC_IDSerializer
    filter_fields = "__all__"


class TyrosineViewSet(ModelViewSet):
    queryset = Tyrosine.objects.all()
    serializer_class = TyrosineSerializer
    filter_fields = "__all__"

class HairMeasurementViewSet(ModelViewSet):
    queryset = HairMeasurement.objects.all()
    serializer_class = HairMeasurementSerializer
    filter_fields = "__all__"

class PlantSpeciesHistoricalViewSet(ModelViewSet):
    queryset = PlantSpeciesHistorical.objects.all()
    serializer_class = PlantSpeciesHistoricalSerializer 
    filter_fields = "__all__"

class ExpansionViewSet(ModelViewSet):
    queryset = Expansion.objects.all()
    serializer_class = ExpansionSerializer 
    filter_fields = "__all__"
