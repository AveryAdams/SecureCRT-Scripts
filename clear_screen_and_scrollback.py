# $language = "python"
# $interface = "1.0"

# A very simple script to clear screen and scrollback for all tabs

def Main():
    initialTab = crt.GetScriptTab()
    
    for i in range(1, crt.GetTabCount()+1):
        tab = crt.GetTab(i)
        tab.Activate()
        tab.Screen.SendSpecial("MENU_CLEAR_SCREEN_AND_SCROLLBACK")
		
    initialTab.Activate()

Main()
