use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, usize> = HashMap::new();

        for (i, &num) in nums.iter().enumerate() {
            if let Some(&pos) = map.get(&(target - num)) {
                return vec![pos as i32, i as i32];
            }
            map.insert(num, i);
        }

        panic!()
    }
}