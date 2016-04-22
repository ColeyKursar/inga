package model;

import javax.annotation.Generated;
import javax.persistence.Entity;
import javax.persistence.Id;
import java.nio.file.Path;

/**
 * Created by Zach Zundel on 14.04.2016.
 */

@Entity
public class Converted {

    @Id
    int id;
    String convertedFilePath;

    public Converted() {
        id = 0;
        convertedFilePath = null;
    }

    public Converted(int id, String path) {
        this.id = id;
        this.convertedFilePath = path;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getConvertedFilePath() {
        return convertedFilePath;
    }

    public void setConvertedFilePath(String convertedFilePath) {
        this.convertedFilePath = convertedFilePath;
    }
}
