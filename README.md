<!--
  Profile README for github.com/ahmedhany-cys

  Identity "Signal" (dark-first)
    ground  #0D1117 / #0B0F15      surface #161B22      border #21262D
    accent  #7AA2F7 (links, titles) alert   #FF9E64 (severity, streak fire only)
    text    #C0CAF5 / #8B949E
    Azure badges use labelColor 0078D4, AWS badges use 232F3E.

  Layout: who I am → what I can do → tools → work (by lifecycle stage) → how I work → activity → contact.
  Adding a project: put it in the lifecycle row it belongs to, keep two cards per row.

  Generated images
    assets/achievements.svg   .github/workflows/achievements.yml (daily, earned achievements only)
    snake on `output` branch  .github/workflows/snake.yml (daily)
  To change the rotating headline, edit the `lines=` parameter of the typing SVG.
-->

<a id="top"></a>

<div align="center">

<img src="./assets/banner.svg" width="100%" alt="Ahmed Hany, cloud security engineer working on AWS and Azure. A pulse moves from logs through detection and response into an incident report." />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3200&pause=1200&color=7AA2F7&center=true&vCenter=true&width=680&height=48&lines=Hi%2C+I'm+Ahmed+Hany;I+build+security+tooling+for+AWS+and+Azure;Detection+%C2%B7+response+%C2%B7+supply+chain+%C2%B7+recovery;Evidence+first%2C+never+a+guess" alt="Hi, I'm Ahmed Hany. I build security tooling for AWS and Azure. Detection, response, supply chain, recovery. Evidence first, never a guess." />

<p>
  <a href="#about-me"><img src="https://img.shields.io/badge/About-161B22?style=flat-square" alt="About" /></a>
  <a href="#skills"><img src="https://img.shields.io/badge/Skills-161B22?style=flat-square" alt="Skills" /></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/Tech%20stack-161B22?style=flat-square" alt="Tech stack" /></a>
  <a href="#selected-work"><img src="https://img.shields.io/badge/Selected%20work-161B22?style=flat-square" alt="Selected work" /></a>
  <a href="#how-i-work"><img src="https://img.shields.io/badge/How%20I%20work-161B22?style=flat-square" alt="How I work" /></a>
  <a href="#activity"><img src="https://img.shields.io/badge/Activity-161B22?style=flat-square" alt="Activity" /></a>
  <a href="#contact"><img src="https://img.shields.io/badge/Contact-161B22?style=flat-square" alt="Contact" /></a>
</p>

</div>

## About me

I'm Ahmed, a cloud security engineer. I build tools that answer the questions a security team actually gets asked: *who could reach this data, what happened in this account, is this release safe to ship, and could we recover if it all went wrong today?*

Most of my work lives on AWS, and lately on Azure too. I write it in Python and Terraform, put a FastAPI or React front end on it when people need to use it, and test it until I can show evidence for every claim it makes. When the evidence isn't there, my tools say **unknown** instead of guessing.

<table>
  <tr>
    <td width="33%" valign="top">
      <sub><code>focus</code></sub><br/>
      <b>Cloud security engineering</b><br/>
      IAM, detection, incident response and secure infrastructure as code
    </td>
    <td width="33%" valign="top">
      <sub><code>recently added</code></sub><br/>
      <b>Azure &amp; supply chain</b><br/>
      SBOMs, signed artifacts and SLSA provenance, with Key Vault-backed signing
    </td>
    <td width="33%" valign="top">
      <sub><code>side project</code></sub><br/>
      <b><a href="https://github.com/ahmedhany-cys/security-cheatsheets">Security cheatsheets</a></b><br/>
      16 quick references, from Nmap and Wireshark to Windows event IDs
    </td>
  </tr>
</table>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Skills

What I can do, and where you can check it.

| Area | What that means in practice | See it in |
|---|---|---|
| **Cloud IAM &amp; attack paths** | Evaluate IAM the way AWS does (explicit deny, boundaries, cross-account trust, conditions) and turn misconfigurations into attack paths with least-privilege fixes | [Attack Path Analyzer](https://github.com/ahmedhany-cys/aws-cloud-attack-path-analyzer) |
| **Threat detection** | Write detection rules over CloudTrail and GuardDuty, mapped to MITRE ATT&amp;CK, each with a confidence level and benign explanations to rule out | [CloudSentinel](https://github.com/ahmedhany-cys/cloudsentinel-aws-incident-response) · [Incident response](https://github.com/ahmedhany-cys/aws-cloud-security-incident-response) |
| **Incident response** | Correlate events into timelines, estimate blast radius, and run containment only through dry runs, separate-person approval and rollback | [CloudSentinel](https://github.com/ahmedhany-cys/cloudsentinel-aws-incident-response) |
| **Software supply chain** <sub>`new`</sub> | Generate CycloneDX SBOMs, check them against OSV, verify Sigstore signatures and SLSA v1 provenance, and gate releases on policy | [SupplyChain Sentinel](https://github.com/ahmedhany-cys/azure-supplychain-sentinel) |
| **Secure IaC &amp; policy as code** | Generate Terraform from requirements and block it with deterministic policies over the plan JSON, alongside Checkov and Trivy | [Infrastructure as Prompt](https://github.com/ahmedhany-cys/infrastructure-as-prompt) |
| **Cyber resilience** <sub>`new`</sub> | Model system dependencies, check backups against RTO/RPO, simulate ransomware and admin compromise, and plan a safe recovery order | [RecoveryProof](https://github.com/ahmedhany-cys/recoveryproof) |
| **DevSecOps** | CI that lints, type-checks, tests and scans every change: secrets, dependencies, containers and IaC | the `ci.yml` in each repository |
| **Security tooling UX** | Turn analysis into something people can use: CLIs with CI exit codes, REST APIs, dashboards and print-ready reports | all of the above |

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Tech stack

<div align="center">
  <img src="https://skillicons.dev/icons?i=aws,azure,terraform,py,ts,react,fastapi,docker,githubactions,bash,linux,git&perline=12" alt="AWS, Azure, Terraform, Python, TypeScript, React, FastAPI, Docker, GitHub Actions, Bash, Linux, Git" />
</div>

<br/>

<table>
  <tr>
    <td width="22%"><b>Languages</b></td>
    <td>
      <a href="https://docs.python.org/3/"><img src="https://img.shields.io/badge/Python-161B22?style=flat-square&logo=python&logoColor=3776AB" alt="Python" /></a>
      <a href="https://www.typescriptlang.org/docs/"><img src="https://img.shields.io/badge/TypeScript-161B22?style=flat-square&logo=typescript&logoColor=3178C6" alt="TypeScript" /></a>
      <a href="https://developer.hashicorp.com/terraform/language"><img src="https://img.shields.io/badge/HCL-161B22?style=flat-square&logo=hashicorp&logoColor=white" alt="HCL" /></a>
      <a href="https://www.gnu.org/software/bash/manual/"><img src="https://img.shields.io/badge/Bash-161B22?style=flat-square&logo=gnubash&logoColor=4EAA25" alt="Bash" /></a>
    </td>
  </tr>
  <tr>
    <td><b>AWS</b></td>
    <td>
      <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/"><img src="https://img.shields.io/badge/AWS-IAM-161B22?style=flat-square&labelColor=232F3E" alt="AWS IAM" /></a>
      <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/"><img src="https://img.shields.io/badge/AWS-CloudTrail-161B22?style=flat-square&labelColor=232F3E" alt="AWS CloudTrail" /></a>
      <a href="https://docs.aws.amazon.com/guardduty/latest/ug/"><img src="https://img.shields.io/badge/AWS-GuardDuty-161B22?style=flat-square&labelColor=232F3E" alt="Amazon GuardDuty" /></a>
      <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/"><img src="https://img.shields.io/badge/AWS-EventBridge-161B22?style=flat-square&labelColor=232F3E" alt="Amazon EventBridge" /></a>
      <a href="https://docs.aws.amazon.com/lambda/latest/dg/"><img src="https://img.shields.io/badge/AWS-Lambda-161B22?style=flat-square&labelColor=232F3E" alt="AWS Lambda" /></a>
      <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/"><img src="https://img.shields.io/badge/AWS-S3-161B22?style=flat-square&labelColor=232F3E" alt="Amazon S3" /></a>
      <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/"><img src="https://img.shields.io/badge/AWS-CloudWatch-161B22?style=flat-square&labelColor=232F3E" alt="Amazon CloudWatch" /></a>
      <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html"><img src="https://img.shields.io/badge/AWS-boto3-161B22?style=flat-square&labelColor=232F3E" alt="boto3" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Azure</b> <sub><code>new</code></sub></td>
    <td>
      <a href="https://learn.microsoft.com/azure/key-vault/"><img src="https://img.shields.io/badge/Azure-Key%20Vault-161B22?style=flat-square&labelColor=0078D4" alt="Azure Key Vault" /></a>
      <a href="https://learn.microsoft.com/azure/container-registry/"><img src="https://img.shields.io/badge/Azure-Container%20Registry-161B22?style=flat-square&labelColor=0078D4" alt="Azure Container Registry" /></a>
      <a href="https://learn.microsoft.com/azure/storage/"><img src="https://img.shields.io/badge/Azure-Storage-161B22?style=flat-square&labelColor=0078D4" alt="Azure Storage" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Security tooling</b></td>
    <td>
      <a href="https://attack.mitre.org/"><img src="https://img.shields.io/badge/MITRE%20ATT%26CK-161B22?style=flat-square" alt="MITRE ATT&CK" /></a>
      <a href="https://cyclonedx.org/docs/"><img src="https://img.shields.io/badge/CycloneDX-161B22?style=flat-square" alt="CycloneDX" /></a>
      <a href="https://github.com/anchore/syft"><img src="https://img.shields.io/badge/Syft-161B22?style=flat-square" alt="Syft" /></a>
      <a href="https://google.github.io/osv-scanner/"><img src="https://img.shields.io/badge/OSV--Scanner-161B22?style=flat-square" alt="OSV-Scanner" /></a>
      <a href="https://docs.sigstore.dev/cosign/"><img src="https://img.shields.io/badge/Cosign%20%2F%20Sigstore-161B22?style=flat-square" alt="Cosign and Sigstore" /></a>
      <a href="https://slsa.dev/spec/v1.0/"><img src="https://img.shields.io/badge/SLSA%20v1-161B22?style=flat-square" alt="SLSA v1" /></a>
      <a href="https://trivy.dev/latest/docs/"><img src="https://img.shields.io/badge/Trivy-161B22?style=flat-square&logo=trivy&logoColor=1904DA" alt="Trivy" /></a>
      <a href="https://www.checkov.io/"><img src="https://img.shields.io/badge/Checkov-161B22?style=flat-square" alt="Checkov" /></a>
      <a href="https://github.com/gitleaks/gitleaks"><img src="https://img.shields.io/badge/Gitleaks-161B22?style=flat-square" alt="Gitleaks" /></a>
      <a href="https://bandit.readthedocs.io/"><img src="https://img.shields.io/badge/Bandit-161B22?style=flat-square" alt="Bandit" /></a>
      <a href="https://pypi.org/project/pip-audit/"><img src="https://img.shields.io/badge/pip--audit-161B22?style=flat-square" alt="pip-audit" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Apps &amp; APIs</b></td>
    <td>
      <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-161B22?style=flat-square&logo=fastapi&logoColor=009688" alt="FastAPI" /></a>
      <a href="https://docs.pydantic.dev/"><img src="https://img.shields.io/badge/Pydantic-161B22?style=flat-square&logo=pydantic&logoColor=E92063" alt="Pydantic" /></a>
      <a href="https://react.dev/"><img src="https://img.shields.io/badge/React-161B22?style=flat-square&logo=react&logoColor=61DAFB" alt="React" /></a>
      <a href="https://vite.dev/guide/"><img src="https://img.shields.io/badge/Vite-161B22?style=flat-square&logo=vite&logoColor=646CFF" alt="Vite" /></a>
      <a href="https://tailwindcss.com/docs"><img src="https://img.shields.io/badge/Tailwind%20CSS-161B22?style=flat-square&logo=tailwindcss&logoColor=06B6D4" alt="Tailwind CSS" /></a>
      <a href="https://docs.streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-161B22?style=flat-square&logo=streamlit&logoColor=FF4B4B" alt="Streamlit" /></a>
      <a href="https://networkx.org/documentation/stable/"><img src="https://img.shields.io/badge/NetworkX-161B22?style=flat-square" alt="NetworkX" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Infrastructure &amp; CI</b></td>
    <td>
      <a href="https://developer.hashicorp.com/terraform/docs"><img src="https://img.shields.io/badge/Terraform-161B22?style=flat-square&logo=terraform&logoColor=7B42BC" alt="Terraform" /></a>
      <a href="https://docs.docker.com/"><img src="https://img.shields.io/badge/Docker-161B22?style=flat-square&logo=docker&logoColor=2496ED" alt="Docker" /></a>
      <a href="https://docs.github.com/actions"><img src="https://img.shields.io/badge/GitHub%20Actions-161B22?style=flat-square&logo=githubactions&logoColor=2088FF" alt="GitHub Actions" /></a>
      <a href="https://docs.github.com/code-security/dependabot"><img src="https://img.shields.io/badge/Dependabot-161B22?style=flat-square&logo=dependabot&logoColor=white" alt="Dependabot" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Testing &amp; quality</b></td>
    <td>
      <a href="https://docs.pytest.org/"><img src="https://img.shields.io/badge/pytest-161B22?style=flat-square&logo=pytest&logoColor=0A9EDC" alt="pytest" /></a>
      <a href="https://vitest.dev/guide/"><img src="https://img.shields.io/badge/Vitest-161B22?style=flat-square&logo=vitest&logoColor=6E9F18" alt="Vitest" /></a>
      <a href="https://playwright.dev/docs/intro"><img src="https://img.shields.io/badge/Playwright-161B22?style=flat-square" alt="Playwright" /></a>
      <a href="https://docs.astral.sh/ruff/"><img src="https://img.shields.io/badge/Ruff-161B22?style=flat-square&logo=ruff&logoColor=D7FF64" alt="Ruff" /></a>
      <a href="https://mypy.readthedocs.io/"><img src="https://img.shields.io/badge/mypy-161B22?style=flat-square" alt="mypy" /></a>
      <a href="https://www.conventionalcommits.org/"><img src="https://img.shields.io/badge/Conventional%20Commits-161B22?style=flat-square&logo=conventionalcommits&logoColor=FE5196" alt="Conventional Commits" /></a>
    </td>
  </tr>
</table>

<sub>Only tools used in my public repositories are listed. Every badge links to the official documentation.</sub>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Selected work

Ordered by the stage of the security lifecycle each one covers, from shipping code to recovering from an incident. All are MIT licensed and tested, and the demos use synthetic data or simulation mode unless a project says otherwise.

<table>
  <tr>
    <td width="50%" valign="top">
      <sub><code>01 · build</code> &nbsp;Is this release safe to ship?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/azure-supplychain-sentinel"><img src="./assets/projects/sentinel.jpg" width="100%" alt="Azure SupplyChain Sentinel security overview dashboard" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/azure-supplychain-sentinel"><b>Azure SupplyChain Sentinel</b></a> <sub><code>new</code></sub>
      <br/>A release gate that turns SBOM, vulnerability, signature and SLSA provenance evidence into a <b>PASS / FAIL / INDETERMINATE</b> decision under a versioned policy.
      <br/><sub><code>Python</code> · <code>Syft</code> · <code>OSV</code> · <code>Cosign</code> · <code>SLSA</code> · <code>FastAPI</code> · <code>Azure</code></sub>
    </td>
    <td width="50%" valign="top">
      <sub><code>01 · build</code> &nbsp;Is this infrastructure safe to deploy?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/infrastructure-as-prompt"><img src="./assets/projects/iap.jpg" width="100%" alt="Infrastructure as Prompt architecture options and cost comparison" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/infrastructure-as-prompt"><b>Infrastructure as Prompt</b></a> <sub><code>new</code></sub>
      <br/>Plain-English requirements become traceable AWS requirements and reviewed Terraform, gated by <b>38 deterministic policies</b> over the plan JSON.
      <br/><sub><code>Python</code> · <code>Terraform</code> · <code>React</code> · <code>Checkov</code> · <code>Trivy</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <sub><code>02 · harden</code> &nbsp;Who could reach admin or sensitive data?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/aws-cloud-attack-path-analyzer"><img src="./assets/projects/attackpath.jpg" width="100%" alt="AWS Cloud Attack Path Analyzer HTML report summary" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/aws-cloud-attack-path-analyzer"><b>AWS Cloud Attack Path Analyzer</b></a> <sub><code>new</code></sub>
      <br/>Offline, graph-based analysis of IAM and network exposure: a tri-state IAM evaluator, <b>22 checks</b> and least-privilege fixes, with zero runtime dependencies.
      <br/><sub><code>Python</code> · <code>IAM</code> · <code>graph analysis</code> · <code>boto3</code></sub>
    </td>
    <td width="50%" valign="top">
      <sub><code>03 · detect</code> &nbsp;Did someone just change something risky?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response"><img src="./assets/projects/incident.jpg" width="100%" alt="Incident report JSON written to S3, with the account ID and source IP redacted" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response"><b>AWS Cloud Security Incident Response</b></a>
      <br/>Serverless monitoring: CloudTrail → EventBridge → Lambda → S3 incident reports. Tested against a real account, where it found its own blind spot. <b>$0/month</b>.
      <br/><sub><code>Python</code> · <code>Terraform</code> · <code>Lambda</code> · <code>EventBridge</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <sub><code>04 · respond</code> &nbsp;What happened, and what do we do now?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/cloudsentinel-aws-incident-response"><img src="./assets/projects/cloudsentinel.jpg" width="100%" alt="CloudSentinel security overview dashboard in simulation mode" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/cloudsentinel-aws-incident-response"><b>CloudSentinel</b></a> <sub><code>new</code></sub>
      <br/>AWS threat detection and investigation: <b>17 rules mapped to MITRE ATT&amp;CK</b>, incident timelines, blast radius, and approval-gated containment with rollback.
      <br/><sub><code>Python</code> · <code>FastAPI</code> · <code>React</code> · <code>GuardDuty</code> · <code>Terraform</code></sub>
    </td>
    <td width="50%" valign="top">
      <sub><code>05 · recover</code> &nbsp;Could we actually come back from it?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/recoveryproof"><img src="./assets/projects/recoveryproof.jpg" width="100%" alt="RecoveryProof executive overview with a readiness score" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/recoveryproof"><b>RecoveryProof</b></a> <sub><code>new</code></sub>
      <br/>Evidence-based disaster-recovery analysis: RTO/RPO compliance, dependency-aware recovery order and <b>10 incident scenarios</b>, including ransomware.
      <br/><sub><code>Python</code> · <code>Streamlit</code> · <code>NetworkX</code> · <code>Plotly</code></sub>
    </td>
  </tr>
</table>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## How I work

The same rules run through every project above.

- **Facts, inferences and guesses stay separate.** Findings are labelled as observed, derived, hypothetical or unknown, and my tools return *indeterminate* rather than a false all-clear.
- **Test the outcome, not the deployment.** A successful `terraform apply` proves nothing about whether a rule fires. Only an observed result does.
- **Check assumptions against reality.** API names are not always event names; CloudTrail logs `PutBucketPublicAccessBlock`, not `PutPublicAccessBlock`.
- **Automation never acts alone.** Containment needs a dry run and approval from a different person; a deployment approval is bound to the hash of the exact plan that was reviewed.
- **Least privilege is a design input, not a cleanup step.** Every role gets exactly what it needs, and every unavoidable `*` gets a comment explaining why.
- **Write down the limitations.** Every project documents what it does not do. A partial result with a documented cause beats a green check nobody can trust.
- **Share evidence safely and cheaply.** Real identifiers are redacted, demos use synthetic data, and I like running whole stacks inside the free tier.

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Activity

<div align="center">
  <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=ahmedhany-cys&theme=tokyonight" alt="GitHub statistics for ahmedhany-cys: stars, commits, pull requests and issues" />
  <img height="170" src="https://streak-stats.demolab.com?user=ahmedhany-cys&hide_border=true&border_radius=5&background=1A1B27&stroke=21262D&ring=7AA2F7&fire=FF9E64&currStreakNum=E6EDF3&sideNums=C0CAF5&currStreakLabel=7AA2F7&sideLabels=8B949E&dates=6E7681" alt="Contribution streak for ahmedhany-cys" />
</div>

<br/>

<div align="center">
  <img src="https://raw.githubusercontent.com/ahmedhany-cys/ahmedhany-cys/output/github-snake-dark.svg" width="100%" alt="Contribution graph animation: a snake eats the contribution cells of the past year" />
</div>

<details>
<summary><b>Achievements</b></summary>
<br/>

<div align="center">
  <a href="https://github.com/ahmedhany-cys">
    <img src="./assets/achievements.svg" width="100%" alt="GitHub achievements earned by ahmedhany-cys, with locked slots for ones not yet earned" />
  </a>
  <br/>
  <sub>Real badges from my <a href="https://github.com/ahmedhany-cys">GitHub profile</a>, redrawn daily. Locked slots are ones I haven't earned yet.</sub>
</div>

<br/>

| Locked achievement | How it is earned |
|---|---|
| Pull Shark | Open pull requests that get merged |
| Quickdraw | Close an issue or pull request within five minutes of opening it |
| YOLO | Merge a pull request without a review |
| Pair Extraordinaire | Co-author commits on a merged pull request |
| Galaxy Brain | Have answers accepted in GitHub Discussions |
| Starstruck | Create a repository that reaches 16 stars |

<sub>Source: <a href="https://docs.github.com/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile#displaying-achievements-on-your-profile">GitHub Docs</a>.</sub>

</details>

<div align="center">
  <sub>Cards are generated live from public data.</sub><br/>
  <img src="https://komarev.com/ghpvc/?username=ahmedhany-cys&style=flat-square&color=7AA2F7&labelColor=161B22&label=profile%20views" alt="Profile views" />
</div>

<!--
  Certifications: add only ones you hold, each linking to its public verification page.
  <a href="https://www.credly.com/badges/YOUR-BADGE-ID"><img src="https://img.shields.io/badge/CERT%20NAME-161B22?style=flat-square" alt="CERT NAME" /></a>
-->

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Contact

<div align="center">
  <a href="https://github.com/ahmedhany-cys"><img src="https://img.shields.io/badge/GitHub-ahmedhany--cys-161B22?style=for-the-badge&logo=github&logoColor=white" alt="GitHub: ahmedhany-cys" /></a>
  <!--
    Add verified profiles here, then move the lines out of this comment:
    <a href="https://www.linkedin.com/in/YOUR-HANDLE"><img src="https://img.shields.io/badge/LinkedIn-161B22?style=for-the-badge&logoColor=0A66C2" alt="LinkedIn" /></a>
    <a href="mailto:YOU@EXAMPLE.COM"><img src="https://img.shields.io/badge/Email-161B22?style=for-the-badge&logo=gmail&logoColor=EA4335" alt="Email" /></a>
  -->
</div>

<br/>

<div align="center">
  <sub>Built in the open. Every claim on this page links to the code or docs that back it.</sub>
</div>
