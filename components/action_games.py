
import flet as ft

# 动作游戏内容信息
games_info = [
    {
        "id": 1,
        "title": "Shadow Fight",
        "image": "../assets/action_games/shadowFight.png",
        "downloads": "20M",
        "stars": 4.5
    },
    {
        "id": 2,
        "title": "Valor Arena",
        "image": "../assets/action_games/valorArena.png",
        "downloads": "10k",
        "stars": 3.4
    },
    {
        "id": 3,
        "title": "Frag",
        "image": "../assets/action_games/frag.png",
        "downloads": "80k",
        "stars": 4.6
    },
    {
        "id": 4,
        "title": "Zooba Wildlife",
        "image": "../assets/action_games/zoobaGame.png",
        "downloads": "40k",
        "stars": 3.5
    },
    {
        "id": 5,
        "title": "Clash of Clans",
        "image": "../assets/action_games/clashofclans.png",
        "downloads": "20k",
        "stars": 4.2
    },
    {
        "id": 6,
        "title": "Angry Birds",
        "image": "../assets/action_games/angryBirds.png",
        "downloads": "10M",
        "stars": 4.8
    },
]

def game_bar(title, star, download_num):
    return ft.Column(
        controls=[
            # 游戏名
            ft.Text(
                title,
                size=16,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK,
                text_align=ft.TextAlign.START
            ),
            ft.Row(
                controls=[
                    # 星级
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.STAR, color=ft.Colors.AMBER, size=20),
                                ft.Text(f"{star} stars", size=12, color=ft.Colors.GREY_600),
                            ],
                            spacing=2,
                        ),
                    ),
                    # 下载
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.FILE_DOWNLOAD_OUTLINED, color=ft.Colors.BLUE, size=20),
                                ft.Text(f"{download_num}", size=12, color=ft.Colors.GREY_600)
                            ],
                            spacing=2,
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        ]
    )


#  渐变色 play 按钮
def play_button():
    return ft.Container(
        content=ft.Text("play", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
        bgcolor=None,
        gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_LEFT,
            end=ft.Alignment.BOTTOM_RIGHT,
            colors=[
                ft.Colors.with_opacity(0.9, "#09B5D3"),  # rgba(9, 181, 211, 0.9)
                ft.Colors.with_opacity(0.9, "#3A83F4"),  # rgba(58, 131, 244, 0.9)
            ]
        ),
        border_radius=ft.BorderRadius.all(17),
        width=80,
        height=34,
        alignment=ft.Alignment.CENTER,
    )


def action_games():
    """  动作游戏列表  """
    return ft.Container(
        expand=True,
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Top Action Games", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text("See All", size=14, weight=ft.FontWeight.BOLD,color=ft.Colors.BLUE),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # 左右分布
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                # 水平横向滚动列表
                ft.ListView(
                    expand=True,
                    spacing=12,
                    padding=ft.Padding(0, 0, 16, 0),
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Row(
                            spacing= 20,
                            controls=[
                                ft.Image(
                                    src=game["image"],
                                    width=80,
                                    height=80,
                                    fit=ft.BoxFit.FILL,
                                    border_radius=10
                                ),
                                game_bar(game["title"], game["stars"], game["downloads"]),
                                play_button(),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,           # 左右分布
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        )
                        for game in games_info
                    ]
                )
            ]
        )
    )


def main(page: ft.Page):
    page.window.width = 375
    page.window.height = 812
    page.padding = 20
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    page.bgcolor = ft.Colors.WHITE

    page.add(action_games())


if __name__ == '__main__':
    ft.run(main)



'''



'''