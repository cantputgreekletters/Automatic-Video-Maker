class main:
    def __init__(self) -> None:
        self.__start()
        pass
    
    def create_file_names(self,Index:int):
        list = []
        for i in range(Index):
          x = f"L:\Code\AutomaticVideoMaker\\VideoElements\\speech{i}.mp3"
          list.append(x)
        return list
    def __start(self):
        print("Gettin Text from subreddits...")
        from GetText import get_text_list
        Text_list = get_text_list()
        del get_text_list
        print("Got Text from subreddits")

        
        print("Creatin TTS...")
        tts_names = self.create_file_names(len(Text_list))
        from TextToSPeech import create_tts
        create_tts(Text_list,tts_names)
        del create_tts

        print("Created TTS")
        print("Making Video...")
        
        from multiprocessing import Process
        from VideoMaker import create_video

        
        if __name__ == '__main__':
            p = Process(target=(create_video(Text_list,tts_names)), args=('bob',))
            p.start()
            p.join()

        del create_video
        del Process
        print("Finished")
main()