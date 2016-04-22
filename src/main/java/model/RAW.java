package model;

import javax.persistence.Entity;
import javax.persistence.Id;
import java.nio.file.Path;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
@Entity
public class RAW {
    @Id
    int id;
    String rawFilePath;

    public RAW() {
        this.id = 0;
        rawFilePath = null;
    }

    public RAW(int id, String path) {
        this.id = id;
        this.rawFilePath = path;
    }


    public String getRawFilePath() {
        return rawFilePath;
    }

    public void setRawFilePath(String rawFilePath) {
        this.rawFilePath = rawFilePath;
    }
}
