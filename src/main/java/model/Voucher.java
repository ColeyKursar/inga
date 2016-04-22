package model;

import javax.persistence.Entity;
import javax.persistence.Id;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class Voucher {
    @Id
    int id;

    public Voucher() {
        this.id = 0;
    }

    public Voucher(int id) {
        this.id = id;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
}
