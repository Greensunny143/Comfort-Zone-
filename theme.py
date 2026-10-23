
from pyscript import document
from datetime import datetime

# Student promo event
def check_student_offer(event):
    now = datetime.now()

    # Weekdays: Monday = 0, Friday = 4
    is_weekday = now.weekday() < 5
    is_student_hour = 14 <= now.hour < 17

    message = document.querySelector("#student-message")

    if is_weekday and is_student_hour:
        message.innerText = (
            "You qualify for 10% off signature lemonade! "
            "Please present a valid school ID."
        )
    else:
        message.innerText = (
            "The student offer runs on weekdays from "
            "2:00 PM to 5:00 PM. Please visit us during "
            "student hour and bring your school ID."
        )


# Promo order button events
def order_promo(event):
    promo_name = event.currentTarget.getAttribute("data-promo")

    message = document.querySelector("#promo-message")
    message.innerText = (
        f"You selected {promo_name}! "
        "Continue to the order page to complete your purchase."
    )

    # Navigate to the order page
    window_location = document.location
    window_location.href = "order.html"


# Loyalty card events
stamps = 0

def add_stamp(event):
    global stamps

    message = document.querySelector("#stamp-message")

    if stamps < 8:
        stamps += 1

    document.querySelector("#stamp-count").innerText = (
        f"{stamps} / 8"
    )

    if stamps == 8:
        message.innerText = (
            "Congratulations! You earned a free large drink!"
        )
    else:
        message.innerText = (
            f"Stamp added! You need {8 - stamps} more "
            "stamp(s) to earn your reward."
        )


def reset_stamps(event):
    global stamps
    stamps = 0

    document.querySelector("#stamp-count").innerText = "0 / 8"
    document.querySelector("#stamp-message").innerText = (
        "Your loyalty stamps have been reset."
    )


# Register event listeners
document.querySelector("#student-btn").addEventListener(
    "click", check_student_offer
)

for button in document.querySelectorAll(".order-promo"):
    button.addEventListener("click", order_promo)

document.querySelector("#stamp-btn").addEventListener(
    "click", add_stamp
)

document.querySelector("#reset-btn").addEventListener(
    "click", reset_stamps
)
