class main:
    def __init__(self) -> None:
        self.__start()
        pass
    
    def create_file_names(self,Index:int):
        #Returns a list of names for each file
        list = []
        for i in range(Index):
          #Edit this to specify your path
          x = f"L:\Code\AutomaticVideoMaker\\VideoElements\\speech{i}.mp3"
          list.append(x)
        return list

    def __start(self):
        print("Gettin Text from subreddits...")
        from GetText import get_text_list
        subbreddit = str(input("Give subreddit's name\n"))
        n = int(input("How many posts do you want to fetch?\n"))
        Text_list = get_text_list(subbreddit,n)
        #Deletes the imported function because it won't be used again.
        del get_text_list,n
        print("Got Text from subreddits")

        
        print("Creatin TTS...")
        tts_names = self.create_file_names(len(Text_list))
        from TextToSPeech import create_tts
        create_tts(Text_list,tts_names)
        del create_tts

        print("Created TTS")
        print("Making Video...")
        
        #Creates video
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