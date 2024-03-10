# Explanation of the Predator-Prey Simulation Algorithm

## Introduction

The provided algorithm simulates a predator-prey ecosystem within a grid environment, where wolves (predators) and sheep (prey) interact with each other and with their environment, represented by grass. This simulation is a simplified model of real-world ecological dynamics, capturing essential aspects like **reproduction, starvation, and overcrowding**.

## Environment Setup

The simulation environment is a 20x20 grid where each cell can contain a wolf, a sheep, grass, or be empty. The initial population of wolves and sheep is determined randomly based on predefined spawn probabilities:

- Wolves have a 5% chance of spawning in any given cell.
- Sheep have a 20% chance of spawning in any given cell.
- Cells that don't spawn wolves or sheep are filled with grass.

This setup creates a diverse environment where the initial number of entities varies with each simulation run, introducing variability and mimicking natural ecosystems' unpredictability.

## Entity Behavior

### Wolves (Predators)

Wolves move through the grid, seeking adjacent sheep to eat. If a sheep is found in a neighboring cell, the wolf moves to that cell, consuming the sheep, which is then removed from the grid. If no adjacent sheep are available, wolves have an 80% chance of starving and are removed from the grid if they don't eat.

After eating a sheep a wolf can reproduce if there's another wolf in an adjacent cell and an empty cell nearby to place the new wolf. The reproduction probability is 5%, reflecting the challenges in offspring survival.

### Sheep (Prey)

Sheep behave similarly to wolves but seek grass instead of other entities. If adjacent grass is available, a sheep will move to that cell, consuming the grass. If no grass is nearby, sheep have an 80% chance of starving.

After eating grass, sheep reproduction follows the same rules as wolves, with a 15% chance if another sheep is adjacent and there's available space.

### Overcrowding

Both wolves and sheep face the risk of death due to overcrowding. If more than three wolves or sheep are adjacent to a cell, the entity in that cell dies, simulating natural mechanisms where high population density can lead to increased competition for resources and higher mortality rates.

## Initial Setup

![initial_setup](./images/initial_setup.png)

## Simulation Loop

The simulation progresses in cycles, where each cycle involves randomly selecting a grid cell and executing the behavior logic for the entity in that cell. This process includes movement, eating, potential starvation, reproduction, and overcrowding checks.

The simulation continues as long as there are wolves or sheep present in the grid, reflecting an ongoing ecosystem. However, if one species goes extinct, the dynamics change significantly, demonstrating the interdependence of species within ecosystems.

## Simulation Environment Variations

To explore different ecological dynamics, we can adjust the simulation parameters. Here are three sets of values designed to simulate various environmental conditions:

### Set 1: Stable Ecosystem

- `wolf_initial_spawn`: 3% - A lower initial wolf population to reduce predation pressure.
- `sheep_initial_spawn`: 25% - A higher initial sheep population ensures ample food for wolves.
- `wolf_reproduction_prob`: 4% - A moderate wolf reproduction rate to maintain population balance.
- `sheep_reproduction_prob`: 15% - A higher sheep reproduction rate supports predator sustenance.
- `wolf_starvation_chance`: 15% - A lower chance of wolf starvation indicates sufficient prey availability.
- `sheep_starvation_chance`: 5% - A lower chance of sheep starvation suggests abundant grass.

This configuration aims to create a balanced ecosystem where both predator and prey populations can sustain themselves over time.

### Set 2: Predator-Heavy Environment

- `wolf_initial_spawn`: 10% - A higher initial wolf population increases predation.
- `sheep_initial_spawn`: 15% - A lower initial sheep population introduces more competition among wolves.
- `wolf_reproduction_prob`: 8% - An increased wolf reproduction rate to test the impact on prey.
- `sheep_reproduction_prob`: 10% - A moderate sheep reproduction rate under higher predation pressure.
- `wolf_starvation_chance`: 30% - A higher chance of wolf starvation due to increased competition.
- `sheep_starvation_chance`: 20% - An increased chance of sheep starvation as they are more likely to be preyed upon.

This set represents an environment where predators are more dominant, potentially leading to rapid prey depletion and higher starvation risks for predators.

### Set 3: Prey-Heavy Environment

- `wolf_initial_spawn`: 2% - A very low initial wolf population minimizes predation pressure.
- `sheep_initial_spawn`: 30% - A very high initial sheep population could lead to overgrazing.
- `wolf_reproduction_prob`: 5% - A moderate wolf reproduction rate in a prey-rich environment.
- `sheep_reproduction_prob`: 20% - A very high sheep reproduction rate could lead to population booms.
- `wolf_starvation_chance`: 10% - A lower chance of wolf starvation due to abundant prey.
- `sheep_starvation_chance`: 5% - A lower chance of sheep starvation, assuming grass is plentiful.

This configuration simulates an environment where prey is abundant, potentially leading to overgrazing and subsequent challenges for the prey population.

## Conclusion

This algorithm offers a simplified yet insightful representation of predator-prey dynamics, illustrating how individual behaviors can lead to complex system-level behaviors in ecology. By adjusting parameters like spawn probabilities and starvation chances, users can explore different ecological scenarios, gaining a deeper understanding of the delicate balance within natural ecosystems.
