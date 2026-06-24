
import flet as ft

game_categories = ['Action', 'Family', 'Puzzle', 'Adventure', 'Racing', 'Education', 'Others']

def browse_games():
    """ 游戏栏  """
    return ft.Container(
        #padding=ft.Padding(16, 12, 0, 12),  # 左右上下边距
        content=ft.Column(
            spacing=5,
            controls=[
                ft.Text("Browse Games", size=28, weight=ft.FontWeight.BOLD),
                # 水平横向滚动列表
                ft.ListView(
                    expand=True,
                    height=36,      # 固定列表元素高度
                    horizontal=True,
                    spacing=8,
                    padding=ft.Padding(0, 0, 16, 0),
                    scroll=ft.ScrollMode.HIDDEN,        # 隐藏滚动条
                    controls=[
                        ft.Container(
                            padding=ft.Padding(14, 4, 14, 4),
                            bgcolor="#BFDBFE",
                            border_radius=18,
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text(i, size=14)
                        )
                        for i in game_categories
                    ]
                )
            ]
        )
    )



def main(page: ft.Page):
    page.window.width = 375
    page.window.height = 812
    page.padding = 0
    # 添加顶部栏
    page.add(browse_games())


if __name__ == '__main__':
    ft.run(main)


'''

Flet 底层基于 Flutter，横向 ListView 默认有两个限制：
普通鼠标滚轮默认只控制垂直滚动，上下滚轮不会驱动水平列表；

原生操作方式：按住 Shift + 鼠标滚轮 才能左右滑。

按住 Shift + 鼠标滚轮 才能左右滑。

'''
