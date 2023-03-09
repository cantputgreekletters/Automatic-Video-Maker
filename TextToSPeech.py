def create_tts(text_list:list,file_names_list:list):
    if len(text_list) != len(file_names_list): raise Exception("Lists length is not the same")
    Index = 0
    # Import the required module for text 
    # to speech conversion
    from gtts import gTTS
      
    for text in text_list:
      
      # The text that you want to convert to audio
      
        
      # Language in which you want to convert
      language = 'en'
      
      #Accent in which you want to convert
      tld = "us"
      
      # Passing the text and language to the engine, 
      # here we have marked slow=False. Which tells 
      # the module that the converted audio should 
      # Be fast at reading
      
      myobj = gTTS(text=text, lang=language, slow=False, tld=tld)
        
      # Saving the converted audio in a mp3 file named Speech.mp3
      
      myobj.save(file_names_list[Index])
      Index += 1
  