# Contribution Guidelines

## Requirements

* **Optimization:** All code must be optimized for small Linux computers and the Raspberry Pi Pico 2. Avoid heavy libraries that cause lag.
* **Naming:** Variable names must follow Python naming conventions (`snake_case`) or be clear enough to understand "from a mile away."
* **Forking:** Forking is allowed for this repo for personal use (per our Apache 2.0 license). But forking requires the [LICENSE](./LICENSE) to be avaible and the headers in every file too.
* **Branching:** Please create a specific branch for your feature. We prefer you open a "Draft Pull Request" (unfinished) so we can see your progress.
* **Pull Requests:** To submit, use the "New Pull Request" button. Use your branch as the "compare" branch. Please add relevant tags, a clear title, and a detailed description.
* **Libraries:** To use "Tailings" it requires libraries. To intall libraries first intall python next run ```python -m venv .venv``` then run ```source .venv/bin/activate``` . After that run ```pip install -r requirements.txt```
* **Linux Usage:** Sadly contributing requires linux, but you can use a raspberry pi and use ssh so nothing to worry over.
