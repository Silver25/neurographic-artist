from django.shortcuts import render
from django.contrib import messages
from .forms import NewsletterForm

# Create your views here.
def index(request):
    """
    Renders the Home page
    """

    if request.method == "POST":
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.add_message(request, messages.SUCCESS, "Your request for newsletter was send! You can soon expect news from us.")

    newsletter_form = NewsletterForm()


    return render(
        request,
        "home/index.html",
        {
            "newsletter_form": newsletter_form
        },
    )
