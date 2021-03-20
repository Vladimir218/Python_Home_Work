from tkinter import Tk, Canvas


class TrafficLight(Tk, Canvas):

    def __init__(self):
        super().__init__()
        self.__color = {"red": 7, "yellow": 2, "green": 5}
        self.title("Светофор")
        self.c = Canvas(self, width=110, height=310, bg="black")
        self.g = self.c.create_oval(10, 210, 100, 300, fill="gray")
        self.y = self.c.create_oval(10, 110, 100, 200, fill="gray")
        self.r = self.c.create_oval(10, 10, 100, 100, fill="gray")
        self.c.pack()
        self.position_traffic_light = 0
        self.after(0, self.running)

    def running(self):
        if self.position_traffic_light == 0:
            self.position_traffic_light = 1
            self.c.itemconfigure(self.g, fill="gray")
            self.c.itemconfigure(self.y, fill="gray")
            self.c.itemconfigure(self.r, fill="red")
            self.after(self.__color["red"] * 1000, self.running)
        elif self.position_traffic_light == 1:
            self.position_traffic_light = 2
            self.c.itemconfigure(self.g, fill="gray")
            self.c.itemconfigure(self.r, fill="gray")
            self.c.itemconfigure(self.y, fill="yellow")
            self.after(self.__color["yellow"] * 1000, self.running)
        elif self.position_traffic_light == 2:
            self.position_traffic_light = 0
            self.c.itemconfigure(self.g, fill="green")
            self.c.itemconfigure(self.r, fill="gray")
            self.c.itemconfigure(self.y, fill="gray")
            self.after(self.__color["green"] * 1000, self.running)


tl = TrafficLight()
tl.mainloop()
