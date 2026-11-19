# Annotated Bibliography

**PC Building Specialist AI** · Aedan Johnson · Self-Directed Passion Project
Format: APA 7th edition. Sources are listed alphabetically by author.

---

**AMD. (n.d.). *AMD Radeon RX graphics cards: Product specifications*.** Retrieved November 18, 2026, from https://www.amd.com/en/products/specifications/graphics.html

AMD's official specification pages list the total board power for each Radeon graphics card. I used them to fill in the power numbers for every RX card in the `GPU_SPECS` table in `pc_ai.py`, which checker rule 5 uses to decide whether a power supply is strong enough. It is a primary source because AMD makes the cards.

**Anthropic. (2025). *Claude Code* [Computer software].** https://claude.com/product/claude-code

Claude Code is an AI coding assistant that reads a project, writes code, and runs commands. I used it to help write and debug `pc_ai.py`, organize the GitHub repository, and draft documents such as this bibliography, and I checked and tested what it produced. I list it here because the assignment asks me to be clear about any help I get, including AI tools.

**GitHub, Inc. (n.d.). *GitHub* [Online platform].** Retrieved November 18, 2026, from https://github.com

GitHub hosts Git repositories and pull requests. My project lives at github.com/Aedan-Johnson/PC-Building-AI, and every change went through a branch and a pull request, which gives a dated record of my progress. It is the most widely used code hosting platform and is where both of my main code references publish their code.

**Intel. (n.d.). *Intel Arc graphics: Product specifications*.** Retrieved November 18, 2026, from https://www.intel.com/content/www/us/en/products/details/discrete-gpus/arc.html

Intel's official product pages list the total board power for its Arc graphics cards. I used them for the Arc A750, A770, B570, and B580 power numbers in `GPU_SPECS`. As the manufacturer's own specifications, they are a primary source.

**Karpathy, A. (2023, January 17). *Let's build GPT: From scratch, in code, spelled out* [Video]. YouTube.** https://www.youtube.com/watch?v=kCc8FmEb1nY

This two-hour video builds a small GPT language model in Python step by step, starting from a character-level tokenizer and ending with a working transformer. It was my main guide for the tokenizer, model, and training loop (sections 6 to 8 of `pc_ai.py`), and the code comment in section 7 credits it. Karpathy was a founding member of OpenAI and led AI at Tesla, and the video is one of the most widely used introductions to how GPT models work.

**NVIDIA. (n.d.). *GeForce graphics cards: Compare specs*.** Retrieved November 18, 2026, from https://www.nvidia.com/en-us/geforce/graphics-cards/compare/

NVIDIA's official comparison pages list the total graphics power for each GeForce RTX card. I used them for the RTX 30, 40, and 50 series power numbers in `GPU_SPECS`, which feed checker rule 5. It is a primary source because NVIDIA designs the chips.

**Oliver, D. (2021–2025). *pc-part-dataset* [Data set]. GitHub.** https://github.com/docyx/pc-part-dataset

This open dataset (MIT License) has spreadsheets of thousands of CPUs, motherboards, RAM kits, graphics cards, cases, power supplies, coolers, and drives, collected from PCPartPicker. It is the parts data for my whole project: the CSVs are stored unchanged in `data/parts/`, and the builder and checker read from them. I chose it because it is large, openly licensed, kept up to date, and comes from the most popular PC building site, but it was missing CPU socket, RAM type, GPU power, and case GPU clearance, so I had to add those myself.

**Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J., Chanan, G., Killeen, T., Lin, Z., Gimelshein, N., Antiga, L., Desmaison, A., Köpf, A., Yang, E., DeVito, Z., Raison, M., Tejani, A., Chilamkurthy, S., Steiner, B., Fang, L., … Chintala, S. (2019). PyTorch: An imperative style, high-performance deep learning library. *Advances in Neural Information Processing Systems, 32*, 8024–8035.** https://pytorch.org

PyTorch is the machine learning library I used to build and train my 10.9M-parameter model. It provided the neural network layers, the AdamW optimizer, and support for running training on my Mac's Apple Silicon GPU. The paper was peer reviewed at NeurIPS, one of the top AI conferences, and PyTorch is one of the most widely used AI libraries in research and industry.

**PCPartPicker. (n.d.). *PCPartPicker* [Website].** Retrieved November 18, 2026, from https://pcpartpicker.com

PCPartPicker is a website for planning PC builds that lists parts, specs, prices, and basic compatibility warnings. It is the original source of the data in pc-part-dataset, and I used it as a reference for part prices and details. It is the most widely used PC building tool, and its idea of checking compatibility automatically is what my checker does in a smaller way.

**Raschka, S. (2024). *Build a large language model (from scratch)*. Manning Publications.**

This book explains how to build a GPT-style model from the ground up, including attention, the transformer block, and pretraining. I used chapters 3 to 5 to understand the attention and training code I wrote, and section 7 of `pc_ai.py` credits it. It is my non-internet source: a published book by a machine learning researcher, with its code available at github.com/rasbt/LLMs-from-scratch.

**Tom's Hardware. (2025). [Price reports and deal coverage for PC components, June–August 2025].** Future US. https://www.tomshardware.com

Tom's Hardware is a long-running technology news and review site that reports prices and deals on PC parts. I used its dated mid-2025 price reports to set the typical prices in `data/price_overrides.csv`; the `basis` column names it for parts such as the Ryzen 5 7600, Ryzen 7 7800X3D, RTX 5080, and DDR5 RAM. It is credible because it has covered PC hardware since 1996 and dates its price reports, which let me choose prices from one consistent period.

**Textualize. (n.d.). *Rich* [Computer software].** Retrieved November 18, 2026, from https://rich.readthedocs.io/en/stable/

Rich is a Python library for printing colored text and tables in the terminal. I used it and its documentation to build the chat interface and the parts tables the AI shows. It is open source and widely used in Python tools, and the official documentation was the clearest reference.

---

### Still to add before Dec 3

The assignment needs at least 7 credible sources, including an expert interview or another non-internet source. This list has 12 sources, with Raschka's book as the non-internet one. Still to do:

- **Expert interview.** The plan lists one (an IT teacher, someone in AI or IT, or a Geek Squad tech). Add it here once it is done, with the person's name, role, date, and what I learned.
- **Planned sources, if I used them.** The plan also lists 3Blue1Brown's "Transformers" and "Attention" videos, Karpathy's microgpt post, Eldan and Li's "TinyStories" (2023), Vaswani et al.'s "Attention Is All You Need" (2017), and the OWASP Top 10 for LLM Applications. Only add the ones I actually used.
- **Starter code.** If any of the model code came from the `mini_gpt.py` starter file, credit it here.
- **Exact pages.** For the manufacturer and Tom's Hardware entries, swap in the exact page or article URLs if my notes have them.
