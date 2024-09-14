# Media Player Application

This project implements a media player application following SOLID principles. It defines interfaces for various playback functions and implements classes for different types of media players.

## Project Description

The task, translated from Georgian, is as follows:

Create a media player application. Define interfaces for play, pause, stop, rewind, and fast forward functions. Implement classes for audio player, video player, and streaming player. Ensure that each player implements only its functional interfaces. Maximize the use of SOLID principles!!!

## Implementation Details

The project is structured as follows:

1. **Interfaces**: We define separate interfaces (using Python's implicit interfaces) for each functionality:
   - `Playable`
   - `Pausable`
   - `Stoppable`
   - `Rewindable`
   - `FastForwardable`

2. **Base Class**: `StreamingPlayer` implements basic playback controls (play, pause, stop).

3. **Specific Players**:
   - `AudioPlayer`: Extends `StreamingPlayer` and adds rewind and fast forward capabilities.
   - `VideoPlayer`: Extends `StreamingPlayer` and adds rewind and fast forward capabilities.

## SOLID Principles Applied

- **Single Responsibility Principle**: Each class and interface has a single, well-defined responsibility.
- **Open/Closed Principle**: The design allows for easy extension (e.g., adding new player types) without modifying existing code.
- **Liskov Substitution Principle**: Any instance of `StreamingPlayer` (including its subclasses) can be used wherever a `StreamingPlayer` is expected.
- **Interface Segregation Principle**: Interfaces are segregated into small, specific functionalities.
- **Dependency Inversion Principle**: High-level modules depend on abstractions (interfaces) rather than concrete implementations.

## Usage

Here's a basic example of how to use the media player classes:

```python
streaming_player = StreamingPlayer()
audio_player = AudioPlayer()
video_player = VideoPlayer()

def use_player(player: StreamingPlayer):
    player.play()
    player.pause()
    player.stop()
    
    if isinstance(player, Rewindable):
        player.rewind()
    
    if isinstance(player, FastForwardable):
        player.fast_forward()

# Test the implementation
print("Testing StreamingPlayer:")
use_player(streaming_player)

print("\nTesting AudioPlayer:")
use_player(audio_player)

print("\nTesting VideoPlayer:")
use_player(video_player)
```

## Future Improvements

- Add more specific functionality to differentiate between audio and video players.
- Implement a user interface for interacting with the media players.
- Add support for different media formats and codecs.

## Contributing

Contributions to improve the implementation or extend the functionality are welcome. Please ensure that any modifications or additions adhere to the SOLID principles.

## License

[MIT]