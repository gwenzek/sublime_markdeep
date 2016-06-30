# Markdeep

[Markdeep](https://casual-effects.com/markdeep) is a Markdown-like language to generate web pages.
IMHO the main avantages versus Markdown are:

- Markdeep doesn't need compilation, it can directly been opened in a browser. 
- Markdeep can embed Latex formula (with `$ ... $` for inline Latex or `$$ ... $$` for blocks).
- Markdeep have table of contents.

More information are available on the [Markdeep site](https://casual-effects.com/markdeep).

# Getting started

Once this plugin has been installed in Sublime Text,
open a file, change the syntax to Markdeep, type `markdeep` press `TAB`.
You have inserted a snippet containing a simple Markdeep document.
Markdeep supports most of the syntax of Markdown, so it's esay to start using it !

There is two ways of naming your Markdeep files.

- `*.md.html` will be open in the default browser by the system, but as `html` by Sublime.
- `*.md-html` will be open as Markdeep by Sublime, but you'll have to configure your system to open it in a web browser.

I personally use the second option for editing files, but if I share them with others I rename them in `md.html`.

Once your file is saved to the disk, you can use `File: Open in browser` to see you Markdeep in browser.
To refresh your browser as soons as you modified your file, I recommend the Firefox [Auto Reload plugin](https://addons.mozilla.org/en-US/firefox/addon/auto-reload/).

# Differences with Markdown

## Code blocks
Code blocks starts and ends with `~~~`. You can use the `~~` snippet to create a code block.
You can add a language to your code block, allowing both Sublime and Markdeep to provide better syntax coloration for it:

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ python
def hello():
    print 'hello world'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

# Note to developers

Feature requests and feedback are welcomed.
The syntax is forked from the Markdown syntax which as several problems.
For one it uses a lot of advanced regexes not supported by Sublime latest engine.

# Final remarks

I'm using Markdown to write this, just because Github doesn't allow `html` Readme (and therefore `md.html`) !
