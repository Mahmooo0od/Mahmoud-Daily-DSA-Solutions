import random

class RandomizedSet:

    def __init__(self):
        self.nums = []           # تحفظ الأرقام للوصول العشوائي
        self.pos_map = {}        # تحفظ (val -> index in nums)

    def insert(self, val: int) -> bool:
        if val in self.pos_map:
            return False
        
        # بنضيف الرقم في آخر الـ List وبنسجل الـ Index بتاعه
        self.pos_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos_map:
            return False
        
        # 1. نجيب index الرقم المراد حذفه
        idx_to_remove = self.pos_map[val]
        last_val = self.nums[-1]
        
        # 2. ننقل آخر عنصر في مكان الرقم المراد حذفه
        self.nums[idx_to_remove] = last_val
        self.pos_map[last_val] = idx_to_remove
        
        # 3. نمسح آخر عنصر من الـ List ومسح الرقم من الـ Map
        self.nums.pop()
        del self.pos_map[val]
        
        return True

    def getRandom(self) -> int:
        # اختيار عنصر عشوائي في O(1)
        return random.choice(self.nums)