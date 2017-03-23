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

## Free Space ##

You might be wondering, isn't

## Representing Digits ##
Much like how hexadecimal represents digits with values greater than 9 using the
letters A through F, RadixN uses a similar system.

| Number        | Representation
| :-----------: |:-------------:|
| 0 - 9     | 0 - 9 |
| 10 - 35 | a - z |
| 36 - 61 | A - Z |
| 62 - 73 | ! - + (the top row) |
| 74 + | (Unicode Region) |

The "top row" is to hold down shift, starting with the number 1 and proceeding
to the equals sign along the top of an English keyboard. After this you enter
"the Unicode region" where every digit is represented by successive Unicode
characters. This is, of course, skipping those characters already used up through 74.

You can remember this with the easy mnemonic:

"Zero through nine is fine, then the alphabet, then the alphabet again but uppercase.
Up to the top through numbers again! But holding shift this time and going 2 past that,
then on to Unicode and dawn!"

Note that for especially large values you may need to lobby for the creation of new
Unicode values. Also note that some Unicode values are unprintable or have side effects,
see the section on "The Danger Zone" for details

## On Color ##
Keep in mind that multiline strings may be a single number, but with a newline in
it. You are encouraged to tell apart numbers using font color.
