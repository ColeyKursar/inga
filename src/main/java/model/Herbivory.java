package model;

import java.util.Date;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class Herbivory {
    int id;
    PlantSpecies species;
    Site site;
    Date date;
    Location location;
    int leavesLeaflets;
    int total;
    float xHerbivory;

    public Herbivory(){
        this.id = 0;
        this.species = null;
        this.site = null;
        this.date = null;
        this.location = null;
        this.leavesLeaflets = 0;
        this.total = 0;
        this.xHerbivory = 0;
    }

    public PlantSpecies getSpecies() {
        return species;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getId() {
        return id;
    }

    public void setSpecies(PlantSpecies species) {
        this.species = species;
    }

    public Site getSite() {
        return site;
    }

    public void setSite(Site site) {
        this.site = site;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public Location getLocation() {
        return location;
    }

    public void setLocation(Location location) {
        this.location = location;
    }

    public int getLeavesLeaflets() {
        return leavesLeaflets;
    }

    public void setLeavesLeaflets(int leavesLeaflets) {
        this.leavesLeaflets = leavesLeaflets;
    }

    public int getTotal() {
        return total;
    }

    public void setTotal(int total) {
        this.total = total;
    }

    public float getxHerbivory() {
        return xHerbivory;
    }

    public void setxHerbivory(float xHerbivory) {
        this.xHerbivory = xHerbivory;
    }
}
