package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class LeafMassArea extends Trait {
    String age;
    String size;
    String light;
    double inches;
    double area;
    double dw_g;
    double dw_area_g;
    String dryingMethod;

    public LeafMassArea(String age, String size, String light, double inches, double area,
                        double dw_g, double dw_area_g, String dryingMethod) {
        this.age = age;
        this.size = size;
        this.light = light;
        this.inches = inches;
        this.area = area;
        this.dw_g = dw_g;
        this.dw_area_g = dw_area_g;
        this.dryingMethod = dryingMethod;
    }

    public LeafMassArea() {
        this.age = null;
        this.size = null;
        this.light = null;
        this.inches = 0;
        this.area = 0;
        this.dw_g = 0;
        this.dw_area_g = 0;
        this.dryingMethod = null;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public String getLight() {
        return light;
    }

    public void setLight(String light) {
        this.light = light;
    }

    public double getInches() {
        return inches;
    }

    public void setInches(double inches) {
        this.inches = inches;
    }

    public double getArea() {
        return area;
    }

    public void setArea(double area) {
        this.area = area;
    }

    public double getDw_g() {
        return dw_g;
    }

    public void setDw_g(double dw_g) {
        this.dw_g = dw_g;
    }

    public double getDw_area_g() {
        return dw_area_g;
    }

    public void setDw_area_g(double dw_area_g) {
        this.dw_area_g = dw_area_g;
    }

    public String getDryingMethod() {
        return dryingMethod;
    }

    public void setDryingMethod(String dryingMethod) {
        this.dryingMethod = dryingMethod;
    }
}
