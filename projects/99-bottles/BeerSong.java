/*****************************************************
* Program that sings the '99 bottles of beer on
* the wall' song.
*
* Author: Jarrett Coker
* Date: 2/6/2016
*****************************************************/

public class BeerSong 
{
	public static void main(String[] args) 
	{
		singBottlesOfBeer();
	}

	private static void singBottlesOfBeer() 
	{
		for (int i = 99; i >= 1; i--)
		{
			if (i != 1)
			{
				System.out.println(i + " bottles of beer on the wall, " + i + " bottles of beer.");
				System.out.println("Take one down and pass it around, " + (i - 1) + 
								   " bottles of beer on the wall.\n");
			}
			else
			{
				System.out.println(i + " bottle of beer on the wall, " + i + " bottle of beer");
				System.out.println("Take one down and pass it around, " +
								   " no more bottles of bottles of beer on the wall.\n");
			}
		}
		System.out.println("No more bottles of beer on the wall, no more bottles of beer.");
		System.out.println("Go to the store and buy some more, 99 bottles of beer on the wall.");
	}
}
