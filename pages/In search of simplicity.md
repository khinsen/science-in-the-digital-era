There are various ongoing attempts to create supporting technology for making simple software that empowers individuals and small groups who are not professional software developers. To the best of my knowledge, there are no commercial or large-scale activities in this sector today (although there were in the past). All of the projects I am aware of are made by people scratching their own itches. As a consequence, they are small projects by small communities, and not very visible.

None of the projects listed below of is about scientific software. Moreover, many of them take an extremist position on some aspect, which may well be incompatible with the requirements of scientific computing. I do not mention these projects here because I think scientists should adopt them. I see them as (1) proof that simplicity in software is possible if you make it a high enough priority and (2) a source of ideas for how to make software more accessible. The only discussion of related issues in the context of academic research that I am aware of is [an issue of "digital humanities quarterly" dedicated to "Minimal Computing"](http://digitalhumanities.org/dhq/vol/16/2/index.html).

The following alphabetically ordered list makes no claim to being exhaustive. It contains projects that I somehow discovered and which looked interesting enough to spend a few hours investigating them.

[Freewheeling apps](https://akkartik.name/freewheeling/) is a small software stack for personal and easy-to-modify applications with graphical user interfaces that are portable across devices and platforms. It is built on top of [LÖVE](https://love2d.org/), a game development framework for the programming language [Lua](https://www.lua.org/). There are [a few examples](https://akkartik.itch.io/) to get started. Lua is an interesting project in its own right from the simplicity point of view, because in spite of being 30 years old (just two years younger than Python), and used in various application domains, it has largely escaped the fate of creeping complexification.

[Gemini](https://gemini.circumlunar.space/) is a minimalist Web-like technology stack, replacing both the HTTP protocol and the HTML markup language by much simpler equivalents. The goal of Gemini is twofold: create a simple technology stack that is easy to implement, and eliminate features seen as undesirable by its community, such as tracking or advertising, by making them technically impossible.

The programming language [Hare](https://harelang.org/), currently in an early stage of development, has the design goal to be simple, stable, and robust. Its plan for avoiding complexification is radical: once the specification reaches version 1.0, it will be frozen forever. The stated goal is to become [a 100-year programming language](https://harelang.org/blog/2023-11-08-100-year-language/).

The [IndieWeb](https://indieweb.org/) is a community dedicated to simple Web sites based on simple standards and simple technology, outside of corporate control. It provides support for people wishing to build and host their own Web sites, using a manageable subset of the official Web standards complemented by conventions such as [microformat](https://indieweb.org/microformats).

[KolibriOS](https://kolibrios.org/en/) is an operating system for old and/or low-resource computers. It does not seem to have an explicit focus on simplicity, but requires such a focus indirectly though resource restrictions.

[Minimacy](https://minimacy.net/) is a small functional programming language, resembling [OCaml](https://ocaml.org/) with its own virtual machine and standard library. It runs inside a host operating system, but is meant to be usable without any operating system in the long run. The goal is to have a technology stack that a single software engineer can understand in its entirety, and build applications on top of it without fearing bad surprises such as [software collapse](Software%20collapse.md) or security issues.

[Smalltalk 80](https://dl.acm.org/doi/10.5555/273) is a programming system designed in the 1970s and 1980 at Xerox' Palo Alto Research Center. Its [design principles](https://www.cs.virginia.edu/~evans/cs655/readings/smalltalk.html) include the goal of "personal mastery", defined as "a system being entirely comprehensible to a single individual." Several descendants, such as [Squeak](https://squeak.org/) and [Pharo](https://pharo.org/), are still actively developed and used, but only [Cuis](https://cuis.st/) has maintained the focus on simplicity.

[UVM](https://github.com/maximecb/uvm) and [Uxn](https://100r.co/site/uxn.html) are small and portable virtual machines that support graphical user interfaces. The [motivation behind UVM](https://github.com/maximecb/uvm/blob/main/doc/vision.md) is simplicity and resilience, to which uxn adds the desire to use low-power computing hardware in order to reduce the material and energy footprint of computing technology.