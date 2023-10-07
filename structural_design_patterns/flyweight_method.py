"""
The Flyweight design pattern is a structural pattern that is used to reduce memory usage or 
computational costs by sharing as much as possible with related objects. It's particularly useful 
when you have a large number of objects that are similar and can share some common state. 
This pattern is commonly used in situations where a large number of similar objects need to be created, 
but the cost of creating and maintaining each object individually would be high.
"""


class CharacterStyle:
    def __init__(self, font_family, font_size, bold=False, italic=False):
        self.font_family = font_family
        self.font_size = font_size
        self.bold = bold
        self.italic = italic

    def render(self, text):
        style = ""
        if self.bold:
            style += "bold "
        if self.italic:
            style += "italic "
        style += f"{self.font_size}px {self.font_family}"
        print(f"Rendering '{text}' in style: {style}")


class CharacterStyleFactory:
    _styles = {}

    def get_style(self, font_family, font_size, bold=False, italic=False):
        key = (font_family, font_size, bold, italic)
        if key not in self._styles:
            self._styles[key] = CharacterStyle(font_family, font_size, bold, italic)
        return self._styles[key]


class TextEditor:
    def __init__(self, character_style_factory):
        self.character_style_factory = character_style_factory
        self.characters = []

    def add_character(self, text, font_family, font_size, bold=False, italic=False):
        style = self.character_style_factory.get_style(font_family, font_size, bold, italic)
        self.characters.append((text, style))

    def render_text(self):
        for text, style in self.characters:
            style.render(text)


if __name__ == "__main__":
    style_factory = CharacterStyleFactory()
    editor = TextEditor(style_factory)

    editor.add_character("Hello", "Arial", 12, True, False)
    editor.add_character(" ", "Times New Roman", 14, False, True)
    editor.add_character("World!", "Arial", 12, True, True)

    editor.render_text()
