impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let s = target;
  
        let mut o = 0;
        let mut p = 1;
        let n = 0;
        let m = 0;
        let l = nums.len()-1 ;
        let mut t: Vec<i32> = Vec::new();
        loop {
            let n= &nums[o];
            let m= &nums[p];
            if (n+m) ==s && o!=p {
                let o: i32 = o as i32;
                let p: i32 = p as i32;
                t.push(o);
                t.push(p);
                return break;
            }
            if o == l{
                o = o-l;
            }
            o = o+1;
            p = p+l;
            if p > l{
                p = p-nums.len();
            }
            
        }
    t
    }
}