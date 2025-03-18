# Python中的統計 statistics
import statistics

# 計算列表中的數字的中位數
# 統計學上，中位數，又稱中央值、中值，
# 是一個樣本、種群或機率分布中之一個數值，
# 其可將數值集合劃分爲數量相等的上下兩部分。
# 對於有限的數集，可以通過把所有觀察值高低排序後找出正中間的一個作爲中位數。
# 如果觀察值有偶數個，則中位數不唯一，通常取最中間的兩個數值的平均數作爲中位數
numList = [1, 4, 7, 9]
print("numList:", numList)
print(f"numList中數字的中位數:{statistics.median(numList)}")
numList2 = [1, 4, 7, 9, 100]
print("numList2:", numList2)
print(f"numList2中數字的中位數:{statistics.median(numList2)}")

# 標準差
# 計算列表中數字的標準差
# variance / standard deviation
# 定義： 用於表示一組數值資料中的各數值相對於該組數值資料之平均數的分散程度。
# 計算各數值與平均數的差，取其平方後加總，再除以數值個數，
# 得「變異數」。 變異數開根號後得「標準差」
numList3 = [1, 4, 6, 9]
print("numList3:", numList2)
print(f"numList3中數字的標準差:{statistics.stdev(numList3)}")
