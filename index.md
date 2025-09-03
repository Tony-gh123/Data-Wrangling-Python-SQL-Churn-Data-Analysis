# Behind the Membership Door: Behavioral Insights for Retention & Growth

This project investigates member behaviors leading to membership cancellation within a gym's median membership tenure and provides actionable strategies to retain members, reduce churn, and increase business profitability. I partnered with a gym manager to uncover churn patterns and design targeted interventions.

[View Github Repository](https://github.com/Tony-gh123/Churn-Data-Analysis) <br>
[Return to Portfolio](https://tony-gh123.github.io/yeral.github.io/)

SKILLS: Python (Numpy, Pandas), SQL, SQLite, Matplotlib, Seaborn, Storytelling, Time Series Analysis, Business Intelligence, Behavioral Analytics. 

**Table of Contents**
- [Executive Summary](#executive-summary)
- [Background](#background)
- [Database Schema](#database-schema)
- [Insights Deep Dive](#insights-deep-dive)
    - Demographics & Sales Seasonality
    - Overall Retention & Churn Analysis
    - Churn by Membership Type
    - Check-In Behavior & Usage Patterns
    - Class Attendance & Personal Training Impact
    - Purchase Behavior & Engagement Signals
    - Payment Timeliness & Retention
    - Cancellation Reasons & External Factors
    - Agreement Type × Check-in Bucket
- [Key Recommendations](#key-recommendations)
    - Maximize Agreement Opportunities for Local Members
    - Recognize Check-In Patterns to Re-Engage Members
    - Engage Members During Peak Hours
    - Address Late Payments Proactively
- [Assumptions](#assumptions)
- [Appendices](#appendices)


## Executive Summary

IKIGAI GYM loses 56.3% of its members by the 105-day mark, leading to significant revenue declines before the critical January and summer sales spikes. Our data reveals that membership type, engagement patterns, and payment behaviors are key drivers of retention and churn. By focusing on annual memberships, boosting engagement through classes and personal training, and proactively addressing early warning signals like low check-ins rates and late payments, the gym can extend member lifecycles and stabilize revenue across sales cycles. Key insights include:

- **Annual contracts significantly outperform month-to-month (105-day retention)**: Annual members churn at 11.6–13.6% within 105 days, compared to 18–25.8% for month-to-month members. Promoting annual plans to stable, local members can reduce early cancellations.

- **Member engagement extends 105-day tenure**: Members with 4+ monthly check-ins churn at 15.3% (vs. 43% for <4 check-ins), and those attending classes or personal training sessions show 17.3% and 12% churn rates, respectively (vs. 21.3% for non-participants). Combining both drops churn to 11%. Encouraging engagement through classes, personal training, and purchases (28.3% churn for buyers vs. 16.9% for non-buyers) strengthens loyalty.

- **Early warning signals can be acted on**: Members with 30+ days of inactivity face a 43.9% cancellation risk, and those with over half their payments late churn at 97.5% within 105 days. Automated flagging, personalized re-engagement, and proactive payment interventions can recover at-risk members.

These findings highlight key drivers of retention and churn. They suggest that focusing on membership type, engagement activities, and timely re-engagement efforts has the potential to meaningfully increase monthly retention and reduce churn across sales cycles.

## Background

The fitness club **IKIGAI GYM** operates in a competitive urban market where seasonal spikes and transient population make retention critical for profitability. The club is overseen by a small corporate division responsible for staff, compliance, and financial performance.

Currently, retention is monitored only through basic churn reports, with limited visibility into member lifecycles or behavior leading up to cancellation. Experiencing only seasonal sales peaks (January, June, August) further challenge long-term growth. The corporate team is particularly interested in extending the average membership lifecycle during slower months to stabilize revenue.

### Database Schema

As a data analyst I was able to retreive the following csv files from the the manager.

<img src="Images/DBSchema.png" alt="DBSchema" width="900"/>

_**Disclaimer**: Synthethic IKIGAI-GYM DB_

# Insights Deep Dive 

## Member Demographics

From August 2023 to August 2025, the gym sold 1,000 memberships. Of these, 682 remain active and 318 have canceled. The member base is 59.8% male and 40.2% female, with an average age of 35 ± 9.4 years.

<img src="Images/age_gender.png" alt="Age Gender" width="475"/>

## Sales Seasonality

We observe an initial sale peak at the beginning of the year, following by slower months towards June, picks up during the summer with seasonal peaks (June & August) and decreases during winter.

<img src="Images/sale_seasonality.png" alt="Age Gender" width="475"/>

## Overall Churn Analysis

While quarterly churn can naturally increase (gym capacity) as we sign-up more members, we can observe patterns accross a member's lifetime for the current population regardless of when they started. This will allow us to observe what the realistic patterns of behaviors are for member across their tenure. We first measured the overall retention rate (of canceled members) by measuring their total tenure from the start to the termination of their membership. This allow us to see what the current churn trends are leading to the 104-day mark.

- **First-month**: By day 30, over 1 in 5 members (21.1%) have already churned, leaving just under 79% retained.

- **Second-Month**: By day 60, retention falls to 65%, meaning more than a 1 out of 3 of members (34.9%) have canceled.

- **Third-Month**: By day 90, retention drops below 56%, with nearly half of members (44.3%) canceled.

- **Fourth-Month**: By day 120, retention falls below 44%, and 56.3% of members have churned.

The median tenure = 105 days, showing half of all new members cancel within 3.5 months.
<br>

<img src="Images/retention_churn_rates.png" alt="Retention Churn Rate" width="475"/>

## Churn Analysis by Membership Type

Now that we have an understanding of what churn trends are, we can further divide each member based on the type of membership they had. This allow us to see which membership performs better at retaining members within our goal.

- **Annual memberships are most stable**: Standard Annual members show the lowest churn rate at 15.5%, followed closely by Passport Annual at 18.2% (11.56% and 13.64% respectively for cancelations within the 105-day window).

- **Month-to-month memberships are riskier**: Standard M2M members churn at 36.4%, while Passport M2M members are the most likely to leave, with churn over 41.9% (18% and 25.83% respectively within the 105-day window).

Across both Standard and Passport plans, annual commitments consistently outperform month-to-month contracts in reducing churn.
<br>

<img src='Images/retention_by_agreement.png' alt='retention_by_agreement' width='500'/>
<img src='Images/churn_rate_by_agreement_type.png' alt='churn_rate_by_agreement_type' width='426'/>

## Check-In History

The gym’s peak hours are between 7–10 AM and 4–6 PM, aligning with typical pre-work and post-work schedules. Understanding check-in behavior during these windows not only helps with staffing and resource allocation, but also provides valuable insight into member commitment and churn risk.

Check-ins are the most fundamental form of engagement — if members are not using the facilities, the likelihood of cancellation by the 105 day rises sharply. When analyzed across all members, several clear patterns emerge: 

- **Usage frequency drives retention**: Members who check in fewer than 4 times per month churn at a  high rate (43.01%), while those with more than 4 monthly visits churn just < 15.3%.

- **The “middle ground” is safer**: Members who check in between 4–12 times per month have a moderate churn rate of ~15.04%, aligning closely with the gym’s overall average of 8–9 visits.

- **Active vs. churned behavior**: Current active members average 9 check-ins per month, compared to just 7 for members who cancel by the 105 day window.

- **Complete inactivity predicts cancellation**: Members who go 30+ days without a check-in have a 43.94% likelihood of canceling, versus only 5.55% for those who stay consistently active.
<br>

<img src='Images/checkin_activity.png' alt='check_in_activity' width='450'/>
<img src='Images/check_in_inactivity.png' alt='check_in_activity' width='482'/>

## Class Attendance & Personal Training Retention Impact

Classes and Personal Training sessions follow the same peak-hour patterns observed in overall check-ins (7–10 AM and 4–6 PM). These engagement activities not only increase facility use but also create social accountability, structure, and personalized progress tracking, all of which directly reduce churn by the 105-day period.

- **Classes boost retention**: Members who attended at least one class churn at a lower rate (17.32%) compared to those who never attended (21.26%).

- **Personal training strengthens commitment**: Members who completed at least one PT session have a churn rate of just 12.0%, compared to 19.1% for those who never participate.

- **The combo effect is strongest**: When members attend both classes and PT, churn drops even further — just 11%, compared to nearly 21% for members who do neither. Even modest exposure to both activities compounds the retention benefit.

Group activities like SPIN appear to be particularly effective in keeping members engaged. As for Personal Training, even minimal exposure to PT yields a meaningful improvement in member retention. Promoting class participation and PT sessions can significantly reduce early cancellations.
<br>

<img src='Images/class_churn.png' alt='class_churn' width='450'/>
<img src='Images/pt_churn.png' alt='pt_churn' height='382'/>
<img src='Images/class_pt_churn.png' alt='pt_churn' width='505'/>

## Purchase Behavior
Encouraging purchases — from small items like water bottles to add-ons like gear or snacks — can serve as a retention strategy by reinforcing members’ sense of belonging.

- **Purchases signal commitment**: Members who make at least one purchase have a churn rate of 28.26%, compared to 16.92% for those who never purchase.

This means that engaged spenders are 11.34% less likely to cancel, showing that even small transactions reflect deeper attachment to the gym.
<br>

<img src='Images/purchase_churn.png' alt='purchase_churn' width='450'/>

## Late Payments & Retention

Payment timeliness is one of the strongest early signals of member commitment versus dropout risk. Proactively addressing late payments (e.g., reminders, payment plans, or in-person collection at check-ins) could help recover at-risk members before cancellation. More importantly, collecting payments is crutial for members considered overall late in their payment behavior. 

- **Late payments are a red flag**: Members with a history of paying more than half their bills late have a churn rate of 97.5% within the first 105 days of their membership.

- **On-time payers are far more stable**: Only 12.6% of consistently on-time members cancel within the same period.

Note: Late payment behavior is considered to half of their payments made late. 
<br>

<img src='Images/payment_churn.png' alt='payment_churn' width='450'/>

## Cancellation Reasons & External Factors

While our data indicates strong predictors of cancellations, our data also shows canceled members (e.g female, 40, Standard M2M, 196 check-ins, canceled due to relocation) with strong engagement patterns. This suggests high engagement doesn’t always prevent churn and are due to external factors like relocation.

Below is the most common reasons for cancellations according to the voluntary exit survey.
<br>

<img src='Images/cancel_reasons.png' alt='cancel_reasons' width='500'/>

## Agreement Type × Check-in Bucket

- **Usage drives loyalty**: Low monthly check-in users churn heavily (38–71%), while high monthly check-in users are extremely stable (3-9%).

- **Commitment matters**: Annual members churn far less than M2M in the stable (medium) monthly check-in bucket (Annual: 10%-11% vs. M2M: 19%-29%).

The heatmap shows how contract type (Annual vs. M2M) interacts with gym usage frequency (Low, Medium, High check-ins). This captures the structural backbone of retention.

<img src='Images/agreement_checkin_heatmap.png' alt='agreement_checkin_heatmap' width='500'/>

# Key Recommendations

### **Maximize Agreement Opportunities for Local Members**
Annual memberships consistently show lower churn than M2M. Encouraging longer commitments among members who are likely to remain in the area is one of the most impactful levers.

- Recommendation: Train sales staff to identify members with longer-term residency (e.g., professionals, families, or students with multi-year programs) and emphasize the stability and savings of annual memberships.

### **Maintain a Variety of Items in the Shop**
Members who make purchases show a 11% higher retention rate than non-purchasers. By promoting small, frequent purchases, the gym can strengthen member commitment and reduce churn.

- Recommendation: Stock a diverse range of affordable and appealing items (e.g., water bottles, apparel, gear, snacks) to encourage impulse purchases and reinforce a sense of belonging.

### **Recognize Check-In Patterns to Re-Engage Members**
Check-in frequency is a strong predictor of churn. Members who go 30+ days without visiting have a 43.94% chance of cancellation.

- Recommendation: Automatically flag members who return after 30+ days and reward them with small incentives (e.g., a free water bottle, apparel, or shop item). This creates a positive “welcome back” moment that can reignite engagement.

- Recommendation: Identify members with fewer than 9 check-ins per month (the active-member average) and reach out with personalized nudges — such as asking about schedule challenges, offering off-peak class suggestions, or extending a PT consultation.

### **Engage Members During Peak Hours**
Peak hours (7–10 AM and 4–6 PM) see the highest member activity, making them the best opportunity for direct engagement and upselling.

- Recommendation: Host free, on-the-spot fitness consultations or “mini drop-in” classes during peak hours to capture casual members who might not otherwise try structured activities.

- Recommendation: Position staff strategically during these hours to interact with members, answer questions, and build rapport.

### **Address Late Payments Proactively**
Late payments are one of the strongest churn signals: members with more than half of their payments late have a 97.5% churn rate within 105 days.

- Recommendation: Once a member has made half their payments late, escalate them to a “high-risk” category. Prioritize payment recovery and intervention (e.g., reminders, flexible payment plans, or in-person collection during check-ins).

- Recommendation: Consider introducing small incentives for on-time payments, such as loyalty points redeemable as once a year free PT session.


## Assumptions

1. Each member_id acts as a unique identifier across all tables and functions as a foreign key for joining datasets (e.g., demographics, agreements, check-ins, purchases, payments).

2. It is assumed there are no restrictions on cancellations during the first month. Members are free to exit at any time without contractual penalties. This assumption explains the high early churn rates observed by day 30 and makes “first-month engagement” a critical driver of retention strategy.

3. The analysis considers only four forms of membership: Standard Annual, Passport Annual, Standard Month-to-Month (M2M), and Passport M2M No hybrid or promotional contracts (e.g., trial passes, corporate packages, or family bundles) are included in the dataset. This simplifies comparison but may understate real-world variability.

4. Payment timeliness is measured strictly as on-time vs. late, with no partial credit or grace period adjustments.

_Disclaimer: The insights in this report are based on synthetic data created for educational and demonstration purposes. They do not reflect real-world behaviors or outcomes and should not be taken as professional advice._

## Appendices

[View Github Repository](https://github.com/Tony-gh123/Churn-Data-Analysis) <br>
[Return to Portfolio](https://tony-gh123.github.io/yeral.github.io/)