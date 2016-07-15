#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The admin module is designed to provide all the forms for game data management
as this app focuses on that purpose.
"""

from django.contrib import admin

from models import Faction, Ability, Formula,\
    Profile, Alchemist, Enhancement, AbilityValue

# TODO: Enhancement inline is silenced until defining how to represent referenced data
# class EnhancementsInline(admin.StackedInline):
#    model = Enhancement
#    extra = 1


class FormulaAdmin(admin.ModelAdmin):
#    inlines = [EnhancementsInline]

    ordering = ['name']


class FormulasInline(admin.TabularInline):
    model = Formula
    show_change_link = True
    extra = 0


class AbilitiesInline(admin.TabularInline):
    model = AbilityValue
    extra = 1


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ('name', 'title'),
        }),
        (u'Caractéristiques générales', {
            'fields': ('action_points', 'movement', 'life_points',
                       'size', 'cost')
        }),
        (u'Combat', {
            'fields': ('damage_cc', 'damage_ra')
        }),
        (u'Competences', {
            'fields': ('combat', 'defense', 'mind', 'reflexes')
        }),
        (None, {
            'fields': ('factions', 'lang',)
        }),
    ]

    inlines = [AbilitiesInline]

    filter_horizontal = ['factions', 'abilities']
    list_filter = ('factions__name',)
    ordering = ['name']


class AlchemistAdmin(ProfileAdmin):
    fieldsets = [
        ('Alchemist', {
            'fields': ('element', 'rank', 'stones'),
        }),
    ]
    fieldsets.extend(ProfileAdmin.fieldsets)

    inlines = [FormulasInline]
    inlines.extend(ProfileAdmin.inlines)


admin.site.register(Faction)
admin.site.register(Ability)
admin.site.register(Enhancement)
admin.site.register(Formula, FormulaAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Alchemist, AlchemistAdmin)

