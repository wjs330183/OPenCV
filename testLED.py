import gpio3

g = gpio3.LinuxGPIO(gpio3.mainline_sunxi_pin("PG11"))
g.direction
