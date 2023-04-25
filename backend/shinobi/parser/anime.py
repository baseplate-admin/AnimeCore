import datetime
from functools import lru_cache

from dateutil import parser
from selectolax.parser import HTMLParser, Node

from shinobi.decorators.return_error_decorator import return_on_error
from shinobi.utilities.regex import RegexHelper
from shinobi.utilities.string import StringHelper


class AnimeParser:
    def __init__(self, html: str) -> None:
        self.parser = self.get_parser(html)

        # Facades
        self.regex_helper = RegexHelper()
        self.string_helper = StringHelper()

    @staticmethod
    def get_parser(html: str) -> HTMLParser:
        return HTMLParser(html)

    @property
    @return_on_error("")
    def get_anime_url(self) -> str:
        return self.parser.css_first("meta[property='og:url']").attributes["content"]

    @property
    @return_on_error("")
    def get_anime_id(self) -> str:
        return self.regex_helper.get_id_from_url(self.get_anime_url)

    @property
    @return_on_error("")
    def get_anime_name(self) -> str:
        return self.parser.css_first("meta[property='og:title']").attributes["content"]

    @property
    @return_on_error("")
    def get_anime_name_japanese(self) -> str:
        node = self.parser.select("span").text_contains("Japanese:").matches
        if len(node) > 1:
            raise ValueError("There are more than one node in name japanese node")

        name_japanese = self.string_helper.cleanse(node[0].next.text())
        return name_japanese

    @property
    @return_on_error("")
    def get_anime_name_synonyms(self) -> list[str]:
        node = self.parser.select("h2").text_contains("Alternative Titles").matches[0]
        alternate_names = []

        next_node: Node

        while True:
            if node.next.tag == "h2":
                break
            elif node.next.tag == "div":
                next_node = node.next

            try:
                alternate_name = self.string_helper.cleanse(
                    next_node.css_first("span").next.text()
                )
                alternate_names.append(alternate_name)

                next_node.decompose(recursive=True)

            # There are no nodes
            except AttributeError:
                break

        return alternate_names

    @property
    @return_on_error("")
    def get_source(self) -> str:
        node = self.parser.select("span").text_contains("Source:").matches
        if len(node) > 1:
            raise ValueError("There are multiple source node")

        source = self.string_helper.cleanse(node[0].next.text())
        return source

    @property
    @return_on_error("")
    @lru_cache(maxsize=None)
    def get_aired_text(self) -> str:
        # aired text contains in this format
        # 'aired_from to aired_to'
        node = self.parser.select("span").text_contains("Aired:").matches
        if len(node) > 1:
            raise ValueError("There are multiple aired node")

        return self.string_helper.cleanse(node[0].next.text())

    @property
    def get_aired_from(self) -> datetime.datetime:
        aired_text = self.get_aired_text
        splitted_text = aired_text.split("to")
        aired_from = parser.parse(self.string_helper.cleanse(splitted_text[0]))
        return aired_from

    @property
    def get_aired_to(self) -> datetime.datetime:
        aired_text = self.get_aired_text
        splitted_text = aired_text.split("to")
        aired_to = parser.parse(self.string_helper.cleanse(splitted_text[1]))
        return aired_to

    @property
    @return_on_error("")
    def get_synopsis(self) -> str:
        node = self.parser.css_first("p[itemprop='description']")

        synopsis = self.string_helper.cleanse(node.text())
        return (
            ""
            if "No synopsis information has been added to this title." in synopsis
            else synopsis
        )

    @property
    @return_on_error("")
    def get_background(self) -> str:
        node = self.parser.select("h2").text_contains("Background").matches
        if len(node) > 1:
            raise ValueError("There are multiple Background node")

        parent_node = node[0].parent.parent
        parent_node.strip_tags(["p", "div"])

        background = self.string_helper.cleanse(parent_node.text())
        return background

    @property
    @return_on_error("")
    def get_rating(self) -> str:
        node = self.parser.select("span").text_contains("Rating:").matches
        if len(node) > 1:
            raise ValueError("There are multiple Rating node")

        rating = self.string_helper.cleanse(node[0].next.text())
        return rating

    @property
    @return_on_error("")
    def get_genres(self) -> list[int]:
        node = self.parser.select("span").text_contains("Genres:").matches
        if len(node) > 1:
            raise ValueError("There are multiple Genre node")

        genre_parent_nodes = node[0].parent
        # Remove all span tags
        genre_parent_nodes.strip_tags(["span"])
        anchor_tags = genre_parent_nodes.css("a[href*='/anime/']")
        return sorted(
            [
                self.regex_helper.get_first_integer_from_url(anchor.attributes["href"])
                for anchor in anchor_tags
            ]
        )

    @property
    @return_on_error("")
    def get_themes(self):
        node = self.parser.select("span").text_contains("Themes:").matches
        if len(node) > 1:
            raise ValueError("There are multiple Genre node")

        theme_parent_nodes = node[0].parent
        # Remove all span tags
        theme_parent_nodes.strip_tags(["span"])
        anchor_tags = theme_parent_nodes.css("a[href*='/anime/']")
        return sorted(
            [
                self.regex_helper.get_first_integer_from_url(anchor.attributes["href"])
                for anchor in anchor_tags
            ]
        )

    def build_dictionary(self):
        dictionary = {
            "mal_id": self.get_anime_id,
            "name": self.get_anime_name,
            "name_japanese": self.get_anime_name_japanese,
            "name_synonyms": self.get_anime_name_synonyms,
            "source": self.get_source,
            "aired_from": self.get_aired_from,
            "aired_to": self.get_aired_to,
            "synopsis": self.get_synopsis,
            "background": self.get_background,
            "rating": self.get_rating,
            # List[int]
            "genres": self.get_genres,
            "themes": self.get_themes,
            "characters": "",
            "studios": "",
            "producers": "",
            "staffs": "",
            "recommendations": "",  # self
            "episodes": "",
            "openings": "",
            "endings": "",
        }
        return dictionary
