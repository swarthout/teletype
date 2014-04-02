"""
TELE-TYPE

This is a program that decodes telephone word codes. It inputs a string of numbers and outputs an array of possible solutions for each code word. For example, if you input 43556, it will output happy!

BETA VERSION
Created by: Scott "Beamer" Swarthout
Notable Associates: Sophia "Cupcake" Farquhar


"""

#These are the two dictionaries used for translating the code. big_list is the full english dictionary including names and places.
#small_list is a list of the most commmonly used words in the english language.
big_list = open("long word list.rtf").read()
big_list = big_list.lower()
big_list = big_list.replace("\\","")
big_list = big_list.split()
small_list = open("frequency list.rtf").read()
small_list = small_list.lower()
small_list = small_list.replace("\\","")
small_list = small_list.split()
import time

def decode():



    code = input("Enter code to be decoded: ")
    start_time = time.time()

    code = code.split("0")

    def find_word(a):



        poss = {}
        temp = []
    #This converts the list of numbers in the code into a dictionary with each number replaced with the set of letters it can possibly be.
        numtoalpha = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        for x in range(0,len(a)):

            word = [i for i in a[x]]

            for z in range(len(word)):

                temp.append(numtoalpha[word[z]])

                poss["word %d"%(x+1)] = temp
            temp = []
        g = 0
        # poss is the dictionary with all of the words and their possible letters


        permutations = {}
        for x in range(len(poss)):

            letters = poss["word %d"%(x+1)]

            def radixconvert(a, b): #This function converts a decimal number into a number with a specified radix set

            #a is the number to be converted. b is the radix set
                if a == 0:
                    return 0
                else:

                    b = str(b)
                    s = a

                    answer = []
                    leftover = a
                    x = 0
                    while leftover >0:

                        y = -x -1
                        f = int(b[y])


                        leftover = (s-(s%f))/f
                        remainder = s%f
                        s = leftover
                        answer.insert(0,int(remainder))
                        x += 1

                    answer = "".join(map(str, answer))
                    answer = int(answer)
                    return answer

            options = 1
            radixset = []
            for i in range(len(letters)):
                options *=len(letters[i])
                radixset.append(len(letters[i]))


            radixset = "".join(map(str, radixset))
            radixset = int(radixset)

            posslist = []
            #options is the number of permutations of the possible letters in the word.
            for i in range(options):

                posslist.append(str(radixconvert(i,radixset)).rjust(len(letters),"0"))


            combos = [] #combos is the list of permutations with each letter separated into a different item

            s = len(letters)
            for nums in posslist:
                for k in range(len(letters)):

                    r = letters[k]
                    combos.append(r[int(nums[k])])



                    newcombo = [] #newcombo is the same list as combos but with each permutation grouped into words

            for x in range(0,int(len(combos)), s):
                guess =combos[x:x+s]

                guess = "".join(guess)

                newcombo.append(guess)




            permutations["word %d"%(g+1)] = newcombo
            g+=1



        validwords = []

    #This loop checks to see if the permutation is a valid word in the dictionary. If so, it adds it to the list of validwords
        for i in range(len(poss)):
            valid = []


            for guess in permutations["word %d"%(i+1)]:

                if guess in small_list:
                    valid.append(guess)
                elif guess in big_list:
                    valid.append(guess)
            validwords.append(valid)


        return (validwords)
        # return (time.time() - start_time, "seconds")

    print(find_word(code))
    print(time.time() - start_time, "seconds")
    decode()
decode()










