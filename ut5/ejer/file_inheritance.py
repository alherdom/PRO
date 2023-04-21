class File:
    def __init__(self, path: str):
        self.path = path
        self.contents = []
    
    def add_content(self, content: str) -> list[str]:
        return self.contents.append(content) # type: ignore
    
    def show_contents(self) -> str:
        return f'✓ Contents:{self.contents}'
        
    @property
    def size(self) -> int:
        return sum(len(content) for content in self.contents)
    
    @property 
    def info(self) -> str:
        return f'✓ Path: {self.path} [size={self.size}B]'
        
class MediaFile(File):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int):
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration
    
    @property
    def info(self):
        return f'{super().info}\n✓ Codec: {self.duration}\n✓ Geolocation:{self.geoloc}\n✓ Duration: {self.duration}'
    
class VideoFile(MediaFile):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int, dimensions: tuple):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions
    
    @property
    def info(self):
        return f'{super().info}\n✓ Dimensions:{self.dimensions}'
    
vanrossum = VideoFile('/home/python/vanrossum.mp4', 'h264', (23.5454, 31.4343), 487, (1920, 1080))
vanrossum.add_content('audio/ogg')
vanrossum.add_content('video/webm')
print(vanrossum.info)
print(vanrossum.show_contents())
