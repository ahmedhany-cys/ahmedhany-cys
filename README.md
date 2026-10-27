<!--
  Profile README for github.com/ahmedhany-cys

  Identity "Signal" (dark-first)
    ground  #0D1117 / #0B0F15      surface #161B22      border #21262D
    accent  #7AA2F7 (links, titles) alert   #FF9E64 (severity, streak fire only)
    text    #C0CAF5 / #8B949E

  Everything below is real: stats cards are generated live, project claims link to
  the repository docs that back them. To change the rotating headline, edit the
  `lines=` parameter of the typing SVG. The contribution snake is produced by
  .github/workflows/snake.yml on the `output` branch.
-->

<a id="top"></a>

<div align="center">

<img src="./assets/banner.svg" width="100%" alt="Ahmed Hany — cloud security and detection engineering. A pulse moves from CloudTrail through EventBridge and Lambda into an S3 incident report." />

<a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3200&pause=1200&color=7AA2F7&center=true&vCenter=true&width=640&height=48&lines=Turning+CloudTrail+into+incident+reports;Detection+engineering+on+AWS;Least-privilege+infrastructure+in+Terraform;Tested+against+a+live+account%2C+not+just+deployed" alt="Turning CloudTrail into incident reports. Detection engineering on AWS. Least-privilege infrastructure in Terraform. Tested against a live account, not just deployed." />
</a>

<p>
  <a href="#about-me"><img src="https://img.shields.io/badge/About-161B22?style=flat-square" alt="About" /></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/Tech%20stack-161B22?style=flat-square" alt="Tech stack" /></a>
  <a href="#featured-project"><img src="https://img.shields.io/badge/Projects-161B22?style=flat-square" alt="Projects" /></a>
  <a href="#achievements"><img src="https://img.shields.io/badge/Achievements-161B22?style=flat-square" alt="Achievements" /></a>
  <a href="#github-statistics"><img src="https://img.shields.io/badge/Statistics-161B22?style=flat-square" alt="Statistics" /></a>
  <a href="#contact"><img src="https://img.shields.io/badge/Contact-161B22?style=flat-square" alt="Contact" /></a>
</p>

</div>

## About me

I build cloud security tooling on AWS, and I care about proving that a detection works, not just that it deploys. My focus is **detection engineering and automated incident response**: turning CloudTrail activity into structured, actionable incident reports with serverless, least-privilege infrastructure defined entirely in Terraform.

<table>
  <tr>
    <td width="50%" valign="top"><sub><code>building</code></sub><br/>Serverless security monitoring on AWS: CloudTrail → EventBridge → Lambda → S3</td>
    <td width="50%" valign="top"><sub><code>method</code></sub><br/>Every detection is exercised end to end against a live account, with redacted evidence committed next to the code</td>
  </tr>
  <tr>
    <td valign="top"><sub><code>constraint</code></sub><br/>The whole stack runs at $0/month inside the AWS Free Tier</td>
    <td valign="top"><sub><code>interests</code></sub><br/>IAM and least privilege, threat detection, infrastructure as code, security automation</td>
  </tr>
</table>

<details>
<summary><b>Principles I build with</b></summary>
<br/>

Lessons from shipping and testing real detections:

- **Test the detection, not the deployment.** A successful `terraform apply` proves nothing about whether a rule fires. Only an observed incident does.
- **API names are not always event names.** CloudTrail logs `PutBucketPublicAccessBlock`, not `PutPublicAccessBlock`. Validate every pattern against real logged events.
- **Least privilege is a design input, not a cleanup step.** Every role gets exactly the actions and resources it needs, and every unavoidable `*` gets a comment explaining why.
- **Evidence leaks more than account IDs.** Source IPs, access key IDs and principal IDs are redacted before anything is committed.
- **Write down the limitations.** A partial result with a documented cause is worth more than a green check nobody can trust.

</details>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Tech stack

<div align="center">
  <img src="https://skillicons.dev/icons?i=aws,terraform,python,bash,git,github,githubactions&perline=7" alt="AWS, Terraform, Python, Bash, Git, GitHub, GitHub Actions" />
</div>

<br/>

<table>
  <tr>
    <td><b>Languages</b></td>
    <td>
      <a href="https://docs.python.org/3.12/"><img src="https://img.shields.io/badge/Python%203.12-161B22?style=flat-square&logo=python&logoColor=3776AB" alt="Python 3.12" /></a>
      <a href="https://www.gnu.org/software/bash/manual/"><img src="https://img.shields.io/badge/Bash-161B22?style=flat-square&logo=gnubash&logoColor=4EAA25" alt="Bash" /></a>
      <a href="https://developer.hashicorp.com/terraform/language"><img src="https://img.shields.io/badge/HCL-161B22?style=flat-square&logo=hashicorp&logoColor=white" alt="HCL" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Cloud &amp; security</b></td>
    <td>
      <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/"><img src="https://img.shields.io/badge/AWS-CloudTrail-161B22?style=flat-square&labelColor=232F3E" alt="AWS CloudTrail" /></a>
      <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/"><img src="https://img.shields.io/badge/AWS-EventBridge-161B22?style=flat-square&labelColor=232F3E" alt="Amazon EventBridge" /></a>
      <a href="https://docs.aws.amazon.com/lambda/latest/dg/"><img src="https://img.shields.io/badge/AWS-Lambda-161B22?style=flat-square&labelColor=232F3E" alt="AWS Lambda" /></a>
      <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/"><img src="https://img.shields.io/badge/AWS-S3-161B22?style=flat-square&labelColor=232F3E" alt="Amazon S3" /></a>
      <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/"><img src="https://img.shields.io/badge/AWS-IAM-161B22?style=flat-square&labelColor=232F3E" alt="AWS IAM" /></a>
      <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/"><img src="https://img.shields.io/badge/AWS-CloudWatch%20Logs-161B22?style=flat-square&labelColor=232F3E" alt="Amazon CloudWatch Logs" /></a>
      <a href="https://docs.aws.amazon.com/sns/latest/dg/"><img src="https://img.shields.io/badge/AWS-SNS-161B22?style=flat-square&labelColor=232F3E" alt="Amazon SNS" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Infrastructure &amp; DevOps</b></td>
    <td>
      <a href="https://developer.hashicorp.com/terraform/docs"><img src="https://img.shields.io/badge/Terraform-161B22?style=flat-square&logo=terraform&logoColor=7B42BC" alt="Terraform" /></a>
      <a href="https://docs.github.com/actions"><img src="https://img.shields.io/badge/GitHub%20Actions-161B22?style=flat-square&logo=githubactions&logoColor=2088FF" alt="GitHub Actions" /></a>
      <a href="https://docs.github.com/code-security/dependabot"><img src="https://img.shields.io/badge/Dependabot-161B22?style=flat-square&logo=dependabot&logoColor=white" alt="Dependabot" /></a>
      <a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/"><img src="https://img.shields.io/badge/AWS-EventBridge%20Scheduler-161B22?style=flat-square&labelColor=232F3E" alt="Amazon EventBridge Scheduler" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Quality &amp; tools</b></td>
    <td>
      <a href="https://docs.pytest.org/"><img src="https://img.shields.io/badge/pytest-161B22?style=flat-square&logo=pytest&logoColor=0A9EDC" alt="pytest" /></a>
      <a href="https://docs.astral.sh/ruff/"><img src="https://img.shields.io/badge/Ruff-161B22?style=flat-square&logo=ruff&logoColor=D7FF64" alt="Ruff" /></a>
      <a href="https://www.shellcheck.net/wiki/"><img src="https://img.shields.io/badge/ShellCheck-161B22?style=flat-square" alt="ShellCheck" /></a>
      <a href="https://git-scm.com/doc"><img src="https://img.shields.io/badge/Git-161B22?style=flat-square&logo=git&logoColor=F05032" alt="Git" /></a>
      <a href="https://www.conventionalcommits.org/"><img src="https://img.shields.io/badge/Conventional%20Commits-161B22?style=flat-square&logo=conventionalcommits&logoColor=FE5196" alt="Conventional Commits" /></a>
    </td>
  </tr>
</table>

<sub>Only tools used in my public repositories are listed. Every badge links to the official documentation.</sub>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Featured project

<a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response">
  <img src="./assets/project-incident-preview.png" width="100%" alt="Incident report JSON written to S3 for test T5 (DeleteBucketPublicAccessBlock), with the account ID and source IP redacted" />
</a>

### [aws-cloud-security-incident-response](https://github.com/ahmedhany-cys/aws-cloud-security-incident-response)

**Serverless AWS security monitoring and automated incident response, deployed with Terraform and proven against a live account.**

<p>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/ahmedhany-cys/aws-cloud-security-incident-response/ci.yml?branch=main&style=flat-square&label=CI&labelColor=161B22" alt="CI status" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/LICENSE"><img src="https://img.shields.io/github/license/ahmedhany-cys/aws-cloud-security-incident-response?style=flat-square&labelColor=161B22&color=7AA2F7" alt="MIT license" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/commits/main"><img src="https://img.shields.io/github/last-commit/ahmedhany-cys/aws-cloud-security-incident-response?style=flat-square&labelColor=161B22&color=7AA2F7" alt="Last commit" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/cost-notes.md"><img src="https://img.shields.io/badge/AWS%20Free%20Tier-%240%2Fmonth-2EA043?style=flat-square&labelColor=161B22" alt="Runs at $0 per month on the AWS Free Tier" /></a>
  <img src="https://img.shields.io/badge/Python-3.12%20%7C%203.13-7AA2F7?style=flat-square&labelColor=161B22&logo=python&logoColor=white" alt="Tested on Python 3.12 and 3.13" />
</p>

```
detect  CloudTrail ─► EventBridge ─► Lambda ─► S3 report
health  every 5 min ─► GetTrailStatus ─► CRITICAL if off
```

<table>
  <tr><td valign="top"><b>Detects</b></td><td>IAM policy changes, CloudTrail tampering and S3 permission changes via EventBridge rules, plus a scheduled trail health check</td></tr>
  <tr><td valign="top"><b>Responds</b></td><td>A Python Lambda classifies each event (severity, category, recommended actions), sanitizes credentials out of the record and writes an idempotent JSON incident report to S3</td></tr>
  <tr><td valign="top"><b>Proven</b></td><td>Seven controlled end-to-end scenarios against the deployed stack (six passed, one partial with a documented cause), 32 unit tests, redacted CLI evidence and console screenshots</td></tr>
  <tr><td valign="top"><b>Hardened</b></td><td>Least-privilege IAM for every role, TLS-only encrypted and versioned buckets, Block Public Access everywhere, no hard-coded account IDs</td></tr>
</table>

<p>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/architecture.md"><img src="https://img.shields.io/badge/Architecture-161B22?style=flat-square" alt="Architecture" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response#detection-rules"><img src="https://img.shields.io/badge/Detection%20rules-161B22?style=flat-square" alt="Detection rules" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/design-decisions.md"><img src="https://img.shields.io/badge/Design%20decisions-161B22?style=flat-square" alt="Design decisions" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/test-cases.md"><img src="https://img.shields.io/badge/Test%20results-161B22?style=flat-square" alt="Test results" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/incident-schema.md"><img src="https://img.shields.io/badge/Incident%20schema-161B22?style=flat-square" alt="Incident schema" /></a>
</p>

<details>
<summary><b>Why this project is interesting</b></summary>
<br/>

- **Testing found a real blind spot.** An attacker who calls `StopLogging` silences the very trail the detections depend on. The fix is a scheduled health check that calls `GetTrailStatus` every five minutes and raises a CRITICAL incident when logging stops.
- **Detections are validated against logged events, not API docs.** The S3 rule matches `PutBucketPublicAccessBlock` because that is what CloudTrail actually records.
- **Reports are idempotent.** The incident ID is derived from the CloudTrail event ID, so a retried Lambda never produces duplicate incidents.
- **Evidence is publishable.** Account IDs, source IPs, access key IDs and console sign-in names are redacted from every committed log and screenshot.
- **CI runs without AWS credentials**: pytest on Python 3.12 and 3.13, Ruff, `terraform fmt` and `validate`, ShellCheck and a docs link check.

</details>

<details>
<summary><b>Screenshots from the live deployment</b></summary>
<br/>

<p>
  <img src="https://raw.githubusercontent.com/ahmedhany-cys/aws-cloud-security-incident-response/main/docs/screenshots/04-eventbridge-rules.png" width="49%" alt="EventBridge rules for the detections" />
  <img src="https://raw.githubusercontent.com/ahmedhany-cys/aws-cloud-security-incident-response/main/docs/screenshots/07-lambda-log-detection.png" width="49%" alt="Lambda log line for a detection" />
  <img src="https://raw.githubusercontent.com/ahmedhany-cys/aws-cloud-security-incident-response/main/docs/screenshots/08-incident-bucket-objects.png" width="49%" alt="Incident report objects in the S3 bucket" />
  <img src="https://raw.githubusercontent.com/ahmedhany-cys/aws-cloud-security-incident-response/main/docs/screenshots/11-billing-free-tier.png" width="49%" alt="Billing page showing Free Tier usage" />
</p>

<sub>All screenshots are redacted. More in <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/tree/main/docs/screenshots">docs/screenshots</a>.</sub>

</details>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Achievements

**Repository quality** <sub>· verifiable in the linked files</sub>

<p>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/ahmedhany-cys/aws-cloud-security-incident-response/ci.yml?branch=main&style=flat-square&label=CI&labelColor=161B22" alt="CI status" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/.github/workflows/ci.yml"><img src="https://img.shields.io/badge/CI%20checks-pytest%20%C2%B7%20Ruff%20%C2%B7%20terraform%20validate%20%C2%B7%20ShellCheck%20%C2%B7%20docs%20links-7AA2F7?style=flat-square&labelColor=161B22" alt="CI checks: pytest, Ruff, terraform validate, ShellCheck, docs links" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/test-cases.md"><img src="https://img.shields.io/badge/live%20scenarios-6%20pass%20%C2%B7%201%20partial%20(documented)-7AA2F7?style=flat-square&labelColor=161B22" alt="Live end-to-end scenarios: 6 passed, 1 partial with documented cause" /></a>
</p>

**Security practice**

<p>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/SECURITY.md"><img src="https://img.shields.io/badge/policy-SECURITY.md-7AA2F7?style=flat-square&labelColor=161B22" alt="Security policy" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/.github/dependabot.yml"><img src="https://img.shields.io/badge/Dependabot-enabled-7AA2F7?style=flat-square&labelColor=161B22&logo=dependabot&logoColor=white" alt="Dependabot enabled" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/deployer-policy.json"><img src="https://img.shields.io/badge/IAM-least%20privilege-7AA2F7?style=flat-square&labelColor=161B22" alt="Least-privilege IAM deployer policy" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/CONTRIBUTING.md"><img src="https://img.shields.io/badge/community-CONTRIBUTING%20%C2%B7%20CODE%20OF%20CONDUCT-7AA2F7?style=flat-square&labelColor=161B22" alt="Contributing guide and code of conduct" /></a>
</p>

**Merged pull requests**

- [#1](https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/pull/1) Repository polish: CI, Dependabot, license, community docs and README badges
- [#2](https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/pull/2) Verification fixes: doc accuracy, path redaction, docs link check, Dependabot grouping
- [#6](https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/pull/6) Redact the console sign-in name from nine screenshots

**GitHub achievements** <sub>· none are public on this profile yet</sub>

Earned achievements appear automatically on the profile sidebar. Nothing in this README imitates them.

<details>
<summary><b>Not yet earned: legitimate ways to earn GitHub achievements</b></summary>
<br/>

| Achievement | How it is earned |
|---|---|
| Pull Shark | Open pull requests that get merged |
| Quickdraw | Close an issue or pull request within five minutes of opening it |
| YOLO | Merge a pull request without a review |
| Pair Extraordinaire | Co-author commits on a merged pull request |
| Galaxy Brain | Have answers accepted in GitHub Discussions |
| Starstruck | Create a repository that reaches 16 stars |

<sub>Source: <a href="https://docs.github.com/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile#displaying-achievements-on-your-profile">GitHub Docs — achievements on your profile</a>. Achievements can also be hidden under Settings → Public profile.</sub>

</details>

<!--
  Certifications: add only ones you hold, each linking to its public verification page.
  <a href="https://www.credly.com/badges/YOUR-BADGE-ID"><img src="https://img.shields.io/badge/CERT%20NAME-161B22?style=flat-square" alt="CERT NAME" /></a>
-->

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## GitHub statistics

<div align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=ahmedhany-cys&show_icons=true&hide_rank=true&hide=stars,contribs,issues&show=prs_merged&hide_border=true&border_radius=8&bg_color=0D1117&title_color=7AA2F7&icon_color=7AA2F7&text_color=C0CAF5&custom_title=GitHub%20activity&cache_seconds=21600" alt="GitHub activity for ahmedhany-cys: commits and pull requests" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ahmedhany-cys&layout=compact&langs_count=6&hide_border=true&border_radius=8&bg_color=0D1117&title_color=7AA2F7&text_color=C0CAF5&custom_title=Languages%20in%20public%20repos&cache_seconds=21600" alt="Languages in public repositories" />
</div>

<div align="center">
  <img src="https://streak-stats.demolab.com?user=ahmedhany-cys&hide_border=true&border_radius=8&background=0D1117&stroke=21262D&ring=7AA2F7&fire=FF9E64&currStreakNum=E6EDF3&sideNums=C0CAF5&currStreakLabel=7AA2F7&sideLabels=8B949E&dates=6E7681" alt="Contribution streak for ahmedhany-cys" />
</div>

<br/>

<div align="center">
  <img src="https://raw.githubusercontent.com/ahmedhany-cys/ahmedhany-cys/output/github-snake-dark.svg" width="100%" alt="Contribution graph animation: a snake eats the contribution cells of the past year" />
</div>

<div align="center">
  <sub>Cards are generated live from public data. The language mix covers public repositories only and is not a measure of overall skill.</sub><br/>
  <img src="https://komarev.com/ghpvc/?username=ahmedhany-cys&style=flat-square&color=7AA2F7&labelColor=161B22&label=profile%20views" alt="Profile views" />
</div>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Contact

<div align="center">
  <a href="https://github.com/ahmedhany-cys"><img src="https://img.shields.io/badge/GitHub-ahmedhany--cys-161B22?style=for-the-badge&logo=github&logoColor=white" alt="GitHub: ahmedhany-cys" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/issues"><img src="https://img.shields.io/badge/Open%20an%20issue-161B22?style=for-the-badge&logo=github&logoColor=7AA2F7" alt="Open an issue on the featured project" /></a>
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
