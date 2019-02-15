# General Warmup 1

## Information
| Points |Category  | Level|
|--|--|--|
| 50 | General Skills |Easy |

## Challenge

> If I told you your grade was 0x41 in hexadecimal, what would it be in ASCII?

### Hint

> Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution
Let's open python and check the value - 

    Open termianl -> "python" -*> chr(0x41)

*chr() - it's function to cast from int value to char,
we wrote **0x**41 to indicate that its in hex base.

## Flag
> `picoCTF{A}`


