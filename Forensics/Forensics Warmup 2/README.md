

# *Resources*

## Information
| Points |Category  | Level|
|--|--|--|
| 50 | Forensics |Easy |

## Challenge

> Hmm for some reason I can't open this [PNG](https://2018shell.picoctf.com/static/1e9d081292d7bf0fc19c5dc43fc7bfc2/flag.png)? Any ideas?

### Hint
>  - How do operating systems know what kind of file it is? (It's not just the ending!
>  -   Make sure to submit the flag as picoCTF{XXXXX}

## Solution

Let's download the file, we can see it's extension name is png, but if we try to open the file
we got an error:

> Fatal error reading PNG image file: Not a PNG file

so if it's not a PNG file what is it?
let's use a terminal command to check it -

      Open terminal -> move to the folder of the file (by cd) -*> file flag.png

**file** - command that show us information about the file.
the information we get back is:

> flag.png: JPEG image data, JFIF standard 1.01, resolution (DPI),
> density 75x75, segment length 16, baseline, precision 8, 909x190, frames 3

so it's a JPEG file and not PNG, we want to rename the extension of the file to JPEG
go back to the terminal -*> mv flag.png flag.jpeg

**mv** - command that move files from path to path and can also be used for rename a file
## Flag
> `picoCTF{extensions_are_a_lie}`


