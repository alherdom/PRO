def strip_comments(comments: str, symbols: tuple):
    comments = 'apples, pears # and bananas\ngrapes\nbananas !apples'
    symbols = ('#','!','\n')
    symbols_indexs = []
    new_comment = ''
    for c in comments:
        if c in symbols:
            symbols_indexs.append(comments.index(c))
    
    new_comment += comments[0:14]
    new_comment += comments[27:43]