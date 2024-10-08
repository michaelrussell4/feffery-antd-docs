import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染组件介绍内容"""
    return [
        fac.AntdBreadcrumb(
            items=[
                {'title': '组件介绍'},
                {'title': '导航'},
                {'title': 'AntdBreadcrumb 面包屑'},
            ],
            style={'marginBottom': 8},
        ),
        fac.AntdTitle('AntdBreadcrumb 面包屑', level=2),
        fac.AntdParagraph('用于展示当前页面在系统层级结构中的位置。'),
    ]
