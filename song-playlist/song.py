"""Simulation of classes that connect with UML notation"""

import random

class Song:
    """Class of song information"""
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

class Playlist:
    """Class of playlist that contains a list of songs"""
    def __init__(self, name):
        self.name = name
        self.playlist = []

    def add_song(self, song: Song):
        """add a song to playlist"""
        self.playlist.append(song)

    def count_song(self):
        """count all songs in playlist"""
        return len(self.playlist)

    def description(self):
        """show the playlist information"""
        return f"{self.name} has {len(self.playlist)} songs."

class Classic(Playlist):
    """One of the playlist"""
    def __init__(self, owner):
        self.owner = owner

    def remove_song(self, song):
        """remove song in playlist by searching for song title"""
        # code omitted
        self.playlist.remove(song)

    def shuffle_songs(self):
        """shuffle songs in playlist"""
        random.shuffle(self.playlist)
