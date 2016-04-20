package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class ExtrafloralNectaries extends Trait {
    double basalmm;
    double midmm;
    double apicalmm;
    String color;
    String shape;
    String Type;
    double xEFNmm;
    String notes1;
    String notes2;

    public ExtrafloralNectaries(double basalmm, double midmm, double apicalmm, String color, String shape,
                                String type, double xEFNmm, String notes1, String notes2) {
        this.basalmm = basalmm;
        this.midmm = midmm;
        this.apicalmm = apicalmm;
        this.color = color;
        this.shape = shape;
        this.Type = type;
        this.xEFNmm = xEFNmm;
        this.notes1 = notes1;
        this.notes2 = notes2;
    }

    public ExtrafloralNectaries() {
        this.basalmm = 0;
        this.midmm = 0;
        this.apicalmm = 0;
        this.color = null;
        this.shape = null;
        this.Type = null;
        this.xEFNmm = 0;
        this.notes1 = null;
        this.notes2 = null;
    }

    public double getBasalmm() {
        return basalmm;
    }

    public void setBasalmm(double basalmm) {
        this.basalmm = basalmm;
    }

    public double getMidmm() {
        return midmm;
    }

    public void setMidmm(double midmm) {
        this.midmm = midmm;
    }

    public double getApicalmm() {
        return apicalmm;
    }

    public void setApicalmm(double apicalmm) {
        this.apicalmm = apicalmm;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }

    public String getType() {
        return Type;
    }

    public void setType(String type) {
        Type = type;
    }

    public double getxEFNmm() {
        return xEFNmm;
    }

    public void setxEFNmm(double xEFNmm) {
        this.xEFNmm = xEFNmm;
    }

    public String getNotes1() {
        return notes1;
    }

    public void setNotes1(String notes1) {
        this.notes1 = notes1;
    }

    public String getNotes2() {
        return notes2;
    }

    public void setNotes2(String notes2) {
        this.notes2 = notes2;
    }
}
