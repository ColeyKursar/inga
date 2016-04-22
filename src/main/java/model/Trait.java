package model;

import javax.persistence.*;
import java.util.Date;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
@Inheritance(strategy=InheritanceType.TABLE_PER_CLASS)
public class Trait {
    @Id
    int id;
    @ManyToOne
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
