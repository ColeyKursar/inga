package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import java.util.Date;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class UPLC_Result {
    @Id
    int id;
    @ManyToOne
    RAW raw;
    @ManyToOne
    Converted converted;
    String diva;
    Date date;
    String mode;
    String sampleType;
    String sampleId;
    @ManyToOne
    Extraction extraction;
    String tunePage;
    String projectName;
    String msMethod;
    String uplcMethod;
    int msMode;
    @ManyToOne
    RTI_QC rti;
    String isTest;
    int isPPM;
    int isRT;
    int rtShift;
    int isTIC;
    int isSN;
    String notes;
    String allInga;
    String chemocoding;

    public UPLC_Result(int id, RAW raw, Converted converted, String diva, Date date, String mode, String sampleType,
                       String sampleId, Extraction extraction, String tunePage, String projectName, String msMethod,
                       String uplcMethod, int msMode, RTI_QC rti, String isTest, int isPPM, int isRT, int rtShift,
                       int isTIC, int isSN, String notes, String allInga, String chemocoding) {
        this.id = id;
        this.raw = raw;
        this.converted = converted;
        this.diva = diva;
        this.date = date;
        this.mode = mode;
        this.sampleType = sampleType;
        this.sampleId = sampleId;
        this.extraction = extraction;
        this.tunePage = tunePage;
        this.projectName = projectName;
        this.msMethod = msMethod;
        this.uplcMethod = uplcMethod;
        this.msMode = msMode;
        this.rti = rti;
        this.isTest = isTest;
        this.isPPM = isPPM;
        this.isRT = isRT;
        this.rtShift = rtShift;
        this.isTIC = isTIC;
        this.isSN = isSN;
        this.notes = notes;
        this.allInga = allInga;
        this.chemocoding = chemocoding;
    }

    public UPLC_Result() {
        this.id = 0;
        this.raw = null;
        this.converted = null;
        this.diva = null;
        this.date = null;
        this.mode = null;
        this.sampleType = null;
        this.sampleId = null;
        this.extraction = null;
        this.tunePage = null;
        this.projectName = null;
        this.msMethod = null;
        this.uplcMethod = null;
        this.msMode = 0;
        this.rti = null;
        this.isTest = null;
        this.isPPM = 0;
        this.isRT = 0;
        this.rtShift = 0;
        this.isTIC = 0;
        this.isSN = 0;
        this.notes = null;
        this.allInga = null;
        this.chemocoding = null;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public RAW getRaw() {
        return raw;
    }

    public void setRaw(RAW raw) {
        this.raw = raw;
    }

    public Converted getConverted() {
        return converted;
    }

    public void setConverted(Converted converted) {
        this.converted = converted;
    }

    public String getDiva() {
        return diva;
    }

    public void setDiva(String diva) {
        this.diva = diva;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public String getSampleType() {
        return sampleType;
    }

    public void setSampleType(String sampleType) {
        this.sampleType = sampleType;
    }

    public String getSampleId() {
        return sampleId;
    }

    public void setSampleId(String sampleId) {
        this.sampleId = sampleId;
    }

    public Extraction getExtraction() {
        return extraction;
    }

    public void setExtraction(Extraction extraction) {
        this.extraction = extraction;
    }

    public String getTunePage() {
        return tunePage;
    }

    public void setTunePage(String tunePage) {
        this.tunePage = tunePage;
    }

    public String getProjectName() {
        return projectName;
    }

    public void setProjectName(String projectName) {
        this.projectName = projectName;
    }

    public String getMsMethod() {
        return msMethod;
    }

    public void setMsMethod(String msMethod) {
        this.msMethod = msMethod;
    }

    public String getUplcMethod() {
        return uplcMethod;
    }

    public void setUplcMethod(String uplcMethod) {
        this.uplcMethod = uplcMethod;
    }

    public int getMsMode() {
        return msMode;
    }

    public void setMsMode(int msMode) {
        this.msMode = msMode;
    }

    public RTI_QC getRti() {
        return rti;
    }

    public void setRti(RTI_QC rti) {
        this.rti = rti;
    }

    public String getIsTest() {
        return isTest;
    }

    public void setIsTest(String isTest) {
        this.isTest = isTest;
    }

    public int getIsPPM() {
        return isPPM;
    }

    public void setIsPPM(int isPPM) {
        this.isPPM = isPPM;
    }

    public int getIsRT() {
        return isRT;
    }

    public void setIsRT(int isRT) {
        this.isRT = isRT;
    }

    public int getRtShift() {
        return rtShift;
    }

    public void setRtShift(int rtShift) {
        this.rtShift = rtShift;
    }

    public int getIsTIC() {
        return isTIC;
    }

    public void setIsTIC(int isTIC) {
        this.isTIC = isTIC;
    }

    public int getIsSN() {
        return isSN;
    }

    public void setIsSN(int isSN) {
        this.isSN = isSN;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }

    public String getAllInga() {
        return allInga;
    }

    public void setAllInga(String allInga) {
        this.allInga = allInga;
    }

    public String getChemocoding() {
        return chemocoding;
    }

    public void setChemocoding(String chemocoding) {
        this.chemocoding = chemocoding;
    }
}
