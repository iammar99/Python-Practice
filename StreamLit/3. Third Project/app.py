import streamlit as st
import requests
from datetime import datetime
import base64

#for image

def get_base64_of_image(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# For Title

st.set_page_config(
    page_title="Weather app",
    page_icon=":cloud:" 
)

# For Date

current_date = datetime.now().strftime("%Y/%m/%d")
st.write(f"### {current_date}")


# For background image


background_mapping = {
    "light intensity drizzle": "light_intensity_drizzle.jpeg",
    "clear sky": "clear_sky.jpeg",
    "haze": "haze.jpeg",
    "moderate rain": "moderate_rain.jpg",
    "light rain": "light_rain.jpg",
    "overcast clouds": "overcast_clouds.jpg",
    "scattered clouds": "scattered_clouds.jpg",
    "broken clouds": "broken_clouds.jpeg",
    "few clouds": "few_clouds.jpg",
    "mist": "mist.jpeg",
    "thunderstorm": "thunderstorm.jpg",
}


# For weather

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        return data.get('message', 'Error fetching weather data')

    weather = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed']
    }

    return weather


countries_cities = {
    "United States": ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin"],
    "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary", "Edmonton", "Ottawa", "Winnipeg", "Quebec City", "Hamilton", "Kitchener"],
    "United Kingdom": ["London", "Manchester", "Birmingham", "Leeds", "Glasgow", "Liverpool", "Edinburgh", "Sheffield", "Bristol", "Cardiff"],
    "Germany": ["Berlin", "Munich", "Frankfurt", "Hamburg", "Cologne", "Stuttgart", "Dusseldorf", "Dortmund", "Essen", "Bremen"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Montpellier", "Strasbourg", "Bordeaux", "Lille"],
    "Italy": ["Rome", "Milan", "Naples", "Turin", "Palermo", "Genoa", "Bologna", "Florence", "Venice", "Bari"],
    "Spain": ["Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza", "Malaga", "Murcia", "Palma", "Las Palmas", "Bilbao"],
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Canberra", "Hobart", "Darwin", "Cairns"],
    "India": ["New Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Pune", "Jaipur", "Lucknow"],
    "China": ["Beijing", "Shanghai", "Shenzhen", "Guangzhou", "Chengdu", "Hangzhou", "Wuhan", "Xi'an", "Dongguan", "Nanjing"],
    "Japan": ["Tokyo", "Osaka", "Kyoto", "Nagoya", "Yokohama", "Kobe", "Fukuoka", "Sapporo", "Hiroshima", "Sendai"],
    "South Korea": ["Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Gwangju", "Suwon", "Jeonju", "Ulsan", "Changwon"],
    "Brazil": ["São Paulo", "Rio de Janeiro", "Salvador", "Fortaleza", "Belo Horizonte", "Brasília", "Curitiba", "Recife", "Porto Alegre", "Manaus"],
    "Mexico": ["Mexico City", "Guadalajara", "Monterrey", "Puebla", "Cancun", "Mérida", "Tijuana", "Chihuahua", "León", "San Luis Potosí"],
    "Russia": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Nizhny Novgorod", "Kazan", "Chelyabinsk", "Omsk", "Rostov-on-Don", "Ufa"],
    "South Africa": ["Johannesburg", "Cape Town", "Durban", "Pretoria", "Port Elizabeth", "Bloemfontein", "East London", "Polokwane", "Mbombela", "Kimberley"],
    "Argentina": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata", "San Miguel de Tucumán", "Salta", "Santa Fe", "San Juan", "Resistencia"],
    "Chile": ["Santiago", "Valparaíso", "Concepción", "La Serena", "Antofagasta", "Temuco", "Rancagua", "Puerto Montt", "Arica", "Iquique"],
    "Colombia": ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Bucaramanga", "Pereira", "Manizales", "Santa Marta", "Cúcuta"],
    "Peru": ["Lima", "Arequipa", "Trujillo", "Chiclayo", "Iquitos", "Cusco", "Piura", "Callao", "Puno", "Huancayo"],
    "Venezuela": ["Caracas", "Maracaibo", "Valencia", "Barquisimeto", "Ciudad Guayana", "Maturín", "San Cristóbal", "Puerto Ordaz", "Barcelona", "Cumana"],
    "Egypt": ["Cairo", "Alexandria", "Giza", "Sharm El Sheikh", "Hurghada", "Luxor", "Aswan", "Port Said", "Suez", "Tanta"],
    "Turkey": ["Istanbul", "Ankara", "Izmir", "Antalya", "Bursa", "Adana", "Gaziantep", "Konya", "Mersin", "Kayseri"],
    "Saudi Arabia": ["Riyadh", "Jeddah", "Mecca", "Medina", "Dhahran", "Khobar", "Dammam", "Abha", "Tabuk", "Hail"],
    "Iran": ["Tehran", "Mashhad", "Isfahan", "Shiraz", "Tabriz", "Ahvaz", "Kerman", "Yazd", "Qom", "Urmia"],
    "Iraq": ["Baghdad", "Basra", "Erbil", "Mosul", "Sulaymaniyah", "Kirkuk", "Najaf", "Kufa", "Hillah", "Amara"],
    "United Arab Emirates": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras al-Khaimah", "Fujairah", "Umm al-Quwain", "Al Ain", "Khor Fakkan", "Dibba Al Fujairah"],
    "Palestine": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod", "Netanya", "Be'er Sheva", "Holon", "Bnei Brak"],
    "Jordan": ["Amman", "Zarqa", "Irbid", "Aqaba", "Madaba", "Karak", "Maan", "Jarrash", "Russeifa", "Salt"],
    "Lebanon": ["Beirut", "Tripoli", "Sidon", "Tyre", "Jounieh", "Zahle", "Baabda", "Byblos", "Bint Jbeil", "Aley"],
    "Pakistan": ["Karachi", "Lahore", "Faisalabad", "Rawalpindi", "Multan", "Peshawar", "Quetta", "Islamabad", "Sialkot", "Gujranwala"],
    "Bangladesh": ["Dhaka", "Chittagong", "Khulna", "Rajshahi", "Sylhet", "Barisal", "Rangpur", "Mymensingh", "Jashore", "Comilla"],
    "Sri Lanka": ["Colombo", "Kandy", "Galle", "Jaffna", "Negombo", "Anuradhapura", "Trincomalee", "Matara", "Batticaloa", "Ratnapura"],
    "Nepal": ["Kathmandu", "Pokhara", "Lalitpur", "Biratnagar", "Bhairahawa", "Janakpur", "Dharan", "Birgunj", "Butwal", "Hetauda"],
    "Myanmar": ["Yangon", "Mandalay", "Naypyidaw", "Bago", "Pathein", "Sittwe", "Taunggyi", "Monywa", "Hpa-An", "Myitkyina"],
    "Thailand": ["Bangkok", "Chiang Mai", "Pattaya", "Nakhon Ratchasima", "Hua Hin", "Khon Kaen", "Hat Yai", "Udon Thani", "Nakhon Si Thammarat", "Samui"],
    "Malaysia": ["Kuala Lumpur", "Penang", "Johor Bahru", "Kota Kinabalu", "Kuching", "Malacca", "Ipoh", "Shah Alam", "Seremban", "Putrajaya"],
    "Singapore": ["Singapore"],
    "Philippines": ["Manila", "Quezon City", "Davao City", "Cebu City", "Zamboanga City", "Taguig", "Iloilo City", "Baguio", "Bacolod", "Cagayan de Oro"],
    "Vietnam": ["Hanoi", "Ho Chi Minh City", "Da Nang", "Hai Phong", "Can Tho", "Hue", "Nha Trang", "Qui Nhon", "Vinh", "Rach Gia"],
    "Cambodia": ["Phnom Penh", "Siem Reap", "Battambang", "Sihanoukville", "Kampong Cham", "Kep", "Kampot", "Pursat", "Svay Rieng", "Kandal"],
}


countries = sorted(countries_cities.keys())



st.sidebar.title("Country and City Selector")


selected_country = st.sidebar.selectbox("Select a country", countries)


if selected_country:
    cities = countries_cities.get(selected_country, [])
    selected_city = st.sidebar.selectbox("Select a city", cities)

        
    st.write(f"## Country :- **{selected_country}**")


# api_key = st.secrets["open_weather_api_key"]
api_key = "9e1f88e6577ec9ef674ca02442e931ed"
city = selected_city
weather = get_weather(api_key, city)


background_file = background_mapping.get(weather["description"])
image_path = f"static/{background_file}"


base64_image = get_base64_of_image(image_path)


st.markdown(
    f"""
    <style>
.background {{
    background-image: url(data:image/jpeg;base64,{base64_image});
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    height: 37vh;
    width: 100%;
    padding: 58px 25px;
    color: white;
    border-radius: 20px;
}}
.col h2,.col h1,.col h3 {{
    padding: 0;
}}
.col h3 b {{
    font-weight: bolder;
}}
p{{
    margin:0;
}}
.row {{
    display: flex;
    justify-content: space-between;
}}
    </style>
    """,
    unsafe_allow_html=True
)

# Create a div with the custom CSS class
st.markdown(
    f"""
        <h1>Welcome to My Weather App</h1>
    <div class="background">
        <div class="row">
            <div class="col">
                <h2>{weather["city"]}</h2>
                <h1>{weather["temperature"]}°C</h1>
            </div>
            <div class="col">
                <h3>
                    <b>{weather["description"].capitalize()}</b>
                </h3>
                <p>Humidity : {weather["humidity"]}%</p>
                <p>Wind Speed : {weather["wind_speed"]}km/h</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
