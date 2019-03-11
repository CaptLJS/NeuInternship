using System;

class Josephus
{

    static int josephus(int n, int k)
    {
        if (n == 1)
            return 1;
        else
            return (josephus(n - 1, k) + k - 1) % n + 1;
    }


    public static void Main()
    {
        int n, step;
        Console.WriteLine("Enter number of people");
        n = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter step");
        step = int.Parse(Console.ReadLine());
        Console.WriteLine("Alive at position " + josephus(n, step));
    }
}

