Creating Merge request:
	• Create merge request on firefox
		○ Don't check "delete source branch" (yet)
		○ Submit Merge
		○ People can comment/approve (useful)
	• At the top you can see the changes/commits from the latest merge request
		○ Go to overview
		○ Can review code with somebody else for approval
		○ Can hit merge (will be green) when there are no conflicts between versions

Make sure local changes are committed:
	• Git status
		○ See what is under "changes not staged for commit"
	• Git add <> (whatever files you want to push to git)
		○ Ex) Git add Admin Excel Files/QIP_database.xlsx (to add single file)
		○ Ex) Git add *.ipf (to add all ipfs listed)
	• Git commit -m "message stating purpose of commit"
	• Git push
		○ This will now push local changes to Firefox

Manual Merge:
	• Go to FireFox, open up merge request
		○ Click "Merge locally" to get instructions
		○ Copy instructions line-by-line (except step 4!)  into git bash terminal
			§ Finalizes changes
			§ If fatal error, skip to line 3b
				□ Branch already exists on git
				□ If error from local version persists, use -f for checkout
		○ Final part of step 3:
			§ Will show which ipfs have conflicts between versions that git could not resolve itself
				□ Cyan color header shows where pseudo merge status is active
					® Need extra caution!!!
					® If pushed changes are not resolved, will crash everyone's version of FQDAT
				□ Make sure all files listed in red/green are one's we want to push to git
					® Move FQDAT_Clean folder
					® Move stand_alone FQDAT functions to a separate folder!
			§ Open .ipf we want to resolve conflicts for in NOTEPAD++, not FQDAT or anything else
				□ Search "<<<<" or HEAD
				□ Everything above ==== is IGOR_8_DEVEL (older version)
					® Everything below is dev/Luke_edits (update)
				□ For conflicts that only involve adding lines:
					® Delete lines with <<<<, >>>>>, and ==== 
				□ When there are manual merges:
					® Must take conflicts one at a time
					® Recommend commenting out old all old code and cycling through changes one at a time to debug
						◊ Must make sure differences in old version are not simply discarded (we may still want those)
					® When one conflict is resolved, save and debug the next one
						◊ Good to have peer review process inserted here
		○ To exit process:
			§ Close git Bash window
			§ Git checkout development branch you are working on
