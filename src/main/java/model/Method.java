package model;

import javax.persistence.Entity;
import javax.persistence.Id;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
@Entity
public class Method {
    @Id
    int methodNumber;
    String description;

    public Method(int methodNumber, String description) {
        this.methodNumber = methodNumber;
        this.description = description;
    }

    public Method() {
        this.methodNumber = 0;
        this.description = null;
    }

    public int getMethodNumber() {
        return methodNumber;
    }

    public void setMethodNumber(int methodNumber) {
        this.methodNumber = methodNumber;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}
