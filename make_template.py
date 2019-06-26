import os

FILE_LOCATION = 'Desktop'

def make_template():
	ticket_number = input("What is the Jira Ticket Number: \n")
	os.system(f"open -a safari https://earthwavetech.atlassian.net/browse/FS-{ticket_number}")
	ticket_desc = input("Ticket Description?: \n")
	git_branch_name = input("What is the Branch Name?: \n")
	if git_branch_name == "":
		git_branch_name = f"fs_{ticket_number}"
	jira_link = f"[FS-{ticket_number}](https://earthwavetech.atlassian.net/browse/FS-{ticket_number})"
	path = f"{FILE_LOCATION}/{f'FS-{ticket_number}'}"
	print(path)
	with open(path,'a') as thefile:
		thefile.write("###-Auto-Generated-Merge-Template-###")
		thefile.write("\n")
		thefile.write("\n")
		thefile.write(f"FS-[{ticket_number}]: {ticket_desc}")
		thefile.write("\n")
		thefile.write("\n\n**Jira Description:**\n")
		thefile.write("\n")
		thefile.write(f"> {ticket_desc}")
		thefile.write("\n")
		thefile.write("\n\n**Jira Link:**\n")
		thefile.write("\n")
		thefile.write(jira_link)
		thefile.write("\n")
		thefile.write("\n\n**Git Branch Name:**\n")
		thefile.write("\n")
		thefile.write(f"`{git_branch_name}`\n")
		thefile.write("\n")
		thefile.write("\n")
		thefile.write("**Steps to Reproduce:**")
		thefile.write("\n")
		thefile.write("\n")
		thefile.write("1.\n")
		thefile.write("2.\n")
		thefile.write("3.\n")
		thefile.write("\n")
	return path

def main():
	file_name = make_template()
	os.system(f'open -a "Sublime Text" ~/{file_name}')

main()