# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from django_tables2 import Table, Column, LinkColumn, TemplateColumn, A

from oscar.core.loading import get_class, get_model

DashboardTable = get_class('dashboard.tables', 'DashboardTable')
Product = get_model('catalogue', 'Product')
Category = get_model('catalogue', 'Category')


class ProductTable(Table):
    title = TemplateColumn(
        verbose_name=_('Title'),
        template_name='dashboard/catalogue/product_row_title.html',
        order_by='title', accessor=A('title'))
    image = TemplateColumn(
        verbose_name=_('Image'),
        template_name='dashboard/catalogue/product_row_image.html',
        orderable=False)
    product_class = Column(
        verbose_name=_('Product type'),
        accessor=A('product_class'),
        order_by='product_class__name')
    actions = TemplateColumn(
        verbose_name=_('Actions'),
        template_name='dashboard/catalogue/product_row_actions.html',
        orderable=False)

    class Meta(DashboardTable.Meta):
        model = Product
        fields = ('upc', 'date_updated')
        sequence = ('title', 'upc', 'image', 'product_class', '...', 'date_updated', 'actions')
        order_by = '-date_updated'


class CategoryTable(Table):
    name = LinkColumn('dashboard:catalogue-category-update', args=[A('pk')])
    description = TemplateColumn(
        template_code='{{ record.description|default:""|striptags'
                      '|cut:"&nbsp;"|truncatewords:6 }}')
    # mark_safe is needed because of
    # https://github.com/bradleyayers/django-tables2/issues/187
    num_children = LinkColumn(
        'dashboard:catalogue-category-detail-list', args=[A('pk')],
        verbose_name=mark_safe(_('Number of child categories')),
        accessor='get_num_children',
        orderable=False)
    actions = TemplateColumn(
		verbose_name=_('Actions'),
        template_name='dashboard/catalogue/category_row_actions.html',
        orderable=False)

    class Meta(DashboardTable.Meta):
        model = Category
        fields = ('name', 'description')
