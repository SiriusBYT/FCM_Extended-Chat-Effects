from flashapi import * 
"""
This tool lets you quickly configure your page in a hurry.
Read https://github.com/SiriusBYT/Flashcord/wiki/The-Flashcord-Store-Template for how this file works.

This script does not do the following but will in the future:
- Set "Other Modules by X" embeds automatically (A long time later! Requires internet & communication to sirio-network.com)
"""

# Edit the following things
isRepluggedPlugin = False
isFlashcordCompetitor = False # TBD, does absolutely nothing for now (Pages for Themes, yes the Flashcord store will... host themes other than Flashcord. This is a stupid idea which is why this isn't implemented yet and why I'm still just thinking about it.)
AllowAPI = True # Allows the script to connect to the SGN servers in order to make your store page more complete without user input


Name = "Extended Chat Effects"
Short_Description = "Bring back Flashcord Alpha Chat Effects to the newest versions!"
Version = "v1.0.3"
License_Year = "2024"
License = "Unlicense"


GitHub_Profile = "SiriusBYT" # Notice: this will be converted to lowercase and will be your folder name after modules/plugins
GitHub_Repo = "FCM_Extended-Chat-Effects" 
GitHub_Contributors = "SiriusBYT"

Discord = "https://sirio-network.com/redirect.discord"
SNDL_Theme = "Dark"
Embed_Color = "#FF69FF"

Store_Page_Name = "extended_chat_effects.html" # NO capitals! Underscores only! CANNOT HAVE "-files" AT THE END!
Folder_Name = "extended_chat_effects-files" # NO capitals! Underscores only! Must have "-files" at the end!
Embed_FileName = "embed-banner.gif" # Notice: GIFs work!
Store_Embed_FileName = "embed-banner.gif" # I would still suggest against it due to AuraCloud-E2A's limited space.

Long_Description = '<h1>This module hooks into the "FC-ChatEffects_Animated" and "FC-ChatEffects_Text" FlashCore Modules.</h1>\n\
                <p>Since Flashcord Beta, several Flashcord Effects got removed due to either poor client performance or due to them being entirely useless.</p>\n\
                <p>This official Flashcord Module will let you have them back.</p>\n\
                <div>\n\
                    <div class="SNDL-Quote SNDL-BC_Disclamer">\n\
                        <div>\n\
                        <h2>Please note:</h2>\n\
                            <p>These effects have been removed for a reason.</p>\n\
                            <p>Nearly nobody uses them and they cause severe lag.</p>\n\
                            <p>Remind yourself also that no one can see the extended chat effects unless they install this module.</p>\n\
                            <p class="SNDL-ParenthesisedText">You do not wanna end up in a weird situation where to the eye of other people,\n\
                                you just drop a http://flashcord/background/red in the middle of nowhere.\n\
                            </p>\n\
                        </div>\n\
                    </div\n\
                </div>\n\
                <div>\n\
                    <h2>Re-Added Chat Effects:</h2>\n\
                    <div class="SNDL-DashList">\n\
                        <div class="SNDL-Quick_FlexGrid" style="justify-content: flex-start;">\n\
                            <p>Rainbow Text</p>\n\
                            <div class="SNDL-CodeBlock" style="scale: 0.8; margin: 0;">\n\
                                <p>http://flashcord/rainbow</p>\n\
                            </div>\n\
                        </div>\n\
                        <p>Colored Message Backgrounds:</p>\n\
                        <div class="SNDL-DashList">\n\
                            <div class="SNDL-Quick_FlexGrid" style="justify-content: flex-start;">\n\
                                <p>Green Background</p>\n\
                                <div class="SNDL-CodeBlock" style="scale: 0.8; margin: 0;">\n\
                                    <p>http://flashcord/background/green</p>\n\
                                </div>\n\
                            </div>\n\
                            <div class="SNDL-Quick_FlexGrid" style="justify-content: flex-start;">\n\
                                <p>Red Background</p>\n\
                                <div class="SNDL-CodeBlock" style="scale: 0.8; margin: 0;">\n\
                                    <p>http://flashcord/background/red</p>\n\
                                </div>\n\
                            </div>\n\
                            <div class="SNDL-Quick_FlexGrid" style="justify-content: flex-start;">\n\
                                <p>Blue Background</p>\n\
                                <div class="SNDL-CodeBlock" style="scale: 0.8; margin: 0;">\n\
                                    <p>http://flashcord/background/blue</p>\n\
                                </div>\n\
                            </div>\n\
                        </div>\n\
                        <div class="SNDL-Quick_FlexGrid" style="justify-content: flex-start;">\n\
                        <p>Loud Effect</p>\n\
                            <div class="SNDL-CodeBlock" style="scale: 0.8; margin: 0;">\n\
                                <p>http://flashcord/loud</p>\n\
                            </div>\n\
                        </div>\n\
                        <div class="SNDL-Quick_FlexGrid" style="justify-content: flex-start;">\n\
                            <p>Quiet Effect</p>\n\
                            <div class="SNDL-CodeBlock" style="scale: 0.8; margin: 0;">\n\
                                <p>http://flashcord/quiet</p>\n\
                            </div>\n\
                        </div>\n\
                        <div class="SNDL-Quick_FlexGrid" style="justify-content: flex-start;">\n\
                            <p>Spinning Effect</p>\n\
                            <div class="SNDL-CodeBlock" style="scale: 0.8; margin: 0;">\n\
                                <p>http://flashcord/spin</p>\n\
                            </div>\n\
                        </div>\n\
                        <div class="SNDL-Quick_FlexGrid" style="justify-content: flex-start;">\n\
                            <p>Rainbow Shadow</p>\n\
                            <div class="SNDL-CodeBlock" style="scale: 0.8; margin: 0;">\n\
                                <p>http://flashcord/rainbow-shadow</p>\n\
                            </div>\n\
                        </div>\n\
                        <div class="SNDL-Quick_FlexGrid" style="justify-content: flex-start;">\n\
                            <p>Splash Text Effect</p>\n\
                            <div class="SNDL-CodeBlock" style="scale: 0.8; margin: 0;">\n\
                                <p>http://flashcord/splash</p>\n\
                            </div>\n\
                        </div>\n\
                    </div>\n\
                    <h2>Chat Effects Preview</h2>\n\
                    <p>Notice: Certain animations may look broken and are infinitely looping.</p>\n\
                    <p class="RainbowText">Rainbow Text</p>\n\
                    <p class="Green">Green Background</p>\n\
                    <p class="Red">Red Background</p>\n\
                    <p class="Blue">Blue Background</p>\n\
                    <p class="Loud">Loud Effect</p>\n\
                    <p class="Quiet">Quiet Effect</p>\n\
                    <p class="Spin">Spinning Effect</p>\n\
                    <p class="RainbowShadow">Rainbow Shadow</p>\n\
                    <p class="Splash">Splash Text Effect</p>\n\
                </div>\n\
            </div>'

# NOT recommended to modify, do this only if you know what you're doing! 
StoreTemplate = "flashcord/store/templates/default/default-store_template.html"
EmbedTemplate = "flashcord/store/templates/default/default-embed_template.html"

# Don't touch this, it will get overwritten anyways but still. Don't touch just in case.
HTMLFile = ""

# Don't touch this either. This will cause problems if your store page is for a Flashcord Module!
UserFolderName = GitHub_Profile.lower()

def GetEmbedCode():
    HTMLCode = ''
    API_Folders = []
    def CallAPI():
        if isRepluggedPlugin == True:
            API_Request = "GET/" + "PLUGINS/" + GitHub_Profile.upper()
        elif isFlashcordCompetitor == True:
            API_Request = "GET/" + "THEMES/" + GitHub_Profile.upper()
        else:
            API_Request = "GET/" + "MODULES/" + GitHub_Profile.upper()
        RequestResults = FlashClient_API_Request(API_Request)
        return RequestResults
    API_Folders = CallAPI()
    #print("TYPE:",type(API_Folders))
    #print("DATA:",API_Folders)
    if API_Folders != None:
        API_Folders = API_Folders.replace("[","").replace("]","").replace('"','').split(",")
        for cycle in range (len(API_Folders)):
            API_Folders[cycle] = API_Folders[cycle] + "-files"
        if Folder_Name in API_Folders:
            API_Folders.remove(Folder_Name)
        for cycle in range (len(API_Folders)):
            HTMLCode = HTMLCode + '<iframe class="Flashcord-Module_Embed" src="' + API_Folders[cycle] + '/embed.html"></iframe>\n'
    else:
        HTMLCode = HTMLCode + '<iframe class="Flashcord-Module_Embed" src="' + Folder_Name + '/embed.html"></iframe>\n'
    return HTMLCode

# This code is disgusting but it works, will optimize when I feel like it.
# NOTICE: this has ZERO error handling (or very little)! This is fucking horrible but I don't know yet how to do those and at the time of writing it's fucking 23h28
def GetHTMLFile(FileConcerned):
    if FileConcerned == "Store Page":
        if isRepluggedPlugin == True:
            File = "flashcord/store/plugins/" + GitHub_Profile.lower() + "/" + Store_Page_Name
        else:
            File = "flashcord/store/modules/" + GitHub_Profile.lower() + "/" + Store_Page_Name
    elif FileConcerned == "Embed":
        if isRepluggedPlugin == True:
            File = "flashcord/store/plugins/" + GitHub_Profile.lower() + "/" + Folder_Name + "/embed.html"
        else:
            File = "flashcord/store/modules/" + GitHub_Profile.lower() + "/" + Folder_Name + "/embed.html"
    else:
        print('[FlashCFG // GetHTMLFile] ERROR: Sirius A was here and pissed on the moon. (What the fuck is a "', FileConcerned, '"?!)')
        return "FUCK"
    return File

def FileBackup(FileToBackup):
    print("[FlashCFG // Backup] The", FileToBackup, "will now be backed up...")
    HTMLFile = GetHTMLFile(FileToBackup)
    HTMLFile_Backup = HTMLFile.replace(".html",".bak-html")
    try:
        with open(HTMLFile, 'r', encoding='utf-8') as HTMLFile_File:
            with open(HTMLFile_Backup, 'w', encoding='utf-8') as HTMLFile_Backup_File:
                HTMLFile_Backup_File.write((HTMLFile_File.read()))
        print("[FlashCFG // Backup] ", HTMLFile_Backup, "has been created and is now backed up.")
    except:
        print("[FlashCFG // Backup] ", HTMLFile_Backup, "doesn't exist! Creating empty file instead...")
        with open(HTMLFile, 'w', encoding='utf-8') as EditHTML_File:
            EditHTML_File.write("")

def HTMLConfigurator(Step):
    # We're doing this the MarkSNDL way, I can't fucking figure out how to do this the objectively better way
    # This is surprisingly way better than the current version of MarkSNDL though LMFAO
    HTMLArray = []
    if Step == 0:
        print("[FlashCFG // HTML-CFG] Now building the Store Page...")
        HTMLFile = GetHTMLFile("Store Page")
        StepFile = "// Store Page"
    elif Step == 1:
        print("[FlashCFG // HTML-CFG] Now building the Embed...")
        HTMLFile = GetHTMLFile("Embed")
        StepFile = "// Embed"
    else:
        print("[FlashCFG // HTML-CFG] ERROR: Sirius A was here and replaced Sirius B's Yae wallpaper with a Kirara one.", '(What the fuck is Step "', Step, '"?!)')
        return "FUCK"

    if AllowAPI == True:
        print('[FlashCFG // HTML-CFG] Connecting to SGN servers to fill the "More by" section...')
        MoreByCode = GetEmbedCode() # NOTICE: Will phone to the SGN servers!
        print(f'[FlashCFG // HTML-CFG] The "More by" section will have:\n{MoreByCode}')
    else:
        MoreByCode = '<iframe class="Flashcord-Module_Embed" src="' + Folder_Name + '/embed.html"></iframe>\n'
    

    with open(StoreTemplate, 'r', encoding='utf-8') as StoreTemplate_File:
        with open(EmbedTemplate, 'r', encoding='utf-8') as EmbedTemplate_File:
            with open(HTMLFile, 'w', encoding='utf-8') as EditHTML_File:
                EditHTML_File.write("")
            with open(HTMLFile, 'a', encoding='utf-8') as EditHTML_File:
                if Step == 0:
                    HTMLArray = StoreTemplate_File.readlines()
                elif Step == 1:
                    HTMLArray = EmbedTemplate_File.readlines()
                else:
                    print("[FlashCFG // HTML-CFG] WARNING: Sirius A was here and caused another Big Bang", '(What the fuck is Step "', Step, '"?!)')
                    print("[FlashCFG // HTML-CFG] Also how in the LIVING FUCK DID YOU TRIGGER THIS ERROR without triggering the previous one?")
                    return "FUCK"
                for line in range (len(HTMLArray)):
                    # print('[FlashCGG] Processing Line"', line, '" which is "', HTMLArray[line], '".')
                    HTMLArray[line] = HTMLArray[line].replace("[NAME]", Name)
                    HTMLArray[line] = HTMLArray[line].replace("[SHORT_DESC]", Short_Description)
                    HTMLArray[line] = HTMLArray[line].replace("[LONG_DESC]", Long_Description)
                    HTMLArray[line] = HTMLArray[line].replace("[VERSION]", Version)
                    HTMLArray[line] = HTMLArray[line].replace("[LICENSE_YEAR]", License_Year)
                    HTMLArray[line] = HTMLArray[line].replace("[LICENSE]", License)
                    HTMLArray[line] = HTMLArray[line].replace("[GITHUB_PROFILE]", GitHub_Profile)
                    HTMLArray[line] = HTMLArray[line].replace("[GITHUB_REPO]", GitHub_Repo)
                    HTMLArray[line] = HTMLArray[line].replace("[GITHUB_CONTRIBUTORS]", GitHub_Contributors)
                    HTMLArray[line] = HTMLArray[line].replace("[DISCORD_LINK]", Discord)
                    HTMLArray[line] = HTMLArray[line].replace("[THEME]", SNDL_Theme)
                    HTMLArray[line] = HTMLArray[line].replace("[EMBED_COLOR]", Embed_Color)
                    HTMLArray[line] = HTMLArray[line].replace("[STORE_PAGE_FILENAME]", Store_Page_Name)
                    HTMLArray[line] = HTMLArray[line].replace("[FOLDER_NAME]", Folder_Name)
                    HTMLArray[line] = HTMLArray[line].replace("[EMBED_FILENAME]", Embed_FileName)
                    HTMLArray[line] = HTMLArray[line].replace("[STORE_EMBED_FILENAME]", Store_Embed_FileName)
                    HTMLArray[line] = HTMLArray[line].replace("[STORE_USER_FOLDER]", UserFolderName)
                    HTMLArray[line] = HTMLArray[line].replace("[FLASHSTORE_API-EMBEDS]", MoreByCode)
                    EditHTML_File.write(HTMLArray[line])
                    ProcessingProgress = ((line+1)/len(HTMLArray))*100
                    print('[FlashCFG // HTML-CFG] Processed Line', line+1, '/', len(HTMLArray), '(', ProcessingProgress, '%).', StepFile)
                    # print('[FlashCGG] Processed Line is now "', HTMLArray[line], '".')

def FlashcordStoreConfig():
    print("[FlashCFG] Script initiated.")
    FileBackup("Store Page")
    HTMLConfigurator(0)
    FileBackup("Embed")
    HTMLConfigurator(1)
    print("[FlashCFG] Script complete.")
    return

FlashcordStoreConfig()