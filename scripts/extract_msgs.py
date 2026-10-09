import json
import re
import os

def extract_message(sub_id):
    path = f'C:/Users/bafur/.gemini/antigravity/brain/{sub_id}/.system_generated/logs/transcript_full.jsonl'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for l in reversed(lines):
        d = json.loads(l)
        if 'tool_calls' in d:
            for tc in d['tool_calls']:
                if tc.get('name') == 'send_message':
                    return tc['args'].get('Message', '')
    return ''

msg1 = extract_message('0e52b4ac-738b-481e-993b-c8fd3d0de1f8')
msg2 = extract_message('8da4402e-f88d-41d6-8cbb-6657a0db09cd')
msg3 = extract_message('7e3e7c87-9eb5-4a09-88ee-02e74128400b')

os.makedirs('scratch', exist_ok=True)
with open('scratch/msg1.txt', 'w', encoding='utf-8') as f:
    f.write(msg1)
with open('scratch/msg2.txt', 'w', encoding='utf-8') as f:
    f.write(msg2)
with open('scratch/msg3.txt', 'w', encoding='utf-8') as f:
    f.write(msg3)

print("Saved raw messages. Lengths:", len(msg1), len(msg2), len(msg3))
