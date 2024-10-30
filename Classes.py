class Holly:
    site = "Hollywoodbets"
    hwb_url = "https://new.hollywoodbets.net/"
    close = "button[aria-label='Close modal'].CloseButton-sc-1l01k7y-0"
    prematch = "//button/span[contains(text(), 'Upcoming Soccer')]"
    btts1_yes = "((//div[contains(text(), '1st Half - Both Teams to score')]/parent::div)/following-sibling::div)/div/span[contains(text(), 'YES')]"
    btts1_no = "((//div[contains(text(), '1st Half - Both Teams to score')]/parent::div)/following-sibling::div)/div/span[contains(text(), 'NO')]"
    yes_value1 = "(((//div[contains(text(), '1st Half - Both Teams to score')]/parent::div)/following-sibling::div)/div/span[contains(text(), 'YES')])/following-sibling::span"
    no_value1 = "(((//div[contains(text(), '1st Half - Both Teams to score')]/parent::div)/following-sibling::div)/div/span[contains(text(), 'NO')])/following-sibling::span"

    btts2_yes = "((//div[contains(text(), '2nd Half - Both Teams to score')]/parent::div)/following-sibling::div)/div/span[contains(text(), 'YES')]"
    btts2_no = "((//div[contains(text(), '2nd Half - Both Teams to score')]/parent::div)/following-sibling::div)/div/span[contains(text(), 'NO')]"
    yes_value2 = "(((//div[contains(text(), '2nd Half - Both Teams to score')]/parent::div)/following-sibling::div)/div/span[contains(text(), 'YES')])/following-sibling::span"
    no_value2 = "(((//div[contains(text(), '2nd Half - Both Teams to score')]/parent::div)/following-sibling::div)/div/span[contains(text(), 'NO')])/following-sibling::span"

class Supa:
    site = "Supabets"
    team_h = "//a/div[@class='plr_1 ng-binding']"
    url = "https://www.supabets.co.za"
    home_id = "//div[@class='subeventItem']/a//span[@class='ng-binding ng-scope']"
    teams = "//div[@class='subeventItem']/a//span[@class='ng-binding ng-scope']"
    gg_one = "//div[@class='odd ng-scope g1']/div[contains(text(), 'GG 1HT')]/following-sibling::div[@class='oddValue ng-binding']"
    ng_one = "//div[@class='odd ng-scope g1']/div[contains(text(), 'NG 1HT')]/following-sibling::div[@class='oddValue ng-binding']"
    gg_two = "//div[@class='odd ng-scope g1']/div[contains(text(), 'GG 2HT')]/following-sibling::div[@class='oddValue ng-binding']"
    ng_two = "//div[@class='odd ng-scope g1']/div[contains(text(), 'NG 2HT')]/following-sibling::div[@class='oddValue ng-binding']"

if __name__ == '__main__':
    print("classes created")
