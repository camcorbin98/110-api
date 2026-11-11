from flask import Flask, jsonify, request

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

#GET /cohorts/71
@app.get("/cohorts/<int:cohort_number>")
def get_cohort_number(cohort_number):
    return jsonify({"cohort_number": cohort_number})

# GET /greet/xxxxx

@app.get("/greet/<string:student_name>")
def say_hi_to_student(student_name):
    return jsonify(f"Ey hello {student_name}")

# -------- PRODUCTS -------

products = [
    {
        "_id": 1,
        "name": "cake",
        "price": 25
    },
    {
        "_id": 2,
        "name": "ice-cream",
        "price": 5
    },
    {
        "_id": 3,
        "name": "cookie",
        "price": 3
    },
    {
        "_id": 4,
        "name": "chocolate",
        "price": 10
    },
]

# Get /api/products -> return the list fo products


@app.get("/api/products")
def get_products():
    return jsonify(products)

# GET /api/products/<4> -> return a product by id
@app.get("/api/products/<int:product_id>")
def get_product_by_id(product_id):
    # logic here
    for product in products:
        print(product)
        if product ["_id"] == product_id:
            return jsonify({
                "success": True,
                "message": "Product retrieved successfully",
                "data": product
            }), 200 # OK

    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404 #PAGE NOT FOUND

# POST /api/products -> Create a new product
@app.post("/api/products")
def create_product():
    #logic here
    new_product = request.get_json()
    print(new_product)

    new_product["_id"] = products[-1]["_id"]+1 #creating _id key and its value

    products.append(new_product)# pushing new product to the products list(variable)

    return jsonify({
        "success": True,
        "message": "product created successfully"
    }), 201


# PUT /api/products -> update a product by id
@app.put("/api/products/<int:product_id>")
def update_product_by_id(product_id):
    updated_product = request.get_json()
    
    for product in products:
        if product["_id"] == product_id:
            product["name"] = updated_product["name"]
            product["price"] = updated_product["price"]
            return jsonify({
                "success": True,
                "message": "Product updated successfully"
            }), 200 #OK

    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404


# DELETE /api/products/
@app.delete("/api/products/<int:product_id>")
def delete_product_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            products.remove(product)
            return jsonify({
                "success": True,
                "message": "Product deleted successfully"
            }), 200
    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404


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

# POST /api/coupons -> Create a new coupon

@app.post("/api/coupons")
def create_coupon():
    new_coupon = request.get_json(silent=True)

    if not isinstance(new_coupon, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    if "code" not in new_coupon or "discount" not in new_coupon:
        return jsonify({"error": "Code and discount are required"}), 400

    new_coupon["_id"] = max(
        (coupon["_id"] for coupon in coupons),
        default=0
    ) + 1

    coupons.append(new_coupon)

    return jsonify(new_coupon), 201


# GET /api/coupons/<id> -> Return coupon by ID

@app.get("/api/coupons/<int:id>")
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            return jsonify(coupon), 200

    return jsonify({
        "error": "Coupon not found"
    }), 404

@app.put("/api/coupons/<int:id>")
def update_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            updated_data = request.get_json(silent=True)

            if (not isinstance(updated_data, dict)
                    or not any(key in updated_data for key in ("code", "discount"))):
                return jsonify({
                    "error": "Provide a code or discount to update"
                }), 400

            code = updated_data.get("code", coupon["code"])
            discount = updated_data.get("discount", coupon["discount"])

            if (not isinstance(code, str) or not code.strip()
                    or isinstance(discount, bool)
                    or not isinstance(discount, (int, float))
                    or not 0 <= discount <= 100):
                return jsonify({
                    "error": "Provide a coupon code and a discount between 0 and 100"
                }), 400

            coupon["code"] = code.strip()
            coupon["discount"] = discount

            return jsonify(coupon), 200

    return jsonify({
        "error": "Coupon not found"
    }), 404

@app.delete("/api/coupons/<int:id>")
def delete_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            coupons.remove(coupon)

            return jsonify({
                "message": "Coupon deleted successfully"
            }), 200

    return jsonify({
        "error": "Coupon not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)