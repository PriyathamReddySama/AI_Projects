import requests
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Load package.json from GitHub
url = "https://raw.githubusercontent.com/storybookjs/storybook/next/code/package.json"
package_json = requests.get(url).text

# Claude model
llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    temperature=0
)

# Prompt template
prompt = ChatPromptTemplate.from_template("""
You are a cybersecurity vulnerability analyst.

Analyze the dependencies from this package.json and identify:

1. Vulnerable packages
2. Possible CVEs
3. Security risks
4. Recommended updates

package.json:
{data}
""")

chain = prompt | llm

result = chain.invoke({
    "data": package_json
})

print(result.content)