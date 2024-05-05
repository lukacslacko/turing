class Module:
    def __init__(self, name, children=[], **kwargs):
        self.kwargs = kwargs
        self.name = name
        self.children = children

    def lines(self, indent: int=0):
        kwargs = ", ".join(f"{k}={v}" for k, v in self.kwargs.items())
        result = [" "*indent + f"{self.name}({kwargs})" + (";" if not self.children else " {")]
        if self.children:
            for child in self.children:
                result += child.lines(indent+2)
            result += [" "*indent + "}"]
        return result

    def __str__(self):
        return "\n".join(self.lines())

    def __add__(self, other):
        return Module("union", children=[self, other])

    def __mul__(self, other):
        return Module("intersection", children=[self, other])

    def __sub__(self, other):
        return Module("difference", children=[self, other])

    def linear_extrude(self, **kwargs):
        return Module("linear_extrude", children=[self], **kwargs)

    def translate(self, v):
        return Module("translate", children=[self], v=v)

    def rotate(self, a, **kwargs):
        return Module("rotate", children=[self], a=a, **kwargs)

    def scale(self, v):
        return Module("scale", children=[self], v=v)

    def offset(self, r):
        return Module("offset", children=[self], r=r)


for module in ["sphere", "cylinder", "cube"]:
    globals()[module] = lambda module=module, **kwargs: Module(module, **kwargs)

scene = (cylinder(h=10, d=10) + sphere(d=10).translate([20,0,0])) - cube(r=5)
print(scene)
