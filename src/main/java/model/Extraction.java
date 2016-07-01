package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import java.util.Date;

/**
 * Created by Zach Zundel on 14.04.2016.
 */


/*
Marc = final - vial
Mass Extracted = dry weight - marc
Percent Extracted = (masse / dry weight) * 100
 */

@Entity
public class Extraction {
    @Id
    int extractionNumber;

    @ManyToOne
    Chemistry chemistry;
    Date date;
    float method;
    String chemist;
    int notebookNumber;
    int extractionNotebookNumber;
    int pageNumber;
    @ManyToOne
    Extraction parentExtraction;
    @ManyToOne
    Chemistry otherChemistry;
    String box;
    String comments;

    public Extraction(int extractionNumber, Chemistry chemistry, Date date, float method, String chemist,
                      int notebookNumber, int extractionNotebookNumber, int pageNumber, Extraction parentExtraction,
                      Chemistry otherChemistry, String box, String comments) {
        this.extractionNumber = extractionNumber;
        this.chemistry = chemistry;
        this.date = date;
        this.method = method;
        this.chemist = chemist;
        this.notebookNumber = notebookNumber;
        this.extractionNotebookNumber = extractionNotebookNumber;
        this.pageNumber = pageNumber;
        this.parentExtraction = parentExtraction;
        this.otherChemistry = otherChemistry;
        this.box = box;
        this.comments = comments;
    }

    public Extraction() {
        this.extractionNumber = 0;
        this.chemistry = null;
        this.date = null;
        this.method = 0;
        this.chemist = null;
        this.notebookNumber = 0;
        this.extractionNotebookNumber = 0;
        this.pageNumber = 0;
        this.parentExtraction = null;
        this.otherChemistry = null;
        this.box = null;
        this.comments = null;
    }

    public int getExtractionNumber() {
        return extractionNumber;
    }

    public void setExtractionNumber(int extractionNumber) {
        this.extractionNumber = extractionNumber;
    }

    public Chemistry getChemistry() {
        return chemistry;
    }

    public void setChemistry(Chemistry chemistry) {
        this.chemistry = chemistry;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public float getMethod() {
        return method;
    }

    public void setMethod(float method) {
        this.method = method;
    }

    public String getChemist() {
        return chemist;
    }

    public void setChemist(String chemist) {
        this.chemist = chemist;
    }

    public int getNotebookNumber() {
        return notebookNumber;
    }

    public void setNotebookNumber(int notebookNumber) {
        this.notebookNumber = notebookNumber;
    }

    public int getExtractionNotebookNumber() {
        return extractionNotebookNumber;
    }

    public void setExtractionNotebookNumber(int extractionNotebookNumber) {
        this.extractionNotebookNumber = extractionNotebookNumber;
    }

    public int getPageNumber() {
        return pageNumber;
    }

    public void setPageNumber(int pageNumber) {
        this.pageNumber = pageNumber;
    }

    public Extraction getParentExtraction() {
        return parentExtraction;
    }

    public void setParentExtraction(Extraction parentExtraction) {
        this.parentExtraction = parentExtraction;
    }

    public Chemistry getOtherChemistry() {
        return otherChemistry;
    }

    public void setOtherChemistry(Chemistry otherChemistry) {
        this.otherChemistry = otherChemistry;
    }

    public String getBox() {
        return box;
    }

    public void setBox(String box) {
        this.box = box;
    }

    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
}
