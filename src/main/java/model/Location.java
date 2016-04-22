package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
@Entity
public class Location {
    @Id
    int id;
    @ManyToOne
    Plant plant;
    int gps;
    int trail;
    int measure;
    int offset;
    int side;

    public Location(int id, Plant plant, int gps, int trail, int measure, int offset, int side) {
        this.id = id;
        this.plant = plant;
        this.gps = gps;
        this.trail = trail;
        this.measure = measure;
        this.offset = offset;
        this.side = side;
    }

    public Location() {
        this.id = 0;
        this.plant = null;
        this.gps = 0;
        this.trail = 0;
        this.measure = 0;
        this.offset = 0;
        this.side = 0;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Plant getPlant() {
        return plant;
    }

    public void setPlant(Plant plant) {
        this.plant = plant;
    }

    public int getGps() {
        return gps;
    }

    public void setGps(int gps) {
        this.gps = gps;
    }

    public int getTrail() {
        return trail;
    }

    public void setTrail(int trail) {
        this.trail = trail;
    }

    public int getMeasure() {
        return measure;
    }

    public void setMeasure(int measure) {
        this.measure = measure;
    }

    public int getOffset() {
        return offset;
    }

    public void setOffset(int offset) {
        this.offset = offset;
    }

    public int getSide() {
        return side;
    }

    public void setSide(int side) {
        this.side = side;
    }
}
