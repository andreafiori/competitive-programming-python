"""
Defanging an IP Address | Leetcode 1108 | Easy | https://leetcode.com/problems/defanging-an-ip-address/

"""

class DefangingAnIPAddress:

    def solution(self, address: str) -> str:
        return address.replace('.', '[.]')

    # def defangIPaddr(self, address: str) -> str:
    #     # split and join
    #     return '[.]'.join(address.split('.'))
    # def defangIPaddr(self, address: str) -> str:
    #     # replace
    #     return re.sub('\.', '[.]', address)
    # def defangIPaddr(self, address: str) -> str:
    #     return ''.join('[.]' if c == '.' else c for c in address)
