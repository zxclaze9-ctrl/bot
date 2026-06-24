import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = "8876570486:AAGC3HPJh1EcAZfyKZDtkRVdY_S5ZvUOEKY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

jokes = [
    "Bir bola maktabga kech qolibdi. O‘qituvchi: Nega kech qolding? Bola: Tushimda maktabga keldim.",
    "Doktor: Chekishni tashlang. Bemor: Men chekmayman. Doktor: Unda boshlamang.",
    "Talaba: Ustoz, 2 baho qo‘ymang. Ustoz: Mayli, 1 qo‘yaman.",
    "Kompyuter: Men ishlamayapman. Egasi: Men ham."
]

def main_menu():
    kb = ReplyKeyboardBuilder()
    kb.button(text="🎰 Casino")
    kb.button(text="💵 Dollar narxi")
    kb.button(text="😂 Kulgili")
    kb.button(text="🌤 Ob-havo")
    kb.button(text="📰 Yangiliklar")
    kb.button(text="🎲 Tasodifiy fakt")
    kb.button(text="⏰ Soat")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def casino_menu():
    kb = ReplyKeyboardBuilder()
    kb.button(text="🎰 Slot")
    kb.button(text="🪙 Coin Flip")
    kb.button(text="💰 Balans")
    kb.button(text="⬅️ Orqaga")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def funny_menu():
    kb = ReplyKeyboardBuilder()
    kb.button(text="🤣 HZL")
    kb.button(text="⬅️ Orqaga")
    return kb.as_markup(resize_keyboard=True)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Assalomu alaykum!\nBotga xush kelibsiz.",
        reply_markup=main_menu()
    )

@dp.message(F.text == "🎰 Casino")
async def casino(message: Message):
    await message.answer(
        "Casino bo'limi",
        reply_markup=casino_menu()
    )

@dp.message(F.text == "🎰 Slot")
async def slot(message: Message):
    symbols = ["🍒", "🍋", "🍇", "⭐", "💎"]
    result = " ".join(random.choices(symbols, k=3))

    if len(set(result.split())) == 1:
        text = f"{result}\n\n🎉 JACKPOT!"
    else:
        text = f"{result}\n\n😢 Yutqazdingiz."

    await message.answer(text)

@dp.message(F.text == "🪙 Coin Flip")
async def coin(message: Message):
    await message.answer(
        f"Natija: {random.choice(['HEADS', 'TAILS'])}"
    )

@dp.message(F.text == "💰 Balans")
async def balance(message: Message):
    await message.answer("Balans: 1000 coin")

@dp.message(F.text == "💵 Dollar narxi")
async def dollar(message: Message):
    await message.answer(
        "1 USD ≈ 12700 UZS\n\n(API ulansa real kurs chiqadi)"
    )

@dp.message(F.text == "😂 Kulgili")
async def funny(message: Message):
    await message.answer(
        "Kulgili bo'lim",
        reply_markup=funny_menu()
    )

@dp.message(F.text == "🤣 HZL")
async def hzl(message: Message):
    await message.answer(
        random.choice(jokes)
    )

@dp.message(F.text == "🌤 Ob-havo")
async def weather(message: Message):
    await message.answer(
        "Ob-havo moduli keyin API bilan ulanadi."
    )

@dp.message(F.text == "📰 Yangiliklar")
async def news(message: Message):
    await message.answer(
        "Yangiliklar moduli keyin API bilan ulanadi."
    )

@dp.message(F.text == "🎲 Tasodifiy fakt")
async def fact(message: Message):
    facts = [
        "Asal buzilmaydigan mahsulot.",
        "Sakkizoyoqning 3 ta yuragi bor.",
        "Yerda qumdan ko'ra ko'proq yulduz mavjud."
    ]

    await message.answer(random.choice(facts))

@dp.message(F.text == "⏰ Soat")
async def clock(message: Message):
    from datetime import datetime

    now = datetime.now().strftime("%H:%M:%S")
    await message.answer(f"Hozirgi vaqt: {now}")

@dp.message(F.text == "⬅️ Orqaga")
async def back(message: Message):
    await message.answer(
        "Asosiy menyu",
        reply_markup=main_menu()
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())