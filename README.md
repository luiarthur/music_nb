# music_nb
a music notebook

# Introduction
This project provides a notebook for musicians who are familiar with scripting.
It makes use of [abcjs][1]


# Installation

1. Clone the repository
2. Add these lines to `bashrc`, 

```bash
export MUSICNB_HOME=path/to/music_nb/
export PATH=$MUSICNB_HOME/bin:$PATH
```

# Getting Started

1. In a terminal, create a new directory, say `notes`
2. In the new directory, enter the command `musicNB`
    - This will generate a `_notes` directory and a hidden `.html` directory
      if they don't already exist. 
    - A server will also be started at port 7777.
    - In a web browser, go to `localhost:7777` and you should see a sample file [sample_abc.mnb][2]. (`mnb` is the file extension for your notebooks.)
    - You can type notes, add headers, and type `absjs`-style music in `music{;}` blocks. See the [sample_abc.mnb][2] file for an example. You can also explore the [absjs][1] site to learn how to use the music notation. It will also be helpful to learn abc music notation from a site like [this][3].
3. The page rendered in the browser will look like this:

> ![sample_img][4]


[1]: https://abcjs.net/#what)
[2]: _notes/sample_abc.mnb
[3]: http://www.lesession.co.uk/abc/abc_notation.htm
[4]: misc/sample.jpg

