# Test Driven Development (TDD) Playground

## Overview of the Product

SWARM (Star Wars Application for Reading Metadata)

A website for displaying information about the Star Wars universe.

## Requirements

Since I am the user, I am generating the requirements based on what I would like to see from this kind of site.

- Character Cards - Bios with images, maybe video, movies they've been in, etc.
- Spaceship Information
- Planet Organization
    - Species Information

## Risks and Unknowns

[The Star Wars API](https://swapi.co/)
    - The structure of the data, ease of retrieving data, unknown
External Data Stores Required?
    - Caching, intermediate joining of data?
    - A: Punt on this, bring it in when required in an XP fashion (YAGNI)
UI Styling (HTML/CSS)
    - Bio cards with images of characters?
    - Prototype this: Marvel -> HTML -> CSS

## Spiking

First prototype is to figure out what the data looks like coming from the SWAPI.
Then we can make a reasonable mock to start using TDD to get the backend up and running.

## BDD User Stories

( ***Focusing on the "What" not the "How".*** For example, parts of these stories might be redundant, the "I am a user on SWARM" step will be a starting piece throughout the suite.

I already started to refine away from the "When I open the menu And I select the <blank>" because that was more about the "How" not the "What")

### Epic: Initial Website

### Feature: Capturing the General Menu Actions

#### User Story: Navigating Around the Website

```
Given that I am a user on SWARM.
When I open the menu
And I select characters
Then I should see a random character bio
And I should see a picture of that character

Given that I am a user on SWARM
When I open the menu
And I select spaceships
Then I should see a choice of Factions on a timeline

Given that I am a user on SWARM
When I open the menu
And I select planets
Then I should see a visualization of the Star Wars universe

Given that I am a user on SWARM
And I navigate to planets
When I select a planet
Then I should see species information for that planet
```

**From here, break down each of the menu segments above into user stories (then to individual scenarios) as they become sprint worthy**

## TDD

Meanwhile, I am a backend dev working on getting the data through to the front end. I know I need to use Flask, not sure how to use that right now, but I at least know I need some way to **get data from the API**, **manipulate it (possibly, spike pending)**, then **return it to the front end**. These can be written using TDD.

So, I can write some python code to get that going.

- Testing Feature/Module: Data Access Layer
    - Get Data from the API (Stub)
    - Manipulate it (Stub, unknown, unimplemented)
    - Return it to the front end - Indicates that there's a function that is called from the front end
        - Let's implement this
        - Call it `get_swapi_data()` (for now)
