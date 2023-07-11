from jinja2 import Environment, FileSystemLoader
import requests

# initialize the environment
environment = Environment(loader=FileSystemLoader("templates/"))
v6_template = environment.get_template("ipv6.j2")
v4_template = environment.get_template("ipv4.j2")


# bogon list sources
v6_source_url = "https://team-cymru.org/Services/Bogons/fullbogons-ipv6.txt"
v4_source_url = "https://team-cymru.org/Services/Bogons/fullbogons-ipv4.txt"


# download the bogon lists to memory
r6 = requests.get(v6_source_url, stream=True)
ipv6_bogons = {"ipv6_bogons": r6.text.splitlines()[2:]}

r4 = requests.get(v4_source_url, stream=True)
ipv4_bogons = {"ipv4_bogons": r4.text.splitlines()[2:]}


# generate the content using the corresponding jinja templates
v6_content = v6_template.render(ipv6_bogons).lstrip("\n")
v6_filename = "ipv6_bogons.txt"

v4_content = v4_template.render(ipv4_bogons).lstrip("\n")
v4_filename = "ipv4_bogons.txt"


# write the output files using the jinja templates
with open(v6_filename, mode="w", encoding="utf-8") as file:
    file.write(v6_content)
    print(f"wrote {v6_filename}")

with open(v4_filename, mode="w", encoding="utf-8") as file:
    file.write(v4_content)
    print(f"wrote {v4_filename}")
