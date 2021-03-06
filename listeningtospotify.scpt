set countthis to 0
repeat while application "Spotify" is running
	tell application "Spotify"
		set countthis to (countthis + 1)
		if player state is playing then
			set theSong to name of current track
			set theAlbum to album of current track
			set theArtist to artist of current track
			set thisTrack to current track
			set theDate to (current date)
			if contents of theArtist is not "" then
                    #must setup your own information regarding server
				set myFile to open for access "/PATHTOFILE/listening.php" with write permission
				set eof myFile to 0
				write ({"<span style='font-size: 9pt'>Listening To:</span><br>", theSong, " by ", theArtist, "<br><span style='font-size: 9pt'>", theDate, "</span>"} as string) to myFile
				close access myFile
				set AlertURLString to "http://PATHTOSERVER/transmit.php"
				set curlOutput to do shell script "curl '" & AlertURLString & "'"
			end if
			#delay 3
			#end repeat
		end if
	end tell

	delay 30 #repeat every 30 seconds until spotify or script stopped
end repeat
