from tkinter import Tk, Label, Button, PhotoImage, Radiobutton, IntVar
from get_char import RandomChars
from PIL import ImageTk
from urllib.request import urlopen


def main_submit_clicked():

  def radio_button_clicked(value):
    label_char_question.grid_remove()

    for i in Radio_buttons:
      i.grid_remove()
    print(value)
    global count
    count = 0
    full_dict = RandomChars().generate_dict(value)
    print(full_dict)
    l = list(full_dict.keys())

    def clear_grids(c, b1, b2, answered, correct_answer, score, l55):

      b1.destroy()
      b2.destroy()
      if answered == correct_answer:
        label_answer = Label(window,
                             text=" Last Answer : Right ! ",
                             font=('Arial', 8, 'italic'),
                             fg='white',
                             bg='#ED1D24',
                             padx=10,
                             pady=10).grid(row=5, column=0)
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
        label_answer.grid(row=5, column=0)

      run_dict(c, score, l55)

    def run_dict(c, s, l55):

      if c >= value:

        for ln in l55:
          ln.grid_remove()

        last_score = Label(window,
                           text="Your score \n" + str(s),
                           font=('Arial', 20, 'bold'),
                           fg='white',
                           bg='#ED1D24',
                           padx=10,
                           pady=10)
        last_score.grid(row=2, column=0)

        last_label1 = Label(window,
                            text=" Please run the code to play again ",
                            font=('Arial', 10, 'bold'),
                            fg='white',
                            bg='#ED1D24',
                            padx=10,
                            pady=10)
        last_label1.grid(row=4, column=0)
        return None
      else:
        count = c + 1

      imageUrl = full_dict[l[c]]
      u = urlopen(imageUrl)
      raw_data = u.read()
      u.close()
      photo = ImageTk.PhotoImage(data=raw_data)
      label15 = Label(image=photo)
      label15.image = photo
      l55.append(label15)
      label15.grid(row=2, column=0)

      option1, option2 = RandomChars().get_options(l[c])
      print(option1, option2)

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
        count, dict_button12, dict_button22, option1, l[c], s, label55)
      dict_button22['command'] = lambda: clear_grids(
        count, dict_button12, dict_button22, option2, l[c], s, label55)
      dict_button12.grid(row=3, column=0)
      dict_button22.grid(row=4, column=0)

    run_dict(count, 0, label55)

  main_submit_button.grid_remove()
  label_char_question = Label(
    window,
    text=" How many MARVEL characters \n you need to play with ? ",
    font=('Arial', 10, 'bold'),
    fg='white',
    bg='#ED1D24',
    padx=30,
    pady=30)
  label_char_question.grid(row=2, column=0)

  var = IntVar()
  Radio_buttons = []
  n = 3
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
    Radiobutton1.grid(row=n, column=0)
    n += 1


window = Tk()
window.geometry("400x550")

window.title("  Powered by MARVEL API ")
global score
global label55
label55 = []
icon = PhotoImage(file="Marvel_logo.png")
window.iconphoto(True, icon)
window.config(background="#ED1D24")

label = Label(window,
              text="  'MARVEL'LOUS PLAY",
              font=('Arial', 20, 'bold'),
              fg='white',
              bg='#ED1D24',
              padx=20,
              pady=20).grid(row=1, column=0)

main_submit_button = Button(window,
                            text="PLAY",
                            font=('Arial', 20, 'bold'),
                            command=main_submit_clicked)
main_submit_button.grid(row=2, column=0)

window.mainloop()
