import matplotlib.pyplot as plt
import pandas as pd

# Data
categories = ['Diagnosed', 'Undiagnosed (estimated)']
uk_cases = [190000, 1310000]

delay_years = ['Under 2 years', '2-4 years', '4-8 years', 'Over 8 years']
diagnosis_delay = [15, 20, 30, 35]

fertility_labels = ['Infertile due to endometriosis', 'Not affected']
fertility_data = [40, 60]

# Outcome comparison - early vs late diagnosis
outcomes = ['Infertility risk', 'Chronic pain', 'Surgery needed', 'Mental health impact']
early_diagnosis = [20, 30, 25, 35]
late_diagnosis = [60, 80, 70, 75]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Endometriosis & Infertility: Why Early Diagnosis Matters', 
             fontsize=14, fontweight='bold', y=1.02)

# Plot 1 - Diagnosed vs Undiagnosed
ax1.bar(categories, uk_cases, color=['#E8A0BF', '#C62A88'])
ax1.set_title('Endometriosis in the UK\nDiagnosed vs Undiagnosed')
ax1.set_ylabel('Number of people')
ax1.set_ylim(0, 1500000)

# Plot 2 - Diagnosis delay
ax2.bar(delay_years, diagnosis_delay, color='#C62A88')
ax2.set_title('Time to Diagnosis\n% of patients')
ax2.set_ylabel('Percentage of patients (%)')
ax2.set_xlabel('Years to diagnosis')

# Plot 3 - Infertility pie
ax3.pie(fertility_data, labels=fertility_labels, colors=['#C62A88', '#E8A0BF'],
        autopct='%1.1f%%', startangle=90)
ax3.set_title('Endometriosis Patients\nExperiencing Infertility')

# Plot 4 - Early vs late diagnosis outcomes
import matplotlib.pyplot as plt
import pandas as pd

# Data
categories = ['Diagnosed', 'Undiagnosed (estimated)']
uk_cases = [190000, 1310000]

delay_years = ['Under 2 years', '2-4 years', '4-8 years', 'Over 8 years']
diagnosis_delay = [15, 20, 30, 35]

fertility_labels = ['Infertile due to endometriosis', 'Not affected']
fertility_data = [40, 60]

# Outcome comparison - early vs late diagnosis
outcomes = ['Infertility risk', 'Chronic pain', 'Surgery needed', 'Mental health impact']
early_diagnosis = [20, 30, 25, 35]
late_diagnosis = [60, 80, 70, 75]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Endometriosis & Infertility: Why Early Diagnosis Matters', 
             fontsize=14, fontweight='bold', y=1.02)

# Plot 1 - Diagnosed vs Undiagnosed
ax1.bar(categories, uk_cases, color=['#E8A0BF', '#C62A88'])
ax1.set_title('Endometriosis in the UK\nDiagnosed vs Undiagnosed')
ax1.set_ylabel('Number of people')
ax1.set_ylim(0, 1500000)

# Plot 2 - Diagnosis delay
ax2.bar(delay_years, diagnosis_delay, color='#C62A88')
ax2.set_title('Time to Diagnosis\n% of patients')
ax2.set_ylabel('Percentage of patients (%)')
ax2.set_xlabel('Years to diagnosis')

# Plot 3 - Infertility pie
ax3.pie(fertility_data, labels=fertility_labels, colors=['#C62A88', '#E8A0BF'],
        autopct='%1.1f%%', startangle=90)
ax3.set_title('Endometriosis Patients\nExperiencing Infertility')

# Plot 4 - Early vs late diagnosis outcomes
x = range(len(outcomes))
width = 0.35
ax4.bar([i - width/2 for i in x], early_diagnosis, width, 
        label='Early diagnosis', color='#E8A0BF')
ax4.bar([i + width/2 for i in x], late_diagnosis, width, 
        label='Late diagnosis', color='#C62A88')
ax4.set_title('Impact of Early vs Late Diagnosis\non Patient Outcomes')
ax4.set_ylabel('% of patients affected')
ax4.set_xticks(x)
ax4.set_xticklabels(outcomes, wrap=True)
ax4.legend()

plt.tight_layout()
plt.savefig('endometriosis_data.png', bbox_inches='tight')
print("Chart saved!")
