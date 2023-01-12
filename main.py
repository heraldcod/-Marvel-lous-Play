from tkinter import Tk, Label, Button, PhotoImage, Radiobutton, IntVar
from get_char import RandomChars
from PIL import ImageTk
from urllib.request import urlopen
import time
# main function that is called when main play button is clicked


def main_submit_clicked():

  # function that is called when radio button is clicked

  def radio_button_clicked(value):
    label_char_question.destroy()

    for i in Radio_buttons:
      i.destroy()
    print(value)
    global count
    count = 0
    full_dict = RandomChars().generate_dict(value)
    print(full_dict)
    l = list(full_dict.keys())

    # function that is called to clear all the previous grids

    def clear_grids(c, b1, b2, answered, correct_answer, score, l55, lq):
      lq.destroy()
      b1.destroy()
      b2.destroy()
      if answered == correct_answer:
        label_answer = Label(window,
                             text=" Last Answer : Right ! ",
                             font=('Arial', 8, 'italic'),
                             fg='white',
                             bg='#ED1D24',
                             padx=10,
                             pady=10).place(x=450, y=350)
        score = score + 1
        print(score)

      else:

        label_answer = Label(window,
                             text=" Last Answer : Wrong ! ",
                             font=('Arial', 8, 'italic'),
                             fg='white',
                             bg='#ED1D24',
                             padx=10,
                             pady=10)
        label_answer.place(x=450, y=350)

      run_dict(c, score, l55, lq)

    # function that is called to generate pictures and options

    def run_dict(c, s, l55, lq):

      if c >= value:

        for ln in l55:
          ln.destroy()

        last_score = Label(window,
                           text="Your score \n" + str(s),
                           font=('Arial', 20, 'bold'),
                           fg='white',
                           bg='#ED1D24',
                           padx=10,
                           pady=10)
        last_score.place(x=300, y=150)

        last_label1 = Label(window,
                            text=" Please run the code to play again ",
                            font=('Arial', 10, 'bold'),
                            fg='white',
                            bg='#ED1D24',
                            padx=10,
                            pady=10)
        last_label1.place(x=265, y=275)

        return None
      else:
        count = c + 1

      try:

        imageUrl = full_dict[l[c]]
        u = urlopen(imageUrl)
        raw_data = u.read()
        u.close()
        photo = ImageTk.PhotoImage(data=raw_data)
        label15 = Label(image=photo)
        label15.image = photo
        l55.append(label15)
        label15.place(x=100, y=80)

        option1, option2 = RandomChars().get_options(l[c])
        print(option1, option2)

      except Exception:
        print('404 Not Found, Please run again')

      label_q = Label(window,
                      text="Who is this MARVEL character",
                      font=('Arial', 10, 'bold'),
                      fg='white',
                      bg='#ED1D24',
                      padx=10,
                      pady=10)
      label_q.place(x=450, y=100)
      time.sleep(0.3)
      dict_button12 = Radiobutton(window,
                                  text=option1,
                                  font=('Arial', 10, 'bold'),
                                  fg='white',
                                  bg='#ED1D24',
                                  activebackground='#ED1D24',
                                  activeforeground='green',
                                  indicator=0,
                                  padx=10,
                                  pady=10)
      dict_button22 = Radiobutton(window,
                                  text=option2,
                                  font=('Arial', 10, 'bold'),
                                  fg='white',
                                  bg='#ED1D24',
                                  activebackground='#ED1D24',
                                  activeforeground='green',
                                  indicator=0,
                                  padx=10,
                                  pady=10)
      dict_button12['command'] = lambda: clear_grids(
        count, dict_button12, dict_button22, option1, l[c
                                                        ], s, label55, label_q)
      dict_button22['command'] = lambda: clear_grids(
        count, dict_button12, dict_button22, option2, l[c
                                                        ], s, label55, label_q)
      dict_button12.place(x=450, y=180)
      dict_button22.place(x=450, y=230)

    run_dict(count, 0, label55, 0)

  main_submit_button.destroy()

  # prompt options to select number of chracters to play with

  label_char_question = Label(
    window,
    text=" How many MARVEL characters \n you need to play with ? ",
    font=('Arial', 10, 'bold'),
    fg='white',
    bg='#ED1D24',
    padx=30,
    pady=30)
  label_char_question.place(x=265, y=75)

  var = IntVar()
  Radio_buttons = []
  y = 180
  for index in [5, 10, 15, 20]:
    Radiobutton1 = Radiobutton(window,
                               text=str(index),
                               variable=var,
                               value=index,
                               command=lambda: radio_button_clicked(var.get()),
                               font=('Arial', 20, 'bold'),
                               fg='white',
                               bg='#ED1D24',
                               activebackground='#ED1D24',
                               activeforeground='green',
                               indicator=0,
                               padx=10,
                               pady=10)
    Radio_buttons.append(Radiobutton1)
    Radiobutton1.place(x=380, y=y)
    y += 50


window = Tk()
window.geometry("818x427")

window.title("  Powered by MARVEL API ")
global score
global label55
label55 = []
icon = PhotoImage(file="Marvel_logo.png")
window.iconphoto(True, icon)
window.config(background="#ED1D24")

# code to create main label of the game
label = Label(window,
              text="  'MARVEL'LOUS PLAY",
              font=('Arial', 20, 'bold'),
              fg='white',
              bg='#ED1D24',
              padx=20,
              pady=20).place(x=230, y=10)

main_submit_button = Button(window,
                            text="PLAY",
                            font=('Arial', 20, 'bold'),
                            command=main_submit_clicked)
main_submit_button.place(x=350, y=150)

window.mainloop()
