//
//  ClimbingLeaderBoard.swift
//  HackerrankProblemsWithSwift
//
//  Created by Sabit Ahmed on 24/6/22.
//

import Foundation

/*
 * Complete the 'climbingLeaderboard' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY ranked
 *  2. INTEGER_ARRAY player
 */

class ClimbingLeaderBoard {
    
    func climbingLeaderboard(ranked: [Int], player: [Int]) -> [Int] {
        // Write your code here
        var output = [Int]()
        var newRanked = Array(Set(ranked))
        newRanked.sort(by: { $0 > $1 })
        var position = 0
        var lastCheckedIndex = newRanked.count - 1
        
        for i in player {
            if i > newRanked[lastCheckedIndex] {
                if lastCheckedIndex == 0 {
                    position = lastCheckedIndex + 1
                    output.append(position)
                    continue
                }
                // print(lastCheckedIndex)
                for k in (0..<lastCheckedIndex).reversed() {
                    if newRanked[k] > i {
                        lastCheckedIndex = k
                        position = lastCheckedIndex + 1
                        break
                    }
                    else if newRanked[k] == i {
                        if k == 0 {
                            lastCheckedIndex = k
                        }
                        else {
                            lastCheckedIndex = k - 1
                        }
                        
                        position = newRanked.firstIndex(of: i)!
                        break
                    }
                    else {
                        if k == 0 {
                            lastCheckedIndex = k
                            position = lastCheckedIndex
                            break
                        }
                    }
                }
            }
            else if i < newRanked[lastCheckedIndex] {
                position = lastCheckedIndex + 1
            }
            else {
                position = newRanked.firstIndex(of: i)!
            }
            // print(lastCheckedIndex)
            output.append(position + 1)
        }
        // print(output)
        return output
    }
    
    func executeCode() {
        print("Input: ")

        guard let rankedCount = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
        else { fatalError("Bad input") }

        guard let rankedTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }

        let ranked: [Int] = rankedTemp.split(separator: " ").map {
            if let rankedItem = Int($0) {
                return rankedItem
            } else { fatalError("Bad input") }
        }

        guard ranked.count == rankedCount else { fatalError("Bad input") }

        guard let playerCount = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
        else { fatalError("Bad input") }

        guard let playerTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }

        let player: [Int] = playerTemp.split(separator: " ").map {
            if let playerItem = Int($0) {
                return playerItem
            } else { fatalError("Bad input") }
        }

        guard player.count == playerCount else { fatalError("Bad input") }

        let result = climbingLeaderboard(ranked: ranked, player: player)

        print("\n")
        print("Output: ")

        for i in result {
            print(i)
        }

    }
}
