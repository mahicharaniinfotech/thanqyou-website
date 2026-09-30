r"""
Creates Privacy Policy, Terms of Service, and Account Deletion pages
for the website, matching the exact palette/fonts already established
by the Community Guidelines page (--wine #722F37, --paper #FBF3EC,
--gold #C9963E, Sora/Pacifico/Inter). Content reflects the CURRENT
live revenue-share model (30/50/20 ad-revenue split), not the stale
fixed-rate model still shown in the in-app Terms sheet.

Usage:
    python build_legal_pages.py <path-to-website-repo-root>

Example:
    python build_legal_pages.py "C:\Users\workw\Desktop\ThanQYou"
"""

import sys
from pathlib import Path


def fail(msg):
    print(f"FAILED: {msg}")
    sys.exit(1)


STYLE_BLOCK = r'''<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Sora:wght@600;700;800&family=Pacifico&display=swap" rel="stylesheet">
<style>
:root{
  --wine:#722F37; --wine-deep:#4A1E23; --wine-soft:rgba(114,47,55,0.07); --wine-soft2:rgba(114,47,55,0.13);
  --paper:#FBF3EC; --paper2:#F5E9DE; --ink:#241A1C; --ink2:#5C4E4A; --ink3:#8C7D78;
  --gold:#C9963E; --gold-soft:rgba(201,150,62,0.14);
  --white:#FFFFFF;
  --radius:20px;
}
html{scroll-behavior:smooth;}
body{font-family:'Inter',sans-serif;background:var(--paper);color:var(--ink);line-height:1.7;margin:0;}
.script{font-family:'Pacifico',cursive;}
.head{font-family:'Sora',sans-serif;}
nav{position:fixed;top:0;left:0;right:0;z-index:200;display:flex;align-items:center;justify-content:space-between;padding:0 6%;height:76px;background:rgba(251,243,236,0.86);backdrop-filter:blur(18px);border-bottom:1px solid rgba(114,47,55,0.09);}
.brand-name{font-family:'Sora',sans-serif;font-weight:800;font-size:19px;color:var(--wine);letter-spacing:-0.01em;text-decoration:none;}
.back-link{font-size:13px;font-weight:600;color:var(--ink2);text-decoration:none;padding:9px 20px;border-radius:100px;border:1px solid rgba(114,47,55,0.18);transition:all .2s;}
.back-link:hover{background:var(--wine);color:#fff;border-color:var(--wine);}
main{max-width:800px;margin:0 auto;padding:150px 6% 100px;}
h1{font-family:'Sora',sans-serif;font-weight:800;font-size:clamp(2.2rem,5vw,3rem);color:var(--wine);margin:0 0 8px;}
.updated{color:var(--ink3);font-size:14px;margin-bottom:40px;}
h2{font-family:'Sora',sans-serif;font-weight:700;font-size:20px;color:var(--wine-deep);margin:36px 0 12px;}
h3{font-family:'Sora',sans-serif;font-weight:700;font-size:16px;color:var(--wine);margin:24px 0 8px;}
p{color:var(--ink2);font-size:15px;margin:0 0 14px;}
ul,ol{color:var(--ink2);font-size:15px;margin:0 0 14px;padding-left:22px;}
li{margin-bottom:6px;}
.card{background:var(--white);border:1px solid rgba(114,47,55,0.09);border-radius:var(--radius);padding:24px 28px;margin:20px 0;}
.highlight{background:var(--gold-soft);border-radius:var(--radius);padding:22px 26px;margin:24px 0;}
.highlight p{margin:0;color:var(--ink2);}
a.inline{color:var(--wine);font-weight:600;}
footer{padding:40px 6%;text-align:center;color:var(--ink3);font-size:13px;border-top:1px solid rgba(114,47,55,0.09);}
footer a{color:var(--wine);text-decoration:none;font-weight:600;}
table{width:100%;border-collapse:collapse;margin:16px 0;font-size:14px;}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid rgba(114,47,55,0.09);color:var(--ink2);}
th{color:var(--wine);font-family:'Sora',sans-serif;font-weight:700;}
</style>'''

NAV_BLOCK = '''<nav>
  <a href="/" class="brand-name">ThanQYou</a>
  <a href="/" class="back-link">&larr; Back to home</a>
</nav>'''

FOOTER_BLOCK = '''<footer>
  &copy; 2026 MAANYA IT &amp; HR SERVICES. All rights reserved.<br>
  ThanQYou is owned and operated by MAANYA IT &amp; HR SERVICES, Ground Floor, Plot No 235, Road No 93, Near Yaari House, Kapra, Hyderabad, Medchal Malkajgiri District, Telangana 500083, India.<br>
  <a href="/">Home</a> &nbsp;|&nbsp;
  <a href="/privacy-policy.html">Privacy</a> &nbsp;|&nbsp;
  <a href="/terms-of-service.html">Terms</a> &nbsp;|&nbsp;
  <a href="/community-guidelines.html">Community Guidelines</a> &nbsp;|&nbsp;
  <a href="/delete-account.html">Delete Account</a>
</footer>'''


def page(title, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - ThanQYou</title>
<link rel="icon" type="image/png" href="/images/app_icon.png">
{STYLE_BLOCK}
</head>
<body>
{NAV_BLOCK}
<main>
{body}
</main>
{FOOTER_BLOCK}
</body>
</html>
'''


PRIVACY_BODY = '''<h1>Privacy Policy</h1>
<p class="updated">Last updated: September 2026</p>
<p>The ThanQYou mobile application is owned and operated by <strong>MAANYA IT &amp; HR SERVICES</strong>, a partnership firm registered in India with its principal place of business at Ground Floor, Plot No 235, Road No 93, Near Yaari House, Kapra, Hyderabad, Medchal Malkajgiri District, Telangana 500083, India ("ThanQYou", "we", "us", "our"). The app combines messaging, social features, and an ad-revenue-sharing earning system. This policy explains what information we collect, why, and how you can control it.</p>

<h2>1. Information We Collect</h2>
<h3>Account &amp; Identity</h3>
<ul>
  <li>Full name (as per your government ID), date of birth, gender, phone number, email address</li>
  <li>Government ID details for KYC verification (Aadhaar or Passport number, front/back document images, a selfie photo) &mdash; required before your first payout</li>
  <li>Username and public profile information you choose to share (display name, bio, profile photo)</li>
</ul>
<h3>Financial Information</h3>
<ul>
  <li>Bank account number, IFSC code, account holder name, and UPI ID &mdash; collected only when you set up payouts</li>
  <li>PAN card details, if your annual earnings cross the threshold requiring it under Indian tax law</li>
  <li>Transaction and payout history within the app</li>
</ul>
<h3>Content You Create</h3>
<ul>
  <li>Chat messages (end-to-end encrypted), voice messages, and shared media</li>
  <li>Social posts, reels, stories, and comments-equivalent interactions (likes, saves, shares)</li>
  <li>Call metadata (who you called, when, duration) for calls made through the app</li>
</ul>
<h3>Device &amp; Usage Information</h3>
<ul>
  <li>Device contacts (used only to show you which contacts already use ThanQYou for the Chat feature &mdash; never used for Social)</li>
  <li>Camera and microphone access, used only when you actively record a photo/video/voice message or make a call</li>
  <li>Approximate location (used for country-based earning-rate calculation and fraud prevention)</li>
  <li>Device identifiers, app usage patterns, and crash/performance diagnostics</li>
</ul>

<h2>2. How We Use Your Information</h2>
<ul>
  <li>To create and secure your account, and verify your identity for payouts</li>
  <li>To calculate your share of ad revenue under our revenue-share model (see Terms of Service)</li>
  <li>To process payouts via our payment partner, Cashfree</li>
  <li>To deliver notifications, calls, and messages</li>
  <li>To detect fraud, enforce our Community Guidelines, and maintain platform safety</li>
  <li>To improve the app and fix issues</li>
</ul>

<div class="highlight">
  <p><strong>We do not sell your personal data.</strong> We share data only with the service providers below, strictly to operate the app, and never for their own independent marketing purposes.</p>
</div>

<h2>3. Third-Party Services We Use</h2>
<table>
  <tr><th>Service</th><th>Purpose</th></tr>
  <tr><td>Firebase (Google)</td><td>Authentication (phone OTP), push notifications</td></tr>
  <tr><td>Supabase</td><td>Database, file storage, backend logic</td></tr>
  <tr><td>Cashfree</td><td>Payment processing and payouts</td></tr>
  <tr><td>Agora</td><td>Voice and video call infrastructure</td></tr>
  <tr><td>Google AdMob</td><td>Advertising that funds the revenue-share pool</td></tr>
</table>

<h2>4. Chat Encryption</h2>
<p>Direct messages in the Chat tab are end-to-end encrypted. We cannot read the content of your private messages. We may act on user reports of messages that violate our Community Guidelines, based on what the reporting user shares with us.</p>

<h2>5. Data Retention</h2>
<p>We retain your account data for as long as your account is active. KYC documents are retained as required for compliance and fraud-prevention purposes even after account deletion, for the minimum period required by applicable law. Chat messages and social content are deleted when you delete them, or when you delete your account (see our <a class="inline" href="/delete-account.html">Account Deletion</a> page).</p>

<h2>6. Your Rights</h2>
<ul>
  <li>Access and review the personal data we hold about you</li>
  <li>Correct inaccurate information via your profile settings</li>
  <li>Request deletion of your account and associated data</li>
  <li>Opt out of non-essential notifications</li>
</ul>

<h2>7. Children's Privacy</h2>
<p>ThanQYou requires users to be at least 15 years old. We do not knowingly collect data from children under this age. If you believe a minor has created an account in violation of this policy, contact us using the details below.</p>

<h2>8. Security</h2>
<p>We use industry-standard security practices including encrypted connections, access-controlled databases, and server-side verification for all financial operations. No system is completely secure, and we encourage you to use a strong, unique password-equivalent security practice on your device.</p>

<h2>9. Changes to This Policy</h2>
<p>We may update this policy from time to time. Material changes will be communicated in-app before they take effect.</p>

<h2>10. Contact Us</h2>
<p>For privacy questions or data requests: <a class="inline" href="mailto:contact@thanqyou.com">contact@thanqyou.com</a></p>
<div class="card">
  <p><strong>MAANYA IT &amp; HR SERVICES</strong> (Partnership firm)<br>
  Ground Floor, Plot No 235, Road No 93, Near Yaari House, Kapra, Hyderabad, Medchal Malkajgiri District, Telangana 500083, India<br>
  GSTIN: 36ACFFM5558A1ZB</p>
</div>
'''


TERMS_BODY = '''<h1>Terms &amp; Conditions</h1>
<p class="updated">Last updated: September 2026</p>
<p>These Terms are an agreement between you and <strong>MAANYA IT &amp; HR SERVICES</strong>, a partnership firm registered in India with its principal place of business at Ground Floor, Plot No 235, Road No 93, Near Yaari House, Kapra, Hyderabad, Medchal Malkajgiri District, Telangana 500083, India ("ThanQYou", "we", "us"), which owns and operates the ThanQYou app. By creating a ThanQYou account, you agree to these Terms. If you do not agree, please do not use the app.</p>

<h2>1. Eligibility</h2>
<p>You must be at least 15 years old to register. By registering, you confirm the information you provide is accurate and matches your government-issued ID (Aadhaar/Passport).</p>

<h2>2. Account &amp; Identity</h2>
<p>Your legal name must match your Aadhaar Card or Passport exactly for KYC verification purposes, required before your first payout. Providing false information will result in account suspension and forfeiture of pending earnings.</p>

<h2>3. How Earnings Work</h2>
<p>ThanQYou operates on an <strong>ad-revenue-sharing model</strong>. Every rupee paid out is a percentage of actual advertising revenue generated by the platform &mdash; never a fixed, guaranteed rate.</p>
<h3>Revenue Split</h3>
<ul>
  <li><strong>Platform: 30%</strong></li>
  <li><strong>Creator pool: 50%</strong> &mdash; distributed among content creators based on their reels posted, views, likes, watch-hours generated, follower growth, and viewer engagement</li>
  <li><strong>Viewer pool: 20%</strong> &mdash; distributed among viewers based on time spent, likes given, qualifying views, ads seen, and qualified referrals</li>
</ul>
<h3>Payout Schedule</h3>
<ul>
  <li>Earnings are calculated daily as an estimate, and finalized at the end of each calendar month</li>
  <li>Actual payment is released around the 3rd of the following month via Cashfree</li>
  <li>Minimum withdrawal: &#8377;500. Below this, earnings roll over to the next month</li>
  <li>Payouts require KYC verification. Unverified users' earnings accrue and roll over until verification is complete &mdash; nothing is forfeited</li>
</ul>
<h3>Referrals</h3>
<p>A referral only counts toward your earnings once the referred user has stayed active, completed KYC, and reached qualifying activity thresholds. There is no flat bonus simply for creating an account or referring someone who does not meet these conditions.</p>
<p>If your annual earnings exceed &#8377;50,000, providing a PAN card is mandatory under Indian tax law.</p>

<h2>4. Community Guidelines</h2>
<p>All content and behavior on ThanQYou must comply with our <a class="inline" href="/community-guidelines.html">Community Guidelines</a>. Violations can result in content removal, warnings, account suspension, or forfeiture of earnings tied to the violation.</p>

<h2>5. Privacy &amp; Data</h2>
<p>Your personal information is handled as described in our <a class="inline" href="/privacy-policy.html">Privacy Policy</a>. We do not sell your data to third parties.</p>

<h2>6. Chat &amp; Messaging</h2>
<p>Direct messages are end-to-end encrypted. ThanQYou cannot read your private messages, but we reserve the right to act on reported messages that violate our Community Guidelines.</p>

<h2>7. No Randomized Rewards</h2>
<p>ThanQYou does not use randomized or variable-ratio reward mechanics (e.g., loot-box-style random payouts). All earning calculations are transparent and formula-based.</p>

<h2>8. Termination</h2>
<p>ThanQYou may suspend or terminate accounts that violate these Terms. You may delete your account at any time &mdash; see our <a class="inline" href="/delete-account.html">Account Deletion</a> page for details.</p>

<h2>9. Changes to These Terms</h2>
<p>We may update these Terms at any time. Continued use of the app after an update constitutes acceptance of the new Terms.</p>

<h2>10. Contact Us</h2>
<p>For questions: <a class="inline" href="mailto:support@thanqyou.com">support@thanqyou.com</a></p>
<div class="card">
  <p><strong>MAANYA IT &amp; HR SERVICES</strong> (Partnership firm)<br>
  Ground Floor, Plot No 235, Road No 93, Near Yaari House, Kapra, Hyderabad, Medchal Malkajgiri District, Telangana 500083, India<br>
  GSTIN: 36ACFFM5558A1ZB</p>
</div>
'''


DELETE_ACCOUNT_BODY = '''<h1>Delete Your Account</h1>
<p class="updated">Last updated: September 2026</p>
<p>You can permanently delete your ThanQYou account and associated data at any time. This page explains how, and what happens to your information.</p>

<h2>How to Delete Your Account</h2>
<div class="card">
  <p><strong>From within the app:</strong></p>
  <ol>
    <li>Open ThanQYou and go to <strong>Profile</strong></li>
    <li>Tap <strong>Settings</strong></li>
    <li>Tap <strong>Account Settings</strong></li>
    <li>Tap <strong>Delete Account</strong> and confirm</li>
  </ol>
</div>
<div class="card">
  <p><strong>Without the app installed:</strong></p>
  <p>Email <a class="inline" href="mailto:support@thanqyou.com">support@thanqyou.com</a> from the email address linked to your account, with the subject line "Account Deletion Request", including your registered phone number. We will process your request within 7 business days and confirm by email once complete.</p>
</div>

<h2>What Gets Deleted</h2>
<ul>
  <li>Your profile information (name, username, bio, photos)</li>
  <li>Your chat messages and conversation history</li>
  <li>Your social posts, reels, and stories</li>
  <li>Your device contact-matching data</li>
</ul>

<h2>What We Retain, and Why</h2>
<ul>
  <li><strong>KYC documents and identity verification records</strong> &mdash; retained for the minimum period required by financial and anti-fraud regulations, even after account deletion</li>
  <li><strong>Transaction and payout history</strong> &mdash; retained as required for tax and financial compliance purposes</li>
  <li><strong>Any pending earnings below the withdrawal threshold</strong> &mdash; if you have an unpaid balance at the time of deletion, contact support before deleting to arrange final payout, as deletion forfeits any remaining unclaimed balance</li>
</ul>

<h2>How Long Deletion Takes</h2>
<p>In-app deletion requests are processed immediately for visible content (your profile, posts, and messages disappear right away). Backend removal of associated data completes within 30 days, except for the compliance-required records noted above.</p>

<h2>Questions?</h2>
<p>Contact us at <a class="inline" href="mailto:support@thanqyou.com">support@thanqyou.com</a> for anything related to account deletion or your data.</p>
'''


def main():
    if len(sys.argv) < 2:
        fail("Usage: python build_legal_pages.py <path-to-website-repo-root>")
    root = Path(sys.argv[1])
    if not root.exists():
        fail(f"{root} not found.")

    pages = {
        "privacy-policy.html": page("Privacy Policy", PRIVACY_BODY),
        "terms-of-service.html": page("Terms of Service", TERMS_BODY),
        "delete-account.html": page("Delete Your Account", DELETE_ACCOUNT_BODY),
    }

    for filename, content in pages.items():
        path = root / filename
        path.write_text(content, encoding="utf-8", newline="\r\n")
        print(f"Created: {path}")

    # Add footer links to the homepage too, next to Community Guidelines.
    index_path = root / "index.html"
    if index_path.exists():
        text = index_path.read_text(encoding="utf-8")
        if "privacy-policy.html" not in text:
            old_footer = (
                '    <p class="fcopy">\u00a9 2026 ThanQYou. All rights reserved.</p>\n'
                '    <a href="/community-guidelines.html">Community Guidelines</a>\n'
                '    <a href="/admin/">Admin</a>'
            )
            if old_footer in text:
                new_footer = (
                    '    <p class="fcopy">\u00a9 2026 ThanQYou. All rights reserved.</p>\n'
                    '    <a href="/privacy-policy.html">Privacy Policy</a>\n'
                    '    <a href="/terms-of-service.html">Terms of Service</a>\n'
                    '    <a href="/community-guidelines.html">Community Guidelines</a>\n'
                    '    <a href="/delete-account.html">Delete Account</a>\n'
                    '    <a href="/admin/">Admin</a>'
                )
                text = text.replace(old_footer, new_footer, 1)
                index_path.write_text(text, encoding="utf-8", newline="\r\n")
                print(f"Patched: {index_path} (footer links added)")
            else:
                print("NOTE: could not find the expected footer anchor in index.html -- add links manually.")
        else:
            print("SKIP: index.html footer already has these links.")


if __name__ == "__main__":
    main()
