Feature: Site Navigation Menu

Scenario: Navigate to characters
    Given that I am a user on SWARM.
    When I open the menu
    And I select characters
    Then I should see a random character bio
    And I should see a picture of that character

Scenario: Navigate to spaceships
    Given that I am a user on SWARM
    When I open the menu
    And I select spaceships
    Then I should see a choice of Factions on a timeline

Scenario: Navigate to planets
    Given that I am a user on SWARM
    When I open the menu
    And I select planets
    Then I should see a visualization of the Star Wars universe

Scenario: Navigate to species for planet
    Given that I am a user on SWARM
    And I navigate to planets
    When I select a planet
    Then I should see species information for that planet