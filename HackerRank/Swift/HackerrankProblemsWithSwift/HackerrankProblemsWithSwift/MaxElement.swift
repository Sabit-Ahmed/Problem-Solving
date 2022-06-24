//
//  MaxElement.swift
//  HackerrankProblemsWithSwift
//
//  Created by Sabit Ahmed on 24/6/22.
//

import Foundation

/*
 * Complete the 'getMax' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts STRING_ARRAY operations as parameter.
 */

class MaxElement {
    
    private func getMax(operations: [String]) -> [Int] {
        var stack = [Int]()
        var finalStack = [Int]()
        // Write your code here
        for i in operations {
            if Int(i) == 2 {
                stack.removeLast()
            }
            else if Int(i) == 3 {
                finalStack.append(stack.max()!)
            }
            else {
                let charArray = i.split(separator: " ")
                stack.append(Int(charArray[1])!)
            }
        }
        
        return finalStack
    }
    
    func executeCode() {
        
        print("Input: ")
        
        guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
        else { fatalError("Bad input") }

        var ops = [String]()

        for _ in 1...n {
            guard let opsItem = readLine() else { fatalError("Bad input") }

            ops.append(opsItem)
        }

        guard ops.count == n else { fatalError("Bad input") }

        let res = getMax(operations: ops)

        print("\n")
        print("Output: ")

        for i in res {
            print(i)
        }
    }

}
