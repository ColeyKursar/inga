package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class ExtractionWeight {
    Extraction extraction;
    String attribute;
    float weight;

    public ExtractionWeight(Extraction extraction, String attribute, float weight) {
        this.extraction = extraction;
        this.attribute = attribute;
        this.weight = weight;
    }

    public ExtractionWeight() {
        this.extraction = null;
        this.attribute = null;
        this.weight = 0;
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
