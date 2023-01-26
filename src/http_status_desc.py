#!/usr/bin/env python3

# MIT License
# 
# Copyright © 2023 Subhadip Ghosh
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests
import xml.etree.ElementTree as ET

def _fetch_page(url: str) -> str:
    return requests.request('GET', url).text

def _get_desc_for_code(code: int):
    url = f"https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/{code}"
    page = _fetch_page(url)
    print(page)
    exit(0)
    #page_root = ET.fromstring(page)
    page_root = ET.parse('/tmp/page.html')
    print(page_root.findtext('/html/body/div/div/div[2]/main/article/h1'))

def main():
    print(_get_desc_for_code(200))

if __name__=='__main__':
    main()
