package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.persistence.ManyToOne;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
@Entity
public class HerbivoreVoucher {
    @Id
    int id;

    @ManyToOne
    HerbivoreSpecies species;

    public HerbivoreVoucher(int id, HerbivoreSpecies species) {
        this.id = id;
        this.species = species;
    }

    public HerbivoreVoucher() {
        this.id = 0;
        this.species = null;
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
}
