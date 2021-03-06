# -*- coding: utf-8 -*-
from django_tables2 import Table, LinkColumn, TemplateColumn, Column, A

from oscar.core.loading import get_class

DashboardTable = get_class('dashboard.tables', 'DashboardTable')


class UserTable(Table):
    check = TemplateColumn(
        template_name='dashboard/users/user_row_checkbox.html',
        verbose_name=' ', orderable=False)
    email = LinkColumn('dashboard:user-detail', args=[A('id')],
                       accessor='email')
    name = Column(accessor='get_full_name', verbose_name='İsim',
                  order_by=('last_name', 'first_name'))
    active = Column(accessor='is_active', verbose_name='Aktif',)
    staff = Column(accessor='is_staff', verbose_name='Yetkili Kullanıcı',)
    date_registered = Column(accessor='date_joined')
    #num_orders = Column(accessor='orders.count', orderable=False)
    actions = TemplateColumn(
        template_name='dashboard/users/user_row_actions.html',
        verbose_name=' ')

    class Meta(DashboardTable.Meta):
        template = 'dashboard/users/table.html'
