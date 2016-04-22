package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class HPLC_Result {
    @Id
    int id;
    @ManyToOne
    Extraction extraction;
    int tyrosine;

    public HPLC_Result(int id, Extraction extraction, int tyrosine) {
        this.id = id;
        this.extraction = extraction;
        this.tyrosine = tyrosine;
    }

    public HPLC_Result() {
        this.id = 0;
        this.extraction = null;
        this.tyrosine = 0;
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

    public int getTyrosine() {
        return tyrosine;
    }

    public void setTyrosine(int tyrosine) {
        this.tyrosine = tyrosine;
    }
}
