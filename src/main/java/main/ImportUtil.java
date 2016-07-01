package main;

import model.*;
import org.hibernate.Criteria;
import org.hibernate.Session;
import org.hibernate.criterion.Criterion;
import org.hibernate.criterion.Restrictions;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * Created by Zach Zundel on 4/28/2016.
 */
public class ImportUtil {
    public static Chemistry verifyExtractionMatch(String chemistryNumber, int plantNumber, String speciesCode) throws ImportException {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Criteria chemCriteria = session.createCriteria(Chemistry.class);
        Chemistry chemistry = (Chemistry) chemCriteria.add(Restrictions.eq("chemistryNumber", chemistryNumber)).uniqueResult();

        if(chemistry == null) {
            throw new ImportException("Chemistry number: " + chemistryNumber + " does not correspond to any known chemistry!");
        }

        Plant plant = chemistry.getPlant();
        PlantSpecies species;

        if(plantNumber != -1 && plant.getPlantNumber() != plantNumber) {
            throw new ImportException("Plant number does not match plant number for given chemistry number");
        }

        if(plantNumber != -1) {
            Criteria speciesCriteria = session.createCriteria(PlantSpecies.class);
            species = (PlantSpecies) speciesCriteria.add(Restrictions.eq("speciesCode", speciesCode)).uniqueResult();
        } else {
            species = plant.getSpecies();
        }

        if(species == null || !species.getSpeciesCode().equals(speciesCode)) {
            throw new ImportException("Species code does not match species for given chemistry number");
        }

        return chemistry;
    }

    public static HashMap<String, ExtractionWeight> getExtractionWeights(Extraction extraction) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Criteria extractionCriteria = session.createCriteria(ExtractionWeight.class);
        HashMap<String, ExtractionWeight> weights = new HashMap<>();
        for(ExtractionWeight weight : (List<ExtractionWeight>) extractionCriteria.add(Restrictions.eq("extraction", extraction)).list()) {
            weights.put(weight.getAttribute(), weight);
        }

        return weights;
    }

    public static Extraction getExtraction(int extractionNumber) throws ImportException {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Criteria extractionCriteria = session.createCriteria(Extraction.class);
        Extraction extraction = (Extraction) extractionCriteria.add(Restrictions.eq("extractionNumber", extractionNumber)).uniqueResult();

        if(extraction != null) {
            return extraction;
        } else {
            throw new ImportException("No extraction has extraction number " + extractionNumber);
        }
    }
}
