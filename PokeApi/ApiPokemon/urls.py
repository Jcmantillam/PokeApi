from rest_framework import routers
from ApiPokemon.views import Evolution_chainViewSet,PokemonViewSet

router = routers.DefaultRouter()
router.register('api/evolutions', Evolution_chainViewSet, 'evolutions')
router.register('api/pokemons', PokemonViewSet, 'pokemons')

urlpatterns = router.urls