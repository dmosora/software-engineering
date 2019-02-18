## Folder Structure

Behave requires a strict naming scheme and folder structure out of the box. Features should be in `./features` and associated step implementations need to be in `./features/steps` with an appropriate name. If none of these things line up, running `behave` will result in `NotImplementedException`s for missing steps or `ConfigError: No steps directory in '/<current_directory>/features'`

## Setup

For running on Coder.com, follow the setup instructions in the [wiki](https://github.com/dmosora/software-engineering/wiki/Selenium-on-Coder.com).
