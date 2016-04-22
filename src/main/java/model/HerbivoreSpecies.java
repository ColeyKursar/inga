package model;

import javax.persistence.Entity;
import javax.persistence.Id;

/**
 * Created by Zach Zundel on 19.04.2016.
 */
@Entity
public class HerbivoreSpecies {
    @Id
    int id;
    String motu;
    String analysis;
    String sequence;
    String laMotu;
    String blastingFamily;
    String blastingSubfamily;
    String blastingGenus;
    int percentage;
    String bin;
    String notesOnHost;
    String notes;

    public HerbivoreSpecies(int id, String motu, String analysis, String sequence, String laMotu, String blastingFamily,
                            String blastingSubfamily, String blastingGenus, int percentage, String bin,
                            String notesOnHost, String notes) {
        this.id = id;
        this.motu = motu;
        this.analysis = analysis;
        this.sequence = sequence;
        this.laMotu = laMotu;
        this.blastingFamily = blastingFamily;
        this.blastingSubfamily = blastingSubfamily;
        this.blastingGenus = blastingGenus;
        this.percentage = percentage;
        this.bin = bin;
        this.notesOnHost = notesOnHost;
        this.notes = notes;
    }

    public HerbivoreSpecies() {
        this.id = 0;
        this.motu = null;
        this.analysis = null;
        this.sequence = null;
        this.laMotu = null;
        this.blastingFamily = null;
        this.blastingSubfamily = null;
        this.blastingGenus = null;
        this.percentage = 0;
        this.bin = null;
        this.notesOnHost = null;
        this.notes = null;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getMotu() {
        return motu;
    }

    public void setMotu(String motu) {
        this.motu = motu;
    }

    public String getAnalysis() {
        return analysis;
    }

    public void setAnalysis(String analysis) {
        this.analysis = analysis;
    }

    public String getSequence() {
        return sequence;
    }

    public void setSequence(String sequence) {
        this.sequence = sequence;
    }

    public String getLaMotu() {
        return laMotu;
    }

    public void setLaMotu(String laMotu) {
        this.laMotu = laMotu;
    }

    public String getBlastingFamily() {
        return blastingFamily;
    }

    public void setBlastingFamily(String blastingFamily) {
        this.blastingFamily = blastingFamily;
    }

    public String getBlastingSubfamily() {
        return blastingSubfamily;
    }

    public void setBlastingSubfamily(String blastingSubfamily) {
        this.blastingSubfamily = blastingSubfamily;
    }

    public String getBlastingGenus() {
        return blastingGenus;
    }

    public void setBlastingGenus(String blastingGenus) {
        this.blastingGenus = blastingGenus;
    }

    public int getPercentage() {
        return percentage;
    }

    public void setPercentage(int percentage) {
        this.percentage = percentage;
    }

    public String getBin() {
        return bin;
    }

    public void setBin(String bin) {
        this.bin = bin;
    }

    public String getNotesOnHost() {
        return notesOnHost;
    }

    public void setNotesOnHost(String notesOnHost) {
        this.notesOnHost = notesOnHost;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
}
