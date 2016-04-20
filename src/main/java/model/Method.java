package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class Method {
    int methodNumber;

    public Method(int methodNumber) {
        this.methodNumber = methodNumber;
    }

    public Method() {
        this.methodNumber = 0;
    }

    public int getMethodNumber() {
        return methodNumber;
    }

    public void setMethodNumber(int methodNumber) {
        this.methodNumber = methodNumber;
    }
}
