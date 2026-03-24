"""
IP to CIDR | https://leetcode.com/problems/ip-to-cidr/
"""
class IpToCidr:
    """ Given a start IP address ip and a number of ips we need to cover n, return a representation of the range as a list (of smallest possible length) of CIDR blocks. """

    def ipToInt(self, ip: str) -> int:
        ans = 0
        for x in ip.split('.'):
            ans = 256 * ans + int(x)
        return ans

    def intToIP(self, x: int) -> str:
        return ".".join(str((x >> i) % 256)
                        for i in (24, 16, 8, 0))

    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        # Start value of IP
        start = self.ipToInt(ip)
        ans = []
        while n:
            # Last 1 of start or can start from 0
            mask = max(33 - (start & -start).bit_length(), 33 - n.bit_length())
            ans.append(self.intToIP(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)
        return ans
