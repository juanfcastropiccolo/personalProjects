from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.page_width = self.w
        self.name = name

    def set_image(self):
        self.image("shirtificate.png", x=0, y=45)

    def header_title(self):
        self.set_font("Helvetica", "", 50)
        self.set_text_color(0, 0, 0)
        self.cell(0, 25, "CS50 Shirtificate", align="C")

    def print_name(self, name):
        self.set_font("Helvetica", "B", 40 )
        self.set_text_color(255, 255, 255)
        full_display = name + " took CS50"

        x = (self.w - self.get_string_width(full_display)) / 2
        y = 120

        self.text(x, y, full_display)


def get_name():
    return input("Name: ")


def main():
    try:
        name = get_name()

        pdf = PDF(name)
        pdf.add_page()

        pdf.set_image()
        pdf.header_title()

        pdf.print_name(name)
        pdf.output("shirtificate.pdf")

    except Exception as e:
        print("An error occurred:", str(e))




if __name__ == "__main__":
    main()
