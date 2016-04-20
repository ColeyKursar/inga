package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class PlantSpecies{
    int id;
    String oldSpeciesNumber;
    String speciesCode;
    String genus;
    String speciesName;
    String comment;
    String authority;
    String noteChemAnal;

    public PlantSpecies() {
        this.id = 0;
        this.oldSpeciesNumber = null;
        this.speciesCode = null;
        this.genus = null;
        this.speciesName = null;
        this.comment = null;
        this.authority = null;
        this.noteChemAnal = null;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getOldSpeciesNumber() {
        return oldSpeciesNumber;
    }

    public void setOldSpeciesNumber(String oldSpeciesNumber) {
        this.oldSpeciesNumber = oldSpeciesNumber;
    }

    public String getSpeciesCode() {
        return speciesCode;
    }

    public void setSpeciesCode(String speciesCode) {
        this.speciesCode = speciesCode;
    }

    public String getGenus() {
        return genus;
    }

    public void setGenus(String genus) {
        this.genus = genus;
    }

    public String getSpeciesName() {
        return speciesName;
    }

    public void setSpeciesName(String speciesName) {
        this.speciesName = speciesName;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public String getAuthority() {
        return authority;
    }

    public void setAuthority(String authority) {
        this.authority = authority;
    }

    public String getNoteChemAnal() {
        return noteChemAnal;
    }

    public void setNoteChemAnal(String noteChemAnal) {
        this.noteChemAnal = noteChemAnal;
    }
}
