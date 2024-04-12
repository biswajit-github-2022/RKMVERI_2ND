
import java.io.*;
import hex.genmodel.easy.RowData;
import hex.genmodel.easy.EasyPredictModelWrapper;
import hex.genmodel.easy.prediction.*;
import hex.genmodel.MojoModel;

public class main {
  public static void main(String[] args) throws Exception {
    EasyPredictModelWrapper.Config config = new EasyPredictModelWrapper.Config()
       .setModel(MojoModel.load("GBM_model_python_1712856909638_1.zip"))
       .setEnableLeafAssignment(true)
       .setEnableContributions(true);
    EasyPredictModelWrapper model = new EasyPredictModelWrapper(config);

    RowData row = new RowData();
    row.put("AGE", "68");
    row.put("RACE", "2");
    row.put("DCAPS", "2");
    row.put("VOL", "0");
    row.put("GLEASON", "6");

    BinomialModelPrediction p = model.predictBinomial(row);
    System.out.println("Has penetrated the prostatic capsule (1=yes; 0=no): " + p.label);
    System.out.print("Class probabilities: ");
    for (int i = 0; i < p.classProbabilities.length; i++) {
      if (i > 0) {
        System.out.print(",");
      }
      System.out.print(p.classProbabilities[i]);
    }

    System.out.println("Leaf node assignments: ");
    for (int i=0; i < p.leafNodeAssignments.length; i++) {
      if (i > 0) {
        System.out.print(p.leafNodeAssignments[i]);
      }
    }
    System.out.println("");

    System.out.println("Shapley contributions: ");
    for (int i=0; i < p.contributions.length; i++) {
      if (i > 0) {
        System.out.print(", ");
      }
      System.out.print(model.getContributionNames()[i] + ": " + p.contributions[i]);
    }
    System.out.println("");
  }
}