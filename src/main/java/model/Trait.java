package model;

import java.util.Date;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class Trait {
    Plant plant;
    Date date;

    public Plant getPlant() {
        return plant;
    }

    public void setPlant(Plant plant) {
        this.plant = plant;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }
}
