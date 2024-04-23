//JAVA
import java.util.Scanner;

public class Equipo1_ej2 {
    public static String detectarTipoDato(String entrada) {
        try {
            Double.parseDouble(entrada);
            return "numérico";
        } catch (NumberFormatException e) {
            if (entrada.equalsIgnoreCase("true") || entrada.equalsIgnoreCase("false")) {
                return "booleano";
            } else {
                return "cadena";
            }
        }
    }
}