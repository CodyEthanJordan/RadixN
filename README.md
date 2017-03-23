# Radix N #

Radix N is a radical new positional numbering system which allows you to ambiguously
represent any real number. It addresses a number of fundamental problems which simply
systems like binary, hexadecimal, or the familiar base 10 have.

* Being forced to unambiguously represent numbers leads to less variety and overall boredom
* Having to use a negative sign to represent negative numbers
* Number length scales poorly with large numbers

## Theory Behind Radix N ##

In a typical positional number system there is a fixed radix, and each position
has its value multiplied by this radix raised to a power to represent numbers.

In base 10 this looks like
` 10^3 10^2 10^1 10^0`

Which we typically call things like: "the tens place", "the hundred place", and so on.

To view this a bit more abstractly for a given radix *b* this looks like

`b^3 b^2 b^1 b^0`

Even more abstractly we can say that *n* is the position of that particular digit,
meaning that each digit is multiplied by *b^n* and then summed to represent the total value.

In Radix N, rather than being constrained to a constant base *b* every number is
represented by *n^n*. Meaning that we would have: "the one's place", "the four's place",
"the twenty seven's place", "the two hundred and six's place", and so on.
