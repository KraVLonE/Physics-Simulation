# Physics Simulation

## About
This project simulates a physics environment where balls can bounce off the walls and collide with each other. The simulation includes gravitational effects, elastic and inelastic collisions, and interactive controls to modify physics parameters during runtime.

## Usage
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/PhysicsSimulation.git
    cd PhysicsSimulation
    ```
2. Install Pygame if you don't have it installed:
    ```sh
    pip install pygame
    ```
3. Run the simulation:
    ```sh
    python main.py
    ```
4. Follow the prompts to input the initial conditions for the balls.

## Demo

<video width="600" controls>
  <source src="Demo.webm" type="video/webm">
</video>



When you run the simulation, you will be prompted to enter the number of balls and their properties (position, velocity, radius, mass, and color). You can then watch the balls interact with each other. Use the following keys to interact with the simulation:
- Press `G` to increase gravity.
- Press `F` to decrease gravity.
- Press `E` to increase the coefficient of restitution (more elastic collisions).
- Press `I` to decrease the coefficient of restitution (more inelastic collisions).

## Example Input
```python
Enter the number of balls: 3
Enter position (x y): 100 100
Enter velocity (vx vy): 2 3
Enter radius: 20
Enter mass: 1
Enter color (R G B): 255 0 0
Enter position (x y): 300 300
Enter velocity (vx vy): -1 2
Enter radius: 25
Enter mass: 1
Enter color (R G B): 255 255 255
Enter position (x y): 200 200
Enter velocity (vx vy): -2 -1
Enter radius: 30
Enter mass: 1.5
Enter color (R G B): 0 0 255
```
