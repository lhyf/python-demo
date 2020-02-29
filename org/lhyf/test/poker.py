import pprint


class Card:
    def __init__(self, name, type):
        "定义点数和花色"
        self._name = name
        self._type = type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    def __str__(self):
        return f"Card[{self.name},{self.type}]"

    @staticmethod
    def get_type_4_card(name):
        """
        生成四种花色的牌
        :param name: 点数
        :return:
        """
        cards = set()
        cards.add(Card(name, "黑桃"))
        cards.add(Card(name, "红桃"))
        cards.add(Card(name, "梅花"))
        cards.add(Card(name, "方块"))
        return cards

    @staticmethod
    def int_car():
        """
        生成一副扑克
        :return:
        """
        card_list = set()
        for i in range(1, 14):
            if i == 1:
                cards = Card.get_type_4_card("A")
                card_list.update(cards)
            elif i == 11:
                cards = Card.get_type_4_card("J")
                card_list.update(cards)
            elif i == 12:
                cards = Card.get_type_4_card("Q")
                card_list.update(cards)
            elif i == 13:
                cards = Card.get_type_4_card("K")
                card_list.update(cards)
            else:
                cards = Card.get_type_4_card(str(i))
                card_list.update(cards)

        return card_list


if __name__ == "__main__":
    card_set = Card.int_car()
    for card in card_set:
        print(card)
