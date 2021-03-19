from PyQt5.QtWidgets import QDesktopWidget,QApplication
from datetime import timedelta, datetime
from ctypes  import *
import pygame as pg
import random
import sys
import matplotlib.pyplot as plt
from twilio.rest import Client 

pg.init()
app = QApplication(sys.argv)
q= QDesktopWidget().availableGeometry()
w, h = q.width() - 100, q.height() - 100
#w, h = 800, 400
sc = pg.display.set_mode((w, h), 1)
pg.display.update()
sc.fill((255, 255, 255))
pg.display.update()


class Grafiki():
    def __init__(self):
        self.name='Kasper'
    
    def message(self, text):
        if self.message_ok % 2 == 1:
            
            account_sid = 'ACb7fbe60fc6a6d269009183dddaeb9b60' 
            auth_token = '5649c067e88ccc529ba35971745ac35e' 
            client = Client(account_sid, auth_token) 
 
            message = client.messages.create( 
                                          from_='whatsapp:+14155238886',  
                                          body=''+text,      
                                          to='whatsapp:+79160426552' 
                                       ) 
            
            print(message.sid)
    
    #------------------------динамический график--------------------
    
    def din_graph(self):
        plt.figure(figsize=(9.5, 2))
        plt.plot(self.date_array[0:7], self.days, 'r--')
        plt.plot(self.date_array[7:30], self.hours, 'g--')
        plt.plot(self.date_array[30:90], self.minutes, 'b--')
        plt.grid()#setka
        # Names
        plt.title('Динамический график кол-ва шагов')
        plt.savefig('din.png')

        picture = pg.image.load('din.png')
        #picture = pg.transform.scale(picture, (800, 800))
        rect = picture.get_rect(topleft = (912, 486))
        rect = rect.move((0, 0))
        sc.blit(picture, rect)
        pg.display.update()
        
    def din_calc(self):
        self.days = self.sred[0:7]
        self.hours = []
        self.minutes = self.data_array[60*24*7+60*23:60*24*8]
        for i in range(1, 24):
            suma_23 = 0
            kol = 0
            for j in range(60):
                if self.data_array[j*i] > 0:
                    kol += 1
                suma_23 += self.data_array[j*i]
            if kol == 0:
                self.hours.append(suma_23 / 1)
            else:
                self.hours.append(suma_23 / kol)
        
        self.din_array = []
        for i in range(7):
            self.din_array.append(self.days[i])
        for i in range(23):
            self.din_array.append(self.hours[i])
        for i in range(60):
            self.din_array.append(self.minutes[i])
        self.din_graph()
    
    
    
    #-----------------------------base ------------------
    def base(self):
        picture = pg.image.load('on.png')
        picture = pg.transform.scale(picture, (39*2, 21*2))
        rect = picture.get_rect(topleft = (1150, 370 - 80))
        rect = rect.move((0, 0))
        sc.blit(picture, rect)
        pg.display.update()
        
        font = pg.font.SysFont('simsunextb', 34)
        text_mes = font.render('Сообщение выкл/вкл', 1, (0, 200, 0))
        sc.blit(text_mes, (1160 + 39*2, 380 - 80))
        pg.display.update()
        
        
        font = pg.font.SysFont('simsunextb', 27)
        text_mes = font.render('дата', 1, (0, 0, 0))
        sc.blit(text_mes, ((q.width() - 100) // 4 - 40, q.height() - 120))
        pg.display.update()

        font = pg.font.SysFont('simsunextb', 27)
        text_mes = font.render('минуты', 1, (0, 0, 0))
        sc.blit(text_mes, ((q.width() - 100) // 4 * 3 - 40 , q.height() - 120))

        picture = pg.image.load('udav.png')
        picture = pg.transform.scale(picture, (133*3, 54*3))
        rect = picture.get_rect(topleft = (1180, 0))
        rect = rect.move((0, 0))
        sc.blit(picture, rect)
        pg.display.update()
        
        font = pg.font.SysFont('simsunextb', 23)
        text_din = font.render('           7 дней                     23 часа                                                                60 минут                                                                    ', 1, (0, 0, 0), (255, 255, 255))
        sc.blit(text_din, (1000, 670))
        pg.display.update()
        
        font = pg.font.SysFont('simsunextb', 23)
        text_din = font.render('             0                180              360              540               720               900             1080               1260              1440               ', 1, (0, 0, 0), (255, 255, 255))
        sc.blit(text_din, (1000, 670 + 235))
        pg.display.update()
        
        
        
        
        
        font = pg.font.SysFont('simsunextb', 50)
        fontk = pg.font.SysFont('simsunextb', 100)
        
        textka = fontk.render('              Kasper', 1, (0, 0, 250))
        text =   font.render('Диагностика состояния домашних животных', 1, (0, 0, 250))
        textdo = font.render('     по параметрам физической активности', 1, (0, 0, 250))
        sc.blit(textka, (1000, 110))
        pg.display.update()
        sc.blit(text, (1000, 180))
        pg.display.update()
        sc.blit(textdo, (1000, 220))
        pg.display.update()
        
        fontgor = pg.font.SysFont('simsunextb', 27)
        text_gor1 = fontgor.render('--- Среднее за 7 дней', 1, (0, 125, 0))
        sc.blit(text_gor1, (1400, 800))
        pg.display.update()
        
        fontgor = pg.font.SysFont('simsunextb', 27)
        text_gor1 = fontgor.render('--- За последние 24 часа', 1, (0, 0, 200))
        sc.blit(text_gor1, (1400, 820))
        pg.display.update()
        
        
        font = pg.font.SysFont('simsunextb', 32)
        a = 'Дата последней синхронизации: ' + self.nowstr
        text_time = font.render(a, 1, (0, 200, 0))
                    
        sc.blit(text_time, (1150, 470 - 80))
        pg.display.update()
        
        alarmcalc = 0
        predcalc = 0
        
        #----------------предупреждение и авария
        for i in range(len(self.data_array) - 1):
            j = len(self.data_array) - 1 - i
            if self.data_array[j] >= int(self.sred_for_all[0] + (self.sigma_all[0] * 3)):
                if alarmcalc == 0:
                    text_alarm = font.render('Последняя тревога была ' + str(self.date_array[j].strftime("%d.%m-%H:%M")), 1, (255, 0, 0))
                    sc.blit(text_alarm, (1150, 420 - 80))
                    pg.display.update()
                    alarmcalc = 1
                    
                    
                    
            if self.data_array[j] >= int(self.sred_for_all[0] + self.sigma_all[0]):
                if self.data_array[j - 1] >= int(self.sred_for_all[0] + self.sigma_all[0]):
                    if predcalc == 0:
                        text_pred = font.render('Последнее предупреждение было ' + str(self.date_array[j].strftime("%d.%m-%H:%M")), 1, (255, 153, 51))
                        sc.blit(text_pred, (1150, 445 - 80))
                        pg.display.update()
                        predcalc = 1
        
        font_zov = pg.font.SysFont('simsunextb', 27)
        text_pred = font_zov.render('Сумарная разница: ' + str(int(self.zov_par)), 1, (0, 0, 0))
        sc.blit(text_pred, (1400, 780))
        pg.display.update()
        
        predinfive = 0
        alarmcalc = 0
        for i in range(5):
            j = len(self.data_array) - 1 - i
            if self.data_array[j] >= int(self.sred_for_all[0] + (self.sigma_all[0] * 3)):
                if alarmcalc == 0:
                    self.message('Опастность! Ваша собака сделала слишком много шагов! Проведайте её, возможно с ней что-то не так. Красный!')
                    alarmcalc = 1
            if self.data_array[j] >= int(self.sred_for_all[0] + self.sigma_all[0]):
                predinfive+=1
        
        if predinfive > 1:
            self.message('Предупреждение: ближайшие пять минут Ваша собака ходила слишком много, жёлтый.')
        
        
        
        
        picture = pg.image.load('svetofor.JPG')
        picture = pg.transform.scale(picture, (40, 70))
        rect = picture.get_rect(topleft = (1050 + 50, 420 - 80))
        rect = rect.move((0, 0))
        sc.blit(picture, rect)
        pg.display.update()
        
        
        

    #--------------------------горки-----------
    def set_graph_gorka(self):
        plt.figure(figsize=(9.5, 2))
        plt.plot(self.date_array[0:60*24], self.sort_seven, 'g.')
        plt.plot(self.date_array[0:60*24], self.sort_today, 'b.')
        plt.grid()#setka
        # Names
        plt.ylabel('Шаги в минуту')
        plt.title('Распределение по убыванию за 24 часа')
        plt.savefig('gor.png')

        picture = pg.image.load('gor.png')
        #picture = pg.transform.scale(picture, (800, 800))
        rect = picture.get_rect(topleft = (912, 719))
        rect = rect.move((0, 0))
        sc.blit(picture, rect)
        pg.display.update()
        
    
    def gorki_calc(self):
        self.sort_today=sorted(self.data_array[60*24*6:60*24*7], reverse=True)
        self.sort_seven=[]
        for i in range(60*24):
            self.sort_seven.append(0)
        
        for i in range(7):
            sort = sorted(self.data_array[i * 60 * 24:(i+1)*60*24], reverse=True)
            for j in range(60*24):
                self.sort_seven[j]+=sort[j]
        
        for i in range(60*24):
            self.sort_seven[i] = self.sort_seven[i] // 7
        self.zov_par = 0
        for i in range(60*24):
            self.zov_par+=((self.sort_seven[i]-self.sort_today[i])**2)**0.5
        
        
        self.set_graph_gorka()
    
    
    
    
    
    # ------------------------% sleep ----------------------------
    def set_graph_sleep(self):
        
        plt.figure(figsize=(9.5, 2))
        plt.plot(self.date_for_pro, self.sleep_pros, 'b.')
        plt.grid()#setka
        # Names
        plt.ylabel('%')
        plt.title('Сон в неактивности')
        plt.savefig('sleep.png')

        picture = pg.image.load('sleep.png')
        #picture = pg.transform.scale(picture, (800, 800))
        rect = picture.get_rect(topleft = (-40, 20))
        rect = rect.move((0, 0))
        sc.blit(picture, rect)
        pg.display.update()
        
    
    def sleep_calc(self):
        self.sleep_pros = []
        for i in range(8):
            self.sleep_pros.append(0)
            self.sleep_pros[i] = self.sleep_data[i]  / (self.sleep_data[i] + self.otd_data[i]) * 100
        self.set_graph_sleep()
    
    def set_sleep_otd_array(self):
        
        #self.data_array = [1, 2, 3, 64, 3, 0, 5, 0, 0, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 65, 0]
        self.sleep_data = []
        self.otd_data = []
        
        for w in range(8):
            kolvosl = 0
            nul = 0
            for i in range(w * 60 * 24, (w + 1) * 60 * 24):
                if self.data_array[i] == 0:
                    nul+=1
            
            for i in range(w * 60 * 24, (w + 1) * 60 * 24):
                if self.data_array[i] == 0 and i > self.sleep_parametr - 1:
                    tss = 0
                    for j in range(1, self.sleep_parametr + 1):
                        if self.data_array[i - j] == 0:
                            tss += 1
                    if tss == self.sleep_parametr:
                        kolvosl+=1
            self.sleep_data.append(kolvosl)
            self.otd_data.append(nul - kolvosl)
        print(self.sleep_data, self.otd_data, nul) 
        self.sleep_calc()
    
    # ---------------------------------% activity-------------------------
    
    def set_graph_pro(self):
        
        plt.figure(figsize=(9.5, 2))
        plt.plot(self.date_for_pro, self.natur_number, 'b.')
        plt.grid()#setka
        # Names
        plt.ylabel('%')
        plt.title('Активность')
        plt.savefig('pro.png')

        picture = pg.image.load('pro.png')
        #picture = pg.transform.scale(picture, (800, 800))
        rect = picture.get_rect(topleft = (-40, 253))
        rect = rect.move((0, 0))
        sc.blit(picture, rect)
        pg.display.update()
        
    
    def pro_calc(self):
        self.natur_number = []
        self.bolminod = []
        
        for i in range(8):
            self.natur_number.append(0) 
            self.bolminod.append(0) 
            
        for j in range(1, 9):
            for i in range((j-1) * 60 * 24, j * 60 * 24):
                if self.data_array[i] > 0:
                    self.natur_number[j - 1] += 1
        
        
        for j in range(1, 9):
            for i in range((j-1) * 60 * 24, j * 60 * 24):
                if self.data_array[i] > -1:
                    self.bolminod[j - 1] += 1

        for i in range(8):
            if self.bolminod[i] ==0:
                self.bolminod[i]=0.00001
            self.natur_number[i] = self.natur_number[i]  / self.bolminod[i] * 100

        
        
        self.date_for_pro = []
        for i in range(8):
            days = timedelta(7)
            date = self.now - days + timedelta(i)
            self.date_for_pro.append(date.strftime("%d.%m"))
        self.set_sleep_otd_array()
        self.set_graph_pro()
        
    #----------------------------------------------
     
     
    # ----------- среднее-----------------
    #-----последние данные не считаются---
    # работает отлично!2 0
    def set_graph_sred(self):
        
        plt.figure(figsize=(9.5, 2))
        plt.plot(self.date_for_pro, self.sred, 'b.')
        
        plt.plot(self.date_for_pro[0:7], self.sred_for_all, 'g--')# средняя линия
        plt.plot(self.date_for_pro[0:7], self.min_sig, '-', color = 'darkorange')
        plt.plot(self.date_for_pro[0:7], self.plu_sig, '-', color = 'darkorange')
        
        plt.grid()#setka
        # Names
        plt.ylabel('Шаги в минуту')
        plt.title('Среднее за 24 часа')
        plt.savefig('sre.png')

        picture = pg.image.load('sre.png')
        #picture = pg.transform.scale(picture, (800, 800))
        rect = picture.get_rect(topleft = (-40, 719))
        rect = rect.move((0, 0))
        sc.blit(picture, rect)
        pg.display.update()
        
    
    
    def sigma_for_all(self):
        
        self.sigma_all = []
        self.sigma_all.append(0)
        
        for i in range(7*24*60):
            if self.data_array[i] > 0:
                self.sigma_all[0] += (self.data_array[i] - self.sred_for_all[0])**2
        if self.nat ==0:
                self.nat=0.00001
        self.sigma_all[0] = (self.sigma_all[0] / self.nat)**0.5
        
        
        
        for i in range(7):
            self.sigma_all.append(self.sigma_all[0])
            
        self.min_sig = []
        for i in range(7):
            self.min_sig.append(self.sred_for_all[0] - self.sigma_all[0])
        
        self.plu_sig = []
        for i in range(7):
            self.plu_sig.append(self.sred_for_all[0] + self.sigma_all[0])
    
    def sred_calc(self):
        self.ne_nul = []
        self.sred = []
        self.suma = []
        for i in range(8):
            self.sred.append(0) 
            self.suma.append(0) 
            self.ne_nul.append(0) 
        
        for j in range(1, 9):
            for i in range((j-1) * 60 * 24, j * 60 * 24):
                if self.data_array[i] > 0:
                    self.suma[j - 1] += self.data_array[i]
                    self.ne_nul[j - 1] += 1
            if self.ne_nul[j - 1] ==0:
                self.ne_nul[j - 1]=0.00001
            self.sred[j - 1] = self.suma[j - 1] / self.ne_nul[j - 1]

        
        self.sred_for_all = []
        self.nat = 0
        for i in range(7*60*24):
            if self.data_array[i] > 0:
                self.nat += 1
        if self.nat ==0:
                self.nat=0.00001
        sred_all = sum(self.data_array[0:60*24*7]) / self.nat 
        
        for i in range(7):
            self.sred_for_all.append(sred_all)
        
        self.sigma_for_all()
        self.set_graph_sred()
    # ---------------------------------------------
    
    
    # --------sigma--------------------
    #20
    def set_graph_sig(self):
        
        plt.figure(figsize=(9.5, 2))
        plt.plot(self.date_for_pro, self.sigma, 'b.')
        plt.grid()#setka
        # Names
        plt.ylabel('Шаги в минуту')
        plt.title('Стандартное отклонение, σ')
        plt.savefig('sig.png')

        picture = pg.image.load('sig.png')
        #picture = pg.transform.scale(picture, (800, 800))
        rect = picture.get_rect(topleft = (-40, 486))
        rect = rect.move((0, 0))
        sc.blit(picture, rect)
        pg.display.update()
    
     
    def sigma_calc(self):
        self.sel_number = []   
        self.sigma = []
        for i in range(8):
            self.sigma.append(0) 
            self.sel_number.append(0)     
            
        for j in range(1, 9):
            for i in range((j-1) * 60 * 24, j * 60 * 24):
                if self.data_array[i] > 0:
                    self.sigma[j - 1] += (self.data_array[i] - self.sred[j - 1])**2
                    
            for i in range((j-1) * 60 * 24, j * 60 * 24):
                if self.data_array[i] > 0:
                    self.sel_number[j - 1] += 1       
            
            
            if self.sel_number[j - 1] ==0:
                self.sel_number[j - 1]=0.00001
            self.sigma[j - 1] = self.sigma[j - 1] / (self.sel_number[j - 1])
            self.sigma[j - 1] = (self.sigma[j - 1])**0.5
            

        self.set_graph_sig()
        
    #---------------------------------------------------------        
    #2 0
    def set_data_and_date_array(self, xxx, yyy):
        
        for i in range(len(yyy)):
            yyy[i] = datetime.strptime(yyy[i], '%d.%m.%Y %H:%M')
            yyy[i] = yyy[i].strftime("%d.%m.%Y %H:%M")
            yyy[i] = datetime.strptime(yyy[i], "%d.%m.%Y %H:%M")
        
        self.now = yyy[len(yyy) - 1]
        self.nowstr = self.now.strftime("%d.%m.%Y %H:%M")

        self.sleep_parametr = 5
        self.date_array = yyy
        self.data_array = xxx
        i = 0
        sss = 0
        # удаление лишних первых данных new
        self.first_day = self.now - timedelta(8) 
        
        for i in range(60*24*8):
            if self.date_array[i - sss] <= self.first_day:
                self.date_array.pop(i - sss)
                self.data_array.pop(i - sss)
                sss+=1

        # добавляем -1 в начало new
        for i in range(60*24*7):
            mine = timedelta(minutes = i) + timedelta(1)
            date = self.now - mine
            if not date in self.date_array:
                self.date_array.insert(0, date)
                self.data_array.insert(0, -1)
        
        
        self.pro_calc()
        self.sred_calc()
        self.sigma_calc()
        self.gorki_calc()
        self.din_calc()
        self.base()
        
        
        self.message_ok = 1
        udav_calc = 1
        #self.message('Опастность! Ваша собака сделала слишком много шагов! Проведайте её, возможно с ней что-то не так.')
        while True:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
                elif i.type == pg.MOUSEBUTTONDOWN:
                    
                    if i.pos[0] > 1180 and i.pos[0] < 1180 + 399:
                        if i.pos[1] > 0 and i.pos[1] < 54*3:
                            udav_calc+=1
                            if udav_calc % 2 == 1:
                                picture = pg.image.load('udav.png')
                                picture = pg.transform.scale(picture, (133*3, 54*3))
                                rect = picture.get_rect(topleft = (1180, 0))
                                rect = rect.move((0, 0))
                                sc.blit(picture, rect)
                                pg.display.update()
                                
                                fontk = pg.font.SysFont('simsunextb', 100)
                                textka = fontk.render('              Kasper', 1, (0, 0, 250))
                                sc.blit(textka, (1000, 110))
                                pg.display.update()
                            
                            else:
                                picture = pg.image.load('udavrengen.png')
                                picture = pg.transform.scale(picture, (133*3, 54*3))
                                rect = picture.get_rect(topleft = (1180, 0))
                                rect = rect.move((0, 0))
                                sc.blit(picture, rect)
                                pg.display.update()
                                
                                fontk = pg.font.SysFont('simsunextb', 100)
                                textka = fontk.render('              Kasper', 1, (0, 0, 250))
                                sc.blit(textka, (1000, 110))
                                pg.display.update()
                                
                                
                    
                    
                    
                    if i.pos[0] > 1150 and i.pos[0] < 1150 + 39 * 2:
                        if i.pos[1] > 370 - 80 and i.pos[1] < 370 + 42 - 80:
                            self.message_ok +=1
                            if self.message_ok % 2 == 1:
                                picture = pg.image.load('on.png')
                                picture = pg.transform.scale(picture, (39*2, 21*2))
                                rect = picture.get_rect(topleft = (1150, 370 - 80))
                                rect = rect.move((0, 0))
                                sc.blit(picture, rect)
                                pg.display.update()
                                
                            else:
                                picture = pg.image.load('off.png')
                                picture = pg.transform.scale(picture, (39*2, 21*2))
                                rect = picture.get_rect(topleft = (1150, 370 - 80))
                                rect = rect.move((0, 0))
                                sc.blit(picture, rect)
                                pg.display.update()
                    
        



