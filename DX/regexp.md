# Regular Expressions

Regular expressions can be used in DX to parse or find information in text. If regular expressions are allowed, the specific DX documentation for that feature will say so.

## Introduction

Regexps are built up from expressions, quantifiers, and assertions. The simplest expression is a character, e.g. x or 5. An expression can also be a set of characters enclosed in square brackets. [ABCD] will match an A or a B or a C or a D. We can write this same expression as [A-D], and an expression to match any capital letter in the English alphabet is written as [A-Z].
A quantifier specifies the number of occurrences of an expression that must be matched. x{1,1} means match one and only one x. x{1,5} means match a sequence of x characters that contains at least one x but no more than five.
Note that in general regexps cannot be used to check for balanced brackets or tags. For example, a regexp can be written to match an opening html <b> and its closing </b>, if the <b> tags are not nested, but if the <b> tags are nested, that same regexp will match an opening <b> tag with the wrong closing </b>. For the fragment <b>bold <b>bolder</b></b>, the first <b> would be matched with the first </b>, which is not correct. However, it is possible to write a regexp that will match nested brackets or tags correctly, but only if the number of nesting levels is fixed and known. If the number of nesting levels is not fixed and known, it is impossible to write a regexp that will not fail.

Suppose we want a regexp to match integers in the range 0 to 99. At least one digit is required, so we start with the expression [0-9]{1,1}, which matches a single digit exactly once. This regexp matches integers in the range 0 to 9. To match integers up to 99, increase the maximum number of occurrences to 2, so the regexp becomes [0-9]{1,2}. This regexp satisfies the original requirement to match integers from 0 to 99, but it will also match integers that occur in the middle of strings. If we want the matched integer to be the whole string, we must use the anchor assertions, ^ (caret) and $ (dollar). When ^ is the first character in a regexp, it means the regexp must match from the beginning of the string. When $ is the last character of the regexp, it means the regexp must match to the end of the string. The regexp becomes ^[0-9]{1,2}$. Note that assertions, e.g. ^ and $, do not match characters but locations in the string.

If you have seen regexps described elsewhere, they may have looked different from the ones shown here. This is because some sets of characters and some quantifiers are so common that they have been given special symbols to represent them. [0-9] can be replaced with the symbol \d. The quantifier to match exactly one occurrence, {1,1}, can be replaced with the expression itself, i.e. x{1,1} is the same as x. So our 0 to 99 matcher could be written as ^\d{1,2}$. It can also be written ^\d\d{0,1}$, i.e. From the start of the string, match a digit, followed immediately by 0 or 1 digits. In practice, it would be written as ^\d\d?$. The ? is shorthand for the quantifier {0,1}, i.e. 0 or 1 occurrences. ? makes an expression optional. The regexp ^\d\d?$ means From the beginning of the string, match one digit, followed immediately by 0 or 1 more digit, followed immediately by end of string.

To write a regexp that matches one of the words 'mail' or 'letter' or 'correspondence' but does not match words that contain these words, e.g., 'email', 'mailman', 'mailer', and 'letterbox', start with a regexp that matches 'mail'. Expressed fully, the regexp is m{1,1}a{1,1}i{1,1}l{1,1}, but because a character expression is automatically quantified by {1,1}, we can simplify the regexp to mail, i.e., an 'm' followed by an 'a' followed by an 'i' followed by an 'l'. Now we can use the vertical bar | , which means or, to include the other two words, so our regexp for matching any of the three words becomes mail|letter|correspondence. Match 'mail' or 'letter' or 'correspondence'.

While this regexp will match one of the three words we want to match, it will also match words we don't want to match, e.g., 'email'. To prevent the regexp from matching unwanted words, we must tell it to begin and end the match at word boundaries. First we enclose our regexp in parentheses, (mail|letter|correspondence). Parentheses group expressions together, and they identify a part of the regexp that we wish to capture. Enclosing the expression in parentheses allows us to use it as a component in more complex regexps. It also allows us to examine which of the three words was actually matched. To force the match to begin and end on word boundaries, we enclose the regexp in \b word boundary assertions: \b(mail|letter|correspondence)\b. Now the regexp means: Match a word boundary, followed by the regexp in parentheses, followed by a word boundary. The \b assertion matches a position in the regexp, not a character. A word boundary is any non-word character, e.g., a space, newline, or the beginning or ending of a string.

If we want to replace ampersand characters with the HTML entity &amp;, the regexp to match is simply &. But this regexp will also match ampersands that have already been converted to HTML entities. We want to replace only ampersands that are not already followed by amp;. For this, we need the negative lookahead assertion, (?!__). The regexp can then be written as &(?!amp;), i.e. Match an ampersand that is not followed by amp;.

If we want to count all the occurrences of 'Eric' and 'Eirik' in a string, two valid solutions are \b(Eric|Eirik)\b and \bEi?ri[ck]\b. The word boundary assertion '\b' is required to avoid matching words that contain either name, e.g. 'Ericsson'. Note that the second regexp matches more spellings than we want: 'Eric', 'Erik', 'Eiric' and 'Eirik'.

> | Element | "Meaning" |  |  |  |
> | --- | --- | --- | --- | --- |
> | c | A character represents itself unless it has a special regexp meaning. e.g. c matches the character c. |  |  |  |
> | \\c | A character that follows a backslash matches the character itself$ | except as specified below. e.g.$ | To match a literal caret at the beginning of a string$ | write \\^. |
> | \\a | Matches the ASCII bell (BEL$ | 0x07). |  |  |
> | \\f | Matches the ASCII form feed (FF$ | 0x0C). |  |  |
> | \\n | Matches the ASCII line feed (LF$ | 0x0A$ | Unix newline). |  |
> | \\r | Matches the ASCII carriage return (CR$ | 0x0D). |  |  |
> | \\t | Matches the ASCII horizontal tab (HT$ | 0x09). |  |  |
> | \\v | Matches the ASCII vertical tab (VT$ | 0x0B). |  |  |
> | \\xhhhh | Matches the Unicode character corresponding to the hexadecimal number hhhh (between 0x0000 and 0xFFFF). |  |  |  |
> | \\0ooo | (i.e.$ | \\zero ooo)     matches the ASCII/Latin1 character for the octal number ooo (between 0 and 0377). |  |  |
> | . (dot) | Matches any character (including newline). |  |  |  |
> | \\d | Matches a digit (QChar::isDigit()). |  |  |  |
> | \\D | Matches a non-digit. |  |  |  |
> | \\s | Matches a whitespace character (QChar::isSpace()). |  |  |  |
> | \\S | Matches a non-whitespace character. |  |  |  |
> | \\w | Matches a word character (QChar::isLetterOrNumber()$ | QChar::isMark()$ | or '_'). |  |
> | \\W | Matches a non-word character. |  |  |  |
> | \\n | The n-th backreference$ | e.g. \\1$ | \\2$ | etc. |

## Sets of Characters

Square brackets mean match any character contained in the square brackets. The character set abbreviations described above can appear in a character set in square brackets. Except for the character set abbreviations and the following two exceptions, characters do not have special meanings in square brackets.

> |  | "" |  |
> | --- | --- | --- |
> | ^ | The caret negates the character set if it occurs as the first character (i.e. immediately after the opening square bracket). [abc] matches 'a' or 'b' or 'c'$ | but [^abc] matches anything but 'a' or 'b' or 'c'. |
> | -- | The dash indicates a range of characters. [W-Z] matches 'W' or 'X' or 'Y' or 'Z'. |  |

Using the predefined character set abbreviations is more portable than using character ranges across platforms and languages. For example, [0-9] matches a digit in Western alphabets but \d matches a digit in any alphabet.

> [!NOTE]
> In other regexp documentation, sets of characters are often called "character classes".

## Quantifiers

By default, an expression is automatically quantified by {1,1}, i.e. it should occur exactly once. In the following list, E stands for expression. An expression is a character, or an abbreviation for a set of characters, or a set of characters in square brackets, or an expression in parentheses.

> |  | "" |  |  |  |  |  |
> | --- | --- | --- | --- | --- | --- | --- |
> | E? | Matches zero or one occurrences of E. This quantifier means The previous expression is optional$ | because it will match whether or not the expression is found. E? is the same as E{0$ | 1}. e.g.$ | dents? matches 'dent' or 'dents'. |  |  |
> | E+ | Matches one or more occurrences of E. E+ is the same as E{1$ | }. e.g.$ | 0+ matches '0'$ | '00'$ | '000'$ | etc. |
> | E* | Matches zero or more occurrences of E. It is the same as E{0$ | }. The * quantifier is often used in error where + should be used. For example$ | if \\s*$$ is used in an expression to match strings that end in whitespace$ | it will match every string because \\s*$$ means Match zero or more whitespaces followed by end of string. The correct regexp to match strings that have at least one trailing whitespace character is \\s+$$. |  |  |
> | E{n} | Matches exactly n occurrences of E. E{n} is the same as repeating E n times. For example$ | x{5} is the same as xxxxx. It is also the same as E{n$ | n}$ | e.g. x{5$ | 5}. |  |
> | E{n$ | } | Matches at least n occurrences of E. |  |  |  |  |
> | E{$ | m} | Matches at most m occurrences of E. E{$ | m} is the same as E{0$ | m}. |  |  |

To apply a quantifier to more than just the preceding character, use parentheses to group characters together in an expression. For example, tag+ matches a 't' followed by an 'a' followed by at least one 'g', whereas (tag)+ matches at least one occurrence of 'tag'.

## Assertions

Assertions make some statement about the text at the point where they occur in the regexp but they do not match any characters. In the following list E stands for any expression.

> |  | "" |  |  |  |
> | --- | --- | --- | --- | --- |
> | ^ | The caret signifies the beginning of the string. If you wish to match a literal ^ you must escape it by writing \\\\^. For example$ | ^#include will only match strings which begin with the characters '#include'. (When the caret is the first character of a character set it has a special meaning$ | see Sets of Characters.) |  |
> | $$ | The dollar signifies the end of the string. For example \\d\\s*$ will match strings which end with a digit optionally followed by whitespace. If you wish to match a literal $ you must escape it by writing \\\$$. |  |  |  |
> | \\b | A word boundary. For example the regexp \\bOK\\b means match immediately after a word boundary (e.g. start of string or whitespace) the letter 'O' then the letter 'K' immediately before another word boundary (e.g. end of string or whitespace). But note that the assertion does not actually match any whitespace so if we write (\\bOK\\b) and we have a match it will only contain 'OK' even if the string is "It's OK now". |  |  |  |
> | \\B | A non-word boundary. This assertion is true wherever \\b is false. For example if we searched for \\Bon\\B in "Left on" the match would fail (space and end of string aren't non-word boundaries)$ | but it would match in "tonne". |  |  |
> | (?=E) | Positive lookahead. This assertion is true if the expression matches at this point in the regexp. For example$ | const(?=\\s+char) matches 'const' whenever it is followed by 'char'$ | as in 'static const char * '. (Compare with const\\s+char$ | which matches 'static const char * '.) |
> | (?!E) | Negative lookahead. This assertion is true if the expression does not match at this point in the regexp. For example$ | const(?!\\s+char) matches 'const' except when it is followed by 'char'. |  |  |
