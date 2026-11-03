<!--
  Profile README for github.com/ahmedhany-cys

  Identity "Signal" (dark-first)
    ground  #0D1117 / #0B0F15      surface #161B22      border #21262D
    accent  #7AA2F7 (links, titles) alert   #FF9E64 (severity only)
    text    #C0CAF5 / #8B949E
    Azure badges use labelColor 0078D4, AWS badges use 232F3E.

  Layout: who I am → featured project → open source → work (by lifecycle stage) → what I can do → tools → how I work → activity → contact.
  Adding a project: put it in the lifecycle row it belongs to, keep two cards per row, and move the `new` tag to it.
  Upstream pull requests: the status badges are live from shields.io, so only add a row, never edit a status by hand.

  Generated images
    assets/achievements.svg   .github/workflows/achievements.yml (daily, earned achievements only)
    snake on `output` branch  .github/workflows/snake.yml (daily)
  To change the rotating headline, edit the `lines=` parameter of the typing SVG.
-->

<a id="top"></a>

<div align="center">

<img src="./assets/banner.svg" width="100%" alt="Ahmed Hany, cloud security engineer working on AWS, Azure and Kubernetes. A pulse moves from logs through detection and response into an incident report." />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3200&pause=1200&color=7AA2F7&center=true&vCenter=true&width=720&height=48&lines=Hi%2C+I'm+Ahmed+Hany;I+build+security+tooling+for+AWS%2C+Azure+and+Kubernetes;Detect+%C2%B7+respond+%C2%B7+investigate+%C2%B7+recover;I+send+fixes+upstream+to+Prowler%2C+Trivy+and+Kubescape;Evidence+first%2C+never+a+guess" alt="Hi, I'm Ahmed Hany. I build security tooling for AWS, Azure and Kubernetes. Detect, respond, investigate, recover. I send fixes upstream to Prowler, Trivy and Kubescape. Evidence first, never a guess." />

<p>
  <a href="#about-me"><img src="https://img.shields.io/badge/About-161B22?style=flat-square" alt="About" /></a>
  <a href="#featured"><img src="https://img.shields.io/badge/Featured-161B22?style=flat-square" alt="Featured" /></a>
  <a href="#open-source"><img src="https://img.shields.io/badge/Open%20source-161B22?style=flat-square" alt="Open source" /></a>
  <a href="#selected-work"><img src="https://img.shields.io/badge/Selected%20work-161B22?style=flat-square" alt="Selected work" /></a>
  <a href="#skills"><img src="https://img.shields.io/badge/Skills-161B22?style=flat-square" alt="Skills" /></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/Tech%20stack-161B22?style=flat-square" alt="Tech stack" /></a>
  <a href="#how-i-work"><img src="https://img.shields.io/badge/How%20I%20work-161B22?style=flat-square" alt="How I work" /></a>
  <a href="#activity"><img src="https://img.shields.io/badge/Activity-161B22?style=flat-square" alt="Activity" /></a>
  <a href="#contact"><img src="https://img.shields.io/badge/Contact-161B22?style=flat-square" alt="Contact" /></a>
</p>

</div>

## About me

I'm Ahmed, a cloud security engineer. I build tools that answer the questions a security team actually gets asked: *who could reach this data, who can mint a token our cloud trusts, what happened in this account or cluster, is this release safe to ship, and could we recover if it all went wrong today?*

Most of my work lives on AWS, with Azure and Kubernetes alongside it. I write it in Python and Terraform, put a FastAPI or React front end on it when people need to use it, and test it until I can show evidence for every claim it makes. When the evidence isn't there, my tools say **unknown** instead of guessing. When a scanner I use gets a case wrong, I send the fix upstream.

<table>
  <tr>
    <td width="25%" valign="top">
      <sub><code>focus</code></sub><br/>
      <b>Cloud security engineering</b><br/>
      IAM, detection, incident response and secure infrastructure as code
    </td>
    <td width="25%" valign="top">
      <sub><code>recently added</code></sub><br/>
      <b>Kubernetes &amp; workload identity</b><br/>
      Runtime detection with Falco and Cilium, and audits of OIDC trusts across AWS, GCP and Azure
    </td>
    <td width="25%" valign="top">
      <sub><code>open source</code></sub><br/>
      <b><a href="#open-source">Upstream pull requests</a></b><br/>
      Checks, rules and fixes for Prowler, Kubescape, Trivy and ASH
    </td>
    <td width="25%" valign="top">
      <sub><code>side project</code></sub><br/>
      <b><a href="https://github.com/ahmedhany-cys/security-cheatsheets">Security cheatsheets</a></b><br/>
      16 quick references, from Nmap and Wireshark to Windows event IDs
    </td>
  </tr>
</table>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Featured

<sub><code>featured project</code> &nbsp;<code>04 · respond</code></sub>

### [KubeShield](https://github.com/ahmedhany-cys/kubeshield)

**Kubernetes runtime threat detection and approval-gated response.**
Say a container drops a binary, reads its service account token and tries to reach a database in another namespace. KubeShield picks that up from Falco, Hubble and Kyverno, correlates it into one incident, and only isolates the pod after an analyst approves. Then it proves the isolation with real connections instead of trusting that a policy object exists.

<a href="https://github.com/ahmedhany-cys/kubeshield"><img src="./assets/featured/kubeshield-hero.jpg" width="100%" alt="KubeShield security overview of a local lab cluster: open incidents, high and critical events, vulnerable images, policy violations and detection activity by source" /></a>

<table>
  <tr>
    <td width="33%" valign="top"><img src="./assets/featured/kubeshield-detect.jpg" width="100%" alt="Runtime threats page listing Falco, Hubble and Kyverno security events by severity" /><br/><sub><b>Detect</b>: Falco, Hubble and Kyverno events in one normalised feed</sub></td>
    <td width="33%" valign="top"><img src="./assets/featured/kubeshield-investigate.jpg" width="100%" alt="Incident with eight correlated detections, an event timeline, ATT&amp;CK techniques and a response panel" /><br/><sub><b>Investigate</b>: detections correlated per pod, with timeline and ATT&amp;CK</sub></td>
    <td width="33%" valign="top"><img src="./assets/featured/kubeshield-respond.jpg" width="100%" alt="Response history with approval mode and post-action verification checks for each action" /><br/><sub><b>Respond</b>: approval-gated actions, each verified after it runs</sub></td>
  </tr>
</table>

<p>
  <img src="https://img.shields.io/badge/end--to--end%20checks-46%2F46%20passed-7AA2F7?style=flat-square&labelColor=161B22" alt="46 of 46 end-to-end checks passed" />
  <img src="https://img.shields.io/badge/attack%20scenarios-9%20validated-7AA2F7?style=flat-square&labelColor=161B22" alt="9 attack scenarios validated" />
  <img src="https://img.shields.io/badge/Falco%20rules-8%20custom-7AA2F7?style=flat-square&labelColor=161B22" alt="8 custom Falco rules" />
  <img src="https://img.shields.io/badge/Kyverno%20guardrails-9-7AA2F7?style=flat-square&labelColor=161B22" alt="9 Kyverno guardrails" />
  <img src="https://img.shields.io/badge/unit%20tests-62-7AA2F7?style=flat-square&labelColor=161B22" alt="62 unit tests" />
</p>
<sub><code>Kubernetes</code> · <code>Falco</code> · <code>Cilium / Hubble</code> · <code>Kyverno</code> · <code>Trivy</code> · <code>FastAPI</code> · <code>PostgreSQL</code> · <code>TypeScript</code> · <code>Helm</code></sub>
<br/><br/>
<a href="https://github.com/ahmedhany-cys/kubeshield/blob/main/docs/validation/detection-validation-report.md">Validation report</a> ·
<a href="https://github.com/ahmedhany-cys/kubeshield#problems-found-by-testing-and-fixed">What testing broke</a> ·
<a href="https://github.com/ahmedhany-cys/kubeshield/blob/main/docs/detection-rules.md">Detection rules</a> ·
<a href="https://github.com/ahmedhany-cys/kubeshield/blob/main/docs/architecture.md">Architecture</a> ·
<a href="https://github.com/ahmedhany-cys/kubeshield/blob/main/docs/security-model.md">Security model</a> ·
<a href="https://github.com/ahmedhany-cys/kubeshield/blob/main/docs/limitations.md">Limitations</a>
<br/>
<sub>A lab project: it runs on a local, loopback-only kind cluster and makes no production-readiness claims. Screenshots are from that lab.</sub>

<br/><br/>

<sub><code>spotlight</code> &nbsp;<code>live on AWS</code></sub>

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/ahmedhany-cys/aws-honeytrap#live-proof-of-concept-aws-2026-10-31"><img src="./assets/projects/honeytrap.jpg" width="100%" alt="AWS HoneyTrap dashboard filtered to live data from the proof of concept: 23 events, 11 sessions and 8 sources, with IPs pseudonymised" /></a>
    </td>
    <td width="50%" valign="top">
      <b><a href="https://github.com/ahmedhany-cys/aws-honeytrap">AWS HoneyTrap</a></b>: a honeypot I put on the real internet<br/><br/>
      On 2026-10-31 I deployed all <b>80 resources</b> with Terraform, left a hardened Cowrie decoy exposed for about <b>5 hours 20 minutes</b>, then tore it down and checked every resource type was gone. Cost: about <b>$0.10</b>.<br/><br/>
      Real scanners arrived from 8 sources and every event travelled the whole pipeline. None logged in, so none of the 18 rules fired, and the README says exactly that.<br/><br/>
      <sub><a href="https://github.com/ahmedhany-cys/aws-honeytrap#live-proof-of-concept-aws-2026-10-31">Live results</a> · <a href="https://github.com/ahmedhany-cys/aws-honeytrap/blob/main/docs/evidence/live-poc/teardown-verification.txt">Teardown check</a> · <a href="https://github.com/ahmedhany-cys/aws-honeytrap/blob/main/docs/detections.md">Detections</a> · <a href="https://github.com/ahmedhany-cys/aws-honeytrap/blob/main/docs/cost-management.md">Cost</a></sub>
    </td>
  </tr>
</table>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Open source

Pull requests to security scanners that other teams run in production. Each one ships with tests and follows the project's own conventions. The status badges are live.

| Project | Contribution | Language | Status |
|---|---|---|---|
| <img src="https://github.com/kubescape.png?size=40" width="16" height="16" alt="" /> **[Kubescape](https://github.com/kubescape/kubescape)** | [New rule `modify-admission-webhooks-v1`](https://github.com/kubescape/kubescape/pull/4509): flags RBAC that lets a subject create or change admission webhooks, with test cases for each binding shape | Rego | <a href="https://github.com/kubescape/kubescape/pull/4509"><img src="https://img.shields.io/github/pulls/detail/state/kubescape/kubescape/4509?style=flat-square&label=%234509&labelColor=161B22" alt="kubescape#4509 status" /></a> |
| <img src="https://github.com/prowler-cloud.png?size=40" width="16" height="16" alt="" /> **[Prowler](https://github.com/prowler-cloud/prowler)** | [New check `wafv2_webacl_managed_injection_rule_groups_enabled`](https://github.com/prowler-cloud/prowler/pull/13220): a WAFv2 web ACL should enable the AWS managed rule groups against injection | Python | <a href="https://github.com/prowler-cloud/prowler/pull/13220"><img src="https://img.shields.io/github/pulls/detail/state/prowler-cloud/prowler/13220?style=flat-square&label=%2313220&labelColor=161B22" alt="prowler#13220 status" /></a> |
| <img src="https://github.com/prowler-cloud.png?size=40" width="16" height="16" alt="" /> **[Prowler](https://github.com/prowler-cloud/prowler)** | [Fix: evaluate S3 secure-transport deny statements the way IAM does](https://github.com/prowler-cloud/prowler/pull/13227) | Python | <a href="https://github.com/prowler-cloud/prowler/pull/13227"><img src="https://img.shields.io/github/pulls/detail/state/prowler-cloud/prowler/13227?style=flat-square&label=%2313227&labelColor=161B22" alt="prowler#13227 status" /></a> |
| <img src="https://github.com/aquasecurity.png?size=40" width="16" height="16" alt="" /> **[Trivy](https://github.com/aquasecurity/trivy)** | [Fix: apply the default TLS policy to ELB listeners that set no `ssl_policy`](https://github.com/aquasecurity/trivy/pull/11520), in both the Terraform and CloudFormation adapters | Go | <a href="https://github.com/aquasecurity/trivy/pull/11520"><img src="https://img.shields.io/github/pulls/detail/state/aquasecurity/trivy/11520?style=flat-square&label=%2311520&labelColor=161B22" alt="trivy#11520 status" /></a> |
| <img src="https://github.com/awslabs.png?size=40" width="16" height="16" alt="" /> **[ASH](https://github.com/awslabs/automated-security-helper)** <sub>AWS Labs</sub> | [Fix: say when `uv sync` removes dependencies that ASH installed](https://github.com/awslabs/automated-security-helper/pull/866) | Python | <a href="https://github.com/awslabs/automated-security-helper/pull/866"><img src="https://img.shields.io/github/pulls/detail/state/awslabs/automated-security-helper/866?style=flat-square&label=%23866&labelColor=161B22" alt="automated-security-helper#866 status" /></a> |

<sub>All my pull requests: <a href="https://github.com/pulls?q=is%3Apr+author%3Aahmedhany-cys+-user%3Aahmedhany-cys">github.com/pulls?author=ahmedhany-cys</a></sub>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Selected work

Ordered by the stage of the security lifecycle each one covers, from shipping code to recovering from an incident. Every project is open source (MIT, or Apache-2.0 for KubeShield) and tested, and the demos use synthetic data or simulation mode unless a project says otherwise.

<table>
  <tr>
    <td width="50%" valign="top">
      <sub><code>01 · build</code> &nbsp;Is this release safe to ship?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/azure-supplychain-sentinel"><img src="./assets/projects/sentinel.jpg" width="100%" alt="Azure SupplyChain Sentinel security overview dashboard" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/azure-supplychain-sentinel"><b>Azure SupplyChain Sentinel</b></a>
      <br/>A release gate that turns SBOM, vulnerability, signature and SLSA provenance evidence into a <b>PASS / FAIL / INDETERMINATE</b> decision under a versioned policy.
      <br/><sub><code>Python</code> · <code>Syft</code> · <code>OSV</code> · <code>Cosign</code> · <code>SLSA</code> · <code>FastAPI</code> · <code>Azure</code></sub>
    </td>
    <td width="50%" valign="top">
      <sub><code>01 · build</code> &nbsp;Is this infrastructure safe to deploy?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/infrastructure-as-prompt"><img src="./assets/projects/iap.jpg" width="100%" alt="Infrastructure as Prompt architecture options and cost comparison" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/infrastructure-as-prompt"><b>Infrastructure as Prompt</b></a>
      <br/>Plain-English requirements become traceable AWS requirements and reviewed Terraform, gated by <b>38 deterministic policies</b> over the plan JSON.
      <br/><sub><code>Python</code> · <code>Terraform</code> · <code>React</code> · <code>Checkov</code> · <code>Trivy</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <sub><code>02 · harden</code> &nbsp;Who could reach admin or sensitive data?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/aws-cloud-attack-path-analyzer"><img src="./assets/projects/attackpath.jpg" width="100%" alt="AWS Cloud Attack Path Analyzer HTML report summary" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/aws-cloud-attack-path-analyzer"><b>AWS Cloud Attack Path Analyzer</b></a>
      <br/>Offline, graph-based analysis of IAM and network exposure: a tri-state IAM evaluator, <b>22 checks</b> and least-privilege fixes, with zero runtime dependencies.
      <br/><sub><code>Python</code> · <code>IAM</code> · <code>graph analysis</code> · <code>boto3</code></sub>
    </td>
    <td width="50%" valign="top">
      <sub><code>02 · harden</code> &nbsp;Who can mint a token our cloud trusts?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/trustmint"><img src="./assets/projects/trustmint.svg" width="100%" alt="TrustMint scan of a synthetic estate: 20 federation trusts ranked from PUBLIC to NONE by who can mint a matching token" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/trustmint"><b>TrustMint</b></a> <sub><code>new</code></sub>
      <br/>Offline audit of OIDC workload identity federation from GitHub Actions, GitLab, HCP Terraform, CircleCI and EKS into AWS, GCP and Azure. Every finding is proved with a <b>witness token</b> the trust really accepts.
      <br/><sub><code>Python</code> · <code>OIDC</code> · <code>IAM</code> · <code>CEL</code> · <code>Terraform plans</code> · <code>SARIF</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <sub><code>03 · detect</code> &nbsp;Did someone just change something risky?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response"><img src="./assets/projects/incident.jpg" width="100%" alt="Incident report JSON written to S3, with the account ID and source IP redacted" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/aws-cloud-security-incident-response"><b>AWS Cloud Security Incident Response</b></a>
      <br/>Serverless monitoring: CloudTrail → EventBridge → Lambda → S3 incident reports. Tested against a real account, where it found its own blind spot. <b>$0/month</b>.
      <br/><sub><code>Python</code> · <code>Terraform</code> · <code>Lambda</code> · <code>EventBridge</code></sub>
    </td>
    <td width="50%" valign="top">
      <sub><code>03 · detect</code> &nbsp;Who is knocking, and what do they try?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/aws-honeytrap"><img src="./assets/projects/honeytrap.jpg" width="100%" alt="AWS HoneyTrap dashboard from the live proof of concept: 23 events from 8 sources, with source IPs pseudonymised" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/aws-honeytrap"><b>AWS HoneyTrap</b></a> <sub><code>new</code> <a href="#featured"><code>live on AWS</code></a></sub>
      <br/>A hardened Cowrie SSH/Telnet decoy feeding S3 → EventBridge → Lambda, with <b>18 detection rules</b> mapped to MITRE ATT&amp;CK. Deployed to AWS once for a live proof of concept, then torn down.
      <br/><sub><code>Python</code> · <code>Terraform</code> · <code>Cowrie</code> · <code>Lambda</code> · <code>Streamlit</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <sub><code>04 · respond</code> &nbsp;What happened, and what do we do now?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/cloudsentinel-aws-incident-response"><img src="./assets/projects/cloudsentinel.jpg" width="100%" alt="CloudSentinel security overview dashboard in simulation mode" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/cloudsentinel-aws-incident-response"><b>CloudSentinel</b></a>
      <br/>AWS threat detection and investigation: <b>17 rules mapped to MITRE ATT&amp;CK</b>, incident timelines, blast radius, and approval-gated containment with rollback.
      <br/><sub><code>Python</code> · <code>FastAPI</code> · <code>React</code> · <code>GuardDuty</code> · <code>Terraform</code></sub>
    </td>
    <td width="50%" valign="top">
      <sub><code>04 · respond</code> &nbsp;Something is running in a pod. Contain it?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/kubeshield"><img src="./assets/projects/kubeshield.jpg" width="100%" alt="KubeShield security overview of a local lab cluster: open incidents, high and critical events, policy violations and detection activity" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/kubeshield"><b>KubeShield</b></a> <sub><code>new</code> <a href="#featured"><code>featured</code></a></sub>
      <br/>Kubernetes runtime detection and approval-gated response on Falco, Cilium/Hubble, Kyverno and Trivy. Containment is verified with real traffic: <b>46 of 46</b> end-to-end checks passed in the last full run.
      <br/><sub><code>Kubernetes</code> · <code>Falco</code> · <code>Cilium</code> · <code>Kyverno</code> · <code>FastAPI</code> · <code>TypeScript</code></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <sub><code>05 · investigate</code> &nbsp;What does the evidence prove?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/traceforge-digital-forensics"><img src="./assets/projects/traceforge.jpg" width="100%" alt="TraceForge investigation dashboard with the simulated Meridian case" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/traceforge-digital-forensics"><b>TraceForge</b></a>
      <br/>Digital forensics platform: EVTX, browser, log and PE analysis, <b>YARA</b>, IOC extraction and an explainable cross-source timeline, with a hash-chained chain of custody.
      <br/><sub><code>Python</code> · <code>FastAPI</code> · <code>React</code> · <code>YARA</code> · <code>pefile</code></sub>
    </td>
    <td width="50%" valign="top">
      <sub><code>06 · recover</code> &nbsp;Could we actually come back from it?</sub><br/>
      <a href="https://github.com/ahmedhany-cys/recoveryproof"><img src="./assets/projects/recoveryproof.jpg" width="100%" alt="RecoveryProof executive overview with a readiness score" /></a>
      <br/><a href="https://github.com/ahmedhany-cys/recoveryproof"><b>RecoveryProof</b></a>
      <br/>Evidence-based disaster-recovery analysis: RTO/RPO compliance, dependency-aware recovery order and <b>10 incident scenarios</b>, including ransomware.
      <br/><sub><code>Python</code> · <code>Streamlit</code> · <code>NetworkX</code> · <code>Plotly</code></sub>
    </td>
  </tr>
</table>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Skills

What I can do, and where you can check it.

| Area | What that means in practice | See it in |
|---|---|---|
| **Cloud IAM &amp; attack paths** | Evaluate IAM the way AWS does (explicit deny, boundaries, cross-account trust, conditions) and turn misconfigurations into attack paths with least-privilege fixes | [Attack Path Analyzer](https://github.com/ahmedhany-cys/aws-cloud-attack-path-analyzer) |
| **Workload identity &amp; OIDC** <sub>`new`</sub> | Work out who can obtain a token that an AWS role, Google service account or Entra app accepts, by evaluating each cloud's own condition language, and flag CI jobs where untrusted code can mint one | [TrustMint](https://github.com/ahmedhany-cys/trustmint) |
| **Threat detection** | Write detection rules over CloudTrail, GuardDuty and honeypot telemetry, mapped to MITRE ATT&amp;CK, each with a confidence level and benign explanations to rule out | [CloudSentinel](https://github.com/ahmedhany-cys/cloudsentinel-aws-incident-response) · [Incident response](https://github.com/ahmedhany-cys/aws-cloud-security-incident-response) · [HoneyTrap](https://github.com/ahmedhany-cys/aws-honeytrap) |
| **Kubernetes security** <sub>`new`</sub> | Detect runtime threats with Falco, enforce admission policy with Kyverno, isolate pods with Cilium and prove the block with real connections; write Kubescape rules for risky RBAC | [KubeShield](https://github.com/ahmedhany-cys/kubeshield) · [Kubescape PR](https://github.com/kubescape/kubescape/pull/4509) |
| **Deception &amp; threat intelligence** <sub>`new`</sub> | Run a contained honeypot with no egress, turn its telemetry into evidence-backed alerts, and label every dataset as live, simulated or synthetic | [HoneyTrap](https://github.com/ahmedhany-cys/aws-honeytrap) |
| **Incident response** | Correlate events into timelines, estimate blast radius, and run containment only through dry runs, separate-person approval and rollback | [CloudSentinel](https://github.com/ahmedhany-cys/cloudsentinel-aws-incident-response) |
| **Digital forensics &amp; malware analysis** | Parse EVTX logs, browser history and PE files, write YARA rules, extract IOCs, rebuild a UTC timeline, and keep a hash-chained chain of custody | [TraceForge](https://github.com/ahmedhany-cys/traceforge-digital-forensics) |
| **Software supply chain** | Generate CycloneDX SBOMs, check them against OSV, verify Sigstore signatures and SLSA v1 provenance, and gate releases on policy | [SupplyChain Sentinel](https://github.com/ahmedhany-cys/azure-supplychain-sentinel) |
| **Secure IaC &amp; policy as code** | Generate Terraform from requirements and block it with deterministic policies over the plan JSON, alongside Checkov and Trivy | [Infrastructure as Prompt](https://github.com/ahmedhany-cys/infrastructure-as-prompt) |
| **Cyber resilience** | Model system dependencies, check backups against RTO/RPO, simulate ransomware and admin compromise, and plan a safe recovery order | [RecoveryProof](https://github.com/ahmedhany-cys/recoveryproof) |
| **DevSecOps** | CI that lints, type-checks, tests and scans every change: secrets, dependencies, containers and IaC | the `ci.yml` in each repository |
| **Open-source contribution** <sub>`new`</sub> | Read a large security codebase, find where a check is wrong or missing, and send a tested fix in the project's own style | [Prowler, Kubescape, Trivy, ASH](#open-source) |
| **Security tooling UX** | Turn analysis into something people can use: CLIs with CI exit codes, REST APIs, dashboards and print-ready reports | all of the above |

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Tech stack

<div align="center">
  <img src="https://skillicons.dev/icons?i=aws,azure,kubernetes,terraform,py,go,ts,react,fastapi,postgres,docker,githubactions,bash,linux,git&perline=15" alt="AWS, Azure, Kubernetes, Terraform, Python, Go, TypeScript, React, FastAPI, PostgreSQL, Docker, GitHub Actions, Bash, Linux, Git" />
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
      <a href="https://go.dev/doc/"><img src="https://img.shields.io/badge/Go-161B22?style=flat-square&logo=go&logoColor=00ADD8" alt="Go" /></a>
      <a href="https://www.openpolicyagent.org/docs/latest/policy-language/"><img src="https://img.shields.io/badge/Rego-161B22?style=flat-square&logo=openpolicyagent&logoColor=7D9199" alt="Rego" /></a>
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
    <td><b>Azure</b></td>
    <td>
      <a href="https://learn.microsoft.com/azure/key-vault/"><img src="https://img.shields.io/badge/Azure-Key%20Vault-161B22?style=flat-square&labelColor=0078D4" alt="Azure Key Vault" /></a>
      <a href="https://learn.microsoft.com/azure/container-registry/"><img src="https://img.shields.io/badge/Azure-Container%20Registry-161B22?style=flat-square&labelColor=0078D4" alt="Azure Container Registry" /></a>
      <a href="https://learn.microsoft.com/azure/storage/"><img src="https://img.shields.io/badge/Azure-Storage-161B22?style=flat-square&labelColor=0078D4" alt="Azure Storage" /></a>
    </td>
  </tr>
  <tr>
    <td><b>Kubernetes</b> <sub><code>new</code></sub></td>
    <td>
      <a href="https://kubernetes.io/docs/home/"><img src="https://img.shields.io/badge/Kubernetes-161B22?style=flat-square&logo=kubernetes&logoColor=326CE5" alt="Kubernetes" /></a>
      <a href="https://falco.org/docs/"><img src="https://img.shields.io/badge/Falco-161B22?style=flat-square&logo=falco&logoColor=00AEC7" alt="Falco" /></a>
      <a href="https://docs.cilium.io/"><img src="https://img.shields.io/badge/Cilium%20%2F%20Hubble-161B22?style=flat-square&logo=cilium&logoColor=F8C517" alt="Cilium and Hubble" /></a>
      <a href="https://kyverno.io/docs/"><img src="https://img.shields.io/badge/Kyverno-161B22?style=flat-square" alt="Kyverno" /></a>
      <a href="https://kubescape.io/docs/"><img src="https://img.shields.io/badge/Kubescape-161B22?style=flat-square" alt="Kubescape" /></a>
      <a href="https://helm.sh/docs/"><img src="https://img.shields.io/badge/Helm-161B22?style=flat-square&logo=helm&logoColor=white" alt="Helm" /></a>
      <a href="https://kind.sigs.k8s.io/"><img src="https://img.shields.io/badge/kind-161B22?style=flat-square" alt="kind" /></a>
      <a href="https://ebpf.io/"><img src="https://img.shields.io/badge/eBPF-161B22?style=flat-square&logo=ebpf&logoColor=white" alt="eBPF" /></a>
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
      <a href="https://yara.readthedocs.io/"><img src="https://img.shields.io/badge/YARA-161B22?style=flat-square" alt="YARA" /></a>
      <a href="https://github.com/erocarrera/pefile"><img src="https://img.shields.io/badge/pefile-161B22?style=flat-square" alt="pefile" /></a>
      <a href="https://github.com/williballenthin/python-evtx"><img src="https://img.shields.io/badge/python--evtx-161B22?style=flat-square" alt="python-evtx" /></a>
      <a href="https://docs.prowler.com/"><img src="https://img.shields.io/badge/Prowler-161B22?style=flat-square" alt="Prowler" /></a>
      <a href="https://cowrie.readthedocs.io/"><img src="https://img.shields.io/badge/Cowrie-161B22?style=flat-square" alt="Cowrie" /></a>
      <a href="https://openid.net/developers/how-connect-works/"><img src="https://img.shields.io/badge/OIDC-161B22?style=flat-square&logo=openid&logoColor=F78C40" alt="OpenID Connect" /></a>
      <a href="https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html"><img src="https://img.shields.io/badge/SARIF-161B22?style=flat-square" alt="SARIF" /></a>
      <a href="https://github.com/terraform-linters/tflint"><img src="https://img.shields.io/badge/tflint-161B22?style=flat-square" alt="tflint" /></a>
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
      <a href="https://www.postgresql.org/docs/"><img src="https://img.shields.io/badge/PostgreSQL-161B22?style=flat-square&logo=postgresql&logoColor=4169E1" alt="PostgreSQL" /></a>
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

<sub>Only tools used in my public repositories or in my upstream pull requests are listed. Every badge links to the official documentation.</sub>

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## How I work

The same rules run through every project above.

- **Facts, inferences and guesses stay separate.** Findings are labelled as observed, derived, hypothetical or unknown, and my tools return *indeterminate* rather than a false all-clear.
- **Test the outcome, not the deployment.** A successful `terraform apply` proves nothing about whether a rule fires. Only an observed result does.
- **Check assumptions against reality.** API names are not always event names; CloudTrail logs `PutBucketPublicAccessBlock`, not `PutPublicAccessBlock`.
- **Automation never acts alone.** Containment needs a dry run and approval from a different person; a deployment approval is bound to the hash of the exact plan that was reviewed.
- **Least privilege is a design input, not a cleanup step.** Every role gets exactly what it needs, and every unavoidable `*` gets a comment explaining why.
- **Write down the limitations.** Every project documents what it does not do. A partial result with a documented cause beats a green check nobody can trust.
- **Fix it where it lives.** When a scanner I rely on gets a case wrong, the fix goes upstream with tests, not into a local workaround.
- **Share evidence safely and cheaply.** Real identifiers are redacted, demos use synthetic data, and I like running whole stacks inside the free tier.

<div align="right"><a href="#top"><sub>back to top ↑</sub></a></div>

## Activity

<div align="center">
  <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=ahmedhany-cys&theme=tokyonight" alt="GitHub statistics for ahmedhany-cys: stars, commits, pull requests and issues" />
  <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=ahmedhany-cys&theme=tokyonight" alt="Languages in the commits of ahmedhany-cys" />
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
  <a href="https://www.instagram.com/ahmedhany.cys"><img src="https://img.shields.io/badge/Instagram-ahmedhany.cys-161B22?style=for-the-badge&logo=instagram&logoColor=E4405F" alt="Instagram: ahmedhany.cys" /></a>
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
