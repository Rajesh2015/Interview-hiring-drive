// Problem Statement

// You are given a string S consisting of lowercase English letters.

// A subsequence of a string is formed by deleting zero or more characters without changing the order of the remaining characters.

// Write a function to generate all possible subsequences of the given string.

// 🔹 Input

// A single string S

// 1 ≤ length(S) ≤ 15

// 🔹 Output

// Return all possible subsequences of the string

// The empty string ("") is considered a valid subsequence

// Example:
// S = "abc"
// Output: List("", "a", "b", "c", "ab", "ac", "bc", "abc")

object Solution {
  
  def subsequences(s: String): List[String] = {
    // Write your solution here
    
    
    
    List()
  }
  
  // Test cases
  def main(args: Array[String]): Unit = {
    // Test case 1
    val test1 = "abc"
    println(s"Input: $test1")
    println(s"Output: ${subsequences(test1)}")
    println()
    
    // Test case 2
    val test2 = "ab"
    println(s"Input: $test2")
    println(s"Output: ${subsequences(test2)}")
    println()
    
    // Add more test cases as needed
  }
}
