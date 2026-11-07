from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/say-hi")
def function_to_say_hi():
    return jsonify("Hello cohort 71")


@app.get("/say-boo")
def function_to_say_boo():
    return jsonify("Say Boo")


students_cohort_71 = ("Cameron", "Angelina", "Noah", "Isaac", "Andy")

@app.get("/students-71")
def get_students_71():
    return jsonify({"students": students_cohort_71})


course_information = {
    "course_name": "APIs with Python and Flask",
    "sessions": 4,
    "description": "Introduction to APIs and endpoints using Python and Flask"
}

@app.get("/course-information")
def get_course_information():
    return jsonify({"course information": course_information})


@app.get("/user")
def get_user():
    return jsonify({
        "name": "Cameron",
        "role": "Student",
        "is_active": True,
        "favorite_technologies": ["Python", "JavaScript", "React"]
    })


# -------------Coupons-----------------

coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]


@app.get("/api/coupons")
def get_coupons():
    return jsonify(coupons)


@app.get("/api/coupons/count")
def get_coupons_count():
    return jsonify({"count": len(coupons)})


if __name__ == "__main__":
    app.run(debug=True)