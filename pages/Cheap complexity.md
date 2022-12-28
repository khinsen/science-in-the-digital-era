In a [2018 talk at CyCon](http://rule11.tech/papers/2018-complexitysecuritysec-dullien.pdf), a [conference on cyber conflict](https://cycon.org/), Thomas Dullien identifies one of the root causes of increasing security issues with computing technology as "the anomaly of cheap complexity." A quote from page 8:

    For most of human history, a more complex device
    was more expensive to build than a simpler device.

    This is not the case in modern computing. It is
    often more cost-effective to take a very
    complicated device, and make it simulate simplicity,
    than to make a simpler device.

What causes this anomaly is economies of scale driving the development of complex general-purpose computing hardware, which can then simulate any simpler machine using software, whose cost at scale is much lower. Unfortunately, the complexity of the general-purpose hardware tends to create unexpected behavior, which evil-minded adversaries can exploit in attacks.

What I would like to point out in the following is that (1) cheap complexity is also an issue in science and (2) it occurs in software for much of the same reasons as in hardware. I will start with point 2, because it is the main contribution to point 1.

Software may be cheaper at scale (i.e. as the number of its users grows) than hardware, requiring no material resources, but producing software is nevertheless very expensive. It thus becomes advantageous to develop complex general-purpose software, whose development cost is shared by a larger number of users, than simpler [situated software](Situated%20software.md) serving only few users. Assuming, of course, that the complexity incurs no excessive cost in development. Every software developer knows that complexity does come at a price, in the form of [technical debt](Technical%20debt.md). However, the software industry has so far escaped from paying the cost because it is not held responsible for the problems caused by bad software. As an illustration, computer viruses have caused enormous economic damage, and yet the companies selling the software that viruses attack are not held responsible for this damage, which is attributed to inadequate vigilance by its users instead. It's thus users who pay the price for the complexity of software.

So why does all this matter for science? Security is rarely a concern in [computer-aided research](Computer-aided%20research.md), at least not beyond issues such as viruses, which affect all users of computers. The enemy of science is not an evil-minded hacker, but good old human nature, well-known to be prone to making mistakes. Science is all about the acquisition of [reliable knowledge](Reliable%20knowledge.md). If the knowledge is encoded in [computational media](Computationa%20media.md), using computational tools, then those tools had better be reliable as well. Complexity is the enemy of reliability. And we all know from first-hand experience that our computers and the software they run are not reliable. How often do you reboot your computer to fix a problem? How often do you install security updates? Is it reasonable to believe that *scientific* software is exempt from these complexity-related reliability issues, just because its failures are less spectacular?

So what do complexity-related failures in computer-aided research look like? The first ones that come to mind are wrong results. Unfortunately, we most often don't know the correct result when we compute something in research, so we never know if a result is correct. Perhaps the most visible failures that we can easily observe are [reproducibility](Computational%20reproducibility.md) failures. If a computed result is not reproducible, we don't really know what has been computed (because computation, being deterministic, *is* reproducible). In most cases, we don't know what has been computed because we don't know which precise software stack we have been running. And we don't know the precise software stack because the software stack is too complex to be easily described and reconstructed. As I explain under [Computational reproducibility](Computational%20reproducibility.md), that problem is solved in principle, and increasingly also solved in practice, by delegating the management of software stacks to computers. Except that... the management software for software stacks is pretty complex as well!

The ultimate solution to the problem of cheap complexity is, of course, paying the higher price for simpler technology. In the not-so-distant past when complexity wasn't cheap, innovation, whether in science or technology, was followed by a phase of consolidation. New scientific knowledge, once it became reliable, was reformulated in ever simpler and more compact ways. Compare, for example, Isaac Newton's "Principia Mathematica" to a modern explanation of the same theory in a textbook for physics students. The modern version is more compact and much easier to understand. The same process happens in technology, for example when breadboard prototypes for electronic circuits get redesigned into printed circuit boards and then integrated circuit chips for industrial mass production. Could this approach work for software and digital scientific knowledge as well? We won't know before we try!