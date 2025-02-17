# from django.shortcuts import render, redirect
# from django.contrib import messages
# import mysql.connector as sql

# def signupaction(request):
#     if request.method == "POST":
#         # Connect to the database
#         try:
#             m = sql.connect(
#                 host="clue-db.mysql.database.azure.com",
#                 user="adminuser",
#                 passwd="Qwertyuiop21_",
#                 database='clue_db',
#                 auth_plugin='mysql_native_password'  # Added for compatibility with MySQL versions
#             )
#             cursor = m.cursor()
#         except sql.Error as e:
#             # Debugging the database connection
#             print(f"Database connection error: {e}")
#             messages.error(request, "Database connection failed: " + str(e))
#             return render(request, 'signup_page.html')

#         # Extracting form data
#         eid = request.POST.get("email", "").strip()
#         name = request.POST.get("fname", "").strip()
#         sid = request.POST.get("sid", "").strip()
#         pwd = request.POST.get("psw", "")
#         cpwd = request.POST.get("psw-repeat", "")

#         # Debug: Show the incoming data
#         print(f"Received data: email={eid}, name={name}, sid={sid}, password={pwd}")

#         # Validations
#         if not eid.endswith("@banasthali.in"):
#             messages.error(request, "Email must belong to the @banasthali.in domain.")
#             return render(request, 'signup_page.html', {
#                 'email': eid,
#                 'fname': name,
#                 'sid': sid
#             })

#         if pwd != cpwd:
#             messages.error(request, "Passwords do not match!")
#             return render(request, 'signup_page.html', {
#                 'email': eid,
#                 'fname': name,
#                 'sid': sid
#             })

#         # Check if the email already exists
#         try:
#             cursor.execute("SELECT * FROM student WHERE email = %s", (eid,))
#             if cursor.fetchone():
#                 messages.error(request, "User with this email already exists. Please use a different email.")
#                 return render(request, 'signup_page.html', {
#                     'email': eid,
#                     'fname': name,
#                     'sid': sid
#                 })
#         except sql.Error as e:
#             # Debugging the email-check query
#             print(f"Email-check query error: {e}")
#             messages.error(request, "Error checking email: " + str(e))
#             return render(request, 'signup_page.html', {
#                 'email': eid,
#                 'fname': name,
#                 'sid': sid
#             })

#         # Insert the new user into the database
#         try:
#             query = "INSERT INTO student (student_id, name, email, password) VALUES (%s, %s, %s, %s)"
#             cursor.execute(query, (sid, name, eid, pwd))
#             m.commit()  # Ensure data is flushed to the database
#             # Debug: Confirm successful insertion
#             print("User inserted successfully.")
#             messages.success(request, "Sign up successful! Please log in.")
#             return redirect('/login/')  # Redirect to the login page after successful signup
#         except sql.Error as e:
#             # Debugging the insertion query
#             print(f"Insert query error: {e}")
#             messages.error(request, "Error during signup: " + str(e))
#             return render(request, 'signup_page.html', {
#                 'email': eid,
#                 'fname': name,
#                 'sid': sid
#             })
#         finally:
#             cursor.close()
#             m.close()

#     # Render the signup page for GET requests
#     return render(request, 'signup_page.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError

def signupaction(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        name = request.POST.get("fname", "").strip()
        student_id = request.POST.get("sid", "").strip()
        password = request.POST.get("psw", "")
        confirm_password = request.POST.get("psw-repeat", "")

        # Ensure all fields are filled
        if not (email and name and student_id and password and confirm_password):
            return render_signup_page(request, email, name, student_id, "All fields are required!")

        # Check if passwords match
        if password != confirm_password:
            return render_signup_page(request, email, name, student_id, "❌ Passwords do not match!")

        # Validate email domain
        if not email.endswith("@banasthali.in"):
            return render_signup_page(request, email, name, student_id, "Email must be from @banasthali.in domain.")

        # Check if email already exists
        if Student.objects.filter(email=email).exists():
            return render_signup_page(request, email, name, student_id, "This email is already registered.")

        # Check if student ID already exists
        if Student.objects.filter(student_id=student_id).exists():
            return render_signup_page(request, email, name, student_id, "Student ID already exists.")

        try:
            # Securely hash the password before storing
            hashed_password = make_password(password)
            student = Student(student_id=student_id, name=name, email=email, password=hashed_password)
            student.save()

            # Add a success message for the login page
            messages.success(request, "✅ Signup successful! Please log in.")

            return redirect("login")  # Redirect to login page
        
        except ValidationError as e:
            return render_signup_page(request, email, name, student_id, f"Validation error: {e}")
        
        except Exception as e:
            return render_signup_page(request, email, name, student_id, "Something went wrong. Please try again.")

    return render(request, "signup_page.html")


def profileview(request):
    student_id = request.session.get('sid')
    if not student_id:
        messages.error(request, "You must log in first!")
        return redirect("login")

    student = Student.objects.filter(student_id=student_id).first()
    
    if not student:
        messages.error(request, "User not found. Please log in again.")
        return redirect("login")

    return render(request, "profile.html", {
        "name": student.name,
        "email": student.email
    })


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        request.session.flush()
        messages.success(request, "You have been logged out successfully.")
    return redirect("login")


# Reusable function for rendering signup page with errors
def render_signup_page(request, email, name, student_id, error_message):
    messages.error(request, error_message)
    return render(request, "signup_page.html", {
        'email': email,
        'fname': name,
        'sid': student_id
    })


def check_email(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        email = data.get("email", "").strip()
        exists = Student.objects.filter(email=email).exists()
        return JsonResponse({"exists": exists})
    return JsonResponse({"error": "Invalid request"}, status=400)
