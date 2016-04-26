package model;

import javax.persistence.*;
import java.util.Date;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class Chemistry {
    @Id
    int id;
    String chemistryNumber;
    @ManyToOne (cascade = CascadeType.ALL)
    Plant plant;
    Date date;
    String size;
    String light;
    String expMin;
    String expMax;
    Double height;
    String DBH;
    String FWg;
    String age;
    String useField;
    double cur_w;
    double vial_w;
    double unusedMaterial;
    String boxNumber;
    String numberPlants;
    String notes;
    String status;
    String extracted;

    public Chemistry() {
        id = 0;
        plant = null;
        chemistryNumber = null;
        date = null;
        size = null;
        light = null;
        expMin = null;
        expMax = null;
        height = null;
        DBH = null;
        FWg = null;
        age = null;
        useField = null;
        cur_w = 0.0;
        vial_w = 0.0;
        unusedMaterial = 0.0;
        boxNumber = null;
        numberPlants = null;
        notes = null;
        status = null;
        extracted = null;
    }

    public Chemistry(int id, Plant plant, String chemistryNumber, Date date, String size,
                     String light, String expMin, String expMax, Double height, String DBH,
                     String FWg, String age, String use, double cur_w, double vial_w,
                     double unusedMaterial, String boxNumber, String numberPlants, String notes,
                     String status, String extracted) {
        this.id = id;
        this.plant = plant;
        this.chemistryNumber = chemistryNumber;
        this.date = date;
        this.size = size;
        this.light = light;
        this.expMin = expMin;
        this.expMax = expMax;
        this.height = height;
        this.DBH = DBH;
        this.FWg = FWg;
        this.age = age;
        this.useField = use;
        this.cur_w = cur_w;
        this.vial_w = vial_w;
        this.unusedMaterial = unusedMaterial;
        this.boxNumber = boxNumber;
        this.numberPlants = numberPlants;
        this.notes = notes;
        this.status = status;
        this.extracted = extracted;
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

    public String getChemistryNumber() {
        return chemistryNumber;
    }

    public void setChemistryNumber(String chemistryNumber) {
        this.chemistryNumber = chemistryNumber;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
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

    public String getExpMin() {
        return expMin;
    }

    public void setExpMin(String expMin) {
        this.expMin = expMin;
    }

    public String getExpMax() {
        return expMax;
    }

    public void setExpMax(String expMax) {
        this.expMax = expMax;
    }

    public Double getHeight() {
        return height;
    }

    public void setHeight(Double height) {
        this.height = height;
    }

    public String getDBH() {
        return DBH;
    }

    public void setDBH(String DBH) {
        this.DBH = DBH;
    }

    public String getFWg() {
        return FWg;
    }

    public void setFWg(String FWg) {
        this.FWg = FWg;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public String getUse() {
        return useField;
    }

    public void setUse(String use) {
        this.useField = use;
    }

    public double getCur_w() {
        return cur_w;
    }

    public void setCur_w(double cur_w) {
        this.cur_w = cur_w;
    }

    public double getVial_w() {
        return vial_w;
    }

    public void setVial_w(double vial_w) {
        this.vial_w = vial_w;
    }

    public double getUnusedMaterial() {
        return unusedMaterial;
    }

    public void setUnusedMaterial(double unusedMaterial) {
        this.unusedMaterial = unusedMaterial;
    }

    public String getBoxNumber() {
        return boxNumber;
    }

    public void setBoxNumber(String boxNumber) {
        this.boxNumber = boxNumber;
    }

    public String getNumberPlants() {
        return numberPlants;
    }

    public void setNumberPlants(String numberPlants) {
        this.numberPlants = numberPlants;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getExtracted() {
        return extracted;
    }

    public void setExtracted(String extracted) {
        this.extracted = extracted;
    }
}
