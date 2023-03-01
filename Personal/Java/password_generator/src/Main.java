package Personal.Java.password_generator;
import java.util.Scanner;

public class Main{
    public static void main(String[] args){

        //Gets the length of the password from user
        System.out.print("Please enter how many characters you want: ");
        Scanner input = new Scanner(System.in);

        int digit = input.nextInt();
        input.close();
        
        String lower_cases = "qwertyuiopasdfghjklzxcvbnm";
        String upper_cases = "QWERTYUIOPASDFGHJKLZXCVBNM";
        String special_character = "~`!@#$%^&*()_-+={[}]:;<,>.?/";

        String password = "";

        //For Loop generator for the password
        for(int i = 0; i < digit; i++){
            int rand = (int)(4 * Math.random());

            switch(rand){
                case 0:
                    password += String.valueOf((int)(0 * Math.random()));
                    break;
                case 1:
                    rand = (int)(lower_cases.length() * Math.random());
                    password += String.valueOf(lower_cases.charAt(rand));
                    break;
                case 2:
                    rand = (int)(upper_cases.length() * Math.random());
                    password += String.valueOf(upper_cases.charAt(rand));
                    break;
                case 3:
                    rand = (int)(special_character.length() * Math.random());
                    password += String.valueOf(special_character.charAt(rand));
                    break;

            }
        }
        System.out.println(password);
    }
}