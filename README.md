<!--
  Profile README for github.com/ahmedhany-cys

  Identity "Signal" (dark-first)
    ground  #0D1117 / #0B0F15      surface #161B22      border #21262D
    accent  #7AA2F7 (links, titles) alert   #FF9E64 (severity, streak fire only)
    text    #C0CAF5 / #8B949E

  Generated images
    assets/achievements.svg   .github/workflows/achievements.yml (daily, earned achievements only)
    snake on `output` branch  .github/workflows/snake.yml (daily)
  To change the rotating headline, edit the `lines=` parameter of the typing SVG.
-->

<a id="top"></a>

<div align="center">

<img src="./assets/banner.svg" width="100%" alt="Ahmed Hany — cloud security and detection engineering. A pulse moves from logs through detection and response into an incident report." />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3200&pause=1200&color=7AA2F7&center=true&vCenter=true&width=640&height=48&lines=Hi%2C+I'm+Ahmed+Hany;I+build+security+tooling+on+AWS;Detection+engineering+%C2%B7+IaC+%C2%B7+automation;I+test+what+I+ship" alt="Hi, I'm Ahmed Hany. I build security tooling on AWS. Detection engineering, infrastructure as code, automation. I test what I ship." />

<p>
  <a href="#about-me"><img src="https://img.shields.io/badge/About-161B22?style=flat-square" alt="About" /></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/Tech%20stack-161B22?style=flat-square" alt="Tech stack" /></a>
  <a href="#projects"><img src="https://img.shields.io/badge/Projects-161B22?style=flat-square" alt="Projects" /></a>
  <a href="#achievements"><img src="https://img.shields.io/badge/Achievements-161B22?style=flat-square" alt="Achievements" /></a>
  <a href="#github-statistics"><img src="https://img.shields.io/badge/Statistics-161B22?style=flat-square" alt="Statistics" /></a>
  <a href="#contact"><img src="https://img.shields.io/badge/Contact-161B22?style=flat-square" alt="Contact" /></a>
</p>

</div>

## About me

I'm Ahmed, and I work on the security side of the cloud. I like building things that notice when something goes wrong and explain it clearly: detections, automated responses and the infrastructure underneath them, all written as code. I care about proving that what I build actually works, so I test against real environments and write down what I learn, including the limitations.

**What I work on**

<table>
  <tr>
    <td width="50%" valign="top"><sub><code>cloud security</code></sub><br/>Securing AWS accounts: least-privilege IAM, encrypted and locked-down storage, audit logging that can't silently stop</td>
    <td width="50%" valign="top"><sub><code>detection engineering</code></sub><br/>Turning raw activity logs into rules that fire on the events that matter, validated against what is really logged</td>
  </tr>
  <tr>
    <td valign="top"><sub><code>infrastructure as code</code></sub><br/>Everything defined in Terraform: repeatable, reviewable, and easy to tear down</td>
    <td valign="top"><sub><code>automation</code></sub><br/>Python and Bash to classify events, write reports and run tests, plus CI that checks it all on every change</td>
  </tr>
</table>

<details>
<summary><b>How I work</b></summary>
<br/>

- **Test the outcome, not the deployment.** A successful `terraform apply` proves nothing about whether a rule fires. Only an observed result does.
- **Check assumptions against reality.** API names are not always event names; CloudTrail logs `PutBucketPublicAccessBlock`, not `PutPublicAccessBlock`.
- **Least privilege is a design input, not a cleanup step.** Every role gets exactly what it needs, and every unavoidable `*` gets a comment explaining why.
- **Share evidence safely.** Account IDs, IPs, keys and sign-in names are redacted before anything is published.
- **Write down the limitations.** A partial result with a documented cause is worth more than a green check nobody can trust.
- **Keep it cheap.** I like constraints such as running a whole stack inside the AWS Free Tier.

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

## Projects

<table>
  <tr>
    <td>
      <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response"><b>aws-cloud-security-incident-response</b></a>
      &nbsp;<a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/ahmedhany-cys/aws-cloud-security-incident-response/ci.yml?branch=main&style=flat-square&label=CI&labelColor=161B22" alt="CI status" /></a>
      <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/LICENSE"><img src="https://img.shields.io/github/license/ahmedhany-cys/aws-cloud-security-incident-response?style=flat-square&labelColor=161B22&color=7AA2F7" alt="MIT license" /></a>
      <br/>
      Serverless AWS security monitoring and automated incident response: CloudTrail events are matched by EventBridge rules, classified by a Python Lambda and written to S3 as JSON incident reports.
      <br/><br/>
      <sub><code>Python</code> · <code>Terraform</code> · <code>CloudTrail</code> · <code>EventBridge</code> · <code>Lambda</code> · <code>S3</code> · <code>IAM</code></sub>
      <br/><br/>
      <b>Interesting because:</b> live testing exposed a real blind spot (an attacker calling <code>StopLogging</code> silences the trail), closed with a 5-minute health check. Seven end-to-end scenarios against a real account, 32 unit tests, and the whole stack runs at $0/month.
    </td>
  </tr>
</table>

<details>
<summary><b>Preview and details</b></summary>
<br/>

<img src="./assets/project-incident-preview.png" width="100%" alt="Incident report JSON written to S3 for test T5 (DeleteBucketPublicAccessBlock), with the account ID and source IP redacted" />

```
detect  CloudTrail ─► EventBridge ─► Lambda ─► S3 report
health  every 5 min ─► GetTrailStatus ─► CRITICAL if off
```

- **Detects** IAM policy changes, CloudTrail tampering and S3 permission changes
- **Responds** by classifying severity, sanitizing credentials and writing an idempotent JSON report
- **Proven** by seven controlled scenarios (six passed, one partial with a documented cause) and 32 unit tests
- **Hardened** with least-privilege IAM, TLS-only encrypted versioned buckets and Block Public Access

<a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/architecture.md">Architecture</a> ·
<a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response#detection-rules">Detection rules</a> ·
<a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/design-decisions.md">Design decisions</a> ·
<a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/blob/main/docs/test-cases.md">Test results</a> ·
<a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response/tree/main/docs/screenshots">Screenshots</a>

</details>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Achievements

<div align="center">
  <a href="https://github.com/ahmedhany-cys">
    <img src="./assets/achievements.svg" width="100%" alt="GitHub achievements earned by ahmedhany-cys, with locked slots for ones not yet earned" />
  </a>
  <br/>
  <sub>Real badges from my <a href="https://github.com/ahmedhany-cys">GitHub profile</a>, redrawn daily. Locked slots are ones I haven't earned yet.</sub>
</div>

<details>
<summary><b>How the locked ones are earned</b></summary>
<br/>

| Achievement | How it is earned |
|---|---|
| Pull Shark | Open pull requests that get merged |
| Quickdraw | Close an issue or pull request within five minutes of opening it |
| YOLO | Merge a pull request without a review |
| Pair Extraordinaire | Co-author commits on a merged pull request |
| Galaxy Brain | Have answers accepted in GitHub Discussions |
| Starstruck | Create a repository that reaches 16 stars |

<sub>Source: <a href="https://docs.github.com/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile#displaying-achievements-on-your-profile">GitHub Docs</a>.</sub>

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
