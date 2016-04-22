package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class ExtractionWeight {
    @Id
    int id;

    @ManyToOne
    Extraction extraction;
    String attribute;
    float weight;

    public ExtractionWeight(int id, Extraction extraction, String attribute, float weight) {
        this.id = id;
        this.extraction = extraction;
        this.attribute = attribute;
        this.weight = weight;
    }

    public ExtractionWeight() {
        this.id = 0;
        this.extraction = null;
        this.attribute = null;
        this.weight = 0;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Extraction getExtraction() {
        return extraction;
    }

    public void setExtraction(Extraction extraction) {
        this.extraction = extraction;
    }

    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }
}
