import flet as ft
import os
from modulos import hoursandDate
from time import sleep

def main(page: ft.Page):
    page.window.width = 900
    page.window.height = 800
    page.padding = 0
    page.scroll = ft.ScrollMode.HIDDEN
    page.window.center()
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    folder = 'assets'
    origin = os.path.join(folder, 'icons')

    def close_banner(e):
        page.close(banner)

    info = ft.Text(
        value= 'Este e um aviso!',
        size= 16,
        color=ft.Colors.BLACK,
        weight= ft.FontWeight.W_400
    )

    style_button = ft.ButtonStyle(
        color= ft.Colors.RED_500,
        bgcolor= 'transparent'
    )

    banner = ft.Banner(
        bgcolor=ft.Colors.AMBER_100,
        leading=ft.Icon(ft.Icons.WARNING, color=ft.Colors.AMBER_800, size=25),
        content=ft.Row([info]),
        actions=[
            ft.TextButton(text='Ok!', style=style_button, on_click=close_banner)
        ]
    )

    logo_sys = ft.Image(
        src= os.path.join(origin, 'system.png'),
        width= 32
    )

    h1 = ft.Text(
        value= 'mySystem 0.1.1',
        size= 30,
        weight= ft.FontWeight.W_400
    )

    h2 = ft.Text(
        value= 'Esse e um software de teste.',
        size= 14,
        weight= ft.FontWeight.W_400,
        opacity= .6
    )

    bar_search = ft.TextField(
        label= 'Pesquisa',
        cursor_color= 'white',
        border_color= 'transparent',
        bgcolor= ft.Colors.BLACK38,
        width= 200,
        suffix_icon= ft.Icons.SEARCH,
        focused_border_color= 'white',
        capitalization= ft.TextCapitalization.WORDS
    )

    header = ft.Container(
        bgcolor= ft.Colors.BLACK12,
        padding= 20,
        border_radius= 0,
        alignment= ft.Alignment(x=.0, y=.0),
        content=ft.ResponsiveRow(
            controls=[
                ft.Column(col={"sm": 6, "md": 6, "xl": 5}, controls=[ft.Row([logo_sys,ft.Column(spacing=1,controls=[h1,h2])])]),
                ft.Column(col={"sm": 6, "md": 6, "xl": 5}, controls=[ft.Row([bar_search],alignment=ft.MainAxisAlignment.CENTER)]),
            ],alignment=ft.MainAxisAlignment.END, vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    ic_whatsapp = ft.Image(
        src= os.path.join(origin, 'whatsapp.png'),
        width= 20
    )

    paragrafo_1 = ft.Text(
        value= '75999082320',
        size= 16,
        italic= True,
        weight= ft.FontWeight.W_200,
        opacity= .6
    )

    ic_email = ft.Image(
        src= os.path.join(origin, 'email.png'),
        width= 20
    )

    paragrafo_2 = ft.Text(
        value= 'exemple@email.com',
        size= 16,
        italic= True,
        weight= ft.FontWeight.W_200,
        opacity= .6
    )

    ic_insta = ft.Image(
        src= os.path.join(origin, 'instagram.png'),
        width= 20
    )

    paragrafo_3 = ft.Text(
        value= '@Exemplo2024',
        size= 16,
        italic= True,
        weight= ft.FontWeight.W_200,
        opacity= .6
    )

    mylogo = ft.Image(
        src= os.path.join(origin, 'mylogo.png'),
        width=30
    )

    title_header = ft.Text(
        value="Dorabelly®",
        size= 30,
    )

    text = ft.Text(
        value= """
Dorabelly é uma empresa especializada em soluções de refrigeração, atendendo tanto o mercado residencial quanto o comercial. Oferece produtos e serviços que abrangem desde a instalação e manutenção de sistemas de refrigeração até o fornecimento de equipamentos como geladeiras, freezers e câmaras frias. A empresa se destaca pela qualidade técnica de sua equipe e pelo compromisso com a eficiência.
""",
        size= 16,
        italic= True,
        weight= ft.FontWeight.W_200,
        text_align= ft.TextAlign.JUSTIFY,
        opacity= .6
    )

    column_texts = ft.Column(
        controls=[
            ft.Row([mylogo,title_header],alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Column([text],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ic_whatsapp, paragrafo_1],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ic_email, paragrafo_2],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ic_insta, paragrafo_3],alignment=ft.MainAxisAlignment.CENTER),
        ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    section_1 = ft.Container(
        expand= True,
        padding= 60,
        height= 640,
        alignment= ft.Alignment(x=.0, y=.0),
        content=ft.Column(
            controls=[
                column_texts,
            ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    name = ft.TextField(
        label= 'Nome',
        text_align= 'center',
        border_color= 'transparent',
        bgcolor= ft.Colors.BLACK38,
        width= 340,
        height= 60,
        prefix_icon= ft.Icons.PERSON,
        focused_border_color= 'white',
        capitalization= ft.TextCapitalization.WORDS
    )

    tell = ft.TextField(
        label= 'Telefone',
        text_align= 'center',
        border_color= 'transparent',
        bgcolor= ft.Colors.BLACK38,
        width= 340,
        height= 60,
        prefix_icon= ft.Icons.PHONE,
        focused_border_color= 'white',
        max_length= 11
    )

    email = ft.TextField(
        label= 'Email',
        text_align= 'center',
        border_color= 'transparent',
        bgcolor= ft.Colors.BLACK38,
        width= 340,
        height= 60,
        focused_border_color= 'white',
        prefix_icon= ft.Icons.EMAIL
    )

    address = ft.TextField(
        label= 'Endereço',
        text_align= 'center',
        border_color= 'transparent',
        bgcolor= ft.Colors.BLACK38,
        width= 340,
        height= 60,
        focused_border_color= 'white',
        prefix_icon= ft.Icons.HOME
    )

    problems = ft.TextField(
        label= 'Problema',
        text_align= 'center',
        border_color= 'transparent',
        bgcolor= ft.Colors.BLACK38,
        width= 150,
        focused_border_color= 'white',
        prefix_icon= ft.Icons.WARNING_ROUNDED,
        max_length= 16
    )

    description_problem = ft.TextField(
        border_color= 'transparent',
        bgcolor= ft.Colors.BLACK38,
        expand=True,
        width= 320,
        max_lines= 6,
        focused_border_color= 'white',
        multiline= True,
    )

    date_request = ft.TextField(
        label= 'Pedido',
        border_color= 'transparent',
        bgcolor= ft.Colors.BLACK38,
        width= 110,
        focused_border_color= 'white',
        disabled= True
    )

    date_visit = ft.TextField(
        label= 'Visita',
        border_color= 'transparent',
        bgcolor= ft.Colors.BLACK38,
        width= 110,
        focused_border_color= 'white',
        disabled= True
    )

    #Funcoes para pegar as datas
    def handle_change(e):
        dates = f"{e.control.value.strftime("%d/%m/%Y")}"
        date_request.value = dates
        date_request.update()
        
    def handle_2_change(e):
        dates = f"{e.control.value.strftime("%d/%m/%Y")}"
        date_visit.value = dates
        date_visit.update()

    def handle_dismissal(e):
        page.close(date_picker)
        page.close(date_2_picker)

    day, month, yaer = hoursandDate.get_dates()
    date_picker = ft.DatePicker(
        first_date= hoursandDate.datetime(year=yaer, month=month, day=day),
        last_date= hoursandDate.datetime(year=2030, month=12, day=31),
        on_change=handle_change,
        on_dismiss=handle_dismissal
    )
    date_2_picker = ft.DatePicker(
        first_date= hoursandDate.datetime(year=yaer, month=month, day=day),
        last_date= hoursandDate.datetime(year=2030, month=12, day=31),
        on_change=handle_2_change,
        on_dismiss=handle_dismissal
    )

    button_calender = ft.IconButton(
        icon= ft.Icons.CALENDAR_MONTH,
        icon_color=ft.Colors.WHITE,
        bgcolor= 'transparent',
        on_click= lambda e:page.open(date_picker)
    )
    button2_calender = ft.IconButton(
        icon= ft.Icons.CALENDAR_MONTH,
        icon_color=ft.Colors.WHITE,
        bgcolor= 'transparent',
        on_click= lambda e:page.open(date_2_picker)
    )

    date_sections = ft.Row([
        date_request, button_calender,
        date_visit, button2_calender
    ])

    service_condition = ft.Dropdown(
        width=160,
        label= 'CONDICÃO',
        border_color= 'transparent',
        label_style= ft.TextStyle(color=ft.Colors.WHITE54),
        focused_border_color= 'white',
        options=[
            ft.dropdown.Option('NÃO ATENDIDO'),
            ft.dropdown.Option('ATENDIDO')
        ]
    )

    payment_condition = ft.Dropdown(
        width= 160,
        label= 'CONDICÃO',
        label_style= ft.TextStyle(color=ft.Colors.WHITE54),
        border_color= 'transparent',
        focused_border_color= 'white',
        options=[
            ft.dropdown.Option('EM ABERTO'),
            ft.dropdown.Option('PAGO')
        ]
    )

    expenses = ft.TextField(
        label= 'Valor',
        border_color= 'transparent',
        bgcolor= ft.Colors.BLACK38,
        width= 110,
        focused_border_color= 'white'
    )

    button_register = ft.ElevatedButton(
        text= 'Registrar',
        width= 140,
        bgcolor= ft.Colors.WHITE,
        color= ft.Colors.BLACK,
        on_click=lambda e: page.open(banner)
    )

    style_btn = ft.ButtonStyle(
        color= 'white',
        text_style= ft.TextStyle(
            weight=ft.FontWeight.W_300,
            italic= True,
            size= 18
        )
    )

    def animate(e):
        section_client.content = section_2 if section_client.content == section_2_next else section_2_next
        page.update()

    button_next = ft.TextButton(
        text= 'Proximo >',
        style=style_btn,
        on_click= animate
    )
    button_back = ft.TextButton(
        text= '< Voltar',
        style=style_btn,
        on_click= animate
    )

    section_2 = ft.Container(
        expand= True,
        padding= 50,
        height=640,
        bgcolor=ft.Colors.WHITE10,
        alignment= ft.alignment.center,
        content=ft.Column(
            spacing= 14,
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                ft.Text('Sessao Cliente', size=20),
                ft.Divider(height=1),
                name,
                tell,
                email,
                address,
                ft.Row([button_next],alignment=ft.MainAxisAlignment.END),
            ]
        )
    )

    section_2_next = ft.Container(
        expand= True,
        padding= 40,
        height=640,
        bgcolor=ft.Colors.WHITE10,
        alignment= ft.alignment.center,
        content=ft.Column(
            spacing= 14,
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                problems,
                ft.Text('Descrição do problema', size=16),
                description_problem,
                date_sections,
                ft.Text('Clente foi atendido?', size=16),
                service_condition,
                ft.Text('Orçamento Total:', size=16),
                ft.Row([expenses, payment_condition]),
                button_register,
                ft.Divider(height=1),
                ft.Row([button_back],alignment=ft.MainAxisAlignment.START),
            ]
        )
    )

    section_data = ft.Container(
        expand= True,
        padding= 20,
        bgcolor=ft.Colors.WHITE10,
        alignment= ft.alignment.center,
        content=ft.Column(
            spacing= 14,
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                ft.Text('Dados para criacao do PDF', size=20),
            ]
        )
    )

    section_client = ft.AnimatedSwitcher(
        section_2,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=400,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.EASE_OUT,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
    )

    main = ft.ResponsiveRow(
            [
                ft.Column(col={"sm": 6, "md": 6, "xl": 6}, controls=[section_1]),
                ft.Column(col={"sm": 6, "md": 6, "xl": 6}, controls=[section_client]),
                ft.Column(col={"sm": 6, "md": 14, "xl":14}, controls=[section_data])
            ],alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
    
    footer = ft.Container(
        bgcolor= ft.Colors.BLUE_300,
        padding= 20,
        border_radius= 0,
        alignment= ft.Alignment(x=.0, y=.0),
        content=ft.Column(
            spacing= 2,
            controls=[
                ft.Text(value='Desenvolvido por: Hitamar Silva® - 2024', size=12, color=ft.Colors.BLACK)
            ]
        )
    )

    body = ft.Column(
        controls=[
            header,
            main,
        ]
    )

    page.add(
        body,
        footer
    )

if __name__ == '__main__':
    ft.app(target=main)