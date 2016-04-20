package model;

import java.util.ArrayList;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class RTI_QC {
    String rti;
    ArrayList<RTI_QCMember> members;
    boolean pass;
    String notes;

    public RTI_QC(String rti, ArrayList<RTI_QCMember> members, boolean pass, String notes) {
        this.rti = rti;
        this.members = members;
        this.pass = pass;
        this.notes = notes;
    }

    public RTI_QC() {
        this.rti = null;
        this.members = null;
        this.pass = false;
        this.notes = null;
    }

    public String getRti() {
        return rti;
    }

    public void setRti(String rti) {
        this.rti = rti;
    }

    public ArrayList<RTI_QCMember> getMembers() {
        return members;
    }

    public void setMembers(ArrayList<RTI_QCMember> members) {
        this.members = members;
    }

    public boolean isPass() {
        return pass;
    }

    public void setPass(boolean pass) {
        this.pass = pass;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
}
