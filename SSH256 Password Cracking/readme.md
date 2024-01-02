# Password craking in sha256sum

1. Install pwntools with
```
pip install pwntools
```

2. Create or use a word list file
3. Get a hash value to compare with. Hash value in terminal
```
echo -ne <word> | sha256sum
```
