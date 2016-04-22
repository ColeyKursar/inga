package model;

import javax.persistence.*;
import java.util.Date;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
@Entity
public class Chlorophyll extends Trait {

    int percentExposed;
    String size;
    String light;
    int spadd;
    double chl_mg_dm2;
    String notes;

    public Chlorophyll() {
        id = 0;
        plant = null;
        date = null;
        percentExposed = 0;
        size = null;
        light = null;
        spadd = 0;
        chl_mg_dm2 = 0.0;
        notes = null;
    }

    public Chlorophyll(int id, Plant plant, Date date, int percentExposed, String size, String light,
                       int spadd, double chl_mg_dm2, String notes) {
        this.id = id;
        this.plant = plant;
        this.date = date;
        this.percentExposed = percentExposed;
        this.size = size;
        this.light = light;
        this.spadd = spadd;
        this.chl_mg_dm2 = chl_mg_dm2;
        this.notes = notes;
    }

    public int getChlorophyllId() {
        return id;
    }

    public void setChlorophyllId(int id) {
        this.id = id;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public int getPercentExposed() {
        return percentExposed;
    }

    public void setPercentExposed(int percentExposed) {
        this.percentExposed = percentExposed;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public String getLight() {
        return light;
    }

    public void setLight(String light) {
        this.light = light;
    }

    public int getSpadd() {
        return spadd;
    }

    public void setSpadd(int spadd) {
        this.spadd = spadd;
    }

    public double getChl_mg_dm2() {
        return chl_mg_dm2;
    }

    public void setChl_mg_dm2(double chl_mg_dm2) {
        this.chl_mg_dm2 = chl_mg_dm2;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
}
