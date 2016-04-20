package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class PlantDNA {
    String DNA;
    Plant plant;

    public PlantDNA(String DNA, Plant plant) {
        this.DNA = DNA;
        this.plant = plant;
    }

    public PlantDNA() {
        this.DNA = null;
        this.plant = null;
    }

    public String getDNA() {
        return DNA;
    }

    public void setDNA(String DNA) {
        this.DNA = DNA;
    }

    public Plant getVoucher() {
        return plant;
    }

    public void setVoucher(Plant plant) {
        this.plant = plant;
    }
}
