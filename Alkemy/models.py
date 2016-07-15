#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The Alkemy app model is designed to help keep track of the game data.

    Default language
    ----------------

    As Alkemy is a french edited game with most of its audience in France, the
    default language is set to french and so are the labels.

    updatedAt
    ---------

    Most if not all of the models does have a updatedAt field. That field is
    used to keep track of the last update of the model.

"""

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class GameDataCommon(models.Model):
    """
    Common attributes for data classes.

    Statuses should be:

      - published: Something
      - draft: Something else
      - removed: The last thing

    :param lang: Language of this object, ISO format
    :param updatedAt: Timestamp of the last update, intended to be used for sync features.
    :param status: Status of the stat, the expected behavior is described above.
    """
    FRENCH = 'fr'
    ENGLISH = 'en'
    LANG_CHOICES = (
        (FRENCH, u'Français'),
        (ENGLISH, u'Anglais')
    )

    STATUS_PUBLISHED = 'pub'
    STATUS_DRAFT = 'dft'
    STATUS_REMOVED = 'del'
    STATUS_CHOICES = (
        (STATUS_DRAFT, u'Brouillon'),
        (STATUS_PUBLISHED, u'Publié'),
        (STATUS_REMOVED, u'Supprimé')
    )

    lang = models.CharField(max_length=2,
                            choices=LANG_CHOICES,
                            default=FRENCH)

    status = models.CharField(max_length=3,
                              choices=STATUS_CHOICES,
                              default=STATUS_DRAFT)

    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Faction(GameDataCommon):
    """
    Each profile belongs to one or more faction(s).

    :param name: Name of the faction
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


@python_2_unicode_compatible
class Ability(GameDataCommon):
    """
    Standard description of abilities. This will be displayed in the list of
    abilities and in the details of a profile.

    :param name: The name of the ability
    :param description: A description of this ability
    """
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Abilities"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Profile(GameDataCommon):
    """
    Profile object describes a single Alkemy profile.
    """
    name = models.CharField('Nom', max_length=30)
    title = models.CharField('Titre', max_length=50, blank=True)
    life_points = models.CommaSeparatedIntegerField('Points de vie',
                                                    max_length=8)
    movement = models.CommaSeparatedIntegerField('Mouvement', max_length=8)
    damage_cc = models.CommaSeparatedIntegerField('Corps à corps',
                                                  max_length=16)
    damage_ra = models.CommaSeparatedIntegerField('Combat à distance',
                                                  max_length=16, blank=True)
    action_points = models.IntegerField('Points d\'Action')
    cost = models.IntegerField('Cout')
    combat = models.IntegerField('Combat')
    defense = models.IntegerField('Défense')
    mind = models.IntegerField('Esprit')
    reflexes = models.IntegerField('Réflexes')
    size = models.IntegerField('Taille', default=2)

    factions = models.ManyToManyField(Faction)

    abilities = models.ManyToManyField(Ability, through='AbilityValue')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Alchemist(Profile):

    element = models.CharField(max_length=10)
    rank = models.CharField(max_length=30)
    stones = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


@python_2_unicode_compatible
class Formula(GameDataCommon):
    THRESHOLD_TARGET = 'Cible'
    THRESHOLD_AUTO = 'Auto'
    THRESHOLD_CHOICES = (
        (THRESHOLD_TARGET, 'Cible'),
        (THRESHOLD_AUTO, 'Auto')
    )

    name = models.CharField(max_length=50)
    effect = models.TextField()
    focus_level = models.IntegerField()
    components = models.CharField(max_length=20)
    threshold = models.CharField(max_length=5, choices=THRESHOLD_CHOICES,
                                 default=THRESHOLD_TARGET)
    range = models.IntegerField()

    alchemist = models.ForeignKey(Alchemist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Enhancement(GameDataCommon):
    """
    Enhancements are formula related objects.
    """
    description = models.TextField()

    formula = models.ManyToManyField(Formula,
                                     null=True)

    def __str__(self):
        return self.description


@python_2_unicode_compatible
class AbilityValue(models.Model):
    """
    This class associate an ability to a profile as an ability may have specific
    value for a profile. The value is optional.
    """
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    value = models.CharField(max_length=10, blank=True)

    def __str__(self):
        """
        String description is formated depending on the value.

        :return:
         The string representation of this object which is either the ability
         name or the ability name and the value associated.
        """
        if self.value:
            return '%s (%s)' % (self.ability.name, self.value)
        else:
            return '%s' % self.ability.name
