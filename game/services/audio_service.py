import raylibpy

class AudioService:
    """Handles all the audio in the game.

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._sounds = {}
        
    def play_sound(self, filename, volume=1.0, pitch=1.0):
        """
        Plays the sound file provided. Make sure to call start_audio before this is called.
        """
        
        if pitch != 1.0:
            if filename + str(pitch) not in self._sounds.keys():
                loaded = raylibpy.load_sound(filename)
                self._sounds[filename + str(pitch)] = loaded
                raylibpy.set_sound_pitch(self._sounds[filename + str(pitch)], pitch)
        else:
            if filename not in self._sounds.keys():
                loaded = raylibpy.load_sound(filename)
                self._sounds[filename] = loaded

        if pitch != 1.0:
            sound = self._sounds[filename + str(pitch)]
        else:
            sound = self._sounds[filename]
        raylibpy.set_sound_volume(sound, volume)  
        raylibpy.play_sound(sound)

        
    def stop_sound(self, filename):
        sound = self._sounds[filename]
        raylibpy.stop_sound(sound)

    def start_audio(self):
        """
        Initializes the audio device so that sounds can be played.
        """
        raylibpy.init_audio_device()

    def stop_audio(self):
        """
        Closes the audio device at the end of the program.
        """
        raylibpy.close_audio_device()