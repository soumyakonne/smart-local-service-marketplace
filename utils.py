import re
def format_price(price):
    """
    Format price values consistently.
    Handles numeric values and strings like '20/km'.
    """
    try:
        if isinstance(price, (int, float)):
            return f"₹{price:.2f} per hour"
        elif isinstance(price, str):
            if "/km" in price:
                return f"₹{price.replace('/km','')} per km"
            else:
                return f"₹{price} per hour"
    except Exception:
        return str(price)


def validate_email(email):
    """
    Validate email format using regex.
    Returns True if valid, False otherwise.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def normalize_text(text):
    """
    Normalize text for case-insensitive comparisons.
    """
    return text.strip().lower()
def filter_by_rating(providers, min_rating=4.5):
    """
    Return providers with rating >= min_rating.
    """
    return [p for p in providers if float(p.rating) >= min_rating]
def filter_by_price(providers, max_price=500):
    """
    Return providers with price <= max_price.
    Handles numeric and string price values.
    """
    result = []
    for p in providers:
        try:
            price_str = str(p.price).replace("/km", "")
            if price_str.isdigit() and float(price_str) <= max_price:
                result.append(p)
        except Exception:
            continue
    return result
def availability_match(provider, day_keyword):
    """
    Check if provider availability contains a given day keyword.
    Example: 'Mon-Sat' or 'Daily'.
    """
    return day_keyword.lower() in provider.availability.lower()
def provider_summary(provider):
    """
    Generate a short summary string for display.
    """
    return (f"{provider.name} offers {provider.service} "
            f"in {provider.location} at {format_price(provider.price)} "
            f"(Rating: {provider.rating})")
if __name__ == "__main__":
    # Example usage with dummy provider object
    class DummyProvider:
        def __init__(self, name, service, location, price, rating, availability):
            self.name = name
            self.service = service
            self.location = location
            self.price = price
            self.rating = rating
            self.availability = availability

    provider = DummyProvider("Anita Sharma", "Deep Cleaning", "Hyderabad", 500, 4.6, "Mon-Sat 9AM-6PM")
    print(provider_summary(provider))
    print("Valid email:", validate_email("anita.clean@example.com"))
