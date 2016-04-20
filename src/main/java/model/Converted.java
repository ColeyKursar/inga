package model;

import java.nio.file.Path;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class Converted {
    Path convertedFilePath;

    public Converted() {
        convertedFilePath = null;
    }

    public Converted(Path path) {
        this.convertedFilePath = path;
    }

    public Path getConvertedFilePath() {
        return convertedFilePath;
    }

    public void setConvertedFilePath(Path convertedFilePath) {
        this.convertedFilePath = convertedFilePath;
    }
}
