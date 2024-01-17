import justpy as jp5

def app():
    wp = jp5.QuasarPage()
    h1 = jp5.QDiv(a = wp , text ="Analysis Page" , classes= "text-h3")
    p1 = jp5.QDiv(a = wp , text ="Course Analysis")
    return wp

jp5.justpy(app)