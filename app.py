from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def cars():

    cars = [
        {"brand": "BMW", "year": 2020},
        {"brand": "Audi", "year": 2018},
        {"brand": "Tesla", "year": 2022},
        {"brand": "Toyota", "year": 2016},
        {"brand": "Kia", "year": 2019}
    ]

    newest = max(cars, key=lambda x: x["year"])
    oldest = min(cars, key=lambda x: x["year"])

    return render_template(
        "index.html",
        cars=cars,
        newest=newest,
        oldest=oldest
    )


if __name__ == "__main__":
    app.run(debug=True)
