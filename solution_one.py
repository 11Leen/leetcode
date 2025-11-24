class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // هنا تكتب الحل (مثل: استخدام قاموس)
        // مثال:
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j}; // تعيد الموضعين (مثل: {0, 1})
                }
            }
        }
        return {}; // (لا يُستخدم هنا لأن الحل موجود دائمًا)
    }
};
