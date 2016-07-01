package main;

import com.intellij.uiDesigner.core.GridConstraints;
import com.intellij.uiDesigner.core.GridLayoutManager;
import com.intellij.uiDesigner.core.Spacer;
import model.Chemistry;
import model.Extraction;
import model.ExtractionWeight;

import javax.swing.*;
import javax.swing.text.JTextComponent;
import java.awt.*;
import java.awt.event.*;
import java.util.HashMap;
import java.util.List;
import java.util.Date;

/**
 * Created by Zach Zundel on 4/24/2016.
 */
public class MainFrame {
    private Extraction extraction;
    private HashMap<String, ExtractionWeight> weights;
    private JTabbedPane mainPane;
    private JPanel Extraction;
    private JPanel mainPanel;
    private JTextField yearField;
    private JTextField monthField;
    private JTextField dayField;
    private JTextField chemistField;
    private JTextField extractionNumberField;
    private JTextField chemistryNumberField;
    private JTextField dryWeightField;
    private JTextField emptyVialWeightField;
    private JTextField speciesCodeField;
    private JTextField plantNumberField;
    private JTextField finalWeightField;
    private JTextField proportionRemainingField;
    private JTextField reweighedFinalWeightField;
    private JTextField methodField;
    private JTextField boxField;
    private JButton submitButton;
    private JButton retrieveButton;
    private JLabel percentExtracted;
    private JLabel massExtracted;
    private JLabel dryMarcWeightField;

    public MainFrame() {
        extraction = new Extraction();
        weights = new HashMap<>();

        weights.put("Dry Weight", new ExtractionWeight("Dry Weight"));
        weights.put("Empty Vial Weight", new ExtractionWeight("Empty Vial Weight"));
        weights.put("Mass Extracted", new ExtractionWeight("Mass Extracted"));
        weights.put("Final Weight", new ExtractionWeight("Final Weight"));
        weights.put("Proportion Remaining", new ExtractionWeight("Proportion Remaining"));
        weights.put("Percent Extracted", new ExtractionWeight("Percent Extracted"));
        weights.put("Reweighed Final", new ExtractionWeight("Reweighed Final"));
        weights.put("Dry Marc", new ExtractionWeight("Dry Marc"));

        System.out.println(weights.keySet());

        HibernateUtil.init();
        $$$setupUI$$$();
        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    int month = FormUtil.readInt(monthField);
                    int day = FormUtil.readInt(dayField);
                    int year = FormUtil.readInt(yearField);
                    String chemist = FormUtil.readString(chemistField);
                    String chemistry = FormUtil.readString(chemistryNumberField);
                    double dryWeight = FormUtil.readDouble(dryWeightField);
                    double emptyVialWeight = FormUtil.readDouble(emptyVialWeightField);
                    double massExtractedWeight = FormUtil.readDouble(massExtracted);
                    int extractionNumber = FormUtil.readInt(extractionNumberField);
                    String speciesCode = FormUtil.readString(speciesCodeField);
                    int plantNumber = FormUtil.readInt(plantNumberField);
                    double finalWeight = FormUtil.readDouble(finalWeightField);
                    double proportionRemainingWeight = FormUtil.readDouble(proportionRemainingField);
                    double percentExtractedWeight = FormUtil.readDouble(percentExtracted);
                    double reweighedFinalWeight = FormUtil.readDouble(reweighedFinalWeightField);
                    float method = FormUtil.readFloat(methodField);
                    String box = FormUtil.readString(boxField);
                    double dryMarcWeight = FormUtil.readDouble(dryMarcWeightField);
                    Chemistry chem = ImportUtil.verifyExtractionMatch(chemistry, plantNumber, speciesCode);

                    extraction.setExtractionNumber(extractionNumber);
                    extraction.setDate(new Date(year, month, day));
                    extraction.setChemist(chemist);
                    extraction.setChemistry(chem);
                    extraction.setMethod(method);
                    extraction.setBox(box);

                    HibernateUtil.persistExtraction(extraction);

                    System.out.println(weights.keySet());
                    for(ExtractionWeight weight : weights.values()) {
                        weight.setExtraction(extraction);
                    }
                    weights.get("Dry Weight").setWeight(dryWeight);
                    weights.get("Empty Vial Weight").setWeight(emptyVialWeight);
                    weights.get("Mass Extracted").setWeight(massExtractedWeight);
                    weights.get("Final Weight").setWeight(finalWeight);
                    weights.get("Proportion Remaining").setWeight(proportionRemainingWeight);
                    weights.get("Percent Extracted").setWeight(percentExtractedWeight);
                    weights.get("Reweighed Final").setWeight(reweighedFinalWeight);
                    weights.get("Dry Marc").setWeight(dryMarcWeight);

                    HibernateUtil.persistExtractionWeights(weights.get("Dry Weight"), weights.get("Empty Vial Weight"),
                            weights.get("Mass Extracted"), weights.get("Final Weight"), weights.get("Proportion Remaining"),
                            weights.get("Percent Extracted"), weights.get("Reweighed Final"), weights.get("Dry Marc"));


                    clearForm();

                } catch (ImportException ie) {
                    JOptionPane.showMessageDialog(mainPane, ie.getMessage());
                }
            }
        });
        retrieveButton.addComponentListener(new ComponentAdapter() {
        });
        retrieveButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    int extractionNumber = FormUtil.readInt(extractionNumberField);
                    if (extractionNumber == -1) {
                        throw new ImportException("No extraction number supplied!");
                    }
                    extraction = ImportUtil.getExtraction(extractionNumber);
                    HashMap<String, ExtractionWeight> weight = ImportUtil.getExtractionWeights(extraction);
                    weights = weight;
                    refreshForm();

                } catch (ImportException ie) {
                    JOptionPane.showMessageDialog(mainPane, ie.getMessage());
                }
            }
        });
        emptyVialWeightField.addFocusListener(new FocusAdapter() {
            @Override
            public void focusLost(FocusEvent e) {
                calculateWeights();
                super.focusLost(e);
            }
        });

        finalWeightField.addFocusListener(new FocusAdapter() {
            @Override
            public void focusLost(FocusEvent e) {
                calculateWeights();
                super.focusLost(e);
            }
        });

        dryWeightField.addFocusListener(new FocusAdapter() {
            @Override
            public void focusLost(FocusEvent e) {
                calculateWeights();
                super.focusLost(e);
            }
        });
    }

    private void calculateWeights() {
        if (necessaryWeightsFilled()) {
            try {
                double dryWeight = FormUtil.readDouble(dryWeightField);
                double finalWeight = FormUtil.readDouble(finalWeightField);
                double emptyVial = FormUtil.readDouble(emptyVialWeightField);

                double dryMarc = finalWeight - emptyVial;
                double massExtracted = dryWeight - dryMarc;
                double percentExtracted = (massExtracted / dryWeight) * 100;


                this.massExtracted.setText(String.format("%.4f", massExtracted));
                this.dryMarcWeightField.setText(String.format("%.4f", dryMarc));
                this.percentExtracted.setText(String.format("%.4f", percentExtracted));
            } catch (ImportException ie) {
                JOptionPane.showMessageDialog(mainPane, ie.getMessage());
            }
        }
    }

    private boolean necessaryWeightsFilled() {
        try {
            return (FormUtil.readDouble(dryWeightField) != -1) &&
                    (FormUtil.readDouble(finalWeightField) != -1) &&
                    (FormUtil.readDouble(emptyVialWeightField) != -1);
        } catch (ImportException ie) {
            JOptionPane.showMessageDialog(mainPane, ie.getMessage());
        }

        return false;
    }

    private void clearForm() {
        yearField.setText("YYYY");
        monthField.setText("MM");
        dayField.setText("DD");
        chemistField.setText("");
        extractionNumberField.setText("");
        chemistryNumberField.setText("");
        dryWeightField.setText("");
        emptyVialWeightField.setText("");
        massExtracted.setText("Incomplete Data");
        speciesCodeField.setText("");
        plantNumberField.setText("");
        finalWeightField.setText("");
        proportionRemainingField.setText("");
        percentExtracted.setText("Incomplete Data");
        reweighedFinalWeightField.setText("");
        methodField.setText("");
        boxField.setText("");
        dryMarcWeightField.setText("Incomplete Data");
    }

    private void refreshForm() {
        ExtractionWeight dry = weights.get("Dry Weight");
        ExtractionWeight emptyVial = weights.get("Empty Vial Weight");
        ExtractionWeight massEx = weights.get("Mass Extracted");
        ExtractionWeight finalW = weights.get("Final Weight");
        ExtractionWeight percent = weights.get("Percent Extracted");
        ExtractionWeight proportion = weights.get("Proportion Remaining");
        ExtractionWeight reweighed = weights.get("Reweighed Final");

        populateFromExtractionWeight(dry, dryWeightField);
        populateFromExtractionWeight(emptyVial, emptyVialWeightField);
        populateFromExtractionWeight(massEx, massExtracted);
        populateFromExtractionWeight(finalW, finalWeightField);
        populateFromExtractionWeight(percent, percentExtracted);
        populateFromExtractionWeight(proportion, proportionRemainingField);
        populateFromExtractionWeight(reweighed, reweighedFinalWeightField);

        refreshExtractionData();
    }

    private void refreshExtractionData() {
        dayField.setText(Integer.toString(extraction.getDate().getDay()));
        monthField.setText(Integer.toString(extraction.getDate().getMonth()));
        yearField.setText(Integer.toString(extraction.getDate().getYear()));
        chemistField.setText(extraction.getChemist());
        extractionNumberField.setText(Integer.toString(extraction.getExtractionNumber()));
        methodField.setText(Float.toString(extraction.getMethod()));
        chemistryNumberField.setText(extraction.getChemistry().getChemistryNumber());
        speciesCodeField.setText(extraction.getChemistry().getPlant().getSpecies().getSpeciesCode());
        boxField.setText(extraction.getBox());
        plantNumberField.setText(Integer.toString(extraction.getChemistry().getPlant().getPlantNumber()));
    }

    private void populateFromExtractionWeight(ExtractionWeight weight, JTextComponent field) {
        if (weight != null) {
            field.setText(String.format("%.4f", weight.getWeight()));
        }
    }

    private void populateFromExtractionWeight(ExtractionWeight weight, JLabel field) {
        if (weight != null) {
            field.setText(String.format("%.4f", weight.getWeight()));
        }
    }

    public static void main(String[] args) {
        try {
            // Set System L&F
            UIManager.setLookAndFeel(
                    UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {
            // handle exception
        }

        JFrame frame = new JFrame("MainFrame");
        frame.setContentPane(new MainFrame().mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }

    /**
     * Method generated by IntelliJ IDEA GUI Designer
     * >>> IMPORTANT!! <<<
     * DO NOT edit this method OR call it in your code!
     *
     * @noinspection ALL
     */
    private void $$$setupUI$$$() {
        mainPanel = new JPanel();
        mainPanel.setLayout(new GridLayoutManager(1, 2, new Insets(0, 0, 0, 0), -1, -1));
        mainPane = new JTabbedPane();
        mainPanel.add(mainPane, new GridConstraints(0, 0, 1, 2, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_BOTH, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(200, 200), null, 0, false));
        Extraction = new JPanel();
        Extraction.setLayout(new GridLayoutManager(3, 2, new Insets(10, 10, 10, 10), -1, -1));
        mainPane.addTab("Extraction", Extraction);
        final JPanel panel1 = new JPanel();
        panel1.setLayout(new GridLayoutManager(1, 7, new Insets(0, 0, 0, 0), -1, -1));
        Extraction.add(panel1, new GridConstraints(0, 0, 1, 1, GridConstraints.ANCHOR_NORTH, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        yearField = new JTextField();
        yearField.setName("Year");
        yearField.setText("YYYY");
        panel1.add(yearField, new GridConstraints(0, 5, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(50, -1), null, 0, false));
        final Spacer spacer1 = new Spacer();
        panel1.add(spacer1, new GridConstraints(0, 6, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_WANT_GROW, 1, null, null, null, 0, false));
        final JLabel label1 = new JLabel();
        label1.setText("Date");
        panel1.add(label1, new GridConstraints(0, 0, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        monthField = new JTextField();
        monthField.setName("Month");
        monthField.setText("MM");
        panel1.add(monthField, new GridConstraints(0, 1, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(25, -1), null, 1, false));
        dayField = new JTextField();
        dayField.setName("Day");
        dayField.setText("DD");
        panel1.add(dayField, new GridConstraints(0, 3, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(25, -1), null, 0, false));
        final JLabel label2 = new JLabel();
        label2.setText("/");
        panel1.add(label2, new GridConstraints(0, 2, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label3 = new JLabel();
        label3.setText("/");
        panel1.add(label3, new GridConstraints(0, 4, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(5, -1), null, 0, false));
        final JPanel panel2 = new JPanel();
        panel2.setLayout(new GridLayoutManager(8, 11, new Insets(0, 0, 0, 0), -1, -1));
        Extraction.add(panel2, new GridConstraints(2, 0, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_BOTH, GridConstraints.SIZEPOLICY_CAN_SHRINK | GridConstraints.SIZEPOLICY_CAN_GROW, GridConstraints.SIZEPOLICY_CAN_SHRINK | GridConstraints.SIZEPOLICY_CAN_GROW, null, null, null, 0, false));
        final JLabel label4 = new JLabel();
        label4.setText("Chemist");
        panel2.add(label4, new GridConstraints(0, 0, 1, 1, GridConstraints.ANCHOR_EAST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final Spacer spacer2 = new Spacer();
        panel2.add(spacer2, new GridConstraints(0, 10, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_WANT_GROW, 1, null, null, null, 0, false));
        final Spacer spacer3 = new Spacer();
        panel2.add(spacer3, new GridConstraints(7, 0, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_VERTICAL, 1, GridConstraints.SIZEPOLICY_WANT_GROW, null, null, null, 0, false));
        final JLabel label5 = new JLabel();
        label5.setText("Extraction Number");
        panel2.add(label5, new GridConstraints(0, 4, 1, 1, GridConstraints.ANCHOR_EAST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        extractionNumberField = new JTextField();
        panel2.add(extractionNumberField, new GridConstraints(0, 5, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(100, -1), null, 0, false));
        final JSeparator separator1 = new JSeparator();
        separator1.setOrientation(1);
        panel2.add(separator1, new GridConstraints(0, 3, 8, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_VERTICAL, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(5, -1), null, 0, false));
        final JSeparator separator2 = new JSeparator();
        separator2.setOrientation(1);
        panel2.add(separator2, new GridConstraints(0, 7, 8, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_BOTH, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_WANT_GROW, null, new Dimension(5, -1), null, 0, false));
        chemistryNumberField = new JTextField();
        panel2.add(chemistryNumberField, new GridConstraints(1, 1, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(100, -1), null, 0, false));
        dryWeightField = new JTextField();
        dryWeightField.setName("Dry Weight");
        panel2.add(dryWeightField, new GridConstraints(2, 1, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(100, -1), null, 0, false));
        emptyVialWeightField = new JTextField();
        emptyVialWeightField.setName("Empty Vial Weight");
        panel2.add(emptyVialWeightField, new GridConstraints(3, 1, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(100, -1), null, 0, false));
        final JLabel label6 = new JLabel();
        label6.setText("Chemistry Number");
        panel2.add(label6, new GridConstraints(1, 0, 1, 1, GridConstraints.ANCHOR_EAST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label7 = new JLabel();
        label7.setText("Dry Weight");
        panel2.add(label7, new GridConstraints(2, 0, 1, 1, GridConstraints.ANCHOR_EAST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label8 = new JLabel();
        label8.setText("Empty Vial Weight");
        panel2.add(label8, new GridConstraints(3, 0, 1, 1, GridConstraints.ANCHOR_EAST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label9 = new JLabel();
        label9.setText("Mass Extracted");
        panel2.add(label9, new GridConstraints(4, 0, 1, 1, GridConstraints.ANCHOR_EAST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        chemistField = new JTextField();
        panel2.add(chemistField, new GridConstraints(0, 1, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(50, -1), null, 0, false));
        speciesCodeField = new JTextField();
        panel2.add(speciesCodeField, new GridConstraints(1, 5, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(100, -1), null, 0, false));
        plantNumberField = new JTextField();
        panel2.add(plantNumberField, new GridConstraints(2, 5, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(100, -1), null, 0, false));
        finalWeightField = new JTextField();
        finalWeightField.setName("Final Weight");
        panel2.add(finalWeightField, new GridConstraints(3, 5, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(100, -1), null, 0, false));
        proportionRemainingField = new JTextField();
        proportionRemainingField.setName("Proportion Remaining");
        panel2.add(proportionRemainingField, new GridConstraints(4, 5, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(100, -1), null, 0, false));
        reweighedFinalWeightField = new JTextField();
        reweighedFinalWeightField.setName("Reweighed Final Weight");
        panel2.add(reweighedFinalWeightField, new GridConstraints(6, 5, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(100, -1), null, 0, false));
        final JLabel label10 = new JLabel();
        label10.setText("Species Code");
        panel2.add(label10, new GridConstraints(1, 4, 1, 1, GridConstraints.ANCHOR_EAST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label11 = new JLabel();
        label11.setText("Plant Number");
        panel2.add(label11, new GridConstraints(2, 4, 1, 1, GridConstraints.ANCHOR_EAST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label12 = new JLabel();
        label12.setText("Final Weight");
        panel2.add(label12, new GridConstraints(3, 4, 1, 1, GridConstraints.ANCHOR_EAST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label13 = new JLabel();
        label13.setText("Proportion Remaining");
        panel2.add(label13, new GridConstraints(4, 4, 1, 1, GridConstraints.ANCHOR_EAST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label14 = new JLabel();
        label14.setText("Percent Extracted");
        panel2.add(label14, new GridConstraints(5, 4, 1, 1, GridConstraints.ANCHOR_EAST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label15 = new JLabel();
        label15.setText("Reweighed Final Weight");
        panel2.add(label15, new GridConstraints(6, 4, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(161, -1), null, 0, false));
        final JLabel label16 = new JLabel();
        label16.setText("Method");
        panel2.add(label16, new GridConstraints(0, 8, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        methodField = new JTextField();
        methodField.setName("Method");
        panel2.add(methodField, new GridConstraints(0, 9, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(50, -1), null, 0, false));
        boxField = new JTextField();
        boxField.setName("Box");
        panel2.add(boxField, new GridConstraints(1, 9, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(50, -1), null, 0, false));
        final JLabel label17 = new JLabel();
        label17.setText("Box");
        panel2.add(label17, new GridConstraints(1, 8, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label18 = new JLabel();
        label18.setText("Dry Marc Weight");
        panel2.add(label18, new GridConstraints(2, 8, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        submitButton = new JButton();
        submitButton.setText("Submit");
        panel2.add(submitButton, new GridConstraints(6, 9, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(84, -1), null, 0, false));
        final JLabel label19 = new JLabel();
        label19.setText("g");
        panel2.add(label19, new GridConstraints(2, 2, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label20 = new JLabel();
        label20.setText("g");
        panel2.add(label20, new GridConstraints(3, 2, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label21 = new JLabel();
        label21.setText("g");
        panel2.add(label21, new GridConstraints(4, 2, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label22 = new JLabel();
        label22.setText("g");
        panel2.add(label22, new GridConstraints(3, 6, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JLabel label23 = new JLabel();
        label23.setText("g");
        panel2.add(label23, new GridConstraints(6, 6, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(9, -1), null, 0, false));
        final JLabel label24 = new JLabel();
        label24.setText("g");
        panel2.add(label24, new GridConstraints(2, 10, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        retrieveButton = new JButton();
        retrieveButton.setText("Retrieve");
        panel2.add(retrieveButton, new GridConstraints(6, 8, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_CAN_SHRINK | GridConstraints.SIZEPOLICY_CAN_GROW, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        percentExtracted = new JLabel();
        percentExtracted.setText("Incomplete Data");
        panel2.add(percentExtracted, new GridConstraints(5, 5, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        massExtracted = new JLabel();
        massExtracted.setText("Incomplete Data");
        panel2.add(massExtracted, new GridConstraints(4, 1, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        dryMarcWeightField = new JLabel();
        dryMarcWeightField.setText("Incomplete Data");
        panel2.add(dryMarcWeightField, new GridConstraints(2, 9, 1, 1, GridConstraints.ANCHOR_WEST, GridConstraints.FILL_NONE, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, null, null, 0, false));
        final JSeparator separator3 = new JSeparator();
        Extraction.add(separator3, new GridConstraints(1, 0, 1, 1, GridConstraints.ANCHOR_CENTER, GridConstraints.FILL_HORIZONTAL, GridConstraints.SIZEPOLICY_FIXED, GridConstraints.SIZEPOLICY_FIXED, null, new Dimension(-1, 4), null, 0, false));
        label1.setLabelFor(monthField);
    }

    /**
     * @noinspection ALL
     */
    public JComponent $$$getRootComponent$$$() {
        return mainPanel;
    }
}
