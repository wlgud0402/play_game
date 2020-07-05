style = "flex-direction: column; padding-bottom: 390px; padding-top: 31740px;"

pxStyle = style[style.index("padding-top") + 13:]
size = pxStyle[0:-3]

print(type(size), int(size))