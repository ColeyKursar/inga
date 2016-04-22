package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.persistence.ManyToOne;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class Field {
    @Id
    int id;
    Date date;

    @ManyToOne
    Plant plant;
    int origID;
    String evm;
    String expMin;
    String expMax;
    int efn;
    int ants;
    double antsEFN;
    String antCollection;
    int totalHerbivores;

    @ManyToMany
    List<HerbivoreSpeciesObservation> herbivoreSpeciesObservation;

    @ManyToMany
    List<HerbivoreCollectionObservation> herbivoreCollectionObservation;
    String notes;

    public Field(int id, Date date, Plant plant, int origID, String evm, String expMin, String expMax, int efn, int ants,
                 double antsEFN, String antCollection, int totalHerbivores,
                 ArrayList<HerbivoreSpeciesObservation> herbivoreSpeciesObservation,
                 ArrayList<HerbivoreCollectionObservation> herbiforeCollectionObservation, String notes) {
        this.id = id;
        this.date = date;
        this.plant = plant;
        this.origID = origID;
        this.evm = evm;
        this.expMin = expMin;
        this.expMax = expMax;
        this.efn = efn;
        this.ants = ants;
        this.antsEFN = antsEFN;
        this.antCollection = antCollection;
        this.totalHerbivores = totalHerbivores;
        this.herbivoreSpeciesObservation = herbivoreSpeciesObservation;
        this.herbivoreCollectionObservation = herbiforeCollectionObservation;
        this.notes = notes;
    }

    public Field() {
        this.id = 0;
        this.date = null;
        this.plant = null;
        this.origID = 0;
        this.evm = null;
        this.expMin = null;
        this.expMax = null;
        this.efn = 0;
        this.ants = 0;
        this.antsEFN = 0;
        this.antCollection = null;
        this.totalHerbivores = 0;
        this.herbivoreSpeciesObservation = null;
        this.herbivoreCollectionObservation = null;
        this.notes = null;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public Plant getPlant() {
        return plant;
    }

    public void setPlant(Plant plant) {
        this.plant = plant;
    }

    public int getOrigID() {
        return origID;
    }

    public void setOrigID(int origID) {
        this.origID = origID;
    }

    public String getEvm() {
        return evm;
    }

    public void setEvm(String evm) {
        this.evm = evm;
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

    public int getEfn() {
        return efn;
    }

    public void setEfn(int efn) {
        this.efn = efn;
    }

    public int getAnts() {
        return ants;
    }

    public void setAnts(int ants) {
        this.ants = ants;
    }

    public double getAntsEFN() {
        return antsEFN;
    }

    public void setAntsEFN(double antsEFN) {
        this.antsEFN = antsEFN;
    }

    public String getAntCollection() {
        return antCollection;
    }

    public void setAntCollection(String antCollection) {
        this.antCollection = antCollection;
    }

    public int getTotalHerbivores() {
        return totalHerbivores;
    }

    public void setTotalHerbivores(int totalHerbivores) {
        this.totalHerbivores = totalHerbivores;
    }

    public List<HerbivoreSpeciesObservation> getHerbivoreSpeciesObservation() {
        return herbivoreSpeciesObservation;
    }

    public void setHerbivoreSpeciesObservation(List<HerbivoreSpeciesObservation> herbivoreSpeciesObservation) {
        this.herbivoreSpeciesObservation = herbivoreSpeciesObservation;
    }

    public List<HerbivoreCollectionObservation> getHerbiforeCollectionObservation() {
        return herbivoreCollectionObservation;
    }

    public void setHerbiforeCollectionObservation(ArrayList<HerbivoreCollectionObservation> herbivoreCollectionObservation) {
        this.herbivoreCollectionObservation = herbivoreCollectionObservation;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
}
