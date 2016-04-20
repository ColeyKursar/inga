package model;

import java.nio.file.Path;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class RAW {
    Path rawFilePath;

    public RAW() {
        rawFilePath = null;
    }

    public RAW(Path path) {
        this.rawFilePath = path;
    }

    public Path getRawFilePath() {
        return rawFilePath;
    }

    public void setRawFilePath(Path rawFilePath) {
        this.rawFilePath = rawFilePath;
    }
}
