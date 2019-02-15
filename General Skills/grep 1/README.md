# *grep 1*
## Information
| Points |Category  | Level|
|--|--|--|
| 75 | General Skills |Easy |

## Challenge

> Can you find the flag in [file](https://2018shell.picoctf.com/static/805ac70722810caa0b1c02bc88ef68d8/file)? This would be really obnoxious to look through by hand, see if you can find a faster way. You can also find the file in /problems/grep-1_0_c0c0c16438cdbee39591397e16389f59 on the shell server.

### Hint

> grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)
## Solution
Let's download the file, it's full in garbage.
The name of the challenge is grep so let's use it.
> open terminal -> move to the folder of the file (by cd) -*> grep "picoCTF" file

 
* grep - the grep command search a pattern in the text 
	* command syntax:
		>   grep "PATTERN" FILENAME

## Flag
> `picoCTF{grep_and_you_will_find_52e63a9f}`

