# There was a day where I have too many color schemes in iTerm2 and I want to remove them all.
# iTerm2 doesn't have "bulk remove" and it was literally painful to delete them one-by-one.

# iTerm2 save it's preference in ~/Library/Preferences/com.googlecode.iterm2.plist in a binary format
# What you need to do is basically copy that somewhere, convert to xml and remove color schemes in the xml files.

$ cd /tmp/
$ cp ~/Library/Preferences/com.googlecode.iterm2.plist .
$ plutil -convert xml1 com.googlecode.iterm2.plist
$ vi com.googlecode.iterm2.plist

# Now remove the color schemes in the <key> and <dict> tags, 
# to make it easier, record a macro in vi to remove the key (e.g: Desert/Solarized) using `dd`,
# and then remove its color dict with `dat` (delete around tag), and repeat the macro until 
# all color schemes you want to delete is gone.

# Save the file, and copy it back:

$ cp com.googlecode.iterm2.plist ~/Library/Preferences/

# Note that iTerm2 has 'fallback' configuration in case something is wrong,
# You might want to remove them as well:

$ rm ~/Library/Preferences/iTerm2.plist
$ rm ~/Library/Preferences/net.sourceforge.iTerm.plist

# Now reload the configuration

$ cd ~/Library/Preferences/
$ defaults read com.googlecode.iterm2

# Restart iTerm, and check the color-scheme list in the Preferences menu, you shouldn't see the old color-schemes now.
