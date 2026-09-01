"""
IP to CIDR | LeetCode 751 | https://leetcode.com/problems/ip-to-cidr/

A CIDR block is a compact representation of a range of IP addresses. It is represented as a string in the format "a.b.c.d/x", where "a.b.c.d" is the base IP address and "x" is the number of leading bits in the subnet mask. The subnet mask determines how many IP addresses are included in the CIDR block.

"""

class IpToCidr:
    def ip_to_int(self, ip):
        ans = 0
        for x in ip.split('.'):
            ans = 256 * ans + int(x)
        return ans

    def int_to_ip(self, x):
        return ".".join(str((x >> i) % 256)
                        for i in (24, 16, 8, 0))

    def ip_to_cidr(self, ip: str, n: int) -> list[str]:
        start = self.ip_to_int(ip)
        ans = []
        while n:
            # Last 1 of start or can start from 0
            mask = max(33 - (start & -start).bit_length(), 33 - n.bit_length())
            ans.append(self.int_to_ip(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)
        return ans
