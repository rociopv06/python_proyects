# Encryption

This simple code encrypts using the Caesar method but with a twist. A key is inserted and used as the number that switches the letters in your message. 

It also decodes so that whoever you are contacting can decrypt it as long as they know the key and use my code.


## Example:
Key: 123
         
Original message: Hi, lovely to meet you!

Encryption: Y{?1~$)w!,2)"2"vw)1-$(3

- Key in My Value:

My Value is just the ASCII value minus 32. 

I do this to try and minimize the amount of times a value overlaps my frame (32-126)
| Original | ASCII |
| ------------- | ------------- |
|'1' | 17|
| '2' | 18  |
| '3' | 19  |

- Message in ASCII

| Original | Original ASCII | Key in My Value | ASCII sum (Original + Key)| Output
| :-------------: | :-------------: |:-------------: | :-------------: |:-------------: |
|'H' | 72  | 17 | 89 | 'Y' | 
| 'i' | 105| 18 | 123 | '{' |
| ',' | 44 | 19 | 63 | '?'|
|' ' | 32  | 17 | 49 | '1' |
| 'l' | 108| 18 | 126 | '~' |
| 'o' | 111| 19 | 36 (111+19=130 --> 130-126 = 4 --> 32+4 = 36)| '$' |
|'v' | 118 | 17 | 41 (118+17=135 --> 135-126 = 9 --> 32+9 = 41)| ')' |
| 'e' | 101| 18 | 119 | 'w' |
| 'l' | 108| 19 | 33 (108+19=128 --> 127-126 = 1 --> 32+1 = 33) | '!' |
|'y' | 121 | 17 | 44 (121+17=138 --> 138-126 = 12 --> 32+12 = 44)| ',' |
| ' ' | 32 | 18 | 50 | '2' |
| 't' | 116| 19 | 41 (116+19=135 --> 135-126 = 9 --> 32+9 = 41) | ')' |
|'o' | 111 | 17 | 34 (111+17=128 --> 128-126 = 2 --> 32+2 = 34)| '"' |
| ' ' | 32 | 18 | 50 | '2' |
| 'm' | 109| 19 | 34 (109+19=128 --> 128-126 = 2 --> 32+2 = 34)| '"' |
|'e' | 101 | 17 | 118 | 'v' |
| 'e' | 101| 18 | 119 | 'w' |
| 't' | 116| 19 | 41 (116+19=135 --> 135-126 = 9 --> 32+9 = 41)| ')' |
|' ' | 32  | 17 | 49 | '1' |
| 'y' | 121| 18 | 45 (121+18=139 --> 139-126 = 13 --> 32+13 = 45)| '-' | 
| 'o' | 111| 19 | 36 (111+19=130 --> 130-126 = 4 --> 32+4 = 36)| '$' |
|'u' | 117 | 17 | 40 (117+17=134 --> 134-126 = 8 --> 32+8 = 40)| '(' |
| '!' | 33 | 18 | 51 | '3' |




## FYI
Now it support the whole standard ASCII table* this means caps and numbers are fine and they can be used both as part of the key as well as part of the messages. At the moment you can use the latin alphabet and special character such as "-". 

I am working on using another framework so other characters can be encrypted. 


*It does not support the first 31 characters which express things such as NULL or DEL. The only downside of this approach is that it does not support multiline.
