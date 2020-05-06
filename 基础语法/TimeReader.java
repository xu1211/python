import java.util.Scanner;

public class TimeReader
{
   public static void main(String[] args)
   {
      Scanner in = new Scanner(System.in);
      if (in.hasNextInt())
      {
         int hour = in.nextInt();
         if (hour >= 1 && hour <= 12)
         {
            String suffix = in.next();
            if ("am".equals(suffix) || "pm".equals(suffix) )
            {
               // Convert hour to military time
               if("am".equals(suffix) && (hour == 12)){
                  hour = 0;
               }else if("pm".equals(suffix) && (hour!=12)){
                  hour += 12;
               }
               System.out.println(hour);
            }
            else 
            {
               System.out.println("Error: The suffix must be am or pm.");
            }
         }
         else 
         {
            System.out.println("Error: The hour must be between 1 and 12.");
         }
      }
      else 
      {
         System.out.println("Error: Not an integer.");
      }
   }
}