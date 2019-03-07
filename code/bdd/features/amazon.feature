Feature: User can search Amazon for products
  
  @run
  Scenario: Search for blenders
     Given we are browsing amazon.com
      When we search for "blender"
      Then we should see a " Blender "

  @run
  Scenario: Search for mowers
     Given we are browsing amazon.com
      When we search for "mower"
      Then we should see a " Mower "
