package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class Collector {
    String name;

    public Collector(String name) {
        this.name = name;
    }

    public Collector() {
        name = null;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
