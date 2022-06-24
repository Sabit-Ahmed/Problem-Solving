import Foundation

/*
 * Complete the 'getMax' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts STRING_ARRAY operations as parameter.
 */

func getMax(operations: [String]) -> [Int] {
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


var ops = [String]()

let res = getMax(operations: ops)

