from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def landing_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ReviewForm()

    return render(request, 'landing_page.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')


def submit_review(request):
    if request.method == 'POST':
        # Process the form submission and save the review data
        # ...

        # Send email notification
        subject = 'New Review Submitted'
        message = 'A new review has been submitted.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['shegebeats@gmail.com']
        html_message = render_to_string('review_email.html', {
            'name': Review.name,
            'email': Review.email,
            'rating': Review.rating,
            'review_text': Review.review_text,
        })
        send_mail(subject, message, from_email, recipient_list, html_message=html_message)
        
        return redirect('thank_you_page')  # Redirect to a thank you page

    # 

