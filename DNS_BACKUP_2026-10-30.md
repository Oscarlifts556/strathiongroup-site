# strathiongroup.com DNS before the GitHub Pages switch (2026-10-30, read from Squarespace)

To undo: re-add the "Squarespace Defaults" preset (DNS Settings > Add preset > Squarespace Defaults)
and delete the GitHub records.

## Squarespace Defaults (website, removed by the switch)
| Type | Name | TTL | Data |
|---|---|---|---|
| A | @ | 4 hrs | 198.185.159.144 |
| A | @ | 4 hrs | 198.185.159.145 |
| A | @ | 4 hrs | 198.49.23.144 |
| A | @ | 4 hrs | 198.49.23.145 |
| CNAME | www | 4 hrs | ext-sq.squarespace.com |
| HTTPS | @ | 4 hrs | 1 . alpn="h2,http/1.1" ipv4hint="198.185.159.144,198.185.159.145,198.49.23.144,198.49.23.145" |

## Squarespace Domain Connect (kept)
| CNAME | _domainconnect | 1 hr | _domainconnect.domains.squarespace.com |

## Custom records: Google Workspace email (kept, never touch)
| Type | Name | Priority | TTL | Data |
|---|---|---|---|---|
| MX | @ | 1 | 1 hr | smtp.google.com |
| TXT | @ | | 1 hr | v=spf1 include:_spf.google.com ~all |
| TXT | _dmarc | | 30 mins | v=DMARC1; p=none; rua=mailto:ojohnston@strathiongroup.com |
| TXT | google._domainkey | | 1 hr | v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAua7QHzQ2A1dztpoDLNAUBl1kJ5MZopxnEGUOvXihFII1Zy8e7LtJhQMuLZ220eCZ93n8eOJcFWKaGqxNjVBexIdR/uGQpMd/EGZdkODqx+APDIMlbuRAdGMdUNSp5BSlFpLKJ6BCngge2lggjx19FSUV2gEGrc1hGz9jt0kOIouXmnQvaU9BprfnDDFJ+RHvGbtR019spO7DkBo9pQSN9mFGNRy2waoWVjU6htlQzbeKI/GtUDQJieZBP6Cc1Xu5vyj1YAU6WeCz3uLc/kPTEKb7MBBZILKTEhUVIefPIGXSp/LnZuOsbSwUD1ZDIB0gPS73N+OYQzTma6ImQmu54QIDAQAB |

## Added for GitHub Pages
| A | @ | 185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153 |
| CNAME | www | oscarlifts556.github.io |
