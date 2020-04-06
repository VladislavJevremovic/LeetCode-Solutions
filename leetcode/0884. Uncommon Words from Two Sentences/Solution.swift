// https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution {
    func uncommonFromSentences(_ A: String, _ B: String) -> [String] {
      let a = A.components(separatedBy: " ")
      let b = B.components(separatedBy: " ")

      var c = [String: Int]()
      for w in a {
        c[w] = (c[w] ?? 0) + 1
      }
      for w in b {
        c[w] = (c[w] ?? 0) + 1
      }

      var r = [String]()
      for (k, v) in c {
        if v == 1 {
          r.append(k)
        }
      }

      return r
    }
}

class Solution {
    func uncommonFromSentences(_ A: String, _ B: String) -> [String] {
        // 1) concatenate sentences then split, doesn't matter if we lookup from a single array
        let C = [A, B].joined(separator: " ").components(separatedBy: " ")
        // 2) count occurences for each word
        let D = C.reduce(into: [String: Int]()) {
            $0[$1] = ($0[$1] ?? 0) + 1
        }

        // 3) filter out words with more than one occurence
        return Array(D.filter { $0.value == 1 }.keys)
    }
}