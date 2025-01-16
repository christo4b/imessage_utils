IMESSAGE_SEND = '''
tell application "Messages"
    try
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{phone}" of targetService
        send "{msg}" to targetBuddy
        delay 2
        set lastMsg to last message of targetBuddy
        if delivered of lastMsg is false then
            error "Message not delivered"
        end if
        return "success"
    on error errMsg
        return "error: " & errMsg
    end try
end tell
'''

SMS_SEND = '''
tell application "Messages"
    try
        set targetService to 1st service whose service type = SMS
        set targetBuddy to buddy "{phone}" of targetService
        send "{msg}" to targetBuddy
        return "success"
    on error errMsg
        return "error: " & errMsg
    end try
end tell
'''

CHECK_STATUS = '''
tell application "Messages"
    try
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{phone}" of targetService
        set msgs to messages of targetBuddy
        repeat with m in msgs
            if content of m is "{msg}" then
                if delivered of m is false then
                    return "not_delivered"
                else
                    return "delivered"
                end if
            end if
        end repeat
        return "not_found"
    on error errMsg
        return "error: " & errMsg
    end try
end tell
'''