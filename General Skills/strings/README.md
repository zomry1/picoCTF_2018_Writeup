# *strings*
## Information
| Points |Category  | Level|
|--|--|--|
| 100 | General Skills |Easy |

## Challenge
> Can you find the flag in this [file](https://2018shell.picoctf.com/static/aead5528718d7c26733c42fadab63b6a/strings) without actually running it? You can also find the file in /problems/strings_3_1dbaafa1f8f0556872cad33e16bc8dc7 on the shell server.

### Hint

> [strings](https://linux.die.net/man/1/strings)
## Solution
First of all, we want to make "strings" file readable, so let's use the strings command
> open terminal -> move to the folder of the file (by cd) -*> strings strings > output.txt

* strings - the strings command cast binary/executable file to human-readable string
	* command syntax:
		>   strings FILENAME
		
added **> output.txt** to save the results of the command in output.txt file.
now, we can open the output.txt file and see a lot of garbage, let's do the same trick we did in
grep 1(add link).

    open terminal -> move to the folder of the file (by cd) -*> grep "picoCTF" file

## Flag
> `picoCTF{sTrIngS_sAVeS_Time_2fbe2166}`



