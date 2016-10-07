from inga.models import Extraction, Chemistry

def build_extraction(form_data):
    extraction = Extraction()
    extraction.extraction_number = form_data["extraction_number"]
    extraction.chemistry = Chemistry.objects.get(chemistry_number=form_data["chemistry"])
    extraction.date = form_data["date"]
    extraction.method = form_data["method"]
    extraction.chemist = form_data["chemist"]
    extraction.dry_weight = form_data["dry_weight"]
    extraction.empty_vial_weight = form_data["empty_vial_weight"]
    extraction.final_weight = form_data["final_weight"]
    extraction.box = form_data["box"]
    extraction.comments = form_data["comments"]
    extraction.save()

    return extraction

def build_extraction_form(extraction):
    data = {}
    data["extraction_number"] = extraction.extraction_number
    data["chemistry"] = extraction.chemistry.chemistry_number
    data["plant"] = extraction.chemistry.plant.plant_number
    data["species"] = extraction.chemistry.plant.species.species_code
    data["date"] = extraction.date
    data["method"] = extraction.method
    data["chemist"] = extraction.chemist
    data["dry_weight"] = extraction.dry_weight
    data["empty_vial_weight
    data["dry_marc_weight"] = extraction.dry_marc_weight
    data["mass_extracted"] = extraction.mass_extracted
    data["percent_extracted"] = extraction.percent_extracted

    return data