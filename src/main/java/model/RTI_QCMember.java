package model;

/**
 * Created by Zach Zundel on 20.04.2016.
 */
public class RTI_QCMember {
    int RT;
    int PPM;
    int SN;
    int PK_WD;

    public RTI_QCMember(int RT, int PPM, int SN, int PK_WD) {
        this.RT = RT;
        this.PPM = PPM;
        this.SN = SN;
        this.PK_WD = PK_WD;
    }

    public RTI_QCMember() {
        this.RT = 0;
        this.PPM = 0;
        this.SN = 0;
        this.PK_WD = 0;
    }

    public int getRT() {
        return RT;
    }

    public void setRT(int RT) {
        this.RT = RT;
    }

    public int getPPM() {
        return PPM;
    }

    public void setPPM(int PPM) {
        this.PPM = PPM;
    }

    public int getSN() {
        return SN;
    }

    public void setSN(int SN) {
        this.SN = SN;
    }

    public int getPK_WD() {
        return PK_WD;
    }

    public void setPK_WD(int PK_WD) {
        this.PK_WD = PK_WD;
    }
}
