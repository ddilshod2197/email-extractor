import re

def top_email_manzillar(matn):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_manzillar = re.findall(email_pattern, matn)
    return email_manzillar

matn = "Mening email manzilim: example@gmail.com. Menning do'stimning email manzili: example2@yahoo.com. Sizning email manzilingiz: example3@hotmail.com."
print(top_email_manzillar(matn))
```

```python
import re

def top_email_manzillar(matn):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_manzillar = re.findall(email_pattern, matn)
    return email_manzillar

matn = "Mening email manzilim: example@gmail.com. Menning do'stimning email manzili: example2@yahoo.com. Sizning email manzilingiz: example3@hotmail.com."
print(top_email_manzillar(matn))
