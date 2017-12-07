# Assemble rules updating Algorithm
my_assemble_dict = {
    "$Rules_Path" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1\Python_STG_Assemble_rules\\",

    "$Rules_modified_Path" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1\Python_STG_Assemble_rules\STG_Assemble_rules_Updated\\",

    "$Assemble_Logs_Report_Path" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1\Python_STG_Assemble_rules\STG_Assemble_Reports_Generated\\",

    "$Apply_Label" : "applylabel:STG_generic",

    "$Remove_Label" : "removelabel:STG_generic",

    "$SendEmailFromName" : "testuser8332",

    "$SendEmailFromAddress" : "testuser8332@auto8.mobileiron.com",

    "$SendEmailToAddress" : "testuser8333@auto8.mobileiron.com",

    # the file name itself will be appended to the below 6 lines.
    "$SendEmailSubject" : "",
    "$SendEmailBody" : "",
    "$ReportMessage" : "",
    "$SendMessageText" : "",
    "$ActionReason" : "",
    "$ReportName" : "",

    "$label_import" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1\Python_STG_Assemble_rules\label_import.csv",

    "$bulk_import" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1\Python_STG_Assemble_rules\/bulkimport.csv",

    "$appcontrol_List" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1\Python_STG_Assemble_rules\/appcontrollist_example.csv",

    "$AppNames" : "AnyConnect,Apps@Work,Docs@Work,Secure Apps Manager,TouchDown for SmartPhones,Tunnel",

    "$Apps_Source_File" : "/Users/Miadmin/Desktop/Assemble/assemble_v47.1/Python_STG_Assemble_rules/appnames_unicode.txt",

    "$Trigger_apps_File_Location" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1\Python_STG_Assemble_rules\/appnames_versions_unicode.txt",

    #If you are working with "appname_unicode" and "appnames_version_unicode" rules, then update the "appname_unicode.txt"
    #and "appnames_version_unicode.txt" files with your corresponding appnames and use those appnames in "AppNames" line in above.

    "$appcontrol_updaterule_entries" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1\Python_STG_Assemble_rules\/appcontrollist_example.csv",

    "$airprint_import" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1\Python_STG_Assemble_rules\/airprint.csv",

    "$Syslog_Server" : "10.101.12.26",

    "$Ldap_group_name" : "Domain Users",

    "$mdm_complete_startdate" : "1/10/2017",
    "$mdm_complete_enddate" : "21/10/2017",

    "$vsp_ip" : "stg-223.auto.mobileiron.com",

    "$AssembleExeLocation" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1/assemble_v47.1_x64.exe",

    "$VSPiniLocation" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1/vsp.ini",

    "$AssembleExecutionLogsPath" : "C:\Users\Miadmin\Desktop\Assemble\/assemble_v47.1\Python_STG_Assemble_rules\STG_Logs_Assemble_run\\",

    "$ModeOfRuleExecution" : "test"

    # Note :
    #1) Element1_trigger=app:version:AnyConnect ---> where ever we use this trigger will work only with the file "appnames_unicode.txt"
    # if you want to work with different appnames trigger, then we have to make changes in the "appnames_unicode.txt" file too with corresponding appname entry in it.

    # 2) Note 1 is applicable for this too. "Element1_trigger=app:version:file:$AppNames_Trigger_File_Location"
}