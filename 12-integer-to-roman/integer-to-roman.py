class Solution(object):
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40,
                  10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
                  "X", "IX", "V", "IV", "I"]

        ans = []

        for value, roman in zip(values, romans):
            count, num = divmod(num, value)
            ans.append(roman * count)

        return "".join(ans)