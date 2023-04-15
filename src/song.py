class Song:
    def __init__(self, input_song_title, input_duration):
        self.song_title = input_song_title
        self.duration = input_duration

    def song_has_name(self):
        return self.song_title
    
    def song_duration_is_float(self):
        duration_float = float(self.duration)
        return round(duration_float, 2)

        # duration_float = float(self.duration)
        # return round(2, duration_float)
    
song_1 = Song("Colors by Halsey", 4.09)
song_2 = Song("Bad Guy by Billie Eilish", 3.14)
song_3 = Song("Lose Yourself by Eminem", 5.20)