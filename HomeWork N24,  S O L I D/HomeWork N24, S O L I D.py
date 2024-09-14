class Playable:
    def play(self):
        pass


class Pause:
    def pause(self):
        pass


class Stoppable:
    def stop(self):
        pass


class Rewindable:
    def rewind(self):
        pass


class FastForwardable:
    def fast_forward(self):
        pass


class StreamingPlayer(Playable, Pause, Stoppable):
    def play(self):
        print("Streaming: Playing")

    def pause(self):
        print("Streaming: Paused")

    def stop(self):
        print("Streaming: Stopped")


class AudioPlayer(StreamingPlayer, Rewindable, FastForwardable):
    def rewind(self):
        print("Audio: Rewinding")

    def fast_forward(self):
        print("Audio: Fast forwarding")


class VideoPlayer(StreamingPlayer, Rewindable, FastForwardable):
    def rewind(self):
        print("Video: Rewinding")

    def fast_forward(self):
        print("Video: Fast forwarding")


def use_player(player: StreamingPlayer):
    player.play()
    player.pause()
    player.stop()

    if isinstance(player, Rewindable):
        player.rewind()

    if isinstance(player, FastForwardable):
        player.fast_forward()


streaming_player = StreamingPlayer()
audio_player = AudioPlayer()
video_player = VideoPlayer()

print("Testing StreamingPlayer:")
use_player(streaming_player)

print("\nTesting AudioPlayer:")
use_player(audio_player)

print("\nTesting VideoPlayer:")
use_player(video_player)