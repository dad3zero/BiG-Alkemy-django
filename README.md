# Django Alkemy app
##### Part of the Brothers in Games project

[Brothers in Games](http://big.dad3zero.net) is a set of apps for miniature
games and gamers. The Alkemy Companion (available on
[Android](https://play.google.com/store/apps/details?id=net.labasland.miniwar.intel.alkemy))
helps [Alkemy](http://alkemy-the-game.com/) players to access all their favorite
game stats.

All the game data are published online so the mobile app can update its
information in (nearly) real time. This Django app was created to manage a data
repository. Using Django model management and admin forms framework, the
repository management is easy to setup.

## App features
The model module provides the model of Alkemy profiles. The admin module
provides all the management forms for the data.

## What is not in this app
This app was not created to provide a user interface, there is no views,
templates or URLs. So, there is no
[Architekt](http://architekt.alkemy-the-game.com/alkemy/architekt/) like feature.

Even if this app was created to sync this repository with remote services, those
features are not provided. The main reason is because such a service should not
be part of this kind of app. This is a data management app and should focus on
that feature. Sync or any other data manipulation for another service is part
of a dedicated _technical_ app.

For legal reasons, there are no game data in this sources (I have no ownership
on those).

## Why is this app published in Open Source
There are two main reasons
* I try to make this a clean example of a Django app, even if it is only a
backend.
* Models and game mechanics are always the harder to define. Anyone wanting to
create an Alkemy web service can clone this app and focus on the interfaces and
services provided.

## Getting started

I assume that you have at least some basic Python knowledge.

First, clone this app anywhere you want. Keep it away of your Django project so
it will be easier to manage the separate history. Then, create a virtualenv, add
Django and add the path to this app.

```bash
mkvirtualenv figAppEnv
pip install django
add2virtualenv /home/user/opensource/BiG-Alkemy-django
```

This is it, you are all set. You can now create your project and add the app to
the list.

Current version does not include the migrations, make sure to run them.

## Links
Alkemy is a game published by
[Alchemist Miniatures](http://alkemy-the-game.com/), Dad 3.0 and Brothers in
Games are not affiliated to Alchemist Miniatures.

For french readers, a blog post will be published soon.

You can get the
[Alkemy Companion for Android](https://play.google.com/store/apps/details?id=net.labasland.miniwar.intel.alkemy)