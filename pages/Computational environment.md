Although now frequently used in the context of [computational reproducibility](Computational%20reproducibility.md), the term "computational environment" is rather recent. It usually refers to the software infrastructure required to run a specific computation: operating system, compilers, interpreters, support libraries, etc. Sometimes it is used in a wider sense that includes the actual hardware on which a computation runs.

Computational environments are the main focus of research and development around computational reproducibility because now that the actual preservation of code is a solved problem (see [Software Heritage](https://www.softwareheritage.org/)), the documentation and preservation of computational environments is the biggest unsolved one.

A computation, as defined by Alan Turing in his [famous 1937 paper](https://doi.org/10.1112/plms/s2-42.1.230) that introduced the [Turing machine](Turing%20machine.md), is a transformation of a a string of input symbols into a string of output symbols via the application of well-defined rules. In today's computers, the symbols are bits (0 or 1), so a computation is the transformation of an input bit sequence to an output bit sequence, the rules being roughly the processor's instruction set.

Human computer users like to divide the input bit sequence into *code* and *input data*, the idea being that "active" code operates on "inert" data. While this is very useful distinction in terms of computer applications, it belongs to the realm of interpretation. For the computer, it's all bits. One way to see that code vs. data is a matter of interpretation is to consider an alternative one: the format of the input data can be seen as a formal language, for which the code reading the data is an interpreter. In this interpretation, everything is code.

Next, human users like to divide the code into a *program* that is run and the *environment* that supports the program. This is an even more arbitrary dividing line. It comes down to a distinction between "the code that I care about" (the program) and "the code that I don't care about" (the environment). The computer cares equally about each bit in its input.

A computation is reproducible if the full input bit sequence is preserved and can be replayed: input data, the code that the authors of the computation care about, but also the code they don't care about. Is it really surprising that all the trouble comes from the code we don't care about? Starting to care about one's computational environments is the key step to improving computational reproducibility.

Today, preserving and replaying computational environments bit by bit has become relatively easy. Container images, via management tools such as [Docker](https://www.docker.com/) or [Singularity](https://sylabs.io/docs/), do the trick. Unfortunately, that has proven insufficient for making computer-aided research reproducible. Container images ensure reproducibility for computers (bits, it's all just bits!), but not for humans. For a human user, a container image proves exactly one fact: that there exists a computer program that produces a given result. Which, for a digital result, is a rather trivial fact. Human users need to *understand* the computation at the level of their *interpretation* of inputs, code, and outputs. Human users need *source code*.

Computational environments being digital artifacts, created via computation (see "[The dual nature of software](The%20dual%20nature%20of%20software.md)"), they always have source code, but we don't yet care enough about environments to (1) preserve this source code (it's often a few lines of shell commands typed in by hand) and (2) make it reproducible. The good news is that this is possible, and even supported by existing tools such as [Guix](Guix.md). As a simple example, the following two source code files fully define a computational environment, bit by bit:

File "manifest.scm":
```
(specifications->manifest
  (list "python"
        "python-matplotlib"
        "python-numpy"))
```

File "channels.scm":
```
(list (channel
        (name 'guix)
        (url "https://git.savannah.gnu.org/git/guix.git")
        (branch "master")
        (commit
          "35b176daf1a466f136f0b77c03de78f482a30702")))
```

Given those two files, and a computer with an installation of [Guix](Guix.md), the environment can be re-created using the command
```
guix time-machine -C channels.scm -- guix shell -m manifest.scm
```
On two computers that have compatible processor instruction sets, this will create environments that are identical, bit for bit.

Why does the source code of an environment consist of two files? Because the creators of Guix decided to separate the list of the software building blocks in the environment (`manifest.scm`) from the list of their precise versions (`channels.scm`), in order to make it easier to vary the versions and thus test for the robustness of the computation. It's a minor technical design decision.

Are you ready to start caring about your computational environments? Then take a serious look at Guix.


Recommended reading:
  - [Dealing with software collapse](https://doi.org/10.1109/MCSE.2019.2900945) ([preprint](https://hal.archives-ouvertes.fr/hal-02117588))
  - [A Dream of Simplicity: Scientific Computing on Turing Machines](https://doi.org/10.1109/MCSE.2017.39) ([preprint](https://hal.archives-ouvertes.fr/hal-02117720))
