ServerEvents.recipes(event => {
    event.shaped(Item.of('minecraft:bookshelf', 1), [
        'AAA',
        'BBB',
        'AAA'
    ], {
        A: '#minecraft:planks',
        B: 'minecraft:book'
    })
    event.shaped(Item.of('minecraft:chest', 1), [
        'AAA',
        'A A',
        'AAA'
    ], {
        A: '#minecraft:planks'
    })
    event.shaped(Item.of('minecraft:ladder', 3), [
        'A A',
        'AAA',
        'A A'
    ], {
        A: 'minecraft:stick'
    })
})