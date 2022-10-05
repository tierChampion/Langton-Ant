# Langton-Ant

Pygame Langton Ant simulation. Langton's ant is a Turing complete cellular automata with emergent behaviour. The original version follows two simple rules: if it steps on a black or an "OFF" cell, then it turns right and if it steps on a white or an "ON" cell it turns left. It then takes a very chaotic path for about 10,000 steps to finally follow a very structured diagonal repeating path forever called a "Highway".

## Implementation

This project allows for many different modifications to the regular Langton's ant. The first one is the addition of more than two rules or more than two states/color of cells. The second modification is the addition of a state to the ant that also gets modified when it moves. The third modification is the generalisation of the rules. This means that a rule takes into consideration the state of the cell and the state of the ant while modifying these states to any new states. Finally the last addition are the two new shape of tiles: Hexagons and Triangles. 

Hexagons have six different moves and are tiled while moving slightly up and down while triangles have only three moves and are tiled while flipping every other triangle. This gives very different behaviours between these three shapes.

The general version of the Langton's ant is called a Turmite. Since there are three Turmites, they will be called respectively 3-Turmite, 4-Turmite and 6-Turmite.

## Common patterns

This next section is all about the possible patterns that can be encountered with the different N-Turmites.

### Square

The general patterns of the 4-Turmites are:

- Highways
- Never-ending
- Growing
- Networks
- Islands
- Builders
- Many more...

### Triangle

The general patterns of the 3-Turmites are:

- Highways
- Screen filling
- Growing

In general, the 3-Turmite is very chaotic and doesn't give a lot a intersting patterns.

### Hexagon

The general patterns of the 6-Turmites are:

- Highways
- Spirals
- Textured surfaces
- Builders
- Islands
- Growing
- Loops
- Counters
- Many more...

Overall the 6-Turmite is the most interesting with the greatest diversity of strange patterns



