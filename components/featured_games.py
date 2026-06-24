import flet as ft

# 游戏内容信息
games_info = [
    {
        "id": 1,
        "title": "Zooba",
        "image": "../assets/featured_games/zooba.png",
        "downloads": "200k",
        "stars": 4
    },
    {
        "id": 2,
        "title": "Subway Surfer",
        "image": "../assets/featured_games/subway.png",
        "downloads": "5M",
        "stars": 4
    },
    {
        "id": 3,
        "title": "Free Fire",
        "image": "../assets/featured_games/freeFire.png",
        "downloads": "100M",
        "stars": 3
    },
    {
        "id": 4,
        "title": "Alto's Adventure",
        "image": "../assets/featured_games/altosAdventure.png",
        "downloads": "20k",
        "stars": 4
    },
]

def star_rating(rating, max_stars=5, size=15):
    """
    创建星级评分显示
    rating: 评分值（如 4.5）
    max_stars: 最大星星数
    size: 星星大小
    """
    stars = []
    full_stars = int(rating)  # 完整 星星 数
    has_half = rating - full_stars >= 0.5  # 是否有半星

    for i in range(max_stars):
        if i < full_stars:
            # 完整星星
            stars.append(
                ft.Icon(
                    ft.Icons.STAR,
                    color=ft.Colors.AMBER,
                    size=size
                )
            )
        elif i == full_stars and has_half:
            # 半星
            stars.append(
                ft.Icon(
                    ft.Icons.STAR_HALF,
                    color=ft.Colors.AMBER,
                    size=size
                )
            )
        else:
            # 空星
            stars.append(
                ft.Icon(
                    ft.Icons.STAR_OUTLINE,
                    color=ft.Colors.GREY_400,
                    size=size
                )
            )

    return ft.Row(
        controls=stars,
        spacing=2,
        tight=True  # 紧凑排列
    )

def featured_games():
    """  精选游戏  """
    return ft.Container(
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Text("Featured Games", size=28, weight=ft.FontWeight.BOLD),
                # 水平横向滚动列表
                ft.ListView(
                    expand=True,
                    height=200,
                    horizontal=True,
                    spacing=12,
                    padding=ft.Padding(0, 0, 16, 0),
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Stack(
                            width=280,
                            height=200,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            controls=[
                                # 底层图片
                                ft.Image(
                                    src=game["image"],
                                    width=280,
                                    height=200,
                                    fit=ft.BoxFit.FILL,
                                    border_radius=10
                                ),
                                # 渐变遮罩层（从顶部透明到底部半透明黑色）
                                ft.Container(
                                    width=280,
                                    height=200,
                                    gradient=ft.LinearGradient(
                                        begin=ft.Alignment.TOP_CENTER,
                                        end=ft.Alignment.BOTTOM_CENTER,
                                        colors=[
                                            ft.Colors.TRANSPARENT,  # 完全透明
                                            ft.Colors.with_opacity(0.6, ft.Colors.BLACK),  # 60% 不透明黑色
                                        ],
                                    ),
                                    border_radius=10,
                                ),
                                # 上层悬浮信息框，Stack直接子控件，left/bottom生效
                                ft.Container(
                                    width=150,
                                    padding=ft.Padding(4, 8, 8, 8),
                                    left=10,
                                    bottom=10,
                                    content=ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                        spacing=2,
                                        controls=[
                                            star_rating(game["stars"]),
                                            ft.Text(
                                                game["title"],
                                                size=16,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.WHITE,
                                                text_align=ft.TextAlign.START
                                            ),
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.START,
                                                spacing=8,
                                                controls=[
                                                    ft.Icon(
                                                        ft.Icons.FILE_DOWNLOAD_OUTLINED,
                                                        color=ft.Colors.WHITE,
                                                        size=20,
                                                    ),
                                                    ft.Text(
                                                        f"{game['downloads']} Downloads",
                                                        size=12,
                                                        color=ft.Colors.WHITE
                                                    ),

                                                ]
                                            )
                                        ]
                                    ),
                                )
                            ]
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

    page.add(featured_games())


if __name__ == '__main__':
    ft.run(main)

'''

Flet 底层基于 Flutter，横向 ListView 默认有两个限制：

普通鼠标滚轮默认只控制垂直滚动，上下滚轮不会驱动水平列表；

原生操作方式：按住 Shift + 鼠标滚轮 才能左右滑。

按住 Shift + 鼠标滚轮 才能左右滑。

'''