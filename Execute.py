from dbControl import *
import multiprocessing


#gui대신 임시로 사용하는 테스트용 실행 클래스


class Execute :


    BookList = []

    def __init__(self) -> None:
        pass
    


    def Show(self) :
        count = 1

        for Book in self.BookList :
            print("%d : %s   %s" %(count, Book.getTitle(), Book.getAuthor()))
            count = count +1

   

    def Start(self) :

        key = "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"

        openai.api_key = key
        #gpt 인증키

        DB = dbControl()

        while(1):
            print("수행할 작업을 선택하시오 : \n")
            print("1. DB에서 불러오기 2. 작가 검색 3. 제목 검색 \n")
            print("4. 책 목록 출력 5. GPT 생성 6.연령별 검색")
 
            number = int(input())

            if number == 1:
                self.BookList = DB.makeListAll()
            elif number == 2:
                author_name = input("작가 이름을 입력하세요: ")
                self.BookList = DB.SearchAuthor(author_name)
            elif number == 3:
                title_name = input("책 제목을 입력하세요: ")
                self.BookList = DB.SearchTitle(title_name)
            elif number == 4:
                self.Show()

            elif number == 5:
                self.GPT()

            elif number == 6:
                age_tag = int(input("1. 일반 도서 2. 어린이 도서"))
                if(age_tag == 1):
                    age_string = "기본"
                    self.BookList = DB.searchAge(age_string)
                elif(age_tag == 2):
                    age_string = "어린이"
                    self.BookList = DB.searchAge(age_string)
                else : print("정의되지 않은 동작 \n\n")

            else :
                print("정의되지 않은 동작\n")


    def GPT(self) :
        print("몇번 책을 고르시겠습니까")
        n = int(input())

        if n < len(self.BookList):
            Book = self.BookList[n-1]

        Review = multiprocessing.Process(target = Book.Review())
        Quote = multiprocessing.Process(target = Book.Quote())
        Summary = multiprocessing.Process(target = Book.Summary())
        Debate = multiprocessing.Process(target = Book.Debate())

        Review.start()
        Quote.start()
        Summary.start()
        Debate.start()
        Review.join()
        Quote.join()
        Summary.join()
        Debate.join()


        print("감상평 : %s\n" % Review)
        
        print("\n")

        ok = input(" 문장이 만족스럽습니까? 1. 만족 2. 불만족")

        if (ok == 1) : pass
        elif(ok == 2) : 
            Review = bookGPT.arrange(Review)
            print("정리된 문장 : %s\n" % Review)

        print("주요 문장 인용 : %s\n" % Quote)
        
        print("\n")

        if (ok == 1) : pass
        elif(ok == 2) : 
            Quote = bookGPT.arrange(Quote)
            print("정리된 문장 : %s\n" % Quote)


        print("줄거리 요약 : %s\n" % Summary)
        
        print("\n")

        ok = input(" 문장이 만족스럽습니까? 1. 만족 2. 불만족")


        if (ok == 1) : pass
        elif(ok == 2) : 
            Summary = bookGPT.arrange(Summary)
            print("정리된 문장 : %s\n" % Summary)

        print("토론 주제 및 답변 : %s\n" % Debate)

        ok = input(" 문장이 만족스럽습니까? 1. 만족 2. 불만족")


        if (ok == 1) : pass
        elif(ok == 2) : 
            Debate = bookGPT.arrange(Debate)
            print("정리된 문장 : %s\n" % Debate)
        
        print("\n")

        
      
Ex = Execute()
Ex.Start()








        

        