from rest_framework.viewsets import ModelViewSet
from ingaapi.serializers import ChemistrySerializer, ChlorophyllSerializer, ConvertedSerializer, DNASerializer, ExtractionSerializer, ExtractionResultWeightSerializer, ExtrafloralNectariesSerializer, FeatureTableRawDataSerializer, FieldSerializer, HairsSerializer, HerbivoreCollectionObservationSerializer, HerbivoreDNASerializer, HerbivoreSpeciesSerializer, HerbivoreCollectionSerializer, HerbivorySerializer, HPLCResultSerializer, LeafMassAreaSerializer, LocationSerializer, MethodSerializer, NitrogenSerializer, PlantSerializer, PlantDNASerializer, PlantPhotoSerializer, PlantSpeciesSerializer, PlantVoucherSerializer, RAWSerializer, SiteSerializer, ToughnessSerializer, UPLCResultSerializer, VoucherSerializer, PC_IDSerializer, TyrosineSerializer
from inga.models import Chemistry, Chlorophyll, Converted, DNA, Extraction, ExtractionResultWeight, ExtrafloralNectaries, FeatureTableRawData, Field, Hairs, HerbivoreCollectionObservation, HerbivoreDNA, HerbivoreSpecies, HerbivoreCollection, Herbivory, HPLCResult, LeafMassArea, Location, Method, Nitrogen, Plant, PlantDNA, PlantPhoto, PlantSpecies, PlantVoucher, RAW, Site, Toughness, UPLCResult, Voucher, PC_ID, Tyrosine


class ChemistryViewSet(ModelViewSet):
    queryset = Chemistry.objects.all()
    serializer_class = ChemistrySerializer


class ChlorophyllViewSet(ModelViewSet):
    queryset = Chlorophyll.objects.all()
    serializer_class = ChlorophyllSerializer


class ConvertedViewSet(ModelViewSet):
    queryset = Converted.objects.all()
    serializer_class = ConvertedSerializer


class DNAViewSet(ModelViewSet):
    queryset = DNA.objects.all()
    serializer_class = DNASerializer


class ExtractionViewSet(ModelViewSet):
    queryset = Extraction.objects.all()
    serializer_class = ExtractionSerializer


class ExtractionResultWeightViewSet(ModelViewSet):
    queryset = ExtractionResultWeight.objects.all()
    serializer_class = ExtractionResultWeightSerializer


class ExtrafloralNectariesViewSet(ModelViewSet):
    queryset = ExtrafloralNectaries.objects.all()
    serializer_class = ExtrafloralNectariesSerializer


class FeatureTableRawDataViewSet(ModelViewSet):
    queryset = FeatureTableRawData.objects.all()
    serializer_class = FeatureTableRawDataSerializer


class FieldViewSet(ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class HairsViewSet(ModelViewSet):
    queryset = Hairs.objects.all()
    serializer_class = HairsSerializer


class HerbivoreCollectionObservationViewSet(ModelViewSet):
    queryset = HerbivoreCollectionObservation.objects.all()
    serializer_class = HerbivoreCollectionObservationSerializer


class HerbivoreDNAViewSet(ModelViewSet):
    queryset = HerbivoreDNA.objects.all()
    serializer_class = HerbivoreDNASerializer


class HerbivoreSpeciesViewSet(ModelViewSet):
    queryset = HerbivoreSpecies.objects.all()
    serializer_class = HerbivoreSpeciesSerializer


class HerbivoreCollectionViewSet(ModelViewSet):
    queryset = HerbivoreCollection.objects.all()
    serializer_class = HerbivoreCollectionSerializer


class HerbivoryViewSet(ModelViewSet):
    queryset = Herbivory.objects.all()
    serializer_class = HerbivorySerializer


class HPLCResultViewSet(ModelViewSet):
    queryset = HPLCResult.objects.all()
    serializer_class = HPLCResultSerializer


class LeafMassAreaViewSet(ModelViewSet):
    queryset = LeafMassArea.objects.all()
    serializer_class = LeafMassAreaSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class MethodViewSet(ModelViewSet):
    queryset = Method.objects.all()
    serializer_class = MethodSerializer


class NitrogenViewSet(ModelViewSet):
    queryset = Nitrogen.objects.all()
    serializer_class = NitrogenSerializer


class PlantViewSet(ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlantDNAViewSet(ModelViewSet):
    queryset = PlantDNA.objects.all()
    serializer_class = PlantDNASerializer


class PlantPhotoViewSet(ModelViewSet):
    queryset = PlantPhoto.objects.all()
    serializer_class = PlantPhotoSerializer


class PlantSpeciesViewSet(ModelViewSet):
    queryset = PlantSpecies.objects.all()
    serializer_class = PlantSpeciesSerializer


class PlantVoucherViewSet(ModelViewSet):
    queryset = PlantVoucher.objects.all()
    serializer_class = PlantVoucherSerializer


class RAWViewSet(ModelViewSet):
    queryset = RAW.objects.all()
    serializer_class = RAWSerializer


class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class ToughnessViewSet(ModelViewSet):
    queryset = Toughness.objects.all()
    serializer_class = ToughnessSerializer


class UPLCResultViewSet(ModelViewSet):
    queryset = UPLCResult.objects.all()
    serializer_class = UPLCResultSerializer


class VoucherViewSet(ModelViewSet):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer


class PC_IDViewSet(ModelViewSet):
    queryset = PC_ID.objects.all()
    serializer_class = PC_IDSerializer


class TyrosineViewSet(ModelViewSet):
    queryset = Tyrosine.objects.all()
    serializer_class = TyrosineSerializer
