package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

/**
 * Created by Zach Zundel on 19.04.2016.
 */

@Entity
public class HerbivoreSpeciesObservation {
    @Id
    int id;
    @ManyToOne
    HerbivoreSpecies species;
    int numberHerbivores;

    public HerbivoreSpeciesObservation(int id, HerbivoreSpecies species, int numberHerbivores) {
        this.id = id;
        this.species = species;
        this.numberHerbivores = numberHerbivores;
    }

    public HerbivoreSpeciesObservation() {
        this.id = 0;
        this.species = null;
        this.numberHerbivores = 0;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public HerbivoreSpecies getSpecies() {
        return species;
    }

    public void setSpecies(HerbivoreSpecies species) {
        this.species = species;
    }

    public int getNumberHerbivores() {
        return numberHerbivores;
    }

    public void setNumberHerbivores(int numberHerbivores) {
        this.numberHerbivores = numberHerbivores;
    }
}
