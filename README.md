![banner](https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=Cody%20Stamey&fontSize=56&fontColor=ffffff&fontAlignY=38&desc=Infrastructure%20%7C%20DevOps%20%7C%20AI-assisted%20engineering&descSize=18&descAlignY=58&animation=fadeIn)

# Cody Stamey

Infrastructure engineer. I automate the boring parts of running systems and spend a lot of my spare time figuring out where AI agents fit into infrastructure work.

Most of what I build has the same shape: take a repetitive operational task, pin down the evidence and the guardrails, then let a script or an agent run it on a schedule.

---

## What I'm working on

### infrastructure_curiosity

A weekly radar for AWS and infrastructure tooling. A scheduled Codex task runs every Monday, pulls practitioner discussions from the last month, checks each lead against dated first-party AWS docs, and opens a review-only pull request with a team brief, a structured evidence record, and a mocked Terraform example.

The part I care most about is the control boundary. The agent can only touch discoveries, weekly briefs, and examples. CI runs with read-only permissions and no cloud credentials. Terraform tests use `command = plan` with mocked providers, so nothing ever gets provisioned. A `make gate` target runs the repo contracts, Terraform validation, TFLint, ShellCheck, and Gitleaks before anything merges.

Recent discoveries include S3 same-day transition to Standard-IA, multi-Region KMS keys, an AWS cost-estimate incident, and cloud workspaces for coding agents.

Repo: https://github.com/cekapitan/infrastructure_curiosity

### second_brain

A personal knowledge base built to be read and written by agents, not just by me. I started with a research pass on existing "company brain" tools to decide what to adopt and what to skip. The patterns I'm keeping are a RAW / WIKI / CONTEXT split, contradiction flagging at write time, a nightly review cycle, a human write gate, and expire-not-delete validity windows. Next up is an observer that runs nightly to lint pages and flag contradictions.

Repo: https://github.com/cekapitan/second_brain

### Forks I'm learning from

- [autoresearch-lite](https://github.com/cekapitan/autoresearch-lite): Karpathy's autonomous ML research loop adapted to run on a free Colab T4.
- [ruflo](https://github.com/cekapitan/ruflo): multi-agent orchestration for Claude. Reading the swarm and workflow code to see what carries over to infra automation.

---

## How I think about infrastructure

Good infrastructure gets out of the way. It should cut the number of things an engineer has to hold in their head, take the repetitive work off their plate, and make it obvious what a system is doing. When it works, nobody thinks about it.

The same applies to AI agents in an ops workflow. An agent that can plan but not apply, that has to cite a dated source before it opens a PR, and that runs behind the same CI gates as a human is one I can actually trust with recurring work.

---

## Skills

### Cloud and infrastructure
![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)

S3 storage classes and lifecycle rules, KMS including multi-Region keys, Cost Explorer. Terraform modules with mocked provider tests so they can be validated without an account.

### Languages and scripting
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?logo=gnubash&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)

Python for automation runners and contract tests. Bash for glue, checked with ShellCheck. Enough TypeScript to read and modify agent orchestration code.

### CI, quality, and security gates
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)
![TFLint](https://img.shields.io/badge/TFLint-000000?logo=terraform&logoColor=white)
![ShellCheck](https://img.shields.io/badge/ShellCheck-4EAA25?logo=gnubash&logoColor=white)
![Gitleaks](https://img.shields.io/badge/Gitleaks-D32F2F?logo=git&logoColor=white)
![Dependabot](https://img.shields.io/badge/Dependabot-025E8C?logo=dependabot&logoColor=white)

Read-only CI pipelines, least-privilege workflow permissions, secret scanning on every PR, and Dependabot for actions and providers. Repo contracts that fail the build if a change would provision resources.

### AI-assisted engineering
![Claude](https://img.shields.io/badge/Claude_Code-D97757?logo=anthropic&logoColor=white)
![OpenAI](https://img.shields.io/badge/Codex-412991?logo=openai&logoColor=white)

Scheduled agent tasks with scoped write access, evidence-backed PR generation, agent-readable knowledge bases, and multi-agent orchestration. Also comfortable running small ML training loops on consumer GPUs.

### Scheduling and automation
![macOS](https://img.shields.io/badge/launchd-000000?logo=apple&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)

Weekly runners on launchd and hosted schedulers, Makefile-driven validation, Git utilities for day-to-day work.

---

## Stats

![GitHub stats](https://github-readme-stats.vercel.app/api?username=cekapitan&show_icons=true&theme=tokyonight&hide_border=true)
![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=cekapitan&layout=compact&theme=tokyonight&hide_border=true)

![GitHub streak](https://streak-stats.demolab.com/?user=cekapitan&theme=tokyonight&hide_border=true)

![Activity graph](https://github-readme-activity-graph.vercel.app/graph?username=cekapitan&theme=tokyo-night&hide_border=true)

---

## Contact

- GitHub: https://github.com/cekapitan
- LinkedIn: https://www.linkedin.com/in/codystamey/

![Profile views](https://komarev.com/ghpvc/?username=cekapitan&style=flat)
