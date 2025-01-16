from imessage_utils import IMessageSender
import argparse
import logging
import sys

logging.basicConfig(
   level=logging.INFO,
   format='%(asctime)s - %(levelname)s - %(message)s'
)

def parse_args():
   parser = argparse.ArgumentParser(description='Send messages via macOS Messages app')
   parser.add_argument('phone', help='Phone number with country code (e.g. +1234567890)')
   parser.add_argument('message', help='Message to send')
   parser.add_argument('--sms-only', action='store_true', help='Only try SMS, skip iMessage')
   parser.add_argument('--imessage-only', action='store_true', help='Only try iMessage, skip SMS fallback')
   return parser.parse_args()

def main():
   args = parse_args()
   sender = IMessageSender()

   if args.sms_only:
       success = sender.send_sms(args.phone, args.message)
   elif args.imessage_only:
       success = sender.send_imessage(args.phone, args.message)
   else:
       success = sender.send(args.phone, args.message)

   if not success:
       logging.error("Failed to send message")
       sys.exit(1)

   logging.info("Message sent successfully")

if __name__ == "__main__":
   main()