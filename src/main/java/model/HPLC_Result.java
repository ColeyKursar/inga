package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class HPLC_Result {
    Extraction extraction;
    int tyrosine;

    public HPLC_Result(Extraction extraction, int tyrosine) {
        this.extraction = extraction;
        this.tyrosine = tyrosine;
    }

    public HPLC_Result() {
        this.extraction = null;
        this.tyrosine = 0;
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
