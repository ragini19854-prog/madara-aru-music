from pyrogram.types import InlineKeyboardButton
import config
from IstkharMusic import app
def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons
def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_7"], url=f"https://t.me/TuneBots"),
        ],
        [
            InlineKeyboardButton(text="🥀 ʀᴇᴘᴏ", url="\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x69\x74\x68\x75\x62\x2e\x63\x6f\x6d\x2f\x54\x45\x41\x4d\x2d\x49\x53\x54\x4b\x48\x41\x52\x2f\x49\x73\x74\x6b\x68\x61\x72\x4d\x75\x73\x69\x63")
        ]
    ]
    return buttons
