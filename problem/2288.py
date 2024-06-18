class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        percent = (100 - discount) / 100
        words = sentence.split(' ')
        for i in range(len(words)):
            word = words[i]
            if word[0] != '$' or not word[1:].isdigit():
                continue

            price = float(word[1:])
            words[i] = f'${price * percent:.2f}'

        return ' '.join(words)


if __name__ == '__main__':
    sentence = "there are $1 $2 and 5$ candies in the shop"
    discount = 50
    res = Solution().discountPrices(sentence, discount)
    print(res)
