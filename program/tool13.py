# par pitié ne pas volé mon code et ne rien modiffié svp sah

import requests
from bs4 import BeautifulSoup
import re
from colorama import init, Fore, Style


init(autoreset=True)


sites = {
    "TikTok": "https://www.tiktok.com/@{}",
    "Instagram": "https://www.instagram.com/{}",
    "Paypal": "https://www.paypal.com/paypalme/{}",
    "GitHub": "https://github.com/{}",
    "Giters": "https://giters.com/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Telegram": "https://t.me/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Blogger": "https://{}.blogspot.com",
    "Tumblr": "https://{}.tumblr.com",
    "SoundCloud": "https://soundcloud.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "About.me": "https://about.me/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Keybase": "https://keybase.io/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "Slideshare": "https://www.slideshare.net/{}",
    "Behance": "https://www.behance.net/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Myspace": "https://myspace.com/{}",
    "Kaggle": "https://www.kaggle.com/{}",
    "Periscope": "https://www.pscp.tv/{}",
    "Disqus": "https://disqus.com/by/{}",
    "Mastodon": "https://mastodon.social/@{}",
    "GitLab": "https://gitlab.com/{}",
    "Giphy": "https://giphy.com/{}",
    "LiveJournal": "https://{}.livejournal.com",
    "CodeWars": "https://www.codewars.com/users/{}",
    "Gumroad": "https://gumroad.com/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Weebly": "https://{}.weebly.com",
    "YouTube": "https://www.youtube.com/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "Mix": "https://mix.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Strava": "https://www.strava.com/athletes/{}",
    "Internet Archive": "https://archive.org/search?query={}",
    "Twitter Archive": "https://web.archive.org/web/*/https://twitter.com/{}/status/*",
    "Linktree": "https://linktr.ee/{}",
    "Xbox": "https://www.xboxgamertag.com/search/{}",
    "Twitter": "https://twitter.com/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Goodreads": "https://www.goodreads.com/{}",
    "VK": "https://vk.com/{}",
    "TripAdvisor": "https://www.tripadvisor.com/members/{}",
    "Dribbble": "https://dribbble.com/{}",
    "AngelList": "https://angel.co/{}",
    "500px": "https://500px.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "WhatsApp": "https://wa.me/{}",
    "Discord": "https://discord.com/users/{}",
    "Weibo": "https://weibo.com/{}",
    "OKCupid": "https://www.okcupid.com/profile/{}",
    "Meetup": "https://www.meetup.com/members/{}",
    "CodePen": "https://codepen.io/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "HackerRank": "https://www.hackerrank.com/{}",
    "Xing": "https://www.xing.com/profile/{}",
    "Deezer": "https://www.deezer.com/en/user/{}",
    "Snapfish": "https://www.snapfish.com/{}",
    "Tidal": "https://tidal.com/{}",
    "Dailymotion": "https://www.dailymotion.com/{}",
    "Ravelry": "https://www.ravelry.com/people/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Vine": "https://vine.co/u/{}",
    "Foursquare": "https://foursquare.com/user/{}",
    "Ello": "https://ello.co/{}",
    "Hootsuite": "https://hootsuite.com/{}",
    "Prezi": "https://prezi.com/{}",
    "Groupon": "https://www.groupon.com/profile/{}",
    "Liveleak": "https://www.liveleak.com/c/{}",
    "Joomla": "https://www.joomla.org/user/{}",
    "StackExchange": "https://stackexchange.com/users/{}",
    "Taringa": "https://www.taringa.net/{}",
    "Shopify": "https://{}.myshopify.com",
    "8tracks": "https://8tracks.com/{}",
    "Couchsurfing": "https://www.couchsurfing.com/people/{}",
    "OpenSea": "https://opensea.io/{}",
    "Trello": "https://trello.com/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "Badoo": "https://badoo.com/profile/{}",
    "Rumble": "https://rumble.com/user/{}",
    "Wix": "https://www.wix.com/website/{}"
}

def site_exception(username, site, page_content):
    """Handle special cases for specific sites."""
    if site == "Paypal":
        page_content = page_content.replace(f'slug_name={username}', '').replace(f'"slug":"{username}"', '').replace(f'2F{username}&amp', '')
    elif site == "TikTok":
        page_content = page_content.replace(f'\\u002f@{username}"', '')
    return page_content

def search_username(username):
    """Search for the username across different sites and print results."""
    number_site = 0
    number_found = 0

    print(f"Searching for username: {username}")

    for site, url_template in sites.items():
        try:
            number_site += 1
            url = url_template.format(username)
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    page_content = re.sub(r'<[^>]*>', '', response.text.lower().replace(url, "").replace(f"/{username}", ""))
                    page_text = soup.get_text().lower().replace(url, "")
                    page_title = soup.title.string.lower() if soup.title else ""

                    page_content = site_exception(username, site, page_content)

                    if username in page_title or username in page_content or username in page_text:
                        number_found += 1
                        print(f"{Fore.GREEN}[+] {site}: {url}{Style.RESET_ALL}")

            except Exception as e:
                print(f"{Fore.YELLOW}{site} error: {e}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}{site} request error: {e}{Style.RESET_ALL}")

    print(f"Total Sites Checked: {number_site}, Total Found: {number_found}")

def run():
    """Run the tool."""
    username = input("Enter username to search: ").strip().lower()
    search_username(username)

if __name__ == "__main__":
    run()
