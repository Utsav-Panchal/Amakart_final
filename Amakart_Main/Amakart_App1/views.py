from asyncio import events
from doctest import debug

from django.http import HttpResponseRedirect
from concurrent.futures import ThreadPoolExecutor
import asyncio
from django.shortcuts import render
from django.views import View
import requests
from bs4 import BeautifulSoup
from time import sleep
from .forms import ModelForm
import time, datetime
# Create your views here.
# Data
# ip_addresses = [
#     '185.164.56.20:20009',
#     'p.webshare.io:20000',
#     'p.webshare.io:20001',
#     'p.webshare.io:20002',
#     'p.webshare.io:20003',
#     'p.webshare.io:20004',
#     'p.webshare.io:20005',
#     'p.webshare.io:20006',
#     'p.webshare.io:20007',
#     'p.webshare.io:20008',
# ]
ip_addresses = ['81.163.116.68:8080','125.166.215.100:8080']

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'

headers = {'User-Agent': user_agent}


proxy_test = {"http": "http://eigbmvrz-1:dfn56ntlzh07@193.8.215.135:80",
              "https": "https://eigbmvrz-1:dfn56ntlzh07@193.8.215.135:80"}

amazon_url_list= []


def amazon_scarping(range_from, range_to, page):
    # amazon_url = f'https://www.amazon.in/s?&rh=p_36:100000-800000&page={2}'
    amazon_url = f"https://www.amazon.in/s?rh=p_36:{int(range_from) * 100}-{int(range_to) * 100}&page={page}"
    print(amazon_url)
    response = requests.get(amazon_url, headers=headers)
    # print(response)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup.prettify())
        all_block = soup.findAll("div", attrs={"class": "a-section a-spacing-medium"})
        for i in all_block:
            href = i.find("a", {"class": "a-link-normal a-text-normal"})
            specific_url = href["href"]
            final_url_string = "https://www.amazon.in" + specific_url
            amazon_url_list.append(final_url_string)
        # all_block = soup.findAll("div",
        #                          attrs={"class": "s-include-content-margin.s-border-bottom.s-latency-cf-section"})
        # if all_block != []:
        #     for url in all_block:
        #         a_url = url.find("a", attrs={"class": "a-link-normal.a-text-normal"})["href"]
        #         print(a_url)
        #         final_url_string = "https://www.amazon.in" + a_url
        #         amazon_url_list.append(final_url_string)
        #     # print(all_block)
        # print(amazon_url_list)
        return all_block
    else:
        print("connection failed")
        return None

def amazon_page_randor(range_from, range_to, page):
    while True:

        amazon_page_url = amazon_scarping(range_from, range_to, page)
        if amazon_page_url != []:
            print("Inside For page", page)
            page = page + 1
            continue
        elif amazon_page_url is None:
            print("connection failed")
            break
        else:
            break
    print("amazon list in page_render", amazon_url_list)
    print("length of list amazon", len(amazon_url_list))
    return amazon_url_list

print(amazon_url_list)





data = ['Mobiles', 'Smart Wearable Tech', 'Mobile Accessories', 'Laptops', 'Desktop PCs',
        'Gaming & Accessories',

        'Computer Accessories', 'Computer Peripherals', 'Tablets', 'Speakers', 'Smart Home Automation',
        'Camera',
        'Camera Accessories', 'Network Components', 'Google Assistant Store', 'Laptops on Buyback Guarantee',
        'Flipkart SmartBuy', 'Li-Polymer Power Banks', 'Sony PS4 Pro & Slim', 'Apple Products',
        'Microsoft Store',
        'Lenovo Phab Series', 'JBL Speakers', 'Smartphones On Buyback Guarantee', 'Philips', 'Dr. Morepen',
        'Complete Mobile Protection', 'Mobiles No Cost EMI', 'Television', 'New Launches', 'Smart & Ultra HD',
        'Washing Machine', 'Air Conditioners', 'Refrigerators', 'Kitchen Appliances',
        'Healthy Living Appliances',
        'Small Home Appliances', 'Livpure', 'Philips', 'Bajaj', 'IFB', 'Eureka Forbes', 'Kaff', 'Buying Guides',
        'New Launches', 'Footwear', "Men's Grooming", 'Clothing', 'Top wear', 'Bottom wear', 'Ties, Socks, '
                                                                                             'Caps & more',
        'Kurta',
        'Pyjama',
        'Fabrics', 'Seasonal Wear', 'Sports wear', 'Innerwear & Sleepwear', 'Watches', 'Accessories',
        'Sports & Fitness Store', 'Smart Watches', 'Smart Bands', 'Personal Care Appliances', 'Watches Store',
        'Footwear Club', 'Bags & Wallet', 'T-Shirt Store', 'Adidas', 'Beardo', 'Reebok', 'Skechers', 'Nike',
        'Clothing', 'Western Wear', 'Lingerie & Sleepwear', 'Swim & Beachwear', 'Party Dresses',
        'Sports & Gym Wear',
        'Winter & Seasonal Wear', 'Ethnic Wear', 'Sports Wear', 'International Brands', 'Footwear', 'Sandals',
        'Shoes', 'Ballerinas', "Slippers & Flip- Flop's", 'Watches', 'Smart Watches',
        'Personal Care Appliances',
        'Beauty & Grooming', 'Jewellery', 'Accessories', 'Forever 21', 'Accessorize', 'W', 'Pantaloons',
        'Chemistry',
        'Lakme', 'Nivea', 'Catwalk', 'Titan-Raga', 'Fastrack', 'Divastri', 'Rare Roots', 'Anmi', 'Coins & Bars',
        'Crocs', 'Kids Clothing', "Boys' Clothing", "Girls' Clothing", 'Baby Boy Clothing',
        'Baby Girl Clothing',
        'Kids Footwear', "Boys' Footwear", "Girls' Footwear", 'Baby Footwear', 'Character Shoes',
        'Kids Winter Wear',
        'Toys', 'School Supplies', 'Baby Care', 'Miss & Chief', 'Barbie', 'Disney', 'United Colors of Benetton',
        "The Children's Place", 'US Polo', 'Flying Machine', 'Crocs', 'Puma', 'Funskool', 'Lego', 'Luvlap',
        'Mamy Poko', 'Mee Mee', 'Kitchen, Cookware & Serveware', 'Tableware & Dinnerware', 'Kitchen Storage',
        'Cleaning Supplies', 'Furniture Top Offers', 'Bed Room Furniture', 'Living Room Furniture',
        'Office & Study '
        'Furniture',
        'DIY Furniture', 'Furnishing', 'Smart Home Automation', 'Home Improvement', 'Home Decor',
        'Home Lighting',
        'Festive Decor & Gifts', 'Pet Supplies', 'Durability Certified Furniture', 'Christmas Store',
        'Gardening '
        'Store',
        'Perfect Home Store', 'Sports', 'Exercise Fitness', 'Food Essentials', 'All Supplements', 'Books',
        'Stationery', 'Auto Accessories', 'Industrial & Scientific tools', 'Pregnancy and Fertility Kits',
        'Hot Water Bag', 'Music', 'Gaming']

data =['Kurta',
        'Pyjama',
        'Fabrics', 'Seasonal Wear', 'Sports wear', 'Innerwear & Sleepwear', 'Watches', 'Accessories',
        ]
data = ['Clothing and Accessories',
        # 'Books',
        # 'Industrial & Scientific Supplies',
        # '2Gud',
        # 'Health Care',
        # 'Home Improvement',
        # 'Building Materials and Supplies',
        # 'Beauty and Grooming',
        # 'Mobiles & Accessories',
        # 'Computers',
        # 'Cameras & Accessories',
        # 'Gaming',
        # 'Music, Movies & Posters',
        # 'Home Entertainment',
        # 'Home & Kitchen',
        # 'Pens & Stationery',
        # 'Bags',
        # ' Wallets & Belts',
        # 'Home Lighting',
        # 'Kitchen',
        # 'Cookware & Serveware',
        # 'Jewellery',
        # 'Home Cleaning & Bathroom Accessories',
        # 'Audio & Video',
        # 'Eyewear',
        # 'Vas',
        # 'Pet Supplies',
        # 'Food & Nutrition',
        # 'Home Furnishing',
        # 'Musical Instruments',
        # 'Exercise & Fitness',
        # 'Watches',
        # 'Kids Accessories',
        # 'Home Decor',
        # 'Furniture',
        # 'Wearable Smart Devices',
        # 'Sunglasses',
        # 'Automation & Robotics',
        # 'Festive Decor & Gifting',
        # 'Sports',
        # 'Health & Personal Care Appliances',
        # 'Automotive',
        # 'Footwear',
        # 'Baby Care',
        # 'Toys',
        # 'Clothing'
        ]
# proxy_test = {'http': ip_addresses[0]}
proxy_test = {"http": "http://eigbmvrz-1:dfn56ntlzh07@193.8.215.135:80",
              "https": "https://eigbmvrz-1:dfn56ntlzh07@193.8.215.135:80"}

data = [
    'https://www.flipkart.com/clothing-and-accessories/pr?sid=clo&otracker=categorytree',
        # 'https://www.flipkart.com/books/pr?sid=bks&otracker=categorytree',
        # 'https://www.flipkart.com/industrial-scientific-supplies/pr?sid=gsx&otracker=categorytree',
        # 'https://www.flipkart.com/2gud/pr?sid=2gd&otracker=categorytree',
        # 'https://www.flipkart.com/health-care/pr?sid=hlc&otracker=categorytree',
        # 'https://www.flipkart.com/home-improvement/pr?sid=h1m&otracker=categorytree',
        # 'https://www.flipkart.com/building-materials-and-supplies/pr?sid=b8s&otracker=categorytree',
        # 'https://www.flipkart.com/beauty-and-grooming/pr?sid=g9b&otracker=categorytree',
        # 'https://www.flipkart.com/mobiles-accessories/pr?sid=tyy&otracker=categorytree',
        # 'https://www.flipkart.com/computers/pr?sid=6bo&otracker=categorytree',
        # 'https://www.flipkart.com/cameras-accessories/pr?sid=jek&otracker=categorytree',
        # 'https://www.flipkart.com/gaming/pr?sid=4rr&otracker=categorytree',
        # 'https://www.flipkart.com/music-movies-posters/pr?sid=4kt&otracker=categorytree',
        # 'https://www.flipkart.com/home-entertainment/pr?sid=ckf&otracker=categorytree',
        # 'https://www.flipkart.com/home-kitchen/pr?sid=j9e&otracker=categorytree',
        # 'https://www.flipkart.com/pens-stationery/pr?sid=dgv&otracker=categorytree',
        # 'https://www.flipkart.com/bags-wallets-belts/pr?sid=reh&otracker=categorytree',
        # 'https://www.flipkart.com/home-lighting/pr?sid=jhg&otracker=categorytree',
        # 'https://www.flipkart.com/kitchen-cookware-serveware/pr?sid=upp&otracker=categorytree',
        # 'https://www.flipkart.com/jewellery/pr?sid=mcr&otracker=categorytree',
        # 'https://www.flipkart.com/home-cleaning-bathroom-accessories/pr?sid=rja&otracker=categorytree',
        # 'https://www.flipkart.com/audio-video/pr?sid=0pm&otracker=categorytree',
        # 'https://www.flipkart.com/eyewear/pr?sid=u73&otracker=categorytree',
        # 'https://www.flipkart.com/vas/pr?sid=mcd&otracker=categorytree',
        # 'https://www.flipkart.com/pet-supplies/pr?sid=p3t&otracker=categorytree',
        # 'https://www.flipkart.com/food-nutrition/pr?sid=7jv&otracker=categorytree',
        # 'https://www.flipkart.com/elearning/pr?sid=xfw&otracker=categorytree',
        # 'https://www.flipkart.com/musical-instruments/pr?sid=ypu&otracker=categorytree',
        # 'https://www.flipkart.com/exercise-fitness/pr?sid=qoc&otracker=categorytree',
        # 'https://www.flipkart.com/watches/pr?sid=r18&otracker=categorytree',
        # 'https://www.flipkart.com/kids-accessories/pr?sid=d69&otracker=categorytree',
        # 'https://www.flipkart.com/home-decor/pr?sid=arb&otracker=categorytree',
        # 'https://www.flipkart.com/furniture/pr?sid=wwe&otracker=categorytree',
        # 'https://www.flipkart.com/wearable-smart-devices/pr?sid=ajy&otracker=categorytree',
        # 'https://www.flipkart.com/sunglasses/pr?sid=26x&otracker=categorytree',
        # 'https://www.flipkart.com/automation-robotics/pr?sid=igc&otracker=categorytree',
        # 'https://www.flipkart.com/festive-decor-gifting/pr?sid=bro&otracker=categorytree',
        # 'https://www.flipkart.com/sports/pr?sid=abc&otracker=categorytree',
        # 'https://www.flipkart.com/health-personal-care-appliances/pr?sid=zlw&otracker=categorytree',
        # 'https://www.flipkart.com/automotive/pr?sid=0hx&otracker=categorytree',
        # 'https://www.flipkart.com/footwear/pr?sid=osp&otracker=categorytree',
        # 'https://www.flipkart.com/baby-care/pr?sid=kyh&otracker=categorytree',
        # 'https://www.flipkart.com/toys/pr?sid=mgl&otracker=categorytree',
        # 'https://www.flipkart.com/clothing/pr?sid=53oq&otracker=categorytree'
]


furl_for_multi_page = []


def flipkart_items(product_name: str, page_start_from: int, range_from: str, range_to: str, session):

    print("Range from inside", range_from, 'IIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNNNNNN')
    print("Range from inside", range_to, 'IIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNNNNN')
    product_name = product_name.replace(' ', '+')
    string_url = f'{product_name}&p[]=facets.price_range.from={range_from}&p[]=facets.price_range.to={range_to}&page={page_start_from}'
    # string_url = f'https://www.flipkart.com/search?q={product_name}&p[]=facets.price_range.from={range_from}&p[]=facets.price_range.to={range_to}&page={page_start_from}'
    print(string_url)
    response = session.get(string_url, proxies=proxy_test, headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        # finding url
        url_main_updown_column = soup.findAll("a", attrs={'class': '_31qSD5'})
        for block_updown in url_main_updown_column:
            if block_updown['href'] is not None:
                particular_url = block_updown['href']
                flipkart_official_site = f'https://www.flipkart.com{particular_url}'
                furl_for_multi_page.append(flipkart_official_site)
            else:
                furl_for_multi_page.append(None)
        # print(furl_for_multi_page)
        url_main_side_column = soup.findAll("a", attrs={'class': 'Zhf2z-'})
        for block_side in url_main_side_column:
            if block_side['href'] is not None:
                particular_url = block_side['href']
                flipkart_official_site = f'https://www.flipkart.com{particular_url}'
                furl_for_multi_page.append(flipkart_official_site)
            else:
                furl_for_multi_page.append(None)
        # print(url_main_side_column)
        url_main_Men_and_women = soup.findAll("a", attrs={'class': '_3dqZjq'})
        for block_men_women in url_main_Men_and_women:
            if block_men_women['href'] is not None:
                particular_url = block_men_women['href']
                flipkart_official_site = f'https://www.flipkart.com{particular_url}'
                furl_for_multi_page.append(flipkart_official_site)
            else:
                furl_for_multi_page.append(None)

    return url_main_updown_column, url_main_side_column, url_main_Men_and_women, furl_for_multi_page


def Page_render(data_from_fun: str, page: int, range_from: str, range_to: str, session):
    all_pages_url = []
    print("range from", range_from, "#####################################")
    print("range to", range_to, "#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    while True:

        function_call_flipkart = flipkart_items(data_from_fun, page, range_from, range_to, session)
        if function_call_flipkart[0] != []:
            print("Inside function for page:", page)
            page = page + 1
            asyncio.sleep(0.2)
            continue
        elif function_call_flipkart[1] != []:
            print("Inside sidebar for page:", page)
            page = page + 1
            asyncio.sleep(0.2)
            continue
        elif function_call_flipkart[2] != []:
            print("Inside sidebar for page:", page)
            page = page + 1
            asyncio.sleep(0.2)
            continue
        else:
            # all_pages_url = all_pages_url + function_call_flipkart[3]
            break
    return furl_for_multi_page


# range_from = 2000
# range_to = 4000
page = 1


class indexClass(View):
    def get(self, request):
        form = ModelForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):

        form = ModelForm(request.POST)
        if form.is_valid():
            print("It always goes from here")
            range_from = form.cleaned_data['range_from']
            range_to = form.cleaned_data['range_to']
            choosing_selling_sites = form.cleaned_data['choosing_selling_sites']
            print(choosing_selling_sites)
            if 'Flipkart' in choosing_selling_sites:
                furl_for_multi_page = []

                async def data_render(data):
                    with ThreadPoolExecutor(max_workers=10) as executor:
                        with requests.session() as session:
                            loop = asyncio.get_event_loop()
                            tasks = [
                                loop.run_in_executor(executor, Page_render,
                                                     *(data_from_fun, page, range_from, range_to, session)) for
                                data_from_fun in data
                            ]
                            for response in await asyncio.gather(*tasks):
                                furl_for_multi_page.append(response)

                    return furl_for_multi_page



                if events._get_running_loop() is not None:
                    raise RuntimeError(
                        "asyncio.run() cannot be called from a running event loop")

                # if not coroutines.iscoroutine(main):
                #     raise ValueError("a coroutine was expected, got {!r}".format(main))

                loop = events.new_event_loop()
                try:
                    events.set_event_loop(loop)
                    loop.set_debug(debug)
                    loop.run_until_complete(data_render(data))
                finally:
                    try:
                        # _cancel_all_tasks(loop)
                        loop.run_until_complete(loop.shutdown_asyncgens())
                    finally:
                        events.set_event_loop(None)
                        loop.close()
                furl_for_multi_page = furl_for_multi_page[0]
                print("length of flipkart", len(furl_for_multi_page))
            else:
                furl_for_multi_page = []
                print("NOT FOR FLIPKART", furl_for_multi_page)

            if 'Amazon' in choosing_selling_sites:
                amazon_url = amazon_page_randor(range_from, range_to, page)
                print("length of amazon", len(amazon_url))
            else:
                amazon_url = []

                print("NOT FOR AMAZON", amazon_url)

            sleep(5)
            return render(request, 'url_table.html', {'furl_for_multi_page': furl_for_multi_page, 'aurl_for_multi_page': amazon_url, 'range_from': range_from, 'range_to':range_to})






