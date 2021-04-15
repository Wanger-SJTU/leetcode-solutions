class Solution {
public:
	vector<int> findErrorNums(vector<int>& nums) {
		int n = nums.size();
		int sum = 0, xor1 = 0, xor2 = 0;
		int dup = -1, mis = 1;
		vector<int> ans(2);
		for (int i = 0; i < n; ++i) {
			sum ^= (i + 1) ^ nums[i];
		}
		int t = sum & -sum; //将sum二进制表示下除最靠右的1保留外，其余都置为0
		for (int i = 1; i < n + 1; ++i) {
			if (t & i)
				xor1 ^= i;
			else
				xor2 ^= i;
		}
		for (int i = 0; i < n; ++i) {
			if (t & nums[i])
				xor1 ^= nums[i];
			else
				xor2 ^= nums[i];
		}
		int count = 0;
		for (int i = 0; i < n; ++i) {
			if (nums[i] == xor1)
				count++;
		}
		if (count == 0) { dup = xor2; mis = xor1; }
		else { dup = xor1; mis = xor2; }

		ans[0] = dup; ans[1] = mis;
		return ans;
    }
};