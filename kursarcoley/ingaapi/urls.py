from rest_framework.routers import SimpleRouter
from ingaapi import views


router = SimpleRouter()

router.register(r'chemistry', views.ChemistryViewSet)
router.register(r'chlorophyll', views.ChlorophyllViewSet)
router.register(r'converted', views.ConvertedViewSet)
router.register(r'dna', views.DNAViewSet)
router.register(r'extraction', views.ExtractionViewSet)
router.register(r'extractionresultweight', views.ExtractionResultWeightViewSet)
router.register(r'extrafloralnectaries', views.ExtrafloralNectariesViewSet)
router.register(r'featuretablerawdata', views.FeatureTableRawDataViewSet)
router.register(r'field', views.FieldViewSet)
router.register(r'hairs', views.HairsViewSet)
router.register(r'herbivorecollectionobservation', views.HerbivoreCollectionObservationViewSet)
router.register(r'herbivoredna', views.HerbivoreDNAViewSet)
router.register(r'herbivorespecies', views.HerbivoreSpeciesViewSet)
router.register(r'herbivorecollection', views.HerbivoreCollectionViewSet)
router.register(r'herbivory', views.HerbivoryViewSet)
router.register(r'hplcresult', views.HPLCResultViewSet)
router.register(r'leafmassarea', views.LeafMassAreaViewSet)
router.register(r'location', views.LocationViewSet)
router.register(r'method', views.MethodViewSet)
router.register(r'nitrogen', views.NitrogenViewSet)
router.register(r'plant', views.PlantViewSet)
router.register(r'plantdna', views.PlantDNAViewSet)
router.register(r'plantphoto', views.PlantPhotoViewSet)
router.register(r'plantspecies', views.PlantSpeciesViewSet)
router.register(r'plantvoucher', views.PlantVoucherViewSet)
router.register(r'raw', views.RAWViewSet)
router.register(r'site', views.SiteViewSet)
router.register(r'toughness', views.ToughnessViewSet)
router.register(r'uplcresult', views.UPLCResultViewSet)
router.register(r'pc_id', views.PC_IDViewSet)
router.register(r'tyrosine', views.TyrosineViewSet)

urlpatterns = router.urls
