#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import re

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# print(re_telephone.match('010-12345').groups())

def is_valid_email(addr):
    re_email = re.compile(r'(^\w+.?\w+)@\w+(.com|.com.cn)$')
    print(re_email.match(addr))