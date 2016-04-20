package model;

/**
 * Created by Zach Zundel on 19.04.2016.
 */
public class HerbivoreSpeciesObservation {
    HerbivoreSpecies species;
    int numberHerbivores;

    public HerbivoreSpeciesObservation(HerbivoreSpecies species, int numberHerbivores) {
        this.species = species;
        this.numberHerbivores = numberHerbivores;
    }

    public HerbivoreSpeciesObservation() {
        this.species = null;
        this.numberHerbivores = 0;
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
