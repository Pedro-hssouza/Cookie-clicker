import turtle

# Cria a janela
wn = turtle.Screen()
wn.title("Cookie Clicker")
wn.bgcolor("black")

# Registra a imagem do cookie
wn.register_shape("cookie.gif")

# Cria o botão de cookie
cookie = turtle.Turtle()
cookie.shape("cookie.gif")

# Contador de cliques
clicks = 0

# Texto que mostra os cliques
text = turtle.Turtle()
text.hideturtle()
text.color("red")
text.penup()
text.goto(0, 200)
text.write(f"Clicks: {clicks}", align="center", font=("Georgia", 46, "normal"))

# Função que é chamada quando o cookie é clicado
def clicked(x, y):  # turtle.onclick precisa de x e y como parâmetros
    global clicks
    text.clear()
    clicks += 1
    text.write(f"Clicks: {clicks}", align="center", font=("Georgia", 46, "normal"))

# Detecta cliques no cookie
cookie.onclick(clicked)

# Mantém a janela aberta
wn.mainloop()
