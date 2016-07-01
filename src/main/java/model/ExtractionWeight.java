package model;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class ExtractionWeight {
    @Id
    @GenericGenerator(name="generator", strategy="increment")
    @GeneratedValue(generator="generator")
    int id;

    @ManyToOne
    Extraction extraction;
    String attribute;
    double weight;

    public ExtractionWeight(Extraction extraction, String attribute, double weight) {
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

    public ExtractionWeight(String attribute) {
        this.attribute = attribute;
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

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }
}
