print("Testing scoring system...")

# Simple age score test
def test_age_score():
    ages = ["22", "35", "60"]
    for age in ages:
        try:
            age_int = int(age)
            if 18 <= age_int <= 25:
                score = 25
            elif 26 <= age_int <= 35:
                score = 20
            elif 36 <= age_int <= 45:
                score = 15
            elif 46 <= age_int <= 55:
                score = 10
            else:
                score = 5
            print(f"Age {age}: {score}/25 points")
        except:
            print(f"Age {age}: 0/25 points (invalid)")

print("Age Scoring Test:")
test_age_score()
print("\nScoring system test completed!")
