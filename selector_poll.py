import nextcord
import random
from get_greads_links import *
from get_books import *
import dhooks
from discord_webhook import DiscordEmbed, DiscordWebhook

import re
# Format
# fiction: b1, b2, b3
# nonfiction: b1, b2, b3
# telugu: b1, b2, b3
def num_to_letter(num, small=True):
    if small:
        return chr(ord('`') + num)
    else:
        return chr(ord('@') + num)


class Emotes:
    regional_indicator = "regional_indicator_"


class BaseRandomPoll(object):
    stripThese = " "
    SequenceSeparator = "\n"
    TitleSeparator = "$"
    ItemSeparator = ";"
    BookAuthorSeparator = " by"

    def __init__(self, text):
        self.text = text
        self.fields = {}
        self.selected = {}

    def select_items(self):
        seqs = self.text.split(self.SequenceSeparator)
        for seq in seqs:
            if seq.strip(self.stripThese):
                title, temp = seq.split(self.TitleSeparator)
                options = temp.split(self.ItemSeparator)
                self.selected[title.strip(self.stripThese)] = random.choice(options)

    def populate_embed(self, title=None, description=None, url=None, author="", author_url=None, icon_url=None, thumbnail_url=None):
        self.embed = DiscordEmbed(title=title, description=description, url=url)
        if author:
            self.embed.set_author(name=author, url=author_url, icon_url=icon_url)
        if thumbnail_url:
            self.embed.set_thumbnail(url=thumbnail_url)
        self.postprocess_selected()
        for index, (name, value) in enumerate(self.selected.items()):
            self.embed.add_embed_field(name=":{}:. {}".format(Emotes.regional_indicator + num_to_letter(index + 1), name), value=value, inline=True)
        self.num_fields = len(self.selected)

    def postprocess_selected(self):
        pass

    def execute_embed(self):
        hook = DiscordWebhook("https://discord.com/api/webhooks/936303043048255508/xWZUJHmu9Z-Eq_9A_3as_xVm3Iiu3ggpf7vsC_m5J8RjO5mXjnVWtGhisZ8706HH_fL3")
        # temp = eval(BuddyRead("!b\n book: A fine balance", username)())
        # print(temp)
        # embed=nextcord.Embed.from_dict() #temp["embeds"][-1]
        hook.add_embed(self.embed)
        # hook.send(botm.embed)
        resp = hook.execute()
        print(resp)

class BoTMSelector(BaseRandomPoll):
    TITLE_NAME = "genre"
    ITEM_NAME = "book"

    def __init__(self, text):
        super(BoTMSelector, self).__init__(text)

    def postprocess_selected(self):
        for name, val in self.selected.items():
            split_ = val.split(self.BookAuthorSeparator)
            if len(split_) == 1:
                split_.append("")
            temp = get_greads_links([[split_[0], split_[1]]])[-1]
            self.selected[name] = "[{name}]({link})".format(name=(temp[0] + self.BookAuthorSeparator + " " + temp[1]) if temp[1] else temp[0],
                                                            link=temp[-1])

    def populate_embed(self, title="Book Of The Month Poll", description=None, url=None, author="", author_url=None, icon_url=None, thumbnail_url=None):
        description = description or "We have selected {ITEM_NAME}s for {num} {TITLE_NAME}s at random. A book is selected for each {TITLE_NAME} from the nominations".format(ITEM_NAME = self.ITEM_NAME, num = len(self.selected),TITLE_NAME=self.TITLE_NAME )
        super(BoTMSelector, self).populate_embed(
            title=title,
            description=description,
            url=url,
            author=author,
            author_url=author_url,
            icon_url=icon_url,
            thumbnail_url=thumbnail_url
        )

def get_reactions(mess):
    # return re.findall(r":{}[a-z]:".format(Emotes.regional_indicator), mess)
    if "We have selected {ITEM_NAME}s for ".format(ITEM_NAME = BoTMSelector.ITEM_NAME) in mess:
        return [":{}:".format(Emotes.regional_indicator + num_to_letter(index + 1)) for index in len()]


if __name__ == "__main__":
    text = """Fiction$ A fine Balance; The God of Small things
    Non-Fiction$ Little history of economics; Naked Economics
    """
    botm = BoTMSelector(text)
    botm.populate_embed()
    print(botm.embed)
    # print(botm.embed.to_dict())
