import tkinter
import tkinter.ttk as ttk

import colorama
colorama.init()

import math

class Application():

        def main(self):
                global window, title, a_field, b_field, c_field, a, b, c

                inputs_padding_y = 2
                buttons_padding_y = 10

                window = tkinter.Tk()
                window.geometry('600x400')
                window.title('Geometry School Helper | Get all info about a triangle!')
                ttk.Style().theme_use('clam')
                window.resizable(False, False)
                window.iconbitmap(r"ico.ico")

                title = tkinter.Label(text='Type here the size of triangle`s sides: ', font='Bellota')
                enter_button = tkinter.Button(text='Get info about a triangle', command=self.get_input, font='Bellota')
                clear_button = tkinter.Button(text='Clear', command=self.clear_entries, font='Bellota')

                a_field = tkinter.Entry()
                b_field = tkinter.Entry()
                c_field = tkinter.Entry()

                title.pack(), a_field.pack(pady=inputs_padding_y), b_field.pack(pady=inputs_padding_y), c_field.pack(pady=inputs_padding_y), enter_button.pack(pady=buttons_padding_y), clear_button.pack(pady=buttons_padding_y)

                window.mainloop()

        def get_input(self):
                global isExist, doesntExist, error
                a, b, c = str(a_field.get()), str(b_field.get()), str(c_field.get())

                if a == '' or b == '' or c == '':
                        error = tkinter.Label(text='Please fill out all fields!', fg='red', font='Bellota')
                        error.pack()

                print(colorama.Style.BRIGHT + colorama.Fore.GREEN + 'Got the input! OwO')

                if (float(a) + float(b)) >= float(c):
                        print(colorama.Style.BRIGHT + colorama.Fore.GREEN + 'Triangle exist!')

                        isExist = tkinter.Label(text='This triangle exist! ((a + b) > c)', font='Bellota', fg='green')
                        isExist.pack()

                        biggest_side = max(float(a), float(b), float(c))
                        smallest_side = min(float(a), float(b), float(c))
                        middle_side = float(biggest_side) - float(smallest_side)

                        if ((smallest_side ** 2 + middle_side ** 2) == biggest_side ** 2):
                                print(colorama.Style.BRIGHT + colorama.Fore.GREEN + 'This triangle is right OwO')
                                right_triangle = tkinter.Label(text='This triangle is right!', font='Bellota', fg='green')
                                right_triangle.pack()
                        else:
                                print(colorama.Style.BRIGHT + colorama.Fore.RED + 'This triangle is not right!')
                                right_triangle = tkinter.Label(text='This triangle is not right!', font='Bellota', fg='red')
                                right_triangle.pack()

                        if a == b and c != a and c != b:  
                                isosceles_triangle = tkinter.Label(text='This triangle is isosceles!', font='Bellota', fg='green')
                                isosceles_triangle.pack()
                        elif b == c and a != b and a != c:
                                isosceles_triangle = tkinter.Label(text='This triangle is isosceles!', font='Bellota', fg='green')
                                isosceles_triangle.pack()
                        elif c == a and b != a and b != c:
                                isosceles_triangle = tkinter.Label(text='This triangle is isosceles!', font='Bellota', fg='green')
                                isosceles_triangle.pack()
                        else:
                                isnot_isosceles_triangle = tkinter.Label(text='This triangle is not isosceles!', font='Bellota', fg='red')
                                isnot_isosceles_triangle.pack()

                        square = self.square(float(a), float(b), float(c))
                        square = math.floor(square)
                        square_lab = tkinter.Label(text=f'The square of the triangle is: {square}', font='Bellota', fg='green')
                        square_lab.pack()

                else:
                        doesntExist = tkinter.Label(text='This triangle does not exist! D: ((a + b) < c)', fg='red', font='Bellota')
                        doesntExist.pack()
                        print(colorama.Style.BRIGHT + colorama.Fore.RED + 'This triangle doesn`t exist! D:')

        def clear_entries(self):
                a_field.delete(0, tkinter.END)
                b_field.delete(0, tkinter.END)
                c_field.delete(0, tkinter.END)

        def max(self, a, b, c):
                if a > b:
                    if a > c:
                        return a
                elif a > c:
                        if a > b:
                            return a
                elif c > a:
                        if c > b:
                            return c
                elif b > a:
                        if b > c:
                            return b
                elif c > b:
                        if c > a:
                            return c
                elif b > c:
                        if b > a:
                            return b

        def min(self, a, b, c):
                if a < b:
                        if a < c:
                                return a
                elif a < c:
                        if a < b:
                            return a
                elif c < a:
                        if c < b:
                            return c
                elif b < a:
                        if b < c:
                            return b
                elif c < b:
                        if c < a:
                            return c
                elif b < c:
                        if b < a:
                            return b

        def square(self, a, b, c):
                p = (a + b + c) // 2
                s = (p*(p-a)*(p-b)*(p-c))**0.5
                return s

app = Application()
app.main()
