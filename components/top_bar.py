
import flet as ft

def top_bar():
    """ 顶部图标栏 """
    return ft.Container(
        padding=10,
        content=ft.WindowDragArea(
            expand=True,
            content=ft.Row(
                controls=[
                    ft.Icon(
                        ft.CupertinoIcons.LINE_HORIZONTAL_3,
                        color="#0D163A",
                        size=30,
                    ),
                    ft.Icon(
                        ft.CupertinoIcons.BELL_FILL,
                        color="#0D163A",
                        size=30,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

def main(page: ft.Page):
    # 去除系统标题栏边框
    page.window.frameless = True
    # 隐藏标题栏上的关闭、最小化、最大化按钮
    page.window_title_bar_buttons_hidden = True
    page.window.width = 375
    page.window.height = 812
    page.padding = 0
    page.add(top_bar())

if __name__ == '__main__':
    ft.run(main)


'''

ft.WindowDragArea  

它在内容控件上模拟了原生操作系统窗口标题栏的行为（拖拽、移动、最大化、恢复）。

适用于隐藏系统默认窗口标题栏 情况下 实现顶部区域拖动窗口  

只有鼠标在ft.WindowDragArea 中 可以拖动窗口

'''