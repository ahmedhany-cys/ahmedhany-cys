<!--
  Profile README for github.com/ahmedhany-cys
  Palette (Tokyo Night): background #0D1117 · accent #7AA2F7 · text #C0CAF5
  Every card below is generated live from GitHub data. Nothing is hard-coded.
  To change the headline lines, edit the `lines=` parameter of the typing SVG.
-->

<div align="center">

<a href="https://github.com/ahmedhany-cys">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3500&pause=1000&color=7AA2F7&center=true&vCenter=true&width=720&height=64&lines=Hi%2C+I'm+Ahmed+Hany;Cloud+Security+%26+Detection+Engineering;AWS+%C2%B7+Terraform+%C2%B7+Python" alt="Hi, I'm Ahmed Hany. Cloud Security and Detection Engineering. AWS, Terraform, Python." />
</a>

<p>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response">
    <img src="https://img.shields.io/badge/Featured-AWS%20Security%20Monitoring%20%26%20Incident%20Response-7AA2F7?style=for-the-badge&logo=github&logoColor=white" alt="Featured project: AWS Security Monitoring and Incident Response" />
  </a>
  <img src="https://komarev.com/ghpvc/?username=ahmedhany-cys&style=for-the-badge&color=7aa2f7&label=Profile+views" alt="Profile views" />
</p>

</div>

## About me

I build cloud security tooling on AWS, and I care about proving that a detection
works, not just that it deploys.

My current focus is **detection engineering and automated incident response**:
turning CloudTrail activity into structured, actionable incident reports with
serverless, least-privilege infrastructure defined entirely in Terraform.

- 🔭 **Building:** serverless security monitoring on AWS (CloudTrail → EventBridge → Lambda → S3)
- 🧪 **How I work:** every detection is exercised end to end against a live account, with redacted evidence committed next to the code
- 💸 **Constraint I enjoy:** the whole stack runs at $0/month inside the AWS Free Tier
- 🧭 **Interests:** AWS IAM and least privilege, threat detection, infrastructure as code, security automation

## Tech stack

<div align="center">
  <img src="https://skillicons.dev/icons?i=aws,terraform,python,bash,git,github,githubactions,linux&perline=8" alt="AWS, Terraform, Python, Bash, Git, GitHub, GitHub Actions, Linux" />
</div>

<br/>

<table align="center">
  <tr>
    <td align="right"><b>Cloud &amp; security</b></td>
    <td>
      <img src="https://img.shields.io/badge/CloudTrail-FF9900?style=flat-square&logoColor=white" alt="CloudTrail" />
      <img src="https://img.shields.io/badge/EventBridge-FF9900?style=flat-square" alt="EventBridge" />
      <img src="https://img.shields.io/badge/Lambda-FF9900?style=flat-square" alt="Lambda" />
      <img src="https://img.shields.io/badge/S3-FF9900?style=flat-square" alt="S3" />
      <img src="https://img.shields.io/badge/IAM-FF9900?style=flat-square" alt="IAM" />
      <img src="https://img.shields.io/badge/CloudWatch-FF9900?style=flat-square" alt="CloudWatch" />
      <img src="https://img.shields.io/badge/SNS-FF9900?style=flat-square" alt="SNS" />
    </td>
  </tr>
  <tr>
    <td align="right"><b>Infrastructure</b></td>
    <td>
      <img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white" alt="Terraform" />
      <img src="https://img.shields.io/badge/Serverless-2EA043?style=flat-square" alt="Serverless" />
      <img src="https://img.shields.io/badge/Infrastructure%20as%20Code-2EA043?style=flat-square" alt="Infrastructure as Code" />
      <img src="https://img.shields.io/badge/Least%20privilege%20IAM-2EA043?style=flat-square" alt="Least privilege IAM" />
    </td>
  </tr>
  <tr>
    <td align="right"><b>Languages &amp; testing</b></td>
    <td>
      <img src="https://img.shields.io/badge/Python%203.12-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.12" />
      <img src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" alt="pytest" />
      <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash" />
      <img src="https://img.shields.io/badge/ShellCheck-4EAA25?style=flat-square" alt="ShellCheck" />
      <img src="https://img.shields.io/badge/Ruff-D7FF64?style=flat-square&logo=ruff&logoColor=black" alt="Ruff" />
    </td>
  </tr>
  <tr>
    <td align="right"><b>Workflow</b></td>
    <td>
      <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />
      <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
      <img src="https://img.shields.io/badge/Dependabot-025E8C?style=flat-square&logo=dependabot&logoColor=white" alt="Dependabot" />
      <img src="https://img.shields.io/badge/Conventional%20Commits-FE5196?style=flat-square&logo=conventionalcommits&logoColor=white" alt="Conventional Commits" />
    </td>
  </tr>
</table>

## Featured project

<div align="center">
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=ahmedhany-cys&repo=aws-cloud-security-incident-response&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=7AA2F7&icon_color=7AA2F7&text_color=C0CAF5" alt="aws-cloud-security-incident-response repository card" />
  </a>
</div>

**[aws-cloud-security-incident-response](https://github.com/ahmedhany-cys/aws-cloud-security-incident-response)**
is a serverless detection and response pipeline for a single AWS account,
deployed entirely with Terraform and proven against a live deployment.

```
Detect:  CloudTrail ─► EventBridge rules ─► Lambda ─► S3 incident report (JSON)
Health:  Scheduler (5 min) ─► Lambda ─► GetTrailStatus ─► CRITICAL if trail stops
```

| | |
|---|---|
| 🔍 **Detects** | IAM policy changes, CloudTrail tampering and S3 permission changes via EventBridge rules, plus a scheduled trail health check that closes the `StopLogging` blind spot found during testing |
| ⚡ **Responds** | A Python Lambda classifies each event (severity, category, recommended actions), sanitises credentials out of the record, and writes an idempotent JSON incident report to S3 |
| 🧪 **Proven** | Seven controlled end-to-end scenarios run against the deployed stack, 32 unit tests, and redacted CLI evidence plus console screenshots committed in the repo |
| 🔐 **Hardened** | Least-privilege IAM for every role, TLS-only encrypted and versioned buckets, Block Public Access everywhere, no hard-coded account IDs |
| 💸 **Cost** | $0/month by design: one trail, management events only, always-free Lambda and EventBridge limits |

<div align="center">
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response#detection-rules"><img src="https://img.shields.io/badge/Detection%20rules-7AA2F7?style=flat-square" alt="Detection rules" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/architecture.md"><img src="https://img.shields.io/badge/Architecture-7AA2F7?style=flat-square" alt="Architecture" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/design-decisions.md"><img src="https://img.shields.io/badge/Design%20decisions-7AA2F7?style=flat-square" alt="Design decisions" /></a>
  <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/test-cases.md"><img src="https://img.shields.io/badge/Test%20results-7AA2F7?style=flat-square" alt="Test results" /></a>
</div>

## Principles I build with

Lessons from shipping and testing real detections:

- **Test the detection, not the deployment.** A successful `terraform apply` proves nothing about whether a rule fires. Only an observed incident does.
- **API names are not always event names.** CloudTrail logs `PutBucketPublicAccessBlock`, not `PutPublicAccessBlock`. Validate every pattern against real logged events.
- **Least privilege is a design input, not a cleanup step.** Every role gets exactly the actions and resources it needs, and every unavoidable `*` gets a comment explaining why.
- **Evidence leaks more than account IDs.** Source IPs, access key IDs and principal IDs are redacted before anything is committed.
- **Write down the limitations.** A partial result with a documented cause is worth more than a green check nobody can trust.

## GitHub stats

<div align="center">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=ahmedhany-cys&show_icons=true&include_all_commits=true&hide_rank=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=7AA2F7&icon_color=7AA2F7&text_color=C0CAF5" alt="GitHub statistics for ahmedhany-cys" />
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ahmedhany-cys&layout=compact&langs_count=6&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=7AA2F7&text_color=C0CAF5" alt="Most used languages" />
</div>

## Let's connect

<div align="center">
  <a href="https://github.com/ahmedhany-cys">
    <img src="https://img.shields.io/badge/GitHub-ahmedhany--cys-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub: ahmedhany-cys" />
  </a>
  <!--
    Add verified profiles here. Replace the handles, then move the lines out of this comment:
    <a href="https://www.linkedin.com/in/YOUR-HANDLE">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge" alt="LinkedIn" />
    </a>
    <a href="mailto:you@example.com">
      <img src="https://img.shields.io/badge/Email-Say%20hello-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
    </a>
  -->
</div>

<br/>

<div align="center">
  <sub>Built in the open. Every stat on this page is live, and every claim links to the code that backs it.</sub>
</div>
