#!/usr/bin/env python
"""
Copyright (C) 2012 Legoktm, Riley Huntley

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
"""
import re
try:
    import pywikibot
except ImportError:
    import wikipedia as pywikibot

regex_skip = """\{\{(Template:)?(Wikivoyage:Graffiti wall/top)\}\}"""
regex_skip = regex_skip.replace('\n', '')
REGEX = re.compile(regex_skip, flags=re.IGNORECASE)

HEADER = "{{Wikivoyage:Graffiti wall/top}}<!--\n*          Welcome to the Graffiti wall!            *\n*          Please leave this part alone             *\n*    Feel free to try your editing skills below     *\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ -->\n"


def clean(box):
    text = box.get()
    if not REGEX.findall(text):
        newtext = HEADER + text
        box.put(newtext, "Reinserting sandbox header")

def main():
    site = pywikibot.getSite()
    generator = [pywikibot.Page(site, "Wikivoyage:Graffiti wall")]
    for sandbox in generator:
        clean(sandbox)

if __name__ == "__main__":
    pywikibot.handleArgs()
    main()
