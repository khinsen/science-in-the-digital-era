Nearly all nontrivial information systems are assemblies of components, often produced independently by different people. Components meant to be used in different contexts are either designed to be *reusable* or *re-editable*.

Software libraries and datasets are the most common examples of reusable components. They are designed to be integrated into an assembly without any modification or adaptation.

Project templates (e.g. for use with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)) and configuration templates are examples of re-editable components. The integrator must study them and then adapt them to the particularities of the system being assembled.

The term "re-editable" was coined by [Donald Knuth](Donald%20Knuth.md) in an [interview](https://www.informit.com/articles/article.aspx?p=1193856) in 2008. He expresses a clear preference for re-editable over reusable software:

> I also must confess to a strong bias against the fashion for
> reusable code. To me, "re-editable code" is much, much better than
> an untouchable black box or toolkit. I could go on and on about
> this. If you’re totally convinced that reusable code is wonderful, I
> probably won’t be able to sway you anyway, but you’ll never convince
> me that reusable code isn’t mostly a menace.

The mainstream view in software engineering, and also in scientific computing, is the opposite. The accepted ideal is a software library with thorough documentation and an equally thorough test suite, maintained by a stable team of competent professionals. Developers needing the functionality of such a library use it as-is and design their own client code around it. In the maintenance phase, they update libraries as quickly as possible. In case of breaking changes to the interfaces, they adapt their own code.

Both approaches have their good and bad sides. The arguments in favor of reusable components are mainstream and easy to find. But which are the advantages of re-editable components? I can't speak for Donald Knuth, who doesn't go into details in the interview, but I can offer my own thoughts.

A particularity of software in [computer-aided research](Computer-aided%20research.md) is its double role as a tool and as an expression of scientific models and methods. Reusable software is designed to be used as a black box, without a deep understanding of its implementation, even when this implementation is accessible ([Open Source](Open%20Source.md)). It is also designed to be useful in a wide range of applications. Re-editable software, on the other hand, is designed to be read and understood by its users, and also more focused on the application its designer had in mind. This makes re-editable software more valuable as a readable expression of scientific models and methods. Moreover, it encourages or even forces its users to read the code and understand what it does, reducing the risk of inappropriate use of the science it embodies. Such inappropriate use is in my opinion an important but little discussed cause of the [reproducibility crisis](Reproducibility%20crisis.md) in science.

Comparing software to material artifacts, reusable software is analogous to industrial products, whereas re-editable software corresponds to bespoke artifacts made by a craftsperson. The mere fact that craftspeople still exist after two centuries of industrialization, even though their products are usually much more expensive, indicates that there is a value in non-standard artifacts based on simpler designs. They are obviously better adapted to their specific context, but they are also more repairable, and adaptable in case of evolving needs. Re-editable software shares those advantages.

Further reading:
 - [Reusable vs. re-editable code](https://doi.org/10.1109/MCSE.2018.03202636) ([preprint](https://hal.archives-ouvertes.fr/hal-01966146))
