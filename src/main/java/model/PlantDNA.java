package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
@Entity
public class PlantDNA {
    @Id
    int id;
    String DNA;
    @ManyToOne
    Plant plant;

    public PlantDNA(int id, String DNA, Plant plant) {
        this.id = id;
        this.DNA = DNA;
        this.plant = plant;
    }

    public PlantDNA() {
        this.id = 0;
        this.DNA = null;
        this.plant = null;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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
