import re

"""
Defanging an IP Address | https://leetcode.com/problems/defanging-an-ip-address/
"""
class DefangingAnIPAddress:

    def replace(self, address: str) -> str:
        return address.replace('.', '[.]')

    def defang_split_join(self, address: str) -> str:
        # split and join
        return '[.]'.join(address.split('.'))

    def defang_re(self, address: str) -> str:
        # replace
        return re.sub('\.', '[.]', address)

    def defang_join(self, address: str) -> str:
        return ''.join('[.]' if c == '.' else c for c in address)
