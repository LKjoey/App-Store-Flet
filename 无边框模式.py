
import flet as ft

from components.top_bar import top_bar                 # 顶部栏
from components.browse_games import browse_games       # 游戏栏
from components.featured_games import featured_games   # 精选游戏
from components.action_games import action_games       # 动作游戏


def main(page: ft.Page):

    # 去除系统标题栏边框
    page.window.frameless = True
    # 隐藏标题栏上的关闭、最小化、最大化按钮
    page.window_title_bar_buttons_hidden = True

    page.title = "AppStore"
    page.window.width = 375
    page.window.height = 812
    page.window.resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    page.border_radius = ft.BorderRadius.all(10),

    # 构建主界面 内容控件
    main_page = ft.Column(
        controls=[
            top_bar(),          # 顶部栏
            browse_games(),     # 游戏列表
            featured_games(),   # 精选游戏
            action_games(),     # 动作游戏
        ],
        horizontal_alignment=ft.CrossAxisAlignment.START,
        alignment=ft.MainAxisAlignment.START,
        expand=True,
        spacing=5,      # 控制子组件间距
    )

    # 主界面 添加 渐变色背景
    page.add(
        ft.Container(
            expand=True,
            gradient=ft.LinearGradient(         # 背景渐变色
                begin=ft.Alignment.TOP_CENTER,
                end=ft.Alignment.BOTTOM_CENTER,
                colors=[
                    ft.Colors.with_opacity(0.4, "#3A83F4"),
                    ft.Colors.with_opacity(0.4, "#09B5D3"),
                ],
            ),
            border_radius=ft.BorderRadius.all(20),
            padding=ft.Padding.all(16),
            content=main_page,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
        )
    )


if __name__ == "__main__":
    ft.run(main)


'''

鼠标在  

top_bar() # 顶部栏 菜单栏和小铃铛之间的区域  中,

可以拖动窗口


按住 shift + 鼠标滚轮可以 左右滑动 browse_games 和 featured_games 区域的内容

'''