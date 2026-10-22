from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            # Append length + delimiter + original string
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        n = len(s)

        while i < n:
            # Find the position of the '#' delimiter
            j = i
            while s[j] != "#":
                j += 1

            # Length of the upcoming string
            length = int(s[i:j])

            # Extract the exact string based on length
            start = j + 1
            end = start + length
            decoded_strs.append(s[start:end])

            # Move pointer past the current decoded string
            i = end

        return decoded_strs