Agency is about exploring and shaping one's environment to achieve one's goals. Technology, including software, can both augment and constrain agency. Most technology increases the agency of some agents while constraining others. Agents can be individuals, coordinated groups of individuals (teams, families, associations), or formally structured organizations of sizes varying from a small company to a nation state or a multinational corporation.

In scientific research, agency is the ability to explore a scientific question and to critically examine the work of others. Scientific agents are individual researchers, research teams, laboratories, large-scale collaborations, or institutions such as universities or national research organizations.

The ubiquity of software in today's research has made software a critical aspect of scientific agency. Each piece of software augments the agency of some agents, to varying degrees depending on their technical competence and the learning effort they invested. On the other hand, when the use of some piece of software is imposed, by regulations or by social norms, the agency of some agents is constrained by it. Whereas the empowering aspect of scientific software is widely advertised, in particular by its developers, the category of agents that is empowered is rarely made explicit, and the category of agents that is constrained is hardly mentioned at all.

As a help for evaluating someone's agency over a piece of software, I propose the following descending scale:

**Full control.** The agent understands the software in sufficient detail to know what it does, verify its correct working, debug it, judge its adequacy for a given scientific context, and adapt it to different questions.

**Autonomous use.** The agent understands the software in sufficient detail to know what it does, confirm its correct working, and judge its adequacy for a given scientific context. The agent is not able to modify the software.

**Trusting use.** The agent can use the software based on available documentation, but must [trust](Trustworthy%20software.md) others for verifying its correctness. The agent has a mental model of how the software works, but cannot interpret the source code, for lack of access to it or for lack of technical competence.

**Constrained use.** The agent can execute the software, supply the information it requests, and retrieve information it provides. The agent does not have a detailed mental model of what the software does.

Finding one's place on that scale is not an easy task, because it depends on many aspects. It depends on the composition and competence of the agent, which can be highly variable (think of a research team composed mainly of PhD students and postdocs on short-term contracts). It depends on the software under scrutiny, but also on the technological context in which it is accessible. Consider a notebook about a data analysis. With just the notebook file and a description of its computational environment, users have high agency but only if they can handle deployment. The same notebook run on-line via [Binder](https://mybinder.org/) requires much less technical competence, but also restricts agency because users can neither inspect nor change the computational environment. This distinction also highlights the importance of the software's dependencies. The users' agency over dependencies is typically lower, and that may well be fine, but for software like scripts and notebooks that provide only the shallow top layer of a computation, agency over dependencies can be the most import criterion in the evaluation of total agency.

Tooling can augment agency, as is nicely illustrated by [computational notebooks](Computational%20notebook.md), which increase agency by facilitating interaction with the code. [Glamorous Toolkit](Glamorous%20Toolkit.md) illustrates that this idea can be taken much further if one is willing to consider alternatives to the development tools inherited from the software industry, which by design draw a sharp borderline between developers and users, augmenting the agency of the former but explicitly reducing the agency of the latter.