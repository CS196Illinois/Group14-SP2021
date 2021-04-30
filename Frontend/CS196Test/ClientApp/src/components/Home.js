import React, { Component } from 'react';
import './Home.css';

export class Home extends Component
{
    static displayName = Home.name;

    render()
    {
        return (
            <div>
            <h1>Home Page</h1>
                <h3>About Us</h3>
                <div class = "person">
                    <img src="profile picture.jpeg" alt="Pic of Anjali"></img>
                    <div class = "description">
                        <h4>Anjali Goel</h4>
                        Anjali is finishing up her freshman year at the University of Illinois
                        at Urbana-Champaign. She is majoring in mechanical engineering and hoping
                        to get a minor in computer science.
                    </div>
                </div>
                <div class="person">
                    <img src="bad pic.jpeg" alt="Default"></img>
                    <div class="description">
                        <h4>Eli Feinberg</h4>
                        Eli is a freshman at the University of Illinois
                        at Urbana-Champaign. He is majoring computer engineering.
                    </div>
                </div>
                <div class="person">
                    <img src="bad pic.jpeg" alt="Default"></img>
                    <div class="description">
                        <h4>Tinrey Du</h4>
                        Tinrey is finishing up his freshman year at the University of Illinois
                        at Urbana-Champaign. He is trying to become a computer science major.
                    </div>
                </div>
                <div class="person">
                    <img src="bad pic.jpeg" alt="Default"></img>
                    <div class="description">
                        <h4>Weixuan Zhang</h4>
                        Weixuan is a freshman at the University of Illinois
                        at Urbana-Champaign. He is majoring in mechanical engineering.
                    </div>
                </div>
            </div>
    );
    }
}
