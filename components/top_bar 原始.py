
import flet as ft


def top_bar():
    """ 顶部 图标栏  """
    return ft.Container(
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
            # 关键：左右两端分布
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


def main(page: ft.Page):
    page.window.width = 375
    page.window.height = 812
    page.padding = 0
    # 添加顶部栏
    page.add(top_bar())



if __name__ == '__main__':
    ft.run(main)

