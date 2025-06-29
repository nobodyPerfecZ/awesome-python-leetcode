import math
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Given an array of strings words and a width maxWidth, format the text such that
        each line has exactly maxWidth characters and is fully (left and right)
        justified.

        You should pack your words in a greedy approach; that is, pack as many words as
        you can in each line. Pad extra spaces ' ' when necessary so that each line has
        exactly maxWidth characters.

        Extra spaces between words should be distributed as evenly as possible. If the
        number of spaces on a line does not divide evenly between words, the empty slots
        on the left will be assigned more spaces than the slots on the right.

        For the last line of text, it should be left-justified, and no extra space is
        inserted between words.

        Note:
        - A word is defined as a character sequence consisting of non-space characters
        only.
        - Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
        - The input array words contains at least one word.
        """
        i = 0
        res = []
        while i < len(words):
            j = i
            wordsWidth, spaceWidth = 0, 0
            while j < len(words) and spaceWidth + len(words[j]) <= maxWidth:
                wordsWidth += len(words[j])
                spaceWidth += len(words[j]) + 1
                j += 1

            k = i
            freeSpace = maxWidth - wordsWidth
            line = ""
            if j >= len(words):
                # left justification
                while k < j:
                    if k != j - 1:
                        numSpace = 1
                    else:
                        numSpace = freeSpace

                    line += words[k]
                    line += numSpace * " "
                    freeSpace -= numSpace
                    k += 1
                res.append(line)
            else:
                # central justification
                numSpacePlace = j - i - 1
                while k < j:
                    if freeSpace > 0 and numSpacePlace == 0:
                        numSpace = freeSpace
                    elif numSpacePlace == 0:
                        numSpace = 0
                    else:
                        numSpace = math.ceil(freeSpace / numSpacePlace)

                    line += words[k]
                    line += numSpace * " "
                    freeSpace -= numSpace
                    numSpacePlace -= 1
                    k += 1
                res.append(line)
            i = j
        return res
