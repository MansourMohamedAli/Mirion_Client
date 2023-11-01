from tkinter import *
import clientTest_async as mbc  # mbc = modbus client
import asyncio
import time

############################################################
#
#                       Modbus Setup
#
############################################################
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
client = mbc.setup_async_client('127.0.0.1', 502)
read_register = mbc.read_input_register


# Exit Button
def exit_application(window):
    window.destroy()


# Variables to store the mouse's initial position
start_x = 0
start_y = 0


# Function to handle the mouse button press event
def on_mouse_press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y


# Function to handle the mouse motion event
# def on_mouse_motion(event, window):
#     x = window.winfo_x() + (event.x - start_x)
#     y = window.winfo_y() + (event.y - start_y)
#     window.geometry(f"+{x}+{y}")


# Function to switch to Page 1
def show_page1(page1_frame, page2_frame=None):
    page2_frame.pack_forget()
    page1_frame.pack(fill="both"
                     , expand=True)


# Function to switch to Page 2
def show_page2(page1_frame, page2_frame=None):
    page1_frame.pack_forget()
    page2_frame.pack(fill="both"
                     , expand=True)


# Function to update the bar graph
def update_graph(data, bgraph, bframe):
    bgraph.delete("all")  # Clear the canvas
    bar_width = bframe.winfo_width()
    max_height = bframe.winfo_height()
    x = 0
    # Draw bars based on the data
    for value in data:
        # x1,y1 = top left, #x2,y2 = bot right, #Origin is Top Left
        bgraph.create_rectangle(x
                                , max_height
                                , x + bar_width
                                , max_height - value
                                , fill="black")
        x += bar_width + 10


def create_tics(num, sx, elx, esx, cont_h, labels, bgraph):
    gap = 0.01666666666 * cont_h
    linePos_y = gap
    label_ypos = gap - 10
    for i in range(0, len(labels)):
        bgraph.create_line(sx
                           , linePos_y
                           , elx
                           , linePos_y)
        labels[i].place(relx=0.75, y=label_ypos)
        bgraph.create_line(sx
                           , linePos_y + gap
                           , esx
                           , linePos_y + gap)

        linePos_y += (cont_h - len(labels) * gap) / (len(labels) + 1)
        label_ypos += (cont_h - len(labels) * gap) / (len(labels) + 1)


async def read_data():
    return await mbc.read_from_server(client, read_register)


async def run_mirion(data):
    ############################################################
    #
    #                 Base Window Properties
    #
    ############################################################
    window = Tk()
    # Window Title (Not Visible)
    window.title("Mirion")
    # Setting Size
    window.geometry("150x600")
    # Setting Color
    window.configure(bg="#A4D347")
    # Prevent resizing of X and Y
    # window.resizable(False, False)
    # Remove Border
    window.overrideredirect(True)

    # Bind mouse button press and motion events to the window
    # window.bind("<ButtonPress-1>", on_mouse_press)
    # window.bind("<B1-Motion>", on_mouse_motion)
    ############################################################
    #
    #                     PAGE 1
    #
    ############################################################
    # Initializing Frame Use same color as window.
    page1_frame = Frame(window, bg=window["bg"])
    # Show Page 1 and fill size of window
    page1_frame.pack(fill="both", expand=True)
    ############################################################
    #                    WIDGETS
    ############################################################
    page1_frame.grid_columnconfigure(0, weight=1)
    page1_frame.grid_rowconfigure(0, weight=1)
    page1_frame.grid_rowconfigure(1, weight=90)
    page1_frame.grid_rowconfigure(2, weight=1)
    page1_frame.grid_rowconfigure(3, weight=1)

    ############################################################
    #
    #                     BAR GRAPH
    #
    ############################################################
    barFrame = Frame(page1_frame, bg=window["bg"])
    barFrame.grid(row=1, column=0, sticky="nsew")

    barFrame.update()
    container_height = barFrame.winfo_height()
    container_width = barFrame.winfo_width()
    bar_Width = container_width / 3

    bar_graph = Canvas(barFrame, width=container_width / 3, height=container_height, bg=window["bg"],
                       highlightthickness=0)

    # x = [asyncio.run(read_data())]
    # asyncio.run(data_stream(x))
    # print(x)
    # update_graph([asyncio.run(read_data())])
    update_graph(data, bar_graph, barFrame)

    # Using Unicode characters for superscripts
    superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

    testLabel1 = Label(barFrame, text="10" + "6".translate(superscript), bg=window["bg"])
    testLabel2 = Label(barFrame, text="10" + "5".translate(superscript), bg=window["bg"])
    testLabel3 = Label(barFrame, text="10" + "4".translate(superscript), bg=window["bg"])
    testLabel4 = Label(barFrame, text="10" + "3".translate(superscript), bg=window["bg"])
    testLabel5 = Label(barFrame, text="10" + "2".translate(superscript), bg=window["bg"])
    testLabel6 = Label(barFrame, text="10" + "1".translate(superscript), bg=window["bg"])
    testLabel7 = Label(barFrame, text="10" + "0".translate(superscript), bg=window["bg"])

    label_list = [testLabel1, testLabel2, testLabel3, testLabel4, testLabel5, testLabel6, testLabel7]

    create_tics(7,  # Number of tic sections.
                5,  # starting x position of tic mark
                35,  # End x position of long tic mark
                25,  # End x position of short tic mark
                container_height,  # gap between long and short x tic mark
                label_list,
                bar_graph)

    bar_graph.place(relx=0.33)
    # Using Unicode characters for superscripts
    # superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    #
    # testLabel1 = Label(barFrame, text = "10"+"6".translate(superscript),bg = window["bg"])
    # testLabel2 = Label(barFrame, text = "10"+"5".translate(superscript),bg = window["bg"])
    # testLabel3 = Label(barFrame, text = "10"+"4".translate(superscript),bg = window["bg"])
    # testLabel4 = Label(barFrame, text = "10"+"3".translate(superscript),bg = window["bg"])
    # testLabel5 = Label(barFrame, text = "10"+"2".translate(superscript),bg = window["bg"])
    # testLabel6 = Label(barFrame, text = "10"+"1".translate(superscript),bg = window["bg"])
    # testLabel7 = Label(barFrame, text = "10"+"0".translate(superscript),bg = window["bg"])

    # ALARM LEVELS
    testLabel9 = Label(barFrame, text="10" + "6".translate(superscript), bg=window["bg"])
    # testLabel9.place(relx = 0.10)

    readoutFrame = Frame(page1_frame, bg=window["bg"])
    readoutFrame.grid(row=2, column=0, sticky="nsew")

    readoutFrame.update()
    container_height = readoutFrame.winfo_height()
    container_width = readoutFrame.winfo_width()

    readout = Canvas(readoutFrame, width=container_width,
                     height=container_height,
                     bg=window["bg"],
                     highlightthickness=0)
    readout_label = Label(readoutFrame, text="uCi/cc\n1.00E+00", bg=window["bg"], font=("Lucida Console", 16))
    # readout_label.pack(fill="both", expand = "True",anchor="n")
    readout_label.pack(anchor="n")

    ############################################################
    #
    #                       TITLE
    #
    ############################################################
    titleSection = Frame(page1_frame, bg=window["bg"])
    titleSection.grid(row=0, column=0, sticky="nsew")

    titleSection.grid_columnconfigure(0, weight=1)
    titleSection.grid_columnconfigure(1, weight=1)
    # titleSection.grid_columnconfigure(1,weight =1)
    # titleSection.grid_propagate(False)

    container_width = barFrame.winfo_width()

    titleLabel = Label(titleSection
                       , text="A Vol Act\n1 1R60A"
                       , font=("Lucida Console", 18)
                       , anchor="w"  # anchored west(left)
                       , bg=window["bg"])
    titleLabel.grid(row=0, column=0)

    titleBlackBar = Canvas(titleSection
                           , width=container_width - 10
                           , height=5, bg="black"
                           , highlightthickness=0)

    titleBlackBar.grid(row=1, column=0, sticky="e")

    ############################################################
    #
    #                       status
    #
    ############################################################
    statusFrame = Frame(page1_frame, bg="yellow")
    statusFrame.grid(row=3, column=0, sticky="nsew")

    statusFrame.grid_columnconfigure(0, weight=1)
    statusFrame.grid_columnconfigure(1, weight=1)
    statusFrame.grid_rowconfigure(0, weight=1)

    # statusFrame.grid_rowconfigure(0,weight =1)
    alarmStatusLabel = Label(statusFrame, text="ALARM\nNONE", font=("Lucida Console", 14), bg=window["bg"])
    alarmStatusLabel.grid(column=0, row=0, sticky="nsew")

    statLabel = Label(statusFrame, text="STATUS\nOK", font=("Lucida Console", 14), bg=window["bg"])
    statLabel.grid(column=1, row=0, sticky="nsew")

    window.mainloop()


async def main():
    data = await read_data()
    await run_mirion([data])


asyncio.run(main())

# Run main window
# if __name__ == "__main__":
#     asyncio.run(run_mirion([500]))
