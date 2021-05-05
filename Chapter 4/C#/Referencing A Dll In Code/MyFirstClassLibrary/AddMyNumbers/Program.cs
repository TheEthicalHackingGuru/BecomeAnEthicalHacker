
using System;
using MyFirstClassLibrary;


namespace AddMyNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            AddNumbers ad = new AddNumbers();
            int newNumber = ad.AddTwoNumbers(1, 2);
            Console.WriteLine(newNumber);
        }
    }
}
