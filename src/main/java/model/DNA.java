package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class DNA {
    String sequence;

    public DNA(String sequence) {
        this.sequence = sequence;
    }

    public DNA() {
        this.sequence = null;
    }

    public String getSequence() {
        return sequence;
    }

    public void setSequence(String sequence) {
        this.sequence = sequence;
    }
}
