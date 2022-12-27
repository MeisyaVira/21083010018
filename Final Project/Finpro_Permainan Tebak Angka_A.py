#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import string


# In[108]:


def welcome():
    print("x"*65)
    print("x", " "*12, "SELAMAT DATANG DI GAME TEBAK ANGKA!", " "*12, "x")
    print("x"*65)
    main()


# In[134]:


def main():
    types = int(input("x           JENIS PERMAINAN:   1. INFINITY                      x\nx                              2. ROGUELIKE                     x\nx                     PILIH:   "))
    if types == 1:
        pass
    elif types == 2:
        lives = 5
        print("x     PADA JENIS PERMAINAN INI KAMU HANYA MEMILIKI 5 NYAWA!     x")
    else:
        print("x                     KETIK ANGKA 1 ATAU 2!                     x")
    print("x"*65)
    level = int(input("x             TINGKAT KESULITAN PERMAINAN:   1. EASY            x\nx                                            2. NORMAL          x\nx                                            3. HARD            x\nx                                   PILIH:   "))
    if level == 1:
        num = 1
        secret = str(random.randint(10**(num-1), 10**(num)-1))
    elif level == 2:
        num = 2
        secret = str(random.randint(10**(num-1), 10**(num)-1))
    elif level == 3:
        num = int(input("x MASUKKAN JUMLAH DIGIT ANGKA YANG INGIN KAMU TEBAK, MINIMAL 3! x\nx                     JUMLAH DIGIT ANGKA:   "))
        if num < 3:
            print("x", " "*21, "MINIMAL 3 DIGIT!", " "*22, "x")
        secret = str(random.randint(10**(num-1), 10**(num)-1))
    print("x"*65)
            
    # TIPE INFINITY LEVEL MUDAH (1-1)
    if level == 1 and types == 1:
            while(True):
                guess = input("x                            TEBAK: ")
                if guess.isdecimal() == False: # Memeriksa apakah string berisi angka
                    print("x             NOTE: MOHON MASUKKAN ANGKA BILANGAN               x")
                    continue
                if len(guess) != len(secret):
                    print(f"x           NOTE: BILANGAN HARUS {len(secret)} dIGIT!          x")
                else:
                    if guess < secret:
                        print("x                 NOTICE: BILANGAN TERLALU KECIL                x")
                        hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                        if hint == 1:
                            answer1 = int(secret)
                            answer2 = int(guess)
                            plus = answer1 - answer2
                            print("x", " "*24, "HINT: ", answer2, "+", plus, " "*23, "x")
                        else:
                            continue
                    if guess > secret:
                        print("x                 NOTICE: BILANGAN TERLALU BESAR                x")
                        hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                        if hint == 1:
                            answer1 = int(secret)
                            answer2 = int(guess)
                            minus = answer2 - answer1
                            print("x", " "*24, "HINT: ", answer2, "-", minus, " "*23, "x")
                        else:
                            continue
                    if guess == secret:
                        print("x                 SELAMAT, TEBAKAN KAMU BENAR!                  x")
                        break
                        
    # TIPE ROGUELIKE LEVEL MUDAH (2-1)
    elif level == 1 and types == 2:
        for i in range(lives):
            i += 1 # i berfungsi sebagai penanda apabila nyawa sudah habis
            guess = input("x                            TEBAK: ")
            if guess.isdecimal() == False:
                print("x             NOTE: MOHON MASUKKAN ANGKA BILANGAN               x")
                continue
            if len(guess) != len(secret): #bila tebakkan tidak sesuai digit
                print(f"x           NOTE: BILANGAN HARUS {len(secret)} dIGIT!          x")
            else:
                if guess < secret:
                    print("x                 NOTICE: BILANGAN TERLALU KECIL                x")
                    if i > 1:
                        hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                        if hint == 1:
                            answer1 = int(secret)
                            answer2 = int(guess)
                            plus = answer1 - answer2
                            print("x", " "*24, "HINT: ", answer2, "+", plus, " "*23, "x")
                        if i == lives: # jika jumlah i sama dengan jumlah nyawa dan tebakan salah
                            print(f"x           MAAF, NYAWA ANDA SUDAH HABIS. (JAWABAN: {secret})          x")
                            break
                        else:
                            continue
                elif guess > secret:
                    print("x                 NOTICE: BILANGAN TERLALU BESAR                x")
                    if i > 1:
                        hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                        if hint == 1:
                            answer1 = int(secret)
                            answer2 = int(guess)
                            minus = answer2 - answer1
                            print("x", " "*24, "HINT: ", answer2, "-", minus, " "*23, "x")
                        if i == lives: # jika jumlah i sama dengan jumlah nyawa dan tebakan salah
                            print(f"x           MAAF, NYAWA ANDA SUDAH HABIS. (JAWABAN: {secret})           x")
                            break
                        else:
                            continue
                else:
                    print("x                 SELAMAT, TEBAKAN KAMU BENAR!                  x")
                    break
                    
    # TIPE INFINITY LEVEL SEDANG (1-2)
    elif level == 2 and types == 1:
        temp = 0 # variabel yang menandakan berapa jumlah digit di posisi yang benar
        n = 0
        while(True):
            guess = input("x                            TEBAK: ")
            if guess.isdecimal() == False:
                print("x             NOTE: MOHON MASUKKAN ANGKA BILANGAN               x")
                continue
            if len(guess) != len(secret):
                print(f"x           NOTE: BILANGAN HARUS {len(secret)} dIGIT!          x")
            else:
                if guess < secret:
                    print("x                 NOTICE: BILANGAN TERLALU KECIL                x")
                    hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                    if hint == 1:
                        answer1 = int(secret)
                        answer2 = int(guess)
                        plus = answer1 - answer2
                        print("x", " "*23, "HINT: ", answer2, "+", plus, " "*22, "x")
                    else:
                        continue
                if guess > secret:
                    print("x                 NOTICE: BILANGAN TERLALU BESAR                x")
                    hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                    if hint == 1:
                        answer1 = int(secret)
                        answer2 = int(guess)
                        minus = answer2 - answer1
                        print("x", " "*23, "HINT: ", answer2, "-", minus, " "*22, "x")
                    else:
                        continue
                if guess == secret:
                    print("x                 SELAMAT, TEBAKAN KAMU BENAR!                  x")
                    break
                    
    #TIPE ROGUELIKE LEVEL SEDANG (2-2)
    elif level == 2 and types == 2:
        for i in range(lives):
            i += 1 # i berfungsi sebagai penanda apabila nyawa sudah habis
            guess = input("x                            TEBAK: ")
            if guess.isdecimal() == False:
                print("x             NOTE: MOHON MASUKKAN ANGKA BILANGAN               x")
                continue
            if len(guess) != len(secret): #bila tebakkan tidak sesuai digit
                print(f"x           NOTE: BILANGAN HARUS {len(secret)} dIGIT!          x")
            else:
                if guess < secret:
                    print("x                 NOTICE: BILANGAN TERLALU KECIL                x")
                    if i > 2:
                        hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                        if hint == 1:
                            answer1 = int(secret)
                            answer2 = int(guess)
                            plus = answer1 - answer2
                            print("x", " "*23, "HINT: ", answer2, "+", plus, " "*22, "x")
                        if i == lives: # jika jumlah i sama dengan jumlah nyawa dan tebakan salah
                            print(f"x           MAAF, NYAWA ANDA SUDAH HABIS. (JAWABAN: {secret})          x")
                            break
                        else:
                            continue
                elif guess > secret:
                    print("x                 NOTICE: BILANGAN TERLALU BESAR                x")
                    if i > 2:
                        hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                        if hint == 1:
                            answer1 = int(secret)
                            answer2 = int(guess)
                            minus = answer2 - answer1
                            print("x", " "*23, "HINT: ", answer2, "-", minus, " "*22, "x")
                        if i == lives: # jika jumlah i sama dengan jumlah nyawa dan tebakan salah
                            print(f"x           MAAF, NYAWA ANDA SUDAH HABIS. (JAWABAN: {secret})          x")
                            break
                        else:
                            continue
                else:
                    print("x                 SELAMAT, TEBAKAN KAMU BENAR!                  x")
                    break
                    
    # TIPE INFINITY LEVEL SULIT
    elif level == 3 and types == 1:
        while(True):
            guess = input("x                            TEBAK: ")
            if guess.isdecimal() == False:
                print("x             NOTE: MOHON MASUKKAN ANGKA BILANGAN               x")
                continue
            if len(guess) != len(secret):
                print(f"x           NOTE: BILANGAN HARUS {len(secret)} dIGIT!          x")
            else:
                if guess < secret:
                    print("x                 NOTICE: BILANGAN TERLALU KECIL                x")
                    hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                    if hint == 1:
                        answer1 = int(secret)
                        answer2 = int(guess)
                        plus = answer1 - answer2
                        print("x", " "*22, "HINT: ", answer2, "+", plus, " "*22, "x")
                    else:
                        continue
                if guess > secret:
                    print("Bx                 NOTICE: BILANGAN TERLALU BESAR                x")
                    hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                    if hint == 1:
                        answer1 = int(secret)
                        answer2 = int(guess)
                        minus = answer2 - answer1
                        print("x", " "*22, "HINT: ", answer2, "-", minus, " "*22, "x")
                    else:
                        continue
                if guess == secret:
                    print("x                 SELAMAT, TEBAKAN KAMU BENAR!                  x")
                    break
                    
    # TIPE ROGUELIKE LEVEL SULIT
    elif level == 3 and types == 2:
        for i in range(lives):
            i += 1 # i berfungsi sebagai penanda apabila nyawa sudah habis
            guess = input("x                            TEBAK: ")
            if guess.isdecimal() == False:
                print("x             NOTE: MOHON MASUKKAN ANGKA BILANGAN               x")
                continue
            if len(guess) != len(secret): #bila tebakkan tidak sesuai digit
                print(f"x           NOTE: BILANGAN HARUS {len(secret)} dIGIT!          x")
            else:
                if guess < secret:
                    print("x                 NOTICE: BILANGAN TERLALU KECIL                x")
                    if i > 3:
                        hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                        if hint == 1:
                            answer1 = int(secret)
                            answer2 = int(guess)
                            plus = answer1 - answer2
                            print("x", " "*22, "HINT: ", answer2, "+", plus, " "*22, "x")
                        if i == lives: # jika jumlah i sama dengan jumlah nyawa dan tebakan salah
                            print(f"x           MAAF, NYAWA ANDA SUDAH HABIS. (JAWABAN: {secret})         x")
                            break
                        else:
                            continue
                elif guess > secret:
                    print("x                 NOTICE: BILANGAN TERLALU BESAR                x")
                    if i > 3:
                        hint = int(input("x                        BUTUH BANTUAN?                         x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
                        if hint == 1:
                            answer1 = int(secret)
                            answer2 = int(guess)
                            minus = answer2 - answer1
                            print("x", " "*22, "HINT: ", answer2, "-", minus, " "*22, "x")
                        if i == lives: # jika jumlah i sama dengan jumlah nyawa dan tebakan salah
                            print(f"x           MAAF, NYAWA ANDA SUDAH HABIS. (JAWABAN: {secret})         x")
                            break
                        else:
                            continue
                else:
                    print("x                 SELAMAT, TEBAKAN KAMU BENAR!                  x")
                    break
    
    print("x"*65)
    repeat = int(input("x                 APA KAMU INGIN BERMAIN LAGI?                  x\nx                        1. IYA                                 x\nx                        2. TIDAK                               x\nx                        PILIH: "))
    if repeat == 1:
        welcome()
    if repeat == 2:
        print("x"*65)
        print("x                  TERIMA KASIH TELAH BERMAIN!                  x")
        print("x"*65)


# In[135]:


welcome()

