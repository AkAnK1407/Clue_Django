# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.db import connection
# from login.models import Student  # Import the Student model


# def loginaction(request):
#     if request.method == 'POST':
#         email = request.POST.get('uname')
#         password = request.POST.get('psw')

#         with connection.cursor() as cursor:
#             # Check if the email exists
#             cursor.execute("SELECT password FROM student WHERE email = %s", [email])
#             result = cursor.fetchone()

#         if result:
#             db_password = result[0]
#             if db_password == password:
#                 # Store user details in the session
#                 request.session['user_email'] = email
#                 # Redirect to the profile page
#                 return redirect('profile')
#             else:
#                 messages.error(request, "Incorrect password.")
#         else:
#             messages.error(request, "Email does not exist.")

#     return render(request, 'login_page.html')


# def profileview(request):
#     # Check if the user is logged in
#     user_email = request.session.get('user_email')
#     if not user_email:
#         messages.error(request, "Please log in to access your profile.")
#         return redirect('login')

#     with connection.cursor() as cursor:
#         # Fetch the user's name and email
#         cursor.execute("SELECT name, email FROM student WHERE email = %s", [user_email])
#         result = cursor.fetchone()

#     if result:
#         user_name, email = result
#         context = {
#             'username': user_name,
#             'email': email,
#         }
#         return render(request, 'profile.html', context)
#     else:
#         messages.error(request, "User not found.")
#         return redirect('login')


from django.shortcuts import render, redirect
from django.contrib import messages
import json
from django.contrib.auth.hashers import check_password
from django.db import connections
from signup.models import Student  # Import auth_student model from signup app 



def loginaction(request):
    if request.method == "POST":
        email = request.POST.get("uname", "").strip()
        password = request.POST.get("psw", "")

        if not email or not password:
            messages.error(request, "Both email and password are required!")
            return render(request, "login_page.html")

        try:
            # Fetch student using Django ORM instead of raw SQL
            student = Student.objects.filter(email=email).first()

            if student:
                # Check hashed password
                if student.verify_password(password):
                    request.session["user_email"] = student.email
                    request.session["user_name"] = student.name
                    request.session["sid"] = student.student_id  # Store student ID in session

                    messages.success(request, "Login successful!")
                    return redirect("profile")  # Redirect to profile page
                else:
                    messages.error(request, "Incorrect password!")
            else:
                messages.error(request, "Email does not exist!")

        except Exception as e:
            messages.error(request, f"Database error: {str(e)}")

    return render(request, "login_page.html")


def profileview(request):
    # Ensure user is logged in by checking session
    student_id = request.session.get("sid")
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
    if request.session.get("sid"):
        request.session.flush()  # Clear all session data
        messages.success(request, "You have been logged out successfully.")

    return redirect("login")

from django.http import JsonResponse
from django.contrib.auth import authenticate

def check_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("username")
        password = data.get("password")

        student = Student.objects.filter(email=email).first()
        if student and student.verify_password(password):
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "failed", "message": "Invalid credentials"})

    return JsonResponse({"error": "Invalid request"}, status=400)
