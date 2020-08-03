from django.core.management.base import BaseCommand, CommandError
from GetPokemon.services import get_evolution_chain, search_save_pokemon

#from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('chain_id', nargs=1, type=int)

    def handle(self, *args, **options):
        chain_id = options.get('chain_id', None)

        if chain_id:
            arg_id = chain_id[0]
            evol_tree = get_evolution_chain(arg_id)
            print("evol_list: ", evol_tree)
            #Añadir los pokemones del árbol
            for node in evol_tree:
                search_save_pokemon(node[0],node[1],evol_tree,chain_id)

        '''for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))'''