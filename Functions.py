from collections import namedtuple
from pyvirtualdisplay import Display
from thefuzz import fuzz

Game = namedtuple('Game', ['site', 'home', 'away', 'fixture', gg1', 'ng1', 'gg2', 'ng2'])

def display_on():
    display = Display(visible=False, size=(1920, 1080))
    display.start()

def display_off():
    display.stop()

def goto_hwb(holly):
        holly.goto()
        holly.wait_for_load_state('load')
        try:
            close_button = holly.locator(close)
            if close_button.is_visible():
                close_button.click()
                print("Popup closed.")
            else:
                print("Popup not found.")
        except Exception as e:
            print(f"Error while trying to close the popup: {e}")

def goto_sb(supa):
        supa.goto(Supa.url)

def get_hwb(holly):
        holly.wait_for_load_state('load')
        holly.wait_for_selector("(//span/span/button/span)[1]")
        all_events = holly.query_selector_all("(//span/span/button/span)")
        events = all_events[:10]
        hbgames = []
        for index in range(len(events)):
          event = events[index]
          event.click()
          holly.wait_for_load_state('load')

          # odds logic

          holly.wait_for_selector(Holly.btts1_yes)

          gg_1 = holly.locator(Holly.yes_value1)
          ng_1 = holly.locator(Holly.no_value1)
          gg_2 = holly.locator(Holly.yes_value2)
          ng_2 = holly.locator(Holly.no_value2)

          gg1 = gg_1.inner_text()
          ng1 = ng_1.inner_text()
          gg2 = gg_2.inner_text()
          ng2 = ng_2.inner_text()
          
          
          
          home = holly.locator("//span[contains(@class, 'team-name')][1]").inner_text()
          away = holly.locator("//span[contains(@class, 'team-name')][2]").inner_text()
          fixture = home + " vs " + away

          game = Game(Holly.site, home, away, fixture, gg1, ng1, gg2, ng2)
          holly.go_back()

          hbgames.append(game)
          holly.wait_for_load_state('load')
        return hbgames

def print_hbgames():
        for hbgame in hbgames:
          print(hbgame)
          print("")
          print("")

def get_sb(supa):

        hxme = supa.locator(Supa.team_h).nth(0)
        hxme.wait_for()

        all_events = supa.query_selector_all(Supa.team_h)
        events = all_events[:10]

        sbgames = []
        for index in range(len(events)):

          event = events[index]
          event.click()

          homename = supa.locator(Supa.home_id).nth(0)
          homename.wait_for()

          home_away = supa.query_selector_all(Supa.teams)
          home = home_away[0].inner_text()
          away = home_away[1].inner_text()
          fixture = home + " v " + away

          gg_1 = supa.locator(Supa.gg_one)
          ng_1 = supa.locator(Supa.ng_one)
          gg_2 = supa.locator(Supa.gg_two)
          ng_2 = supa.locator(Supa.ng_two)

          gg1 = gg_1.inner_text()
          ng1 = ng_1.inner_text()
          gg2 = gg_2.inner_text()
          ng2 = ng_2.inner_text()

          game = Game(Supa.site, home, away, fixture, gg1, ng1, gg2, ng2)
          supa.go_back()

          sbgames.append(game)
          hxme.wait_for()
        return sbgames


def print_sbgames():
        for sbgame in sbgames:
          print(sbgame)
          print("")
          print("")

          
Arb1 = namedtuple('Arb1', ['sites', 'home', 'away', 'event', 'gg1', 'ng1', 'tip'])
Arb2 = namedtuple('Arb2', ['sites', 'home', 'away', 'event', 'gg2', 'ng2', 'tip'])
                              
def arbs():
    #sb, pb, bu, bw, hb = games_list()
    for a in sbgames:
        for b in hbgames: 
            x = fuzz.ratio(a.home, b.home)
            y = fuzz.ratio(a.away, b.away)
            if x > 90 and y > 90:
                    
                h1a = Arb1(a.site + " v " + b.site, a.home, b.away, a.fixture, a.gg1, b.ng1, (((1/a.gg1) + (1/b.ng1)) * 100))
                
                h1b = Arb1(a.site + " v " + b.site, a.home, b.away, a.fixture, b.gg1, a.ng1, (((1/b.gg1) + (1/a.ng1)) * 100)))
                h2a = Arb2(a.site + " v " + b.site, a.home, b.away, a.fixture, a.gg2, b.ng2, (((1/a.gg2) + (1/b.ng2)) * 100)))
                h2b = Arb2(a.site + " v " + b.site, a.home, b.away, a.fixture, b.gg2, a.ng2, (((1/b.gg2) + (1/a.ng2) * 100)))
                
                # write this shit into a file
                # so you don't have to be
                # frustrated by any bs
                
                h1all = []
                h2all = []
                
                h1 = [h1a, h1b]
                h2 = [h2a, h2b]
                                
                for item in h1:
                    if item.tip < 100:
                        h1all.append(item)
                        print(item)
                        
                for item in h2:
                    if item.tip < 100:
                        h2all.append(item)
                        print(item)
                # sort h1all and h2all by tip
                    
    return h1all, h2all

if __name__ == '__main__':
    print("functions created")
