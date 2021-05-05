# Heredoc


content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

Ipsum dolor sit amet consectetur adipiscing. In iaculis nunc sed augue lacus viverra vitae congue eu. Tortor consequat id porta nibh venenatis cras. Nibh cras pulvinar mattis nunc sed. Sed nisi lacus sed viverra tellus in hac. Purus in mollis nunc sed id semper risus in hendrerit. 

Sed risus pretium quam vulputate dignissim. Nunc sed id semper risus in hendrerit gravida rutrum. Sed faucibus turpis in eu mi bibendum neque egestas.
""".strip()


print(repr(content))

long_string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \n\nIpsum dolor sit amet consectetur adipiscing. In iaculis nunc sed augue lacus viverra vitae congue eu. Tortor consequat id porta nibh venenatis cras. Nibh cras pulvinar mattis nunc sed. Sed nisi lacus sed viverra tellus in hac. Purus in mollis nunc sed id semper risus in hendrerit. \n\nSed risus pretium quam vulputate dignissim. Nunc sed id semper risus in hendrerit gravida rutrum. Sed faucibus turpis in eu mi bibendum neque egestas.'

print(long_string)

print(repr(content))
