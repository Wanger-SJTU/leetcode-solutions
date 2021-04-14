#
# @lc app=leetcode.cn id=468 lang=python3
#
# [468] 验证IP地址
#
class Solution:
    def validIPAddress(self, IP: str) -> str:
        ip4=''
        ip6=''
        if '.' in IP and ':' not in IP:
            ip4=IP.split('.')
            if len(ip4)!=4:return "Neither"
        elif ':' in IP and '.' not in IP:
            ip6=IP.split(':')
            if len(ip6)!=8:return "Neither"
        else:return "Neither"
        dic=['a','b','c','d','e','f','A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']
        while ip4:
            for ip in ip4:
                if not ip.isdigit():
                    return "Neither"
                elif int(ip)>255 or int(ip)<0:
                    return "Neither"
                elif ip[0]=='0' and len(ip)>1:
                    return "Neither"
            return "IPv4"
        while ip6:
            for ip in ip6:
                if ip=='' or len(ip)>4:return "Neither"
                for i in ip:
                    if i not in dic:
                        return "Neither"
            return "IPv6"

