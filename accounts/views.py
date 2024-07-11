from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def google_analyz(request):
    from .analyz import get_google_links,math_decide,scrape_paragraphs_from_multiple_urls, contains_crime

    province_or_state = "Cape Town"
    place = "site c"
    query = f"crime in {place} {province_or_state}"
    num_results = 10  # Number of results you want to retrieve

    # Get Google links related to the crime query
    urls = get_google_links(query, num_results)

    valid_urls = []
    for url in urls:
        if "tripadvisor" not in url:
            valid_urls.append(url)
        else:
            print(f"Removed TripAdvisor link: {url}")

    # Scrape paragraphs from the valid URLs
    paragraphs = scrape_paragraphs_from_multiple_urls(valid_urls)

    # Ensure paragraphs is iterable and handle empty case
    if not paragraphs:
        all_text = ""
    else:
        # Combine paragraphs into a single text string
        try:
            all_text = " ".join(paragraphs)
        except TypeError as e:
            print(f"Error joining paragraphs: {e}")
            all_text = ""

    # Analyze the text for crime-related words
    word = contains_crime(all_text)

    v = math_decide(word)
    print(v)

    # Optionally, return a response or render a template
    return render(request,'home.html')


