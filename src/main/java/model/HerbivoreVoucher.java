package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class HerbivoreVoucher {
    HerbivoreSpecies species;

    public HerbivoreVoucher(HerbivoreSpecies species) {
        this.species = species;
    }

    public HerbivoreVoucher() {
        this.species = null;
    }

    public HerbivoreSpecies getSpecies() {
        return species;
    }

    public void setSpecies(HerbivoreSpecies species) {
        this.species = species;
    }
}
