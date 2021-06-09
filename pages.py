from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Example1(Page):
    pass


class Example2(Page):
    pass


class Example3(Page):
    pass


class Example4(Page):
    pass


class Decision1(Page):
    form_model = 'player'
    form_fields = ['first_choice_1', 'second_choice_1']

    def error_message(self, values):
        print('values is', values)
        if (values['first_choice_1']+1 != values['second_choice_1']) \
                and (values['first_choice_1'] != 0) \
                and (values['second_choice_1'] != 0):
            return 'Los valores deben ser consecutivos. Por ej. Si se escogio la loteria A hasta la decision 2, ' \
                   'se debería elegir la lotería B desde la decisión 3'

        if (values['first_choice_1'] == 0) and (values['second_choice_1'] != 1) and (values['second_choice_1'] != 0):
            return 'Si va a escoger solo la segunda lotería en cada decisión, escoja la opción "Ninguna" en la primera' \
                   ' casilla y "1" en la segunda'

        if (values['first_choice_1'] != 14) and (values['first_choice_1'] != 0) and (values['second_choice_1'] == 0):
            return 'Si va a escoger solo la primera lotería en cada decisión, escoja la opción "Ninguna" en la segunda' \
                   ' casilla y "14" en la primera'

        elif (values['first_choice_1'] == 0) \
                and (values['second_choice_1'] == 0):
            return 'Si va a escoger solo una de las loterias en cada decisión, escoja la opción "Ninguna" en la casilla ' \
                   'correspondiente, no en los dos'


class Decision2(Page):
    form_model = 'player'
    form_fields = ['first_choice_2', 'second_choice_2']

    def error_message(self, values):
        print('values is', values)
        if (values['first_choice_2']+1 != values['second_choice_2']) \
                and (values['first_choice_2'] != 0) \
                and (values['second_choice_2'] != 0):
            return 'Los valores deben ser consecutivos. Por ej. Si se escogio la loteria A hasta la decision 2, ' \
                   'se debería elegir la lotería B desde la decisión 3'

        if (values['first_choice_2'] == 0) and (values['second_choice_2'] != 15) and (values['second_choice_2'] != 0):
            return 'Si va a escoger solo la segunda lotería en cada decisión, escoja la opción "Ninguna" en la primera' \
                   ' casilla y "15" en la segunda'

        if (values['first_choice_2'] != 28) and (values['first_choice_2'] != 0) and (values['second_choice_2'] == 0):
            return 'Si va a escoger solo la primera lotería en cada decisión, escoja la opción "Ninguna" en la segunda' \
                   ' casilla y "28" en la primera'

        elif (values['first_choice_2'] == 0) \
                and (values['second_choice_2'] == 0):
            return 'Si va a escoger solo una de las loterias en cada decisión, escoja la opción "Ninguna" en la casilla ' \
                   'correspondiente, no en los dos'


class Decision3(Page):
    form_model = 'player'
    form_fields = ['first_choice_3', 'second_choice_3']

    def error_message(self, values):
        print('values is', values)
        if (values['first_choice_3']+1 != values['second_choice_3']) \
                and (values['first_choice_3'] != 0) \
                and (values['second_choice_3'] != 0):
            return 'Los valores deben ser consecutivos. Por ej. Si se escogio la loteria A hasta la decision 2, ' \
                   'se debería elegir la lotería B desde la decisión 3'

        if (values['first_choice_3'] == 0) and (values['second_choice_3'] != 29) and (values['second_choice_3'] != 0):
            return 'Si va a escoger solo la segunda lotería en cada decisión, escoja la opción "Ninguna" en la primera' \
                   ' casilla y "15" en la segunda'

        if (values['first_choice_3'] != 35) and (values['first_choice_3'] != 0) and (values['second_choice_3'] == 0):
            return 'Si va a escoger solo la primera lotería en cada decisión, escoja la opción "Ninguna" en la segunda' \
                   ' casilla y "35" en la primera'

        elif (values['first_choice_3'] == 0) \
                and (values['second_choice_3'] == 0):
            return 'Si va a escoger solo una de las loterias en cada decisión, escoja la opción "Ninguna" en la casilla ' \
                   'correspondiente, no en los dos'

    def before_next_page(self):
        self.player.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        final_payoff = self.participant.payoff_plus_participation_fee()
        return dict(f_p=final_payoff)


page_sequence = [Introduction, Example1, Example2, Example3, Example4, Decision1, Decision2, Decision3, Results]
