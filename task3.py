def check_password_strength(password):
  """Evaluates password strength based on various criteria.

  Args:
      password: The password string to be evaluated.

  Returns:
      A tuple containing the password score (int) and a feedback message (str).
  """
  score = 0
  feedback = ""

  # Check password length
  if len(password) >= 12:
    score += 2
    feedback += "Length is good! "
  elif len(password) >= 8:
    score += 1
    feedback += "Consider making it longer for better security. "
  else:
    feedback += "Password is too short. Use at least 8 characters. "

  # Check for uppercase letters
  if any(char.isupper() for char in password):
    score += 1
    feedback += "Has uppercase letters. "
  else:
    feedback += "Include uppercase letters for increased security. "

  # Check for lowercase letters
  if any(char.islower() for char in password):
    score += 1
    feedback += "Has lowercase letters. "
  else:
    feedback += "Include lowercase letters for increased security. "

  # Check for numbers
  if any(char.isdigit() for char in password):
    score += 1
    feedback += "Has numbers. "
  else:
    feedback += "Include numbers for increased security. "

  # Check for special characters
  if any(char in "!@#$%^&*()" for char in password):
    score += 1
    feedback += "Has special characters. "
  else:
    feedback += "Include special characters for increased security. "

  # Strength rating based on score
  if score >= 5:
    feedback += "This is a strong password!"
  elif score >= 3:
    feedback += "This password is moderately strong."
  else:
    feedback += "This password is weak. Consider improvements suggested."

  return score, feedback

# Example usage
password = input("Enter your password: ")
score, feedback = check_password_strength(password)

print(f"Password Score: {score} out of 5")
print(feedback)
