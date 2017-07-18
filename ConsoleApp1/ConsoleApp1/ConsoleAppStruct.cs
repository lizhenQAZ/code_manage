
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class ConsoleAppStruct
    {
        static void Main(string[] args)
        {
            Student s1 = new Student();
            s1.age=10;
            Console.WriteLine(s1.age);
        }
        public struct Student
        {
            public int age;
            public int height;
        }
    }
}
