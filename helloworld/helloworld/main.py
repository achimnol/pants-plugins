# Testing relative imports inside Rust binary
# Testing absolute imports inside Rust binary
from helloworld.speaker import say_bye

from . import talker


def main():
    talker.say_hello()
    say_bye()


# In .bzl config, setting python_config.run_module = "helloworld.main" should cause this to run as the entry point
if __name__ == "__main__":
    print("Launching HelloWorld from __main__")
    main()