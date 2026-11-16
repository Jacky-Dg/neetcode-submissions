class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += "~" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        charKey = s[0]
        to_decode = s[1::]

        return to_decode.split(charKey)
