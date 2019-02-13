## Folder Structure

Behave requires a strict naming scheme and folder structure out of the box. Features should be in `./features` and associated step implementations need to be in `./features/steps` with an appropriate name. If none of these things line up, running `behave` will result in `NotImplementedException`s for missing steps or `ConfigError: No steps directory in '/<current_directory>/features'`

## Setup

```
pip install selenium
pip install behave
pip install webdriver-manager
```

### Open Question

Coder.com does not come able to run using selenium running Chrome headless out of the box.
Is there a standard way to do this?