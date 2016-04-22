package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
@Entity
public class RTI_QC {
    @Id
    int id;
    String rti;
    @ManyToMany
    List<RTI_QCMember> members;
    boolean pass;
    String notes;

    public RTI_QC(int id, String rti, List<RTI_QCMember> members, boolean pass, String notes) {
        this.id = id;
        this.rti = rti;
        this.members = members;
        this.pass = pass;
        this.notes = notes;
    }

    public RTI_QC() {
        this.id = 0;
        this.rti = null;
        this.members = null;
        this.pass = false;
        this.notes = null;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getRti() {
        return rti;
    }

    public void setRti(String rti) {
        this.rti = rti;
    }

    public List<RTI_QCMember> getMembers() {
        return members;
    }

    public void setMembers(List<RTI_QCMember> members) {
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
