# Dependency graph creator

You can articulate a dependency chart in plain text, and then use <http://www.nomnoml.com> to turn it into a diagram.

## How to use

Start from your end goal.. for example "I have a cup of tea", and work your way backwards. What do you need in order to be able to have a cup of tea? A mug, tea bag, hot water, and milk. Note that you can decide how much detail to go into, but roughly, if you can see how to achieve the goal from the elements it depends on, that's about enough detail.

    I have a cup of tea
      A mug
      Tea bag
      Hot water
      Milk

Do any of those items need further work?

    I have a cup of tea
      A mug
      Tea bag
      Hot water
        Boil kettle
          Fill kettle
      Milk
        Buy milk

Once you're happy that you know how to tackle each node, you're done.

You can get a nice diagram of your dependency tree, using the script `deps-graph.py`, and <http://www.nomnoml.com>, as follows.

    ./deps-graph.py <deps.txt

It prints out the text, which you can paste into [nomnoml.com](http://www.nomnoml.com).

### My graph has gotten rather deep!

You can break out a subtree, for example.
 
    I have a cup of tea
      A mug
      Tea bag
      Hot water
      Milk
        Buy milk

    Hot water
      Boil kettle
        Fill kettle

