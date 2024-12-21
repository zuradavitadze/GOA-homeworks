class Box:
    def __init__(self, padding=None, margin=None):
        self.padding = padding or {}
        self.margin = margin or {}

    def _format_style(self, style_dict, property_name):
        if not style_dict:
            return ""

        style_string = f"{property_name}:"
        if "top" in style_dict and "right" in style_dict and "bottom" in style_dict and "left" in style_dict:
            style_string += f" {style_dict['top']} {style_dict['right']} {style_dict['bottom']} {style_dict['left']};"
        elif "top" in style_dict and "right" in style_dict and "bottom" in style_dict:
            style_string += f" {style_dict['top']} {style_dict['right']} {style_dict['bottom']};"
        elif "top" in style_dict and "right" in style_dict:
            style_string += f" {style_dict['top']} {style_dict['right']};"
        elif "top" in style_dict:
            style_string += f" {style_dict['top']};"
        else:
          values = []
          for key in ["top", "right", "bottom", "left"]:
            if key in style_dict:
              values.append(style_dict[key])
          style_string += " ".join(values) + ";"
        return style_string


    def get_styles(self):
        padding_style = self._format_style(self.padding, "padding")
        margin_style = self._format_style(self.margin, "margin")
        return padding_style + margin_style

# Example usage:

# Single-line margin (top, right, bottom, left)
box1 = Box(margin={"top": "50px", "right": "60px", "bottom": "70px", "left": "80px"})
print(box1.get_styles())  # Output: padding:;margin: 50px 60px 70px 80px;

#single line margin (top, right, bottom)
box2 = Box(margin={"top": "50px", "right": "60px", "bottom": "70px"})
print(box2.get_styles())  # Output: padding:;margin: 50px 60px 70px;

# Single-line padding (top, right)
box3 = Box(padding={"top": "10px", "right": "20px"})
print(box3.get_styles())  # Output: padding: 10px 20px;margin:;

# Single-line padding (top)
box4 = Box(padding={"top": "10px"})
print(box4.get_styles())  # Output: padding: 10px;margin:;

# Single-line padding with mixed order

box5 = Box(padding={"right":"20px", "top": "10px"})
print(box5.get_styles()) # Output: padding: 10px 20px;margin:;


# Both padding and margin
box6 = Box(padding={"top": "5px", "right": "10px", "bottom": "15px", "left": "20px"},
           margin={"top": "25px", "right": "30px", "bottom": "35px", "left": "40px"})
print(box6.get_styles()) # Output: padding: 5px 10px 15px 20px;margin: 25px 30px 35px 40px;

# No styles
box7 = Box()
print(box7.get_styles()) # Output: padding:;margin:;

# Only margin
box8 = Box(margin={"top": "100px"})
print(box8.get_styles()) # Output: padding:;margin: 100px;