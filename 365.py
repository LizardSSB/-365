python_file = "hello_world.py"
with open(python_file, "w") as f:
    f.write("# coding=utf-8\n")

from pydub import AudioSegment
from pydub.utils import mediainfo
from pydub.playback import play
​
# 从视频中提取声音
sound = AudioSegment.from_file("video.mp4", format="mp4")
sound.export("music.mp3", format="mp3")
​
# 获取媒体信息
info = mediainfo("musci.wav")
print(info)
​
# 播放音频
play("music.mp3")
​
# 合并音频
sound1 = AudioSegment.from_file("music.mp3")
sound2 = AudioSegment.from_file("music.mp3")
combined = sound1 + sound2
combined.export("music_combined.mp3", format="mp3")
​
# 分割音频
sound = AudioSegment.from_file("music.mp3", format="mp3")
sound_1 = sound[:10000]
sound_2 = sound[10000:]
sound_1.export("music_1.mp3", format="mp3")
sound_2.export("music_2.mp3", format="mp3")
​
# 增大或减小音量
sound = AudioSegment.from_file("music.mp3", format="mp3")
sound_volumn = sound + 10
sound_volumn.export("music_volumn.mp3", format="mp3")
​
# 为音频添加静音
sound = AudioSegment.from_file("music.mp3", format="mp3")
sound_silence = sound + AudioSegment.silent(duration=1000)
sound_silence.export("music_silence.mp3", format="mp3")
