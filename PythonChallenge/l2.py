"""
- Simple conditional list comprehensions.
"""

def main():
    filename = 'l2_rarechars'
    with open(filename, 'rU') as f:
        str = f.read()
    chars = list(str)

    search_for_rare_chars(chars)

def search_for_rare_chars(chars):
    common_chars = ['!', '@', '#' , '$', '%', '^', '&', '*', '(', ')', '[',
    ']', '_', '{', '}', '\n', '+', '-'] 
    rare_chars = [ char for char in chars if char not in common_chars ]
    print ''.join(rare_chars)

if __name__ == "__main__":
    main()
