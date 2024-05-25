# views.py
from django.shortcuts import render, redirect

def agregasi(event_id):
    return f"Agregasi data untuk event ID: {event_id}"

def page_event(request):
    event = {
        "name": "Tech Conference 2025",
        "description": "Join us for an exciting tech conference covering the latest trends in technology and innovation.",
        "date": "January 1, 2025",
        "time": "6:00 PM - 10:00 PM",
        "location": "123 Event Street, Event City"
    }
    
    tickets = [
        {
            "id": 1,
            "title": "Seminar Only",
            "description": "Access to all seminar sessions.",
            "price": 50.00,
            "available": 100
        },
        {
            "id": 2,
            "title": "Workshop Only",
            "description": "Access to all workshop sessions.",
            "price": 75.00,
            "available": 50
        },
        {
            "id": 3,
            "title": "Full Package",
            "description": "Access to all seminar and workshop sessions.",
            "price": 120.00,
            "available": 30
        },
    ]

    context = {
        "event": event,
        "tickets": tickets
    }
    return render(request, "app_purchasing/event.html", context)

def page_checkout(request):
    if request.method == 'POST':
        selected_tickets = request.POST.get('selected_tickets')
        # Lakukan proses checkout dengan tiket yang dipilih
        return render(request, "app_purchasing/checkout.html", {"selected_tickets": selected_tickets})
    return redirect('page_event')
