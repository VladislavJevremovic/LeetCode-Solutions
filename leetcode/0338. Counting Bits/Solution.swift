// https://leetcode.com/problems/counting-bits/

class Solution {
	func countBits(_ num: Int) -> [Int] {
	  var r = [0]
	  if num < 1 { return r }

	  for i in 1...num {
	    if i.isMultiple(of: 2) {
	      r.append(r[i/2])
	    } else {
	      r.append(r[i-1] + 1)
	    }
	  }

	  return r
	}
}