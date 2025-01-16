IMESSAGE_SEND = '''
tell application "Messages"
    try
        if not (exists service 1 whose service type = iMessage) then
            error "iMessage service not available"
        end if
        set targetService to 1st service whose service type = iMessage
        
        try
            set targetBuddy to buddy "{phone}" of targetService
        on error
            error "Invalid phone number or contact not found"
        end try
        
        send "{msg}" to targetBuddy
        delay 2
        
        try
            set lastMsg to last message of targetBuddy
            if delivered of lastMsg is false then
                error "Message failed to deliver"
            end if
            if content of lastMsg is not "{msg}" then
                error "Message verification failed"
            end if
        on error errMsg
            error "Delivery verification failed: " & errMsg
        end try
        
        return "success"
    on error errMsg
        return "error: " & errMsg
    end try
end tell
'''

SMS_SEND = '''
tell application "Messages"
    try
        if not (exists service 1 whose service type = SMS) then
            error "SMS service not available"
        end if
        set targetService to 1st service whose service type = SMS
        
        try
            set targetBuddy to buddy "{phone}" of targetService
        on error
            error "Invalid phone number or contact not found"
        end try
        
        send "{msg}" to targetBuddy
        delay 1
        return "success"
    on error errMsg
        return "error: " & errMsg
    end try
end tell
'''

CHECK_STATUS = '''
tell application "Messages"
    try
        if not (exists service 1 whose service type = iMessage) then
            error "iMessage service not available"
        end if
        set targetService to 1st service whose service type = iMessage
        
        try
            set targetBuddy to buddy "{phone}" of targetService
        on error
            error "Invalid phone number or contact not found"
        end try
        
        try
            set msgs to messages of targetBuddy
            if (count of msgs) is 0 then
                error "No messages found with this contact"
            end if
            
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
            error "Message check failed: " & errMsg
        end try
    on error errMsg
        return "error: " & errMsg
    end try
end tell
'''