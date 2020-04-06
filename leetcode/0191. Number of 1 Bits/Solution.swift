// https://leetcode.com/problems/number-of-1-bits/

func hammingWeight(_ n: Int) -> Int {
  var c = 0, m = n
  while m > 0 {
    c += m & 1
    m >>= 1
  }

  return c
}

assert(hammingWeight(0b00000000000000000000000000001011) == 3)
assert(hammingWeight(0b00000000000000000000000010000000) == 1)
assert(hammingWeight(0b11111111111111111111111111111101) == 31)