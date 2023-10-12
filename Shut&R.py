import os
import ctypes
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showwarning, showinfo
from tkinter import ttk
from tkinter import *
from pygame.locals import *
from tkinter import *
from ctypes import windll
from BlurWindow.blurWindow import blur

window = tk.Tk()
window.title("Shut_and_R")
window.geometry('480x320')
window.iconbitmap('images.png')
# window.config(bg='blue')

# window.wm_attributes('-transparentcolor', 'blue')
window.config(bg='gray')

window.wm_attributes("-transparent", 'gray')

hWnd = windll.user32.GetForegroundWindow()
blur(hWnd)


def Cancel():
    window.destroy()

def what_button_will_do_sh():
          while True:
            if hour.get() == '1':
              window.after(3600000, lambda : play_sound())

            if minute.get() == '1':
              window.after(60000, lambda : play_sound())

            if second.get() == '1':
              window.after(1000, lambda : play_sound())

            if hour.get() == '2':
              window.after(2*3600000, lambda : play_sound())

            if minute.get() == '2':
              window.after(2*60000, lambda : play_sound())

            if second.get() == '2':
              window.after(2*1000, lambda : play_sound())

            if hour.get() == '3':
              window.after(3*3600000, lambda : play_sound())

            if minute.get() == '3':
              window.after(3*60000, lambda : play_sound())

            if second.get() == '3':
              window.after(3*1000, lambda : play_sound())

            if hour.get() == '4':
              window.after(4*3600000, lambda : play_sound())

            if minute.get() == '4':
              window.after(4*60000, lambda : play_sound())

            if second.get() == '4':
              window.after(4*1000, lambda : play_sound())

            if hour.get() == '5':
              window.after(5*3600000, lambda : play_sound())

            if minute.get() == '5':
              window.after(5*60000, lambda : play_sound())

            if second.get() == '5':
              window.after(5*1000, lambda : play_sound())

            if hour.get() == '6':
              window.after(6*3600000, lambda : play_sound())

            if minute.get() == '6':
              window.after(6*60000, lambda : play_sound())

            if second.get() == '6':
              window.after(6*1000, lambda : play_sound())

            if hour.get() == '7':
              window.after(7*3600000, lambda : play_sound())

            if minute.get() == '7':
              window.after(7*60000, lambda : play_sound())

            if second.get() == '7':
              window.after(7*1000, lambda : play_sound())

            if hour.get() == '8':
              window.after(8*3600000, lambda : play_sound())

            if minute.get() == '8':
              window.after(8*60000, lambda : play_sound())

            if second.get() == '8':
              window.after(8*1000, lambda : play_sound())

            if hour.get() == '9':
              window.after(9*3600000, lambda : play_sound())

            if minute.get() == '9':
              window.after(9*60000, lambda : play_sound())

            if second.get() == '9':
              window.after(9*1000, lambda : play_sound())

            if hour.get() == '10':
              window.after(10*3600000, lambda : play_sound())

            if minute.get() == '10':
              window.after(10*60000, lambda : play_sound())

            if second.get() == '10':
              window.after(10*1000, lambda : play_sound())

            if hour.get() == '11':
              window.after(11*3600000, lambda : play_sound())

            if minute.get() == '11':
              window.after(11*60000, lambda : play_sound())

            if second.get() == '11':
              window.after(11*1000, lambda : play_sound())

            if hour.get() == '12':
              window.after(12*3600000, lambda : play_sound())

            if minute.get() == '12':
              window.after(12*60000, lambda : play_sound())

            if second.get() == '12':
              window.after(12*1000, lambda : play_sound())

            if hour.get() == '13':
              window.after(13*600000, lambda : play_sound())

            if minute.get() == '13':
              window.after(13*60000, lambda : play_sound())

            if second.get() == '13':
              window.after(13*1000, lambda : play_sound())

            if hour.get() == '14':
              window.after(14*3600000, lambda : play_sound())

            if minute.get() == '14':
              window.after(14*60000, lambda : play_sound())

            if second.get() == '14':
              window.after(14*1000, lambda : play_sound())

            if hour.get() == '15':
              window.after(15*3600000, lambda : play_sound())

            if minute.get() == '15':
              window.after(15*60000, lambda : play_sound())

            if second.get() == '15':
              window.after(15*1000, lambda : play_sound())

            if hour.get() == '16':
              window.after(16*3600000, lambda : play_sound())

            if minute.get() == '16':
              window.after(16*60000, lambda : play_sound())

            if second.get() == '16':
              window.after(16*1000, lambda : play_sound())

            if hour.get() == '17':
              window.after(17*3600000, lambda : play_sound())

            if minute.get() == '17':
              window.after(17*60000, lambda : play_sound())

            if second.get() == '17':
              window.after(17*1000, lambda : play_sound())

            if hour.get() == '18':
              window.after(18*3600000, lambda : play_sound())

            if minute.get() == '18':
              window.after(18*60000, lambda : play_sound())

            if second.get() == '18':
              window.after(18*1000, lambda : play_sound())

            if hour.get() == '19':
              window.after(19*3600000, lambda : play_sound())

            if minute.get() == '19':
              window.after(19*60000, lambda : play_sound())

            if second.get() == '19':
              window.after(19*1000, lambda : play_sound())

            if hour.get() == '20':
              window.after(20*3600000, lambda : play_sound())

            if minute.get() == '20':
              window.after(20*60000, lambda : play_sound())

            if second.get() == '20':
              window.after(20*1000, lambda : play_sound())

            if hour.get() == '21':
              window.after(21*3600000, lambda : play_sound())

            if minute.get() == '21':
              window.after(21*60000, lambda : play_sound())

            if second.get() == '21':
              window.after(21*1000, lambda : play_sound())

            if hour.get() == '22':
              window.after(22*3600000, lambda : play_sound())

            if minute.get() == '22':
              window.after(22*60000, lambda : play_sound())

            if second.get() == '22':
              window.after(22*1000, lambda : play_sound())

            if hour.get() == '23':
              window.after(23*3600000, lambda : play_sound())

            if minute.get() == '23':
              window.after(23*60000, lambda : play_sound())

            if second.get() == '23':
              window.after(23*1000, lambda : play_sound())

            if hour.get() == '24':
              window.after(24*3600000, lambda : play_sound())

            if minute.get() == '24':
              window.after(24*60000, lambda : play_sound())

            if second.get() == '24':
              window.after(24*1000, lambda : play_sound())

            if minute.get() == '25':
              window.after(25*60000, lambda : play_sound())

            if second.get() == '25':
              window.after(25*1000, lambda : play_sound())

            if minute.get() == '26':
              window.after(26*60000, lambda : play_sound())

            if second.get() == '26':
              window.after(26*1000, lambda : play_sound())

            if minute.get() == '27':
              window.after(27*60000, lambda : play_sound())

            if second.get() == '27':
              window.after(27*1000, lambda : play_sound())

            if minute.get() == '28':
              window.after(28*60000, lambda : play_sound())

            if second.get() == '28':
              window.after(28*1000, lambda : play_sound())

            if minute.get() == '29':
              window.after(29*60000, lambda : play_sound())

            if second.get() == '29':
              window.after(29*1000, lambda : play_sound())

            if minute.get() == '30':
              window.after(30*60000, lambda : play_sound())

            if second.get() == '30':
              window.after(30*1000, lambda : play_sound())

            if minute.get() == '31':
              window.after(31*60000, lambda : play_sound())

            if second.get() == '31':
              window.after(31*1000, lambda : play_sound())

            if minute.get() == '32':
              window.after(32*60000, lambda : play_sound())

            if second.get() == '32':
              window.after(32*1000, lambda : play_sound())

            if minute.get() == '33':
              window.after(33*60000, lambda : play_sound())

            if second.get() == '33':
              window.after(33*1000, lambda : play_sound())

            if minute.get() == '34':
              window.after(34*60000, lambda : play_sound())

            if second.get() == '34':
              window.after(34*1000, lambda : play_sound())

            if minute.get() == '35':
              window.after(35*60000, lambda : play_sound())

            if second.get() == '35':
              window.after(35*1000, lambda : play_sound())

            if minute.get() == '36':
              window.after(36*60000, lambda : play_sound())

            if second.get() == '36':
              window.after(36*1000, lambda : play_sound())

            if minute.get() == '37':
              window.after(37*60000, lambda : play_sound())

            if second.get() == '37':
              window.after(37*1000, lambda : play_sound())

            if minute.get() == '38':
              window.after(38*60000, lambda : play_sound())

            if second.get() == '38':
              window.after(38*1000, lambda : play_sound())

            if minute.get() == '39':
              window.after(39*60000, lambda : play_sound())

            if second.get() == '39':
              window.after(39*1000, lambda : play_sound())

            if minute.get() == '40':
              window.after(40*60000, lambda : play_sound())

            if second.get() == '40':
              window.after(40*1000, lambda : play_sound())

            if minute.get() == '41':
              window.after(41*60000, lambda : play_sound())

            if second.get() == '41':
              window.after(41*1000, lambda : play_sound())

            if minute.get() == '42':
              window.after(42*60000, lambda : play_sound())

            if second.get() == '42':
              window.after(42*1000, lambda : play_sound())

            if minute.get() == '43':
              window.after(43*60000, lambda : play_sound())

            if second.get() == '43':
              window.after(43*1000, lambda : play_sound())

            if minute.get() == '44':
              window.after(44*60000, lambda : play_sound())

            if second.get() == '44':
              window.after(44*1000, lambda : play_sound())

            if minute.get() == '45':
              window.after(45*60000, lambda : play_sound())

            if second.get() == '45':
              window.after(45*1000, lambda : play_sound())

            if minute.get() == '46':
              window.after(46*60000, lambda : play_sound())

            if second.get() == '46':
              window.after(46*1000, lambda : play_sound())

            if minute.get() == '47':
              window.after(47*60000, lambda : play_sound())

            if second.get() == '47':
              window.after(47*1000, lambda : play_sound())

            if minute.get() == '48':
              window.after(48*60000, lambda : play_sound())

            if second.get() == '48':
              window.after(48*1000, lambda : play_sound())

            if minute.get() == '49':
              window.after(49*60000, lambda : play_sound())

            if minute.get() == '49':
              window.after(49*1000, lambda : play_sound())

            if minute.get() == '50':
              window.after(50*60000, lambda : play_sound())

            if second.get() == '50':
              window.after(50*1000, lambda : play_sound())

            if second.get() == '51':
              window.after(3600000, lambda : play_sound())
              
            if minute.get() == '51':
              window.after(51*1000, lambda : play_sound())

            if minute.get() == '52':
              window.after(52*60000, lambda : play_sound())

            if second.get() == '52':
              window.after(52*1000, lambda : play_sound())

            if minute.get() == '53':
              window.after(53*60000, lambda : play_sound())

            if second.get() == '53':
              window.after(53*1000, lambda : play_sound())

            if minute.get() == '54':
              window.after(54*60000, lambda : play_sound())

            if second.get() == '54':
              window.after(54*1000, lambda : play_sound())

            if minute.get() == '55':
              window.after(55*60000, lambda : play_sound())

            if second.get() == '55':
              window.after(55*1000, lambda : play_sound())

            if minute.get() == '56':
              window.after(56*60000, lambda : play_sound())

            if second.get() == '56':
              window.after(56*1000, lambda : play_sound())

            if minute.get() == '57':
              window.after(57*60000, lambda : play_sound())

            if second.get() == '57':
              window.after(57*1000, lambda : play_sound())

            if minute.get() == '58':
              window.after(58*60000, lambda : play_sound())

            if second.get() == '58':
              window.after(58*1000, lambda : play_sound())

            if minute.get() == '59':
              window.after(59*60000, lambda : play_sound())

            if second.get() == '59':
              window.after(59*1000, lambda : play_sound())

            if minute.get() == '60':
              window.after(60*60000, lambda : play_sound())

            if second.get() == '60':
              window.after(60*1000, lambda : play_sound())

            if hour.get() == '' and minute.get() == '' and second.get() == '':
              showwarning("Shut&R!", "Please enter a invalid value!")

            showinfo('Shut&R', 'Time has been SET!')

            break

def what_button_will_do_r():
          while True:
            if hour.get() == '1':
              window.after(3600000, lambda : play_sound_r())

            if minute.get() == '1':
              window.after(60000, lambda : play_sound_r())

            if second.get() == '1':
              window.after(1000, lambda : play_sound_r())

            if hour.get() == '2':
              window.after(2*3600000, lambda : play_sound_r())

            if minute.get() == '2':
              window.after(2*60000, lambda : play_sound_r())

            if second.get() == '2':
              window.after(2*1000, lambda : play_sound_r())

            if hour.get() == '3':
              window.after(3*3600000, lambda : play_sound_r())

            if minute.get() == '3':
              window.after(3*60000, lambda : play_sound_r())

            if second.get() == '3':
              window.after(3*1000, lambda : play_sound_r())

            if hour.get() == '4':
              window.after(4*3600000, lambda : play_sound_r())

            if minute.get() == '4':
              window.after(4*60000, lambda : play_sound_r())

            if second.get() == '4':
              window.after(4*1000, lambda : play_sound_r())

            if hour.get() == '5':
              window.after(5*3600000, lambda : play_sound_r())

            if minute.get() == '5':
              window.after(5*60000, lambda : play_sound_r())

            if second.get() == '5':
              window.after(5*1000, lambda : play_sound_r())

            if hour.get() == '6':
              window.after(6*3600000, lambda : play_sound_r())

            if minute.get() == '6':
              window.after(6*60000, lambda : play_sound_r())

            if second.get() == '6':
              window.after(6*1000, lambda : play_sound_r())

            if hour.get() == '7':
              window.after(7*3600000, lambda : play_sound_r())

            if minute.get() == '7':
              window.after(7*60000, lambda : play_sound_r())

            if second.get() == '7':
              window.after(7*1000, lambda : play_sound_r())

            if hour.get() == '8':
              window.after(8*3600000, lambda : play_sound_r())

            if minute.get() == '8':
              window.after(8*60000, lambda : play_sound_r())

            if second.get() == '8':
              window.after(8*1000, lambda : play_sound_r())

            if hour.get() == '9':
              window.after(9*3600000, lambda : play_sound_r())

            if minute.get() == '9':
              window.after(9*60000, lambda : play_sound_r())

            if second.get() == '9':
              window.after(9*1000, lambda : play_sound_r())

            if hour.get() == '10':
              window.after(10*3600000, lambda : play_sound_r())

            if minute.get() == '10':
              window.after(10*60000, lambda : play_sound_r())

            if second.get() == '10':
              window.after(10*1000, lambda : play_sound_r())

            if hour.get() == '11':
              window.after(11*3600000, lambda : play_sound_r())

            if minute.get() == '11':
              window.after(11*60000, lambda : play_sound_r())

            if second.get() == '11':
              window.after(11*1000, lambda : play_sound_r())

            if hour.get() == '12':
              window.after(12*3600000, lambda : play_sound_r())

            if minute.get() == '12':
              window.after(12*60000, lambda : play_sound_r())

            if second.get() == '12':
              window.after(12*1000, lambda : play_sound_r())

            if hour.get() == '13':
              window.after(13*600000, lambda : play_sound_r())

            if minute.get() == '13':
              window.after(13*60000, lambda : play_sound_r())

            if second.get() == '13':
              window.after(13*1000, lambda : play_sound_r())

            if hour.get() == '14':
              window.after(14*3600000, lambda : play_sound_r())

            if minute.get() == '14':
              window.after(14*60000, lambda : play_sound_r())

            if second.get() == '14':
              window.after(14*1000, lambda : play_sound_r())

            if hour.get() == '15':
              window.after(15*3600000, lambda : play_sound_r())

            if minute.get() == '15':
              window.after(15*60000, lambda : play_sound_r())

            if second.get() == '15':
              window.after(15*1000, lambda : play_sound_r())

            if hour.get() == '16':
              window.after(16*3600000, lambda : play_sound_r())

            if minute.get() == '16':
              window.after(16*60000, lambda : play_sound_r())

            if second.get() == '16':
              window.after(16*1000, lambda : play_sound_r())

            if hour.get() == '17':
              window.after(17*3600000, lambda : play_sound_r())

            if minute.get() == '17':
              window.after(17*60000, lambda : play_sound_r())

            if second.get() == '17':
              window.after(17*1000, lambda : play_sound_r())

            if hour.get() == '18':
              window.after(18*3600000, lambda : play_sound_r())

            if minute.get() == '18':
              window.after(18*60000, lambda : play_sound_r())

            if second.get() == '18':
              window.after(18*1000, lambda : play_sound_r())

            if hour.get() == '19':
              window.after(19*3600000, lambda : play_sound_r())

            if minute.get() == '19':
              window.after(19*60000, lambda : play_sound_r())

            if second.get() == '19':
              window.after(19*1000, lambda : play_sound_r())

            if hour.get() == '20':
              window.after(20*3600000, lambda : play_sound_r())

            if minute.get() == '20':
              window.after(20*60000, lambda : play_sound_r())

            if second.get() == '20':
              window.after(20*1000, lambda : play_sound_r())

            if hour.get() == '21':
              window.after(21*3600000, lambda : play_sound_r())

            if minute.get() == '21':
              window.after(21*60000, lambda : play_sound_r())

            if second.get() == '21':
              window.after(21*1000, lambda : play_sound_r())

            if hour.get() == '22':
              window.after(22*3600000, lambda : play_sound_r())

            if minute.get() == '22':
              window.after(22*60000, lambda : play_sound_r())

            if second.get() == '22':
              window.after(22*1000, lambda : play_sound_r())

            if hour.get() == '23':
              window.after(23*3600000, lambda : play_sound_r())

            if minute.get() == '23':
              window.after(23*60000, lambda : play_sound_r())

            if second.get() == '23':
              window.after(23*1000, lambda : play_sound_r())

            if hour.get() == '24':
              window.after(24*3600000, lambda : play_sound_r())

            if minute.get() == '24':
              window.after(24*60000, lambda : play_sound_r())

            if second.get() == '24':
              window.after(24*1000, lambda : play_sound_r())

            if minute.get() == '25':
              window.after(25*60000, lambda : play_sound_r())

            if second.get() == '25':
              window.after(25*1000, lambda : play_sound_r())

            if minute.get() == '26':
              window.after(26*60000, lambda : play_sound_r())

            if second.get() == '26':
              window.after(26*1000, lambda : play_sound_r())

            if minute.get() == '27':
              window.after(27*60000, lambda : play_sound_r())

            if second.get() == '27':
              window.after(27*1000, lambda : play_sound_r())

            if minute.get() == '28':
              window.after(28*60000, lambda : play_sound_r())

            if second.get() == '28':
              window.after(28*1000, lambda : play_sound_r())

            if minute.get() == '29':
              window.after(29*60000, lambda : play_sound_r())

            if second.get() == '29':
              window.after(29*1000, lambda : play_sound_r())

            if minute.get() == '30':
              window.after(30*60000, lambda : play_sound_r())

            if second.get() == '30':
              window.after(30*1000, lambda : play_sound_r())

            if minute.get() == '31':
              window.after(31*60000, lambda : play_sound_r())

            if second.get() == '31':
              window.after(31*1000, lambda : play_sound_r())

            if minute.get() == '32':
              window.after(32*60000, lambda : play_sound_r())

            if second.get() == '32':
              window.after(32*1000, lambda : play_sound_r())

            if minute.get() == '33':
              window.after(33*60000, lambda : play_sound_r())

            if second.get() == '33':
              window.after(33*1000, lambda : play_sound_r())

            if minute.get() == '34':
              window.after(34*60000, lambda : play_sound_r())

            if second.get() == '34':
              window.after(34*1000, lambda : play_sound_r())

            if minute.get() == '35':
              window.after(35*60000, lambda : play_sound_r())

            if second.get() == '35':
              window.after(35*1000, lambda : play_sound_r())

            if minute.get() == '36':
              window.after(36*60000, lambda : play_sound_r())

            if second.get() == '36':
              window.after(36*1000, lambda : play_sound_r())

            if minute.get() == '37':
              window.after(37*60000, lambda : play_sound_r())

            if second.get() == '37':
              window.after(37*1000, lambda : play_sound_r())

            if minute.get() == '38':
              window.after(38*60000, lambda : play_sound_r())

            if second.get() == '38':
              window.after(38*1000, lambda : play_sound_r())

            if minute.get() == '39':
              window.after(39*60000, lambda : play_sound_r())

            if second.get() == '39':
              window.after(39*1000, lambda : play_sound_r())

            if minute.get() == '40':
              window.after(40*60000, lambda : play_sound_r())

            if second.get() == '40':
              window.after(40*1000, lambda : play_sound_r())

            if minute.get() == '41':
              window.after(41*60000, lambda : play_sound_r())

            if second.get() == '41':
              window.after(41*1000, lambda : play_sound_r())

            if minute.get() == '42':
              window.after(42*60000, lambda : play_sound_r())

            if second.get() == '42':
              window.after(42*1000, lambda : play_sound_r())

            if minute.get() == '43':
              window.after(43*60000, lambda : play_sound_r())

            if second.get() == '43':
              window.after(43*1000, lambda : play_sound_r())

            if minute.get() == '44':
              window.after(44*60000, lambda : play_sound_r())

            if second.get() == '44':
              window.after(44*1000, lambda : play_sound_r())

            if minute.get() == '45':
              window.after(45*60000, lambda : play_sound_r())

            if second.get() == '45':
              window.after(45*1000, lambda : play_sound_r())

            if minute.get() == '46':
              window.after(46*60000, lambda : play_sound_r())

            if second.get() == '46':
              window.after(46*1000, lambda : play_sound_r())

            if minute.get() == '47':
              window.after(47*60000, lambda : play_sound_r())

            if second.get() == '47':
              window.after(47*1000, lambda : play_sound_r())

            if minute.get() == '48':
              window.after(48*60000, lambda : play_sound_r())

            if second.get() == '48':
              window.after(48*1000, lambda : play_sound_r())

            if minute.get() == '49':
              window.after(49*60000, lambda : play_sound_r())

            if minute.get() == '49':
              window.after(49*1000, lambda : play_sound_r())

            if minute.get() == '50':
              window.after(50*60000, lambda : play_sound_r())

            if second.get() == '50':
              window.after(50*1000, lambda : play_sound_r())

            if second.get() == '51':
              window.after(3600000, lambda : play_sound_r())
              
            if minute.get() == '51':
              window.after(51*1000, lambda : play_sound_r())

            if minute.get() == '52':
              window.after(52*60000, lambda : play_sound_r())

            if second.get() == '52':
              window.after(52*1000, lambda : play_sound_r())

            if minute.get() == '53':
              window.after(53*60000, lambda : play_sound_r())

            if second.get() == '53':
              window.after(53*1000, lambda : play_sound_r())

            if minute.get() == '54':
              window.after(54*60000, lambda : play_sound_r())

            if second.get() == '54':
              window.after(54*1000, lambda : play_sound_r())

            if minute.get() == '55':
              window.after(55*60000, lambda : play_sound_r())

            if second.get() == '55':
              window.after(55*1000, lambda : play_sound_r())

            if minute.get() == '56':
              window.after(56*60000, lambda : play_sound_r())

            if second.get() == '56':
              window.after(56*1000, lambda : play_sound_r())

            if minute.get() == '57':
              window.after(57*60000, lambda : play_sound_r())

            if second.get() == '57':
              window.after(57*1000, lambda : play_sound_r())

            if minute.get() == '58':
              window.after(58*60000, lambda : play_sound_r())

            if second.get() == '58':
              window.after(58*1000, lambda : play_sound_r())

            if minute.get() == '59':
              window.after(59*60000, lambda : play_sound_r())

            if second.get() == '59':
              window.after(59*1000, lambda : play_sound_r())

            if minute.get() == '60':
              window.after(60*60000, lambda : play_sound_r())

            if second.get() == '60':
              window.after(60*1000, lambda : play_sound_r())

            if hour.get() == '' and minute.get() == '' and second.get() == '':
              showwarning("Shut&R!", "Please enter a invalid value!")

            showinfo('Shut&R', 'Time has been SET!')

            break

def what_button_will_do_s():
          while True:
            if hour.get() == '1':
              window.after(3600000, lambda : play_sound_s())

            if minute.get() == '1':
              window.after(60000, lambda : play_sound_s())

            if second.get() == '1':
              window.after(1000, lambda : play_sound_s())

            if hour.get() == '2':
              window.after(2*3600000, lambda : play_sound_s())

            if minute.get() == '2':
              window.after(2*60000, lambda : play_sound_s())

            if second.get() == '2':
              window.after(2*1000, lambda : play_sound_s())

            if hour.get() == '3':
              window.after(3*3600000, lambda : play_sound_s())

            if minute.get() == '3':
              window.after(3*60000, lambda : play_sound_s())

            if second.get() == '3':
              window.after(3*1000, lambda : play_sound_s())

            if hour.get() == '4':
              window.after(4*3600000, lambda : play_sound_s())

            if minute.get() == '4':
              window.after(4*60000, lambda : play_sound_s())

            if second.get() == '4':
              window.after(4*1000, lambda : play_sound_s())

            if hour.get() == '5':
              window.after(5*3600000, lambda : play_sound_s())

            if minute.get() == '5':
              window.after(5*60000, lambda : play_sound_s())

            if second.get() == '5':
              window.after(5*1000, lambda : play_sound_s())

            if hour.get() == '6':
              window.after(6*3600000, lambda : play_sound_s())

            if minute.get() == '6':
              window.after(6*60000, lambda : play_sound_s())

            if second.get() == '6':
              window.after(6*1000, lambda : play_sound_s())

            if hour.get() == '7':
              window.after(7*3600000, lambda : play_sound_s())

            if minute.get() == '7':
              window.after(7*60000, lambda : play_sound_s())

            if second.get() == '7':
              window.after(7*1000, lambda : play_sound_s())

            if hour.get() == '8':
              window.after(8*3600000, lambda : play_sound_s())

            if minute.get() == '8':
              window.after(8*60000, lambda : play_sound_s())

            if second.get() == '8':
              window.after(8*1000, lambda : play_sound_s())

            if hour.get() == '9':
              window.after(9*3600000, lambda : play_sound_s())

            if minute.get() == '9':
              window.after(9*60000, lambda : play_sound_s())

            if second.get() == '9':
              window.after(9*1000, lambda : play_sound_s())

            if hour.get() == '10':
              window.after(10*3600000, lambda : play_sound_s())

            if minute.get() == '10':
              window.after(10*60000, lambda : play_sound_s())

            if second.get() == '10':
              window.after(10*1000, lambda : play_sound_s())

            if hour.get() == '11':
              window.after(11*3600000, lambda : play_sound_s())

            if minute.get() == '11':
              window.after(11*60000, lambda : play_sound_s())

            if second.get() == '11':
              window.after(11*1000, lambda : play_sound_s())

            if hour.get() == '12':
              window.after(12*3600000, lambda : play_sound_s())

            if minute.get() == '12':
              window.after(12*60000, lambda : play_sound_s())

            if second.get() == '12':
              window.after(12*1000, lambda : play_sound_s())

            if hour.get() == '13':
              window.after(13*600000, lambda : play_sound_s())

            if minute.get() == '13':
              window.after(13*60000, lambda : play_sound_s())

            if second.get() == '13':
              window.after(13*1000, lambda : play_sound_s())

            if hour.get() == '14':
              window.after(14*3600000, lambda : play_sound_s())

            if minute.get() == '14':
              window.after(14*60000, lambda : play_sound_s())

            if second.get() == '14':
              window.after(14*1000, lambda : play_sound_s())

            if hour.get() == '15':
              window.after(15*3600000, lambda : play_sound_s())

            if minute.get() == '15':
              window.after(15*60000, lambda : play_sound_s())

            if second.get() == '15':
              window.after(15*1000, lambda : play_sound_s())

            if hour.get() == '16':
              window.after(16*3600000, lambda : play_sound_s())

            if minute.get() == '16':
              window.after(16*60000, lambda : play_sound_s())

            if second.get() == '16':
              window.after(16*1000, lambda : play_sound_s())

            if hour.get() == '17':
              window.after(17*3600000, lambda : play_sound_s())

            if minute.get() == '17':
              window.after(17*60000, lambda : play_sound_s())

            if second.get() == '17':
              window.after(17*1000, lambda : play_sound_s())

            if hour.get() == '18':
              window.after(18*3600000, lambda : play_sound_s())

            if minute.get() == '18':
              window.after(18*60000, lambda : play_sound_s())

            if second.get() == '18':
              window.after(18*1000, lambda : play_sound_s())

            if hour.get() == '19':
              window.after(19*3600000, lambda : play_sound_s())

            if minute.get() == '19':
              window.after(19*60000, lambda : play_sound_s())

            if second.get() == '19':
              window.after(19*1000, lambda : play_sound_s())

            if hour.get() == '20':
              window.after(20*3600000, lambda : play_sound_s())

            if minute.get() == '20':
              window.after(20*60000, lambda : play_sound_s())

            if second.get() == '20':
              window.after(20*1000, lambda : play_sound_s())

            if hour.get() == '21':
              window.after(21*3600000, lambda : play_sound_s())

            if minute.get() == '21':
              window.after(21*60000, lambda : play_sound_s())

            if second.get() == '21':
              window.after(21*1000, lambda : play_sound_s())

            if hour.get() == '22':
              window.after(22*3600000, lambda : play_sound_s())

            if minute.get() == '22':
              window.after(22*60000, lambda : play_sound_s())

            if second.get() == '22':
              window.after(22*1000, lambda : play_sound_s())

            if hour.get() == '23':
              window.after(23*3600000, lambda : play_sound_s())

            if minute.get() == '23':
              window.after(23*60000, lambda : play_sound_s())

            if second.get() == '23':
              window.after(23*1000, lambda : play_sound_s())

            if hour.get() == '24':
              window.after(24*3600000, lambda : play_sound_s())

            if minute.get() == '24':
              window.after(24*60000, lambda : play_sound_s())

            if second.get() == '24':
              window.after(24*1000, lambda : play_sound_s())

            if minute.get() == '25':
              window.after(25*60000, lambda : play_sound_s())

            if second.get() == '25':
              window.after(25*1000, lambda : play_sound_s())

            if minute.get() == '26':
              window.after(26*60000, lambda : play_sound_s())

            if second.get() == '26':
              window.after(26*1000, lambda : play_sound_s())

            if minute.get() == '27':
              window.after(27*60000, lambda : play_sound_s())

            if second.get() == '27':
              window.after(27*1000, lambda : play_sound_s())

            if minute.get() == '28':
              window.after(28*60000, lambda : play_sound_s())

            if second.get() == '28':
              window.after(28*1000, lambda : play_sound_s())

            if minute.get() == '29':
              window.after(29*60000, lambda : play_sound_s())

            if second.get() == '29':
              window.after(29*1000, lambda : play_sound_s())

            if minute.get() == '30':
              window.after(30*60000, lambda : play_sound_s())

            if second.get() == '30':
              window.after(30*1000, lambda : play_sound_s())

            if minute.get() == '31':
              window.after(31*60000, lambda : play_sound_s())

            if second.get() == '31':
              window.after(31*1000, lambda : play_sound_s())

            if minute.get() == '32':
              window.after(32*60000, lambda : play_sound_s())

            if second.get() == '32':
              window.after(32*1000, lambda : play_sound_s())

            if minute.get() == '33':
              window.after(33*60000, lambda : play_sound_s())

            if second.get() == '33':
              window.after(33*1000, lambda : play_sound_s())

            if minute.get() == '34':
              window.after(34*60000, lambda : play_sound_s())

            if second.get() == '34':
              window.after(34*1000, lambda : play_sound_s())

            if minute.get() == '35':
              window.after(35*60000, lambda : play_sound_s())

            if second.get() == '35':
              window.after(35*1000, lambda : play_sound_s())

            if minute.get() == '36':
              window.after(36*60000, lambda : play_sound_s())

            if second.get() == '36':
              window.after(36*1000, lambda : play_sound_s())

            if minute.get() == '37':
              window.after(37*60000, lambda : play_sound_s())

            if second.get() == '37':
              window.after(37*1000, lambda : play_sound_s())

            if minute.get() == '38':
              window.after(38*60000, lambda : play_sound_s())

            if second.get() == '38':
              window.after(38*1000, lambda : play_sound_s())

            if minute.get() == '39':
              window.after(39*60000, lambda : play_sound_s())

            if second.get() == '39':
              window.after(39*1000, lambda : play_sound_s())

            if minute.get() == '40':
              window.after(40*60000, lambda : play_sound_s())

            if second.get() == '40':
              window.after(40*1000, lambda : play_sound_s())

            if minute.get() == '41':
              window.after(41*60000, lambda : play_sound_s())

            if second.get() == '41':
              window.after(41*1000, lambda : play_sound_s())

            if minute.get() == '42':
              window.after(42*60000, lambda : play_sound_s())

            if second.get() == '42':
              window.after(42*1000, lambda : play_sound_s())

            if minute.get() == '43':
              window.after(43*60000, lambda : play_sound_s())

            if second.get() == '43':
              window.after(43*1000, lambda : play_sound_s())

            if minute.get() == '44':
              window.after(44*60000, lambda : play_sound_s())

            if second.get() == '44':
              window.after(44*1000, lambda : play_sound_s())

            if minute.get() == '45':
              window.after(45*60000, lambda : play_sound_s())

            if second.get() == '45':
              window.after(45*1000, lambda : play_sound_s())

            if minute.get() == '46':
              window.after(46*60000, lambda : play_sound_s())

            if second.get() == '46':
              window.after(46*1000, lambda : play_sound_s())

            if minute.get() == '47':
              window.after(47*60000, lambda : play_sound_s())

            if second.get() == '47':
              window.after(47*1000, lambda : play_sound_s())

            if minute.get() == '48':
              window.after(48*60000, lambda : play_sound_s())

            if second.get() == '48':
              window.after(48*1000, lambda : play_sound_s())

            if minute.get() == '49':
              window.after(49*60000, lambda : play_sound_s())

            if minute.get() == '49':
              window.after(49*1000, lambda : play_sound_s())

            if minute.get() == '50':
              window.after(50*60000, lambda : play_sound_s())

            if second.get() == '50':
              window.after(50*1000, lambda : play_sound_s())

            if second.get() == '51':
              window.after(3600000, lambda : play_sound_s())
              
            if minute.get() == '51':
              window.after(51*1000, lambda : play_sound_s())

            if minute.get() == '52':
              window.after(52*60000, lambda : play_sound_s())

            if second.get() == '52':
              window.after(52*1000, lambda : play_sound_s())

            if minute.get() == '53':
              window.after(53*60000, lambda : play_sound_s())

            if second.get() == '53':
              window.after(53*1000, lambda : play_sound_s())

            if minute.get() == '54':
              window.after(54*60000, lambda : play_sound_s())

            if second.get() == '54':
              window.after(54*1000, lambda : play_sound_s())

            if minute.get() == '55':
              window.after(55*60000, lambda : play_sound_s())

            if second.get() == '55':
              window.after(55*1000, lambda : play_sound_s())

            if minute.get() == '56':
              window.after(56*60000, lambda : play_sound_s())

            if second.get() == '56':
              window.after(56*1000, lambda : play_sound_s())

            if minute.get() == '57':
              window.after(57*60000, lambda : play_sound_s())

            if second.get() == '57':
              window.after(57*1000, lambda : play_sound_s())

            if minute.get() == '58':
              window.after(58*60000, lambda : play_sound_s())

            if second.get() == '58':
              window.after(58*1000, lambda : play_sound_s())

            if minute.get() == '59':
              window.after(59*60000, lambda : play_sound_s())

            if second.get() == '59':
              window.after(59*1000, lambda : play_sound_s())

            if minute.get() == '60':
              window.after(60*60000, lambda : play_sound_s())

            if second.get() == '60':
              window.after(60*1000, lambda : play_sound_s())

            if hour.get() == '' and minute.get() == '' and second.get() == '':
              showwarning("Shut&R!", "Please enter a invalid value!")

            showinfo('Shut&R', 'Time has been SET!')

            break

def what_button_will_do_h():
          while True:
            if hour.get() == '1':
              window.after(3600000, lambda : play_sound_h())

            if minute.get() == '1':
              window.after(60000, lambda : play_sound_h())

            if second.get() == '1':
              window.after(1000, lambda : play_sound_h())

            if hour.get() == '2':
              window.after(2*3600000, lambda : play_sound_h())

            if minute.get() == '2':
              window.after(2*60000, lambda : play_sound_h())

            if second.get() == '2':
              window.after(2*1000, lambda : play_sound_h())

            if hour.get() == '3':
              window.after(3*3600000, lambda : play_sound_h())

            if minute.get() == '3':
              window.after(3*60000, lambda : play_sound_h())

            if second.get() == '3':
              window.after(3*1000, lambda : play_sound_h())

            if hour.get() == '4':
              window.after(4*3600000, lambda : play_sound_h())

            if minute.get() == '4':
              window.after(4*60000, lambda : play_sound_h())

            if second.get() == '4':
              window.after(4*1000, lambda : play_sound_h())

            if hour.get() == '5':
              window.after(5*3600000, lambda : play_sound_h())

            if minute.get() == '5':
              window.after(5*60000, lambda : play_sound_h())

            if second.get() == '5':
              window.after(5*1000, lambda : play_sound_h())

            if hour.get() == '6':
              window.after(6*3600000, lambda : play_sound_h())

            if minute.get() == '6':
              window.after(6*60000, lambda : play_sound_h())

            if second.get() == '6':
              window.after(6*1000, lambda : play_sound_h())

            if hour.get() == '7':
              window.after(7*3600000, lambda : play_sound_h())

            if minute.get() == '7':
              window.after(7*60000, lambda : play_sound_h())

            if second.get() == '7':
              window.after(7*1000, lambda : play_sound_h())

            if hour.get() == '8':
              window.after(8*3600000, lambda : play_sound_h())

            if minute.get() == '8':
              window.after(8*60000, lambda : play_sound_h())

            if second.get() == '8':
              window.after(8*1000, lambda : play_sound_h())

            if hour.get() == '9':
              window.after(9*3600000, lambda : play_sound_h())

            if minute.get() == '9':
              window.after(9*60000, lambda : play_sound_h())

            if second.get() == '9':
              window.after(9*1000, lambda : play_sound_h())

            if hour.get() == '10':
              window.after(10*3600000, lambda : play_sound_h())

            if minute.get() == '10':
              window.after(10*60000, lambda : play_sound_h())

            if second.get() == '10':
              window.after(10*1000, lambda : play_sound_h())

            if hour.get() == '11':
              window.after(11*3600000, lambda : play_sound_h())

            if minute.get() == '11':
              window.after(11*60000, lambda : play_sound_h())

            if second.get() == '11':
              window.after(11*1000, lambda : play_sound_h())

            if hour.get() == '12':
              window.after(12*3600000, lambda : play_sound_h())

            if minute.get() == '12':
              window.after(12*60000, lambda : play_sound_s())

            if second.get() == '12':
              window.after(12*1000, lambda : play_sound_h())

            if hour.get() == '13':
              window.after(13*600000, lambda : play_sound_h())

            if minute.get() == '13':
              window.after(13*60000, lambda : play_sound_h())

            if second.get() == '13':
              window.after(13*1000, lambda : play_sound_h())

            if hour.get() == '14':
              window.after(14*3600000, lambda : play_sound_h())

            if minute.get() == '14':
              window.after(14*60000, lambda : play_sound_h())

            if second.get() == '14':
              window.after(14*1000, lambda : play_sound_h())

            if hour.get() == '15':
              window.after(15*3600000, lambda : play_sound_h())

            if minute.get() == '15':
              window.after(15*60000, lambda : play_sound_h())

            if second.get() == '15':
              window.after(15*1000, lambda : play_sound_h())

            if hour.get() == '16':
              window.after(16*3600000, lambda : play_sound_h())

            if minute.get() == '16':
              window.after(16*60000, lambda : play_sound_h())

            if second.get() == '16':
              window.after(16*1000, lambda : play_sound_h())

            if hour.get() == '17':
              window.after(17*3600000, lambda : play_sound_h())

            if minute.get() == '17':
              window.after(17*60000, lambda : play_sound_h())

            if second.get() == '17':
              window.after(17*1000, lambda : play_sound_h())

            if hour.get() == '18':
              window.after(18*3600000, lambda : play_sound_h())

            if minute.get() == '18':
              window.after(18*60000, lambda : play_sound_h())

            if second.get() == '18':
              window.after(18*1000, lambda : play_sound_h())

            if hour.get() == '19':
              window.after(19*3600000, lambda : play_sound_h())

            if minute.get() == '19':
              window.after(19*60000, lambda : play_sound_h())

            if second.get() == '19':
              window.after(19*1000, lambda : play_sound_h())

            if hour.get() == '20':
              window.after(20*3600000, lambda : play_sound_h())

            if minute.get() == '20':
              window.after(20*60000, lambda : play_sound_h())

            if second.get() == '20':
              window.after(20*1000, lambda : play_sound_h())

            if hour.get() == '21':
              window.after(21*3600000, lambda : play_sound_h())

            if minute.get() == '21':
              window.after(21*60000, lambda : play_sound_h())

            if second.get() == '21':
              window.after(21*1000, lambda : play_sound_h())

            if hour.get() == '22':
              window.after(22*3600000, lambda : play_sound_h())

            if minute.get() == '22':
              window.after(22*60000, lambda : play_sound_h())

            if second.get() == '22':
              window.after(22*1000, lambda : play_sound_h())

            if hour.get() == '23':
              window.after(23*3600000, lambda : play_sound_h())

            if minute.get() == '23':
              window.after(23*60000, lambda : play_sound_h())

            if second.get() == '23':
              window.after(23*1000, lambda : play_sound_h())

            if hour.get() == '24':
              window.after(24*3600000, lambda : play_sound_h())

            if minute.get() == '24':
              window.after(24*60000, lambda : play_sound_h())

            if second.get() == '24':
              window.after(24*1000, lambda : play_sound_h())

            if minute.get() == '25':
              window.after(25*60000, lambda : play_sound_h())

            if second.get() == '25':
              window.after(25*1000, lambda : play_sound_h())

            if minute.get() == '26':
              window.after(26*60000, lambda : play_sound_h())

            if second.get() == '26':
              window.after(26*1000, lambda : play_sound_h())

            if minute.get() == '27':
              window.after(27*60000, lambda : play_sound_h())

            if second.get() == '27':
              window.after(27*1000, lambda : play_sound_h())

            if minute.get() == '28':
              window.after(28*60000, lambda : play_sound_h())

            if second.get() == '28':
              window.after(28*1000, lambda : play_sound_h())

            if minute.get() == '29':
              window.after(29*60000, lambda : play_sound_h())

            if second.get() == '29':
              window.after(29*1000, lambda : play_sound_h())

            if minute.get() == '30':
              window.after(30*60000, lambda : play_sound_h())

            if second.get() == '30':
              window.after(30*1000, lambda : play_sound_h())

            if minute.get() == '31':
              window.after(31*60000, lambda : play_sound_h())

            if second.get() == '31':
              window.after(31*1000, lambda : play_sound_h())

            if minute.get() == '32':
              window.after(32*60000, lambda : play_sound_h())

            if second.get() == '32':
              window.after(32*1000, lambda : play_sound_h())

            if minute.get() == '33':
              window.after(33*60000, lambda : play_sound_h())

            if second.get() == '33':
              window.after(33*1000, lambda : play_sound_h())

            if minute.get() == '34':
              window.after(34*60000, lambda : play_sound_h())

            if second.get() == '34':
              window.after(34*1000, lambda : play_sound_h())

            if minute.get() == '35':
              window.after(35*60000, lambda : play_sound_h())

            if second.get() == '35':
              window.after(35*1000, lambda : play_sound_h())

            if minute.get() == '36':
              window.after(36*60000, lambda : play_sound_h())

            if second.get() == '36':
              window.after(36*1000, lambda : play_sound_h())

            if minute.get() == '37':
              window.after(37*60000, lambda : play_sound_h())

            if second.get() == '37':
              window.after(37*1000, lambda : play_sound_h())

            if minute.get() == '38':
              window.after(38*60000, lambda : play_sound_h())

            if second.get() == '38':
              window.after(38*1000, lambda : play_sound_h())

            if minute.get() == '39':
              window.after(39*60000, lambda : play_sound_h())

            if second.get() == '39':
              window.after(39*1000, lambda : play_sound_h())

            if minute.get() == '40':
              window.after(40*60000, lambda : play_sound_h())

            if second.get() == '40':
              window.after(40*1000, lambda : play_sound_h())

            if minute.get() == '41':
              window.after(41*60000, lambda : play_sound_h())

            if second.get() == '41':
              window.after(41*1000, lambda : play_sound_h())

            if minute.get() == '42':
              window.after(42*60000, lambda : play_sound_h())

            if second.get() == '42':
              window.after(42*1000, lambda : play_sound_h())

            if minute.get() == '43':
              window.after(43*60000, lambda : play_sound_h())

            if second.get() == '43':
              window.after(43*1000, lambda : play_sound_h())

            if minute.get() == '44':
              window.after(44*60000, lambda : play_sound_h())

            if second.get() == '44':
              window.after(44*1000, lambda : play_sound_h())

            if minute.get() == '45':
              window.after(45*60000, lambda : play_sound_h())

            if second.get() == '45':
              window.after(45*1000, lambda : play_sound_h())

            if minute.get() == '46':
              window.after(46*60000, lambda : play_sound_h())

            if second.get() == '46':
              window.after(46*1000, lambda : play_sound_h())

            if minute.get() == '47':
              window.after(47*60000, lambda : play_sound_h())

            if second.get() == '47':
              window.after(47*1000, lambda : play_sound_h())

            if minute.get() == '48':
              window.after(48*60000, lambda : play_sound_h())

            if second.get() == '48':
              window.after(48*1000, lambda : play_sound_h())

            if minute.get() == '49':
              window.after(49*60000, lambda : play_sound_h())

            if minute.get() == '49':
              window.after(49*1000, lambda : play_sound_h())

            if minute.get() == '50':
              window.after(50*60000, lambda : play_sound_h())

            if second.get() == '50':
              window.after(50*1000, lambda : play_sound_h())

            if second.get() == '51':
              window.after(3600000, lambda : play_sound_h())
              
            if minute.get() == '51':
              window.after(51*1000, lambda : play_sound_h())

            if minute.get() == '52':
              window.after(52*60000, lambda : play_sound_h())

            if second.get() == '52':
              window.after(52*1000, lambda : play_sound_h())

            if minute.get() == '53':
              window.after(53*60000, lambda : play_sound_h())

            if second.get() == '53':
              window.after(53*1000, lambda : play_sound_h())

            if minute.get() == '54':
              window.after(54*60000, lambda : play_sound_h())

            if second.get() == '54':
              window.after(54*1000, lambda : play_sound_h())

            if minute.get() == '55':
              window.after(55*60000, lambda : play_sound_h())

            if second.get() == '55':
              window.after(55*1000, lambda : play_sound_h())

            if minute.get() == '56':
              window.after(56*60000, lambda : play_sound_h())

            if second.get() == '56':
              window.after(56*1000, lambda : play_sound_h())

            if minute.get() == '57':
              window.after(57*60000, lambda : play_sound_h())

            if second.get() == '57':
              window.after(57*1000, lambda : play_sound_h())

            if minute.get() == '58':
              window.after(58*60000, lambda : play_sound_h())

            if second.get() == '58':
              window.after(58*1000, lambda : play_sound_h())

            if minute.get() == '59':
              window.after(59*60000, lambda : play_sound_h())

            if second.get() == '59':
              window.after(59*1000, lambda : play_sound_h())

            if minute.get() == '60':
              window.after(60*60000, lambda : play_sound_h())

            if second.get() == '60':
              window.after(60*1000, lambda : play_sound_h())

            if hour.get() == '' and minute.get() == '' and second.get() == '':
              showwarning("Shut&R!", "Please enter a invalid value!")

            showinfo('Shut&R', 'Time has been SET!')

            break



lable = ttk.Label(window, text="hour")
lable.pack()
lable.place(x=153, y=69)

lable2 = ttk.Label(window, text="minute")
lable2.pack()
lable2.place(x=217, y=69)

lable3 = ttk.Label(window, text="second")
lable3.pack()
lable3.place(x=287, y=69)

#        ___          ____    _____
# |   | [   ]  |  |  |    |  | 
# |   | [   ]  |  |  |    |  |
# |___| [   ]  |  |  |____|  |_____     
# |   | [   ]  |  |  | \           |
# |   | [___]  |__|  |  \     _____|


hour= Entry(window, width=4, fg='black', fon=('Arial 24', 11), textvariable="hour")
# x = column and y = row
hour.pack()
hour.place(x=150, y=92)

minute= Entry(window, width=4, fg='black', font=('Arial 24', 11))
# x = column and y = row
minute.pack()
minute.place(x=220, y=92)

second= Entry(window, width=4, fg='black', font=('Arial 24', 11))
# x = column and y = row
second.pack()
second.place(x=290, y=92)








sh_button = ttk.Button(window, text='Shutdown', command=what_button_will_do_sh)
sh_button.pack()
sh_button.place(x=120, y=150)

r_button = ttk.Button(window, text='Restart', command=what_button_will_do_r)
r_button.pack()
r_button.place(x=200, y=150)

s_button = ttk.Button(window, text='Sleep', command=what_button_will_do_s)
s_button.pack()
s_button.place(x=280, y=150)

h_button = ttk.Button(window, text='Hibernate', command=what_button_will_do_h)
h_button.pack()
h_button.place(x=200, y=180)




# def show_value_h():
#   lable.destroy()
#   lable2.destroy()
#   lable3.destroy()
#   hour.place(x=1600, y=900)
#   minute.place(x=1630, y=900)
#   second.place(x=16010, y=900)
#   sh_button.destroy()
#   r_button.destroy()
#   s_button.destroy()
#   lablehour = ttk.Label(window, text=hour.get(), font=('bold', 24))
#   lablehour.pack()
#   lablehour.place(x=240, y=120)




# def show_value_m():
#   lable.destroy()
#   lable2.destroy()
#   lable3.destroy()
#   hour.place(x=1600, y=900)
#   minute.place(x=1630, y=900)
#   second.place(x=16010, y=900)
#   sh_button.destroy()
#   r_button.destroy()
#   s_button.destroy()
#   lablehour = ttk.Label(window, text=minute.get(), font=('bold', 24))
#   lablehour.pack()
#   lablehour.place(x=240, y=120)


# def show_value_s():
#   lable.destroy()
#   lable2.destroy()
#   lable3.destroy()
#   hour.place(x=1600, y=900)
#   minute.place(x=1630, y=900)
#   second.place(x=16010, y=900)
#   sh_button.destroy()
#   r_button.destroy()
#   s_button.destroy()
#   lablehour = ttk.Label(window, text=second.get(), font=('bold', 24))
#   lablehour.pack()
#   lablehour.place(x=380, y=120)


# lable2 = ttk.Label(window, text="hour")
# lable2.pack()
# lable2.place(x=153, y=69)

# r_button = ttk.Button(window, text='Set Time', command=what_button_will_do_r)
# r_button.pack()
# r_button.place(x=200, y=150)

# hour2= Entry(window, width=4, fg='black', fon=('Arial 24', 11))
# # x = column and y = row
# hour2.pack(padx=10, pady=10)
# hour2.place(x=150, y=89)

# lable2 = ttk.Label(window, text="minute")
# lable2.pack()
# lable2.place(x=217, y=69)

# minute2= Entry(window, width=4, fg='black', font=('Arial 24', 11))
# # x = column and y = row
# minute2.pack(padx=10, pady=10)
# minute2.place(x=220, y=89)

# lable2 = ttk.Label(window, text="second")
# lable2.pack()
# lable2.place(x=287, y=69)

# second2= Entry(window, width=4, fg='black', font=('Arial 24', 11))
# # x = column and y = row
# second2.pack(padx=10, pady=10)
# second2.place(x=290, y=89)

# lable3 = ttk.Label(window, text="hour")
# lable3.pack()
# lable3.place(x=153, y=69)

# s_button = ttk.Button(window, text='Set Time', command=what_button_will_do_s)
# s_button.pack()
# s_button.place(x=200, y=150)

# hour3= Entry(window, width=4, fg='black', fon=('Arial 24', 11))
# # x = column and y = row
# hour3.pack(padx=10, pady=10)
# hour3.place(x=150, y=89)

# lable3 = ttk.Label(window, text="minute")
# lable3.pack()
# lable3.place(x=217, y=69)

# minute3= Entry(window, width=4, fg='black', font=('Arial 24', 11))
# # x = column and y = row
# minute3.pack(padx=10, pady=10)
# minute3.place(x=220, y=89)

# lable3 = ttk.Label(window, text="second")
# lable3.pack()
# lable3.place(x=287, y=69)

# second3= Entry(window, width=4, fg='black', font=('Arial 24', 11))
# # x = column and y = row
# second3.pack(padx=10, pady=10)
# second.place(x=290, y=89)

cancel_button = ttk.Button(window, text='Cancel', width=6, command=Cancel)
cancel_button.pack()
cancel_button.place(x=430, y=290)

def play_sound():
  os.system("shutdown /s /t 1")

def play_sound_r():
  os.system("shutdown /r /t 1")

def play_sound_s():
  ctypes.windll.powrprof.SetSuspendState(0, 1, 0)

def play_sound_h():
  os.system("shutdown.exe /h")

# def fade_in():
    # global alpha
    # alpha += 10
    # if alpha <= 255:
    #     label.config(fg=f'#{alpha:02x}{alpha:02x}{alpha:02x}')
    #     window.after(100, fade_in)
    
    # label = tk.Label(window, text="Time has been SET!", font=("Arial", 8), bg='blue')
    # label.pack()
    # label.place(x=190, y=290)
    # window.after(5000, label.destroy())

# alpha = 0


# lable = ttk.Label(window, text="What action do you want to happen?")
# lable.pack()
# lable.place(x=145, y=80)

# button = ttk.Button(window, text='Shut Down', command=button_of_sh)
# button.pack()
# button.place(x=120, y=120)

# button2 = ttk.Button(window, text='Restart', command=button_of_r)
# button2.pack()
# button2.place(x=205, y=120)


# button3 = ttk.Button(window, text='Sleep', command=button_of_s)
# button3.pack()
# button3.place(x=290, y=120)

showinfo('Shut&R', 'Limits:\n\nhour = 24\n\nminute = 60\n\nsecond = 60')

window.mainloop()