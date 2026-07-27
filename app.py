from flask import Flask, render_template

app = Flask(__name__)



house_colours = {"artemis": "green",
                 "helios": "red",
                 "athena": "purple",
                 "poseidon": "blue"}

house_pts = {"artemis": 0,
             "helios": 67676767,
             "athena": -99999,
             "poseidon": 67}

visited_houses = []

analysed_texts = []

@app.route("/")
def home():
    return "<h1>Hello world</h1>"

@app.route("/<text>")
def info(text):
    if text in house_colours.keys():
        house = text
        house_colour = house_colours[text]
        house_pt = house_pts[text]
        if house not in visited_houses:
            visited_houses.append(house)
        return render_template("index.html",
                               house=house,
                               house_colour=house_colour,
                               house_pt=house_pt,
                               visited_houses=visited_houses)

    else:
        length = len(text)
        num_digits = 0
        num_vowels = 0
        num_consonents = 0
        char_dict = {}
        if text != "favicon.ico":
            analysed_texts.append(text)
        for char in text:
            if char.isdigit():
                num_digits += 1

            elif char.isalpha():
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
                if char.lower() in "aeiou":
                    num_vowels += 1
                    
                else:
                    num_consonents += 1
        return render_template("analyse.html", text=text,
                               length=length,
                               num_digits=num_digits,
                               num_vowels=num_vowels,
                               num_consonents=num_consonents,
                               char_dict=char_dict,
                               analysed_texts = analysed_texts)
                
if __name__ == "__main__":
    app.run(port=5678)
    
