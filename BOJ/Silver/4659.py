while True:
  pw = input()
  if pw == 'end' :
    break
  # 모음
  vowels = {'a','e','i','o','u'}
  answer = True
  # 조건 
  # 1. 모음 하나를 반드시 포함
  # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안됨
  # 3. 같은 글자가 연속 두번 X , ee와 oo는 허용 

  # 교집합이 있으면 true 즉 모음이 하나라도 있으면 true
  if not any(v in pw for v in vowels):
    answer = False

  count = 1
  is_vowel = pw[0] in vowels

  for i in range(1, len(pw)):
    if(pw[i] in vowels) == is_vowel:
      count += 1
    else: 
      count = 1
      is_vowel = not is_vowel
    
    if count >= 3:
      answer = False
      break
  
  for i in range(1, len(pw)):
    if pw[i] == pw[i-1] and pw[i] not in {'e', 'o'}:
      answer = False
      break
    
  print(f'<{pw}> is {"acceptable" if answer else "not acceptable"}.')