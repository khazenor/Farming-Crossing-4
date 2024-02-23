ServerEvents.recipes(event => {
  event.shapeless('kubejs:miles_ticket', [
    '#forge:corundum_clusters', '#forge:corundum_clusters',
    '#forge:corundum_clusters', '#forge:corundum_clusters'
  ])
})

ServerEvents.tags('item', event => {
  event.add('forge:corundum_clusters', [
    "quark:black_corundum",
    "quark:blue_corundum",
    "quark:green_corundum",
    "quark:indigo_corundum",
    "quark:orange_corundum",
    "quark:red_corundum",
    "quark:violet_corundum",
    "quark:white_corundum",
    "quark:yellow_corundum",
    "quark:black_corundum_cluster",
    "quark:blue_corundum_cluster",
    "quark:green_corundum_cluster",
    "quark:indigo_corundum_cluster",
    "quark:orange_corundum_cluster",
    "quark:red_corundum_cluster",
    "quark:violet_corundum_cluster",
    "quark:white_corundum_cluster",
    "quark:yellow_corundum_cluster"
  ])
})