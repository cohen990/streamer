#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>
#include "fmodex/fmod.h"

int main()
{
    // Use FMOD because sfml doesn't support mp3
    sf::RenderWindow window(sf::VideoMode(200, 200), "SFML works!");
    sf::CircleShape shape(100.f);
    shape.setFillColor(sf::Color::Green);

    sf::Music music;

    if (!music.openFromFile("../song.mp3"))
    {
        exit(0);
    }

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        window.draw(shape);
        window.display();


        music.play();
    }

    return 0;
}