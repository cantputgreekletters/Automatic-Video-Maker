#Many paths should be edited
def create_video(text_list:list,audio_list:list):
  if len(text_list) != len(audio_list): raise Exception("Audio and texts do not have the same length")
  from moviepy.editor import AudioFileClip,VideoFileClip,concatenate_videoclips,CompositeVideoClip,TextClip
  transition = VideoFileClip("L:\Code\AutomaticVideoMaker\VideoElements\\Transition.mp4")
  clip_list = []
  #Function that returns a seperated text
  def seperate_text(text):
    seperated_text = []
    x = 0
    new_text = ""
    for i in text:
      if x == 150:
          seperated_text.append(new_text)
          new_text = ""
          x = 0
      if i == " ":
        x += 1
      new_text += i
    if new_text not in seperated_text:
          seperated_text.append(new_text)
    return seperated_text

  for i in range(0,len(audio_list)):
    #Gets audio
    audio_clip = AudioFileClip(audio_list[i])
    
    background = VideoFileClip("L:\Code\AutomaticVideoMaker\VideoElements\\background.mp4",audio = True)
    #makes the background loop for the duration of all audio
    clip = background.loop(duration = audio_clip.duration)
    #puts the audio in the clip
    clip.audio = audio_clip
    

    seperated_text = seperate_text(text_list[i])
    texts = []
    #Creates text
    for text in seperated_text:
      
      txt_clip = TextClip(text,fontsize=50, color="white",bg_color="transparent",method="caption",size=(1900,1060)).set_duration(audio_clip.duration // len(seperated_text))
      texts.append(txt_clip)
    txt_clip = concatenate_videoclips(texts)
    del texts,text,seperated_text
    clip = CompositeVideoClip([clip,txt_clip])
    clip_list.append(clip)
    clip_list.append(transition)
  video = concatenate_videoclips([clip,transition])
  #Adds outro
  outro = VideoFileClip("L:\Code\AutomaticVideoMaker\VideoElements\\Outro.mp4")
  clip_list.append(outro)
  video = concatenate_videoclips(clip_list)
  #Exports file
  video.write_videofile("L:\Code\AutomaticVideoMaker\VideoElements\\Videoresult.mp4",threads = 8,fps = 30,logger = None , verbose = False)