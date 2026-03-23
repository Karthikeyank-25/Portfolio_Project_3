# IMPORTING PACKAGES :
from tkinter import *
from PIL import Image, ImageDraw, ImageFont
import tkinter.filedialog

# FUNCTIONS :
def select_img():
    # GETTING WATERMARK TEXT :
    watermark = text_input.get()
    # GETTING FILE PATH OF IMAGE WHICH WE ADD WATERMARKER :
    filepath = tkinter.filedialog.askopenfilename()
    # OPENING THE IMAGE FILE :
    base = Image.open(filepath)
    # CONVERTING RGB IMAGE INTO RGBA FOR GETTING TRANSPARENCY :
    trans_img = base.convert("RGBA")
    # REDUCING TRANSPARENCY :
    change_img = Image.new("RGBA", trans_img.size, (255, 255, 255, 0))
    # GETTING IMAGE WIDTH, HEIGHT :
    width, height = trans_img.size
    # ADDING FONT SIZE, STYLE :
    my_font = ImageFont.truetype("arial.ttf", 30)
    # GETTING IMAGE FOR DRAWING :
    draw = ImageDraw.Draw(change_img)
    # SETTING DRAWING POSITION OF TEXT IN IMAGE :
    position = (width + 20 ,height - 50 )
    # DRAWING TEXT IN IMAGE :
    draw.text(position, watermark, fill=(255, 255, 255, 128),font=my_font)
    # PATH FOR SAVING IMAGE IN COMPUTER :
    export_path = tkinter.filedialog.asksaveasfilename(defaultextension=".jpg")
    # COMBINE BOTH IMAGES :
    combin = Image.alpha_composite(trans_img, change_img)
    # CONVERT BACK THE IMAGE INTO RGB IMAGE :
    img = combin.convert("RGB")
    # SAVING FILE IF PATH IS PROVIDED :
    if export_path:
        img.save(export_path)
        img.show()

# CREATING WINDOW :
window = Tk()
window.title("Watermark Adder")
window.minsize(800,400)

# LABEL :
label_1 = Label(text="Add your watermark here",font=("Courier",30,"bold"))
label_1.pack(pady=50)

# INPUT :
text_input = Entry(width=30,font=("Courier",10))
text_input.pack()

# BUTTON :
button = Button(text="Select Image", command=select_img, font=("Courier",10),width=20)
button.pack(pady=50)

# CLOSING WINDOW :
window.mainloop()