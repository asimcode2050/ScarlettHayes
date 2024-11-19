
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 55000, 60000, 65000]}
df = pd.DataFrame(data)
styler = df.style
styler = styler.applymap(lambda x: 'color: red' if isinstance(
    x, int) and x > 30 else 'color: green')
html_output = styler.to_html()
print(html_output)
