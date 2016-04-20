package model;

/**
 * Created by Zach Zundel on 14.04.2016.
 */
public class Nitrogen extends Trait {
    Chemistry chemistry;
    String age;
    float weightBeforeGrounding;
    String percentageOfExpansion;
    float weightAfterGrounding;
    String sampleNumberForNitrogenAnalysis;
    float subsampleWeight;
    float percentNitrogen;
    String notes;

    public Nitrogen(Chemistry chemistry, String age, float weightBeforeGrounding, String percentageOfExpansion,
                    float weightAfterGrounding, String sampleNumberForNitrogenAnalysis, float subsampleWeight,
                    float percentNitrogen, String notes) {
        this.chemistry = chemistry;
        this.age = age;
        this.weightBeforeGrounding = weightBeforeGrounding;
        this.percentageOfExpansion = percentageOfExpansion;
        this.weightAfterGrounding = weightAfterGrounding;
        this.sampleNumberForNitrogenAnalysis = sampleNumberForNitrogenAnalysis;
        this.subsampleWeight = subsampleWeight;
        this.percentNitrogen = percentNitrogen;
        this.notes = notes;
    }

    public Nitrogen() {
        this.chemistry = null;
        this.age = null;
        this.weightBeforeGrounding = 0;
        this.percentageOfExpansion = null;
        this.weightAfterGrounding = 0;
        this.sampleNumberForNitrogenAnalysis = null;
        this.subsampleWeight = 0;
        this.percentNitrogen = 0;
        this.notes = null;
    }

    public Chemistry getChemistry() {
        return chemistry;
    }

    public void setChemistry(Chemistry chemistry) {
        this.chemistry = chemistry;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public float getWeightBeforeGrounding() {
        return weightBeforeGrounding;
    }

    public void setWeightBeforeGrounding(float weightBeforeGrounding) {
        this.weightBeforeGrounding = weightBeforeGrounding;
    }

    public String getPercentageOfExpansion() {
        return percentageOfExpansion;
    }

    public void setPercentageOfExpansion(String percentageOfExpansion) {
        this.percentageOfExpansion = percentageOfExpansion;
    }

    public float getWeightAfterGrounding() {
        return weightAfterGrounding;
    }

    public void setWeightAfterGrounding(float weightAfterGrounding) {
        this.weightAfterGrounding = weightAfterGrounding;
    }

    public String getSampleNumberForNitrogenAnalysis() {
        return sampleNumberForNitrogenAnalysis;
    }

    public void setSampleNumberForNitrogenAnalysis(String sampleNumberForNitrogenAnalysis) {
        this.sampleNumberForNitrogenAnalysis = sampleNumberForNitrogenAnalysis;
    }

    public float getSubsampleWeight() {
        return subsampleWeight;
    }

    public void setSubsampleWeight(float subsampleWeight) {
        this.subsampleWeight = subsampleWeight;
    }

    public float getPercentNitrogen() {
        return percentNitrogen;
    }

    public void setPercentNitrogen(float percentNitrogen) {
        this.percentNitrogen = percentNitrogen;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
}
