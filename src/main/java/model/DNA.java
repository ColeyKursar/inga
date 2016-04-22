package model;

import javax.persistence.*;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class DNA {

    @Id
    int id;
    String sequence;

    public DNA(int id, String sequence) {
        this.id = id;
        this.sequence = sequence;
    }

    public DNA() {
        this.id = 0;
        this.sequence = null;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getSequence() {
        return sequence;
    }

    public void setSequence(String sequence) {
        this.sequence = sequence;
    }
}
