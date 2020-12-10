#   Import regular expression module
import re

sample = 'ABC DEF GHI'

#   findall: list of all matches
findall_result = re.findall(r'\w+', sample)
print(findall_result)

#   split: produces split of the string where match occurs
sample_split = 'ABC;DEF;GHI'
split_result = re.split(r';', sample_split)
print(split_result)

#   sub: replaces the matched group with the supplied group
#   fourth argument is count, default = 0
sample_sub = 'ABC;DEF;GHI'
sub_result_count_0 = re.sub(r';', '_', sample_sub)
sub_result_count_1 = re.sub(r';', '_', sample_sub, 1)
print(sub_result_count_0)
print(sub_result_count_1)


#   search: searches anywhere like Perl,
#   returns a match object (first match), else None
sample_search = 'ABC;DEF;GHI'
search_result = re.search(r'\w+', sample_search)
print(search_result.group())    # match portion
print(search_result.start())    # start index
print(search_result.span())     # start, end indexes

#   match: searches at the beginning
match_sample = 'ELEPHANT'
match_result = re.match(r'L', match_sample)
print(match_result)     # None!

#   search searches for ^X even in multiline mode
#   (new line starting with X)
new_line_result = re.search('^X', 'A\nB\nX', re.MULTILINE)
print(new_line_result)

#   compilation flag/Regex Flag is a enum
#   re.MULTILINE
#   re.ASCII
#   re.IGNORECASE
#   re.DOTALL  # Make the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline.
#   re.VERBOSE  # Can have comments etc. White space is ignored
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")

#   Compile a regular expression pattern into a
#   regular expression object, which can be used
#   for matching using its match(), search() and
#   other methods, described below
#   compile is more efficient when reuse is possible
prog = re.compile(r'\d+')
result = prog.match('Grand Canyon')

#   equivalent:
result = re.match(r'\d+', 'Grand Canyon')

#   Text munging
#   replacing text with a callback,
#   where the callback receives match object


def replace(match_object):
    return match_object.group(0).upper()


print(re.sub(r'^[a-z]?', replace, 'a1b2c3d4e5'))
