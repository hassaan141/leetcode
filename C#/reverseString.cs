using System;

public static class Kata
{
  public static string Solution(string str) 
  {
    char [] arr = str.ToCharArray();
    Array.Reverse(arr);
    string rev = new string(arr);
    return rev;
  }
}
