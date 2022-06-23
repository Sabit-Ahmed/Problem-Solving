import Foundation

    
func romanToInt(_ s: String) -> Int {
    
    let stringArray = Array(s)
    var value = 0
    var i = 0
    for _ in 0..<stringArray.count {
        if i > stringArray.count - 1 {
            break
        }
        let char1 = String(stringArray[i])
        let char2 = i + 1 < stringArray.count ? String(stringArray[i + 1]) : ""
        let subString = char1 + char2
        
        if getSpecialCaseValue(subString) {
            let specialValue = getInt(char2) - getInt(char1)
            value += specialValue
            i += 2
        }
        else {
            let normalValue = getInt(char1)
            value += normalValue
            i += 1
        }
    }
    
    return value
}

func getInt(_ s: String) -> Int {

    switch s.uppercased() {
        case "I": return 1
        case "V": return 5
        case "X": return 10
        case "L": return 50
        case "C": return 100
        case "D": return 500
        case "M": return 1000
        default: return 0
    }
}

func getSpecialCaseValue(_ s: String) -> Bool {
    switch s.uppercased() {
        case "IV": return true
        case "IX": return true
        case "XL": return true
        case "XC": return true
        case "CD": return true
        case "CM": return true
        default: return false
    }
}

let a = romanToInt("MCMXCIV")
print(a)
