package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class PlantPhoto {
    @Id
    int id;
    String photoPath;
    @ManyToOne
    Plant plant;

    public PlantPhoto(int id, String photoPath, Plant plant) {
        this.id = id;
        this.photoPath = photoPath;
        this.plant = plant;
    }

    public PlantPhoto() {
        this.id = 0;
        this.photoPath = null;
        this.plant = null;
    }

    public String getPhotoPath() {
        return photoPath;
    }

    public void setPhotoPath(String photoPath) {
        this.photoPath = photoPath;
    }

    public Plant getVoucher() {
        return plant;
    }

    public void setVoucher(Plant plant) {
        this.plant = plant;
    }
}
