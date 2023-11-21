The concept of an *environment* is widely used but vaguely defined. If you check its definition in a few dictionaries, you will find different though not incompatible definitions. The general idea is that an environment consists of things around you that you may not be aware of individually, but that matter for you as a whole.

In the context of software, the term "environment" most often refers to [computational environments](Computational%20environment.md), which are the hardware and software stacks that support the execution of a specific program. There are, however, two other kinds of environments that matter in scientific computing. Their conflicting requirements for scientific software is the cause for many difficulties that computational science is facing today. I will call them the *technological* and the *scientific* environment.

The technological environment of a piece of software consists of hardware and other software that influences its design and implementation. This may seem similar to the computational environment, but the differences are profound and important. A computational environment consists of concrete machines and concrete bit sequences in memory, as used when a program is run. A technological environment consists of hardware and software as artifacts that evolve over time. Moreover, it includes hardware and software that has *some* relation to the software under consideration, even if that relation is not a dependency relation. A good example is past hardware that is no longer relevant in practice, but was relevant when the software was initially designed. Another example is software running elsewhere that the software under consideration exchanges data with. If the software under consideration is a Web server, its technological environment includes all client software it is supposed to work with. A good way to visualize the relation between technological and computational environments is the following: a computational environment is a *snapshot* of a *subset* of the technological environment, with the subset defined by dependency relations.

The scientific environment of a piece of software consists of the discipline in which it was designed and the research projects in which it is used. It defines the *interpretation* of the software and its behavior by its users. Like the technological environment, it evolves over time as new methods are developed, older methods become obsolete, and the community's view of best practices changes.

As an illustration of the roles of the three environments, consider the following simple Python program:
```python
from datalib import Dataset

points = [(1, 1), (-1, 1), (2, 4)]

data = Dataset()
for x, y in points:
    if x > 0:
        data.add_value(y)
print(data.average())
```

I have shown this code frequently in talks about reproducible research, and asked the audience what its output is. The most common answer is `2.5`, which is the average of the `y` coordinates of the points whose `x` coordinates are positive. This is indeed the *expected* output according to the *scientific* environment, which assigns meanings to names such as `Dataset`, `add_value`, and `average`.

Experienced computational scientists who think a bit about the question before answering will come up with a different answer: the output depends on the imported module `datalib`. In fact, all the named data and operations are defined in this library module, and you can't really know how what they do until you have seen its code as well.

Consider the following implementation of `datalib`:
```python
class Dataset(object):

    def __init__(self):
        self.values = []

    def add_value(self, value):
        self.values = [value]

    def average(self):
        return sum(self.values, 0)/len(self.values)
```

The implementation of `add_value` is different from the expectation defined by the scientific environment. The latter says that adding a value to a dataset increases the number of data points by one. The code says that the method `add_value` replaces the points of the dataset by a single one.

In this simple case, we call the discrepancy between expected and actual behavior a bug. Real-life cases are more complex and subtle. What the code is expected to do may not be fully consensual in a community. A good example is the average of a list of floating-point values, for which there are many reasonable definitions although many scientists are not aware of this diversity. And what the code actually does is defined by the computational environment, which is usually incompletely defined and not reproducible. It is therefore difficult to assign blame for the discrepancy to anyone or anything more specific than the state of the art of computational science.

Another source of conflict is the different expectations about the time evolution of scientific software. The scientific environment expects software to evolve with its application domain. As concepts are refined and methods improved, code should follow along. The technological environment expects software to be "maintained", which means changed to remain functional as the technological environment itself evolves.

In practice, both tasks are handled in parallel by a single team of developers and maintainers. This doesn't always work out well, because teams tend to be dominated by either technology-aware software engineers or application-aware scientists. Whichever group dominates tends to see other group's focus as a distraction, or even a nuisance. There are two situations which are generally handled satisfactoryly. The first one is a very stable scientific environment, with software tracking its technological environment. This happens for implementations of well-known and widely used algorithms, for example Fourier transforms. The second one is the scientific environment evolving faster than the technological one. In that case, the team implementing "new science" handles code maintenance as a side task. The badly handled scenario is the scientific environment evolving at a slower rate than the technological one. This often ends in [software collapse](Software%20collapse.md).

Let's have another look at the Python example shown above. I have already explained why the scientific environment expects its result to be `2.5`. But what's the perspective of the technological environment? It sees the code as a Python program, with no interpretation of names. The code runs without raising an exception, so there's no reason to suppose a bug. And the output is... `4`. At least for Python versions before 3.0. With Python 3, the new semantics for float division change the output to `4.0`. In fact, what the technological environment's perspective really says is that the output depends on the computational environment, even in the hypothetical complete absence of bugs. Most of today's scientific environments still have a hard time understanding and accepting this fact, which is why [computational reproducibility](Computationa%20reproducibility.md) is still an unsolved problem in practice, even though it is fully understood in theory.
