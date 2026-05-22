import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

disorders = ['Insomnia', 'Sleep Apnoea', 'Restless Leg Syndrome', 'Narcolepsy']
prevalence = [36, 10, 10, 0.03]

health_outcomes = ['Obesity', 'Type 2 Diabetes', 'Heart Disease', 'Stroke', 'Depression']
risk_increase = [55, 83, 48, 15, 65]

conditions = ['Depression', 'Anxiety', 'PTSD', 'Bipolar Disorder', 'Schizophrenia']
poor_sleep_percentage = [75, 70, 90, 65, 80]

age_groups = ['School age', 'Teens', 'Adults', 'Elderly']
recommended = [10, 9, 8, 7.5]
actual = [8.5, 6.5, 6.8, 6.5]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Sleep Science: Prevalence, Health Impact & Mental Health', fontsize=14, fontweight='bold')

ax1.bar(disorders, prevalence, color=['#4A90D9', '#2C5F8A', '#7BB3E0', '#1A3A5C'])
ax1.set_title('Sleep Disorder Prevalence in the UK')
ax1.set_ylabel('Percentage of population (%)')

ax2.barh(health_outcomes, risk_increase, color='#2C5F8A')
ax2.set_title('Increased Health Risk from Sleep Deprivation')
ax2.set_xlabel('Increased risk (%)')

ax3.bar(conditions, poor_sleep_percentage, color='#4A90D9')
ax3.set_title('Poor Sleep in Mental Health Conditions')
ax3.set_ylabel('Percentage of patients (%)')
ax3.set_ylim(0, 100)

x = range(len(age_groups))
width = 0.35
ax4.bar([i - width/2 for i in x], recommended, width, label='Recommended hours', color='#4A90D9')
ax4.bar([i + width/2 for i in x], actual, width, label='Actual hours', color='#2C5F8A')
ax4.set_title('Recommended vs Actual Sleep by Age Group')
ax4.set_ylabel('Hours of sleep')
ax4.set_xticks(x)
ax4.set_xticklabels(age_groups)
ax4.legend()

plt.tight_layout()
plt.savefig('sleep_science.png', bbox_inches='tight')
print("Chart saved!")
