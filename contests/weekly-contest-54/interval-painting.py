class Solution:
  def solve(self, nums, target):
    curr_pos = 0
    blocks = defaultdict(int)

    for dest in nums:
      blocks[curr_pos] += 1 if dest > 0 else -1
      blocks[curr_pos+dest] -= 1 if dest > 0 else -1
      curr_pos += dest

    last_pos = 0
    ans = 0
    walked = 0
    for pos,val in sorted(blocks.items()):
      if walked >= target:
        ans += pos - last_pos

      walked += val
      last_pos = pos

    return ans