import requests
from flask import Flask, Response

app = Flask(__name__)

TOKEN = '8086038655:AAG5FfTAz-WVV-xpdi64UZrUm8aWsm1U7DA'  # এখানে আপনার বটের টোকেন বসাবেন
CHANNEL_USERNAME = (
    '@movielover322'  # এখানে আপনার পাবলিক চ্যানেলের ইউজারনেম দেবেন
)


@app.route('/video/<int:msg_id>')
def stream_video(msg_id):
  # ১. পাবলিক চ্যানেল থেকে মেসেজ ইনফো নেওয়া
  get_msg_url = f'https://api.telegram.org/bot{TOKEN}/forwardMessage?chat_id=@telegram&from_chat_id={CHANNEL_USERNAME}&message_id={msg_id}'
  # (অথবা সরাসরি கெট ফাইল মেথড দিয়েও করা যায়)

  # সহজ পদ্ধতি: সরাসরি টেলিগ্রাম থেকে ফাইলের লিংক ফেচ করা
  # (পাবলিক চ্যানেলের জন্য আমরা সরাসরি টেলিগ্রামের ফাইল পাথ জেনারেট করতে পারি)
  get_file_url = (
      f'https://api.telegram.org/bot{TOKEN}/getChat?chat_id={CHANNEL_USERNAME}'
  )

  # বিকল্প ও সবচেয়ে কার্যকরী উপায় হলো আগের মতো file_id ব্যবহার করা,
  # কারণ পাবলিক চ্যানেলে ভিডিও আপলোড করলেই বটে বা সহজে file_id পাওয়া যায়।
  return 'Ready for streaming!'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)