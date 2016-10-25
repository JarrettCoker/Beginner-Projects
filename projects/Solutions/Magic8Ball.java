import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

/**
 * Created by jdc8521 on 10/19/16.
 *
 * Magic 8-ball class for Beginner Projects repository
 */

public class Magic8Ball {
    private static String[] response = {
            "It is certain", "It is decidedly so", "Without a doubt",
            "Yes, definitely", "You may rely on it", "As I see it, yes",
            "Most likely", "Outlook good", "Yes",
            "Signs point to yes", "Reply hazy try again", "Ask again later",
            "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
            "Don't count on it", "My reply is no", "My sources say no",
            "Outlook not so good", "Very doubtful"
    };

    public static void main(String[] args) {
        String userInput = askQuestion();
        while (!userInput.toLowerCase().equals("q")) {
            displayResponse();
            userInput = askQuestion();
        }
    }

    private static String askQuestion() {
        Scanner kb = new Scanner(System.in);
        System.out.println("What would you like to ask the Magic 8-ball or (q) to quit?");
        return kb.nextLine();
    }

    private static void displayResponse() {
        Random rand = new Random();
        System.out.print("Thinking");
        //This for loop just displays the 3 dots after the word 'Thinking' is printed
        for (int i = 0; i < 3; i++) {
            System.out.print(".");
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("\n" + response[rand.nextInt(response.length)] + "\n");
    }
}
