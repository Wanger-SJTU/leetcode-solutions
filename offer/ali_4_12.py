
from scipy.special import comb, perm

res1 = 1/ comb(16,2) 
res2 = 1/ comb(8,2)
res3 = 1/ comb(4,2)

res = res1/2 + (1-res1)/2 * res2 *1/2 + (1-res1)/2 * (1-res2) *1/2 *res3/2 + (1-res1)/2 * (1-res2) *1/2 *1/2
print(res)
