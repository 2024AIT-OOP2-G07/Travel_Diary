from datetime import datetime, timedelta
from models.place import Place
import random
from faker import Faker
from urllib.request import Request, urlopen
import json
from urllib.parse import quote
from models import initialize_database

fake = Faker("ja_JP")


class RandomPoint:
    place_index = 0
    places: list[str] = []
    addresses: list[str] = []
    coordinates: list[list[float]] = []
    
    comment_index = 0
    comments = [
        "ここはとても楽しかったです！",
        "家族で訪れるのに最適な場所ですね。",
        "もう一度行きたいと思える素敵な場所でした。",
        "雰囲気が良くて心が癒されました。",
        "施設が充実していて満足しました！",
        "子どもたちも大喜びでした！",
        "アクセスも便利で助かりました。",
        "スタッフの対応がとても良かったです。",
        "期待以上に楽しめました！",
        "ここで一日中過ごしても飽きません。",
        "また友達を連れて来たいと思います。",
        "新しい発見がたくさんありました！",
        "展示がとても面白かったです。",
        "清潔感があり、気持ちよく過ごせました。",
        "近くにこんな素敵な場所があったとは驚きです。",
        "心地よい空間でリラックスできました。",
        "周辺にも魅力的な場所が多かったです。",
        "展示が印象的でした。",
        "写真映えするスポットがたくさんありました！",
        "こんなに楽しい場所だとは思いませんでした。",
        "詳細な説明があって分かりやすかったです。",
        "天気の良い日に行くとさらに楽しめそうですね。",
        "季節ごとに楽しめるイベントがあるのが良いです。",
        "普段の忙しさを忘れてリフレッシュできました。",
        "子どもから大人まで楽しめる場所だと思います。",
        "周囲の景色もとても美しかったです。",
        "来るたびに新しい発見があります！",
        "地元の人にも愛されている場所ですね。",
        "訪れて本当に良かったと思える場所でした。",
        "説明や案内が丁寧で助かりました。",
        "休日に行くと少し混雑しますが、それでも楽しめます。",
        "静かで落ち着いた雰囲気が良かったです。",
        "ここにしかない特別な魅力がありました。",
        "近くでランチを楽しむのも良いですね。",
        "友達や家族と来るともっと楽しめると思います。",
        "施設内の装飾がとても素敵でした。",
        "アクセスしやすい立地で助かりました。",
        "思わず長居してしまうような素敵な場所でした。",
        "初めて訪れましたが、大満足です！",
        "毎回新しいイベントがあって飽きません。",
        "説明文やパンフレットが充実していました。",
        "また違う季節に訪れてみたいです。",
        "一人でも楽しめる貴重な場所だと思います。",
        "とても清潔感があり、快適に過ごせました。",
        "ここでしか味わえない体験ができました！",
        "行くたびに新しい発見があります。",
        "時間を忘れて楽しむことができました。",
        "こんな素敵な場所を教えてくれてありがとう！",
        "また行きたいと思えるお気に入りの場所になりました。",
        "訪れるたびに新しい思い出が増えていきます。",
    ]

    def __init__(self):
        prefix = ["ペンギン", "ガラ", "ハリネズミ", "カメ", "ワニ", "カンガルー"]
        place = [
            "動物園",
            "水族館",
            "博物館",
            "美術館",
            "遊園地",
            "公園",
            "カフェ",
            "レストラン",
            "研究所",
            "図書館",
            "動物園",
        ]
        self.places = [p + q for q in place for p in prefix]

        while len(self.addresses) < len(self.places):
            address = fake.address()
            if "愛知県" in address:
                self.addresses.append(address)

        for _ in range(len(self.addresses)):
            lat = random.uniform(35.0, 35.5)
            lon = random.uniform(136, 138)
            self.coordinates.append([lon, lat])

    def _random_date(self):
        start_date = datetime(2010, 1, 1)
        end_date = datetime(2024, 12, 31)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)
        return random_date

    def _get_place(self):
        place = self.places[self.place_index]
        address = self.addresses[self.place_index]
        coordinates = self.coordinates[self.place_index]

        self.place_index = (self.place_index + 1) % len(self.places)

        return place, address, coordinates

    def _get_comment(self):
        comment = self.comments[self.comment_index]
        self.comment_index = (self.comment_index + 1) % len(self.comments)
        return comment

    def get(self):
        name, address, coordinates = self._get_place()
        return {
            "day": self._random_date(),
            "name": name,
            "address": address,
            "lat": coordinates[1],
            "lon": coordinates[0],
            "evaluation": random.randint(1, 5),
            "comment": self._get_comment(),
        }


def seed(n=50):
    Place.delete().execute()
    random_place = RandomPoint()

    for _ in range(n):
        place = random_place.get()
        Place.create(
            name=place["name"],
            day=place["day"],
            address=place["address"],
            lat=place["lat"],
            lon=place["lon"],
            evaluation=place["evaluation"],
            comment=place["comment"],
        )


if __name__ == "__main__":
    initialize_database()
    seed(n=200)
