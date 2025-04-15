from django.shortcuts import render, redirect
from .forms import ContentForm
from .utils import generate_title_suggestions

def home_view(request):
    """View for the home page with the content form."""
    form = ContentForm()
    return render(request, 'title_app/home.html', {'form': form})

def generate_titles_view(request):
    """View for generating and displaying title suggestions."""
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            # Save the request
            title_request = form.save()
            
            # Generate title suggestions
            content = title_request.content
            title_suggestions = generate_title_suggestions(content)
            
            # Pass the suggestions to the template
            return render(request, 'title_app/results.html', {
                'title_suggestions': title_suggestions,
                'content': content,
            })
    
    # If not a POST request or form is invalid, redirect to home
    return redirect('home')

