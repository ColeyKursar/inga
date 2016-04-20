package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class PlantPhoto {
    String photoPath;
    Plant plant;

    public PlantPhoto(String photoPath, Plant plant) {
        this.photoPath = photoPath;
        this.plant = plant;
    }

    public PlantPhoto() {
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
