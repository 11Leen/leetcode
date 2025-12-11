#include <iostream>
#include <vector> // يجب تضمين المكتبة لدعم المتجهات

using namespace std;

// ملاحظة: يُفضل عادةً وضع هذا المنطق داخل دالة (Function)
int main()
{
    // 1. تعريف مصفوفة الأرقام والهدف (يمكنك تغيير هذه القيم)
    vector<int> nums = { 2, 7, 11, 15 };
    int target = 9;

    // 2. تعريف المتغيرات
    int n = nums.size(); // نحصل على حجم المتجه
    int i, j;

    // 3. الحل بالقوة الغاشمة (Brute Force)
    for (i = 0; i < n; i++)
    {
        // تبدأ j من i + 1 لتجنب تكرار الأزواج واستخدام نفس العنصر مرتين
        for (j = i + 1; j < n; j++)
        {
            // التحقق من المجموع
            if (nums[i] + nums[j] == target)
            {
                // طباعة المؤشرات (الطلب الأصلي يطبع j ثم i)
                cout << "Indices are: " << i << " and " << j << endl;

                // بما أن هناك "حل واحد فقط" (حسب شروط المشكلة)، يمكن الخروج مباشرة
                return 0;
            }
        }
    }

    // إذا لم يتم العثور على حل
    cout << "No two sum solution found." << endl;
    return 0;


