package model;

import javax.persistence.*;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class Collector {
    @Id
    int id;
    String name;

    public Collector(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public Collector() {
        id = 0;
        name = null;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
