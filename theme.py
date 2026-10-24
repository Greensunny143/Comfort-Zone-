from pyscript import document, window
from datetime import datetime
import asyncio

# Student promo event
def check_student_offer(event=None):
    now = datetime.now()

    # Weekdays: Monday = 0, Friday = 4
    is_weekday = now.weekday() < 5
    is_student_hour = 14 <= now.hour < 17

    message = document.querySelector("#student-message")
    if not message:
        return

    if is_weekday and is_student_hour:
        message.innerText = (
            "🎉 You qualify for 10% off signature lemonade! "
            "Please present a valid school ID at the counter."
        )
        message.style.color = "var(--ok)"
    else:
        current_time_str = now.strftime("%I:%M %p")
        day_name = now.strftime("%A")
        message.innerText = (
            f"It's currently {day_name}, {current_time_str}. "
            "The student offer runs on weekdays from 2:00 PM to 5:00 PM. "
            "Visit us during student hour with your school ID!"
        )
        message.style.color = "var(--pink)"


# Promo order button events
def order_promo(event):
    btn = event.currentTarget or event.target
    promo_name = btn.getAttribute("data-promo") or "Selected Promo"

    message = document.querySelector("#promo-message")
    if message:
        message.innerText = (
            f"✓ You selected {promo_name}! "
            "Redirecting to the order page..."
        )
        message.style.display = "block"

    async def redirect():
        await asyncio.sleep(1)
        window.location.href = "order.html"

    asyncio.ensure_future(redirect())


# Loyalty card events
stamps = 0

def add_stamp(event=None):
    global stamps

    message = document.querySelector("#stamp-message")
    count_el = document.querySelector("#stamp-count")

    if stamps < 8:
        stamps += 1

    if count_el:
        count_el.innerText = f"{stamps} / 8"

    if message:
        if stamps == 8:
            message.innerText = (
                "🎉 Congratulations! You earned a free large drink! "
                "Show this at the counter to claim."
            )
            message.style.color = "var(--ok)"
        else:
            message.innerText = (
                f"Stamp added! You need {8 - stamps} more "
                "stamp(s) to earn your free reward."
            )
            message.style.color = "var(--pink)"


def reset_stamps(event=None):
    global stamps
    stamps = 0

    count_el = document.querySelector("#stamp-count")
    if count_el:
        count_el.innerText = "0 / 8"

    message = document.querySelector("#stamp-message")
    if message:
        message.innerText = "Your loyalty stamps have been reset."
        message.style.color = "var(--muted)"


# Register event listeners safely with element verification
student_btn = document.querySelector("#student-btn")
if student_btn:
    student_btn.addEventListener("click", check_student_offer)

for button in document.querySelectorAll(".order-promo"):
    button.addEventListener("click", order_promo)

stamp_btn = document.querySelector("#stamp-btn")
if stamp_btn:
    stamp_btn.addEventListener("click", add_stamp)

reset_btn = document.querySelector("#reset-btn")
if reset_btn:
    reset_btn.addEventListener("click", reset_stamps)
