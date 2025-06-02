from flask import Flask, request, abort
from linebot.v3 import WebhookHandler
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.messaging import (
    MessagingApi,
    ApiClient,
    Configuration,
    ReplyMessageRequest,
    TextMessage
)
import random

print("🚀 現在執行的是新版 Line Bot 程式！")

app = Flask(__name__)

# 你的 Channel Access Token 和 Secret
CHANNEL_ACCESS_TOKEN = "FMabfaQ78pv25pP1Qi0HV9OWob4kP0chNtH30qqgDtUbeBYo7qtIsTBlo9Js/f+mv+qO2GCtUSZIGPU0f5L5bZEzR2/sXRkWBfa0vmJZcKn/9X1iuxSMn9/xyG4fkC1HVVGuIIWL9x/wEvONQoaXuwdB04t89/1O/w1cDnyilFU="
CHANNEL_SECRET = "731af951f0c6900e0916cd22a02ab0dd"


configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# 你的店家資料
responses = {
    "早餐": [
        "登登登登～☀️\n\n今日早餐推薦🥪：「如意樂活蔬食早午餐」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/zTDE2dpqtRpBnzDq6?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「711」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/PJLd53hRzE2gDyct8",
        "登登登登～☀️\n\n今日早餐推薦🥪：「太陽漢堡」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/khbnBb6iczgJYd5k6?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「麥田早點」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/xNRBBWYbgj5fUQEw9",
        "登登登登～☀️\n\n今日早餐推薦🥪：「拉亞漢堡」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/QYdPzgZeiNbvFqHo8",
        "登登登登～☀️\n\n今日早餐推薦🥪：「白鳥餐飲店」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/vHfyisyfFHgGXTUb8",
        "登登登登～☀️\n\n今日早餐推薦🥪：「金色晨光早午餐」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Fbk8ueMJjAX89QHw7?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「米嵐早午餐」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/8bPbagzxvDNt4mWH8?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「弘爺漢堡」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/jR3NvU183xEnMURv8",
        "登登登登～☀️\n\n今日早餐推薦🥪：「7-11」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/11eTn77FMNNGhKwh7?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「昌昌早餐店」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/41g2wjpiqbCrNj9k7?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「弘爺漢堡 竹進店」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/PqhrBeGHquVUCpvS7?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「黑輪姨關東煮」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/CH57LDaCgc9X52Bs9",
        "登登登登～☀️\n\n今日早餐推薦🥪：「晨間廚房」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/TT9AKN7xRRsLekPh9?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「1+1炒麵」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/utCyUYTGjmzES6AW9?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「85度C-彰化師大店」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/EtgducAqaHskKnKZ8?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「麥味登 彰化力行店」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/zKDQ7PiCgWdEhVhd9?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「早安美芝城」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/MbCW4S9zY12Tkao67",
        "登登登登～☀️\n\n今日早餐推薦🥪：「喜得炭火燒三明治彰化師大店（中山路）」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/gz7PHpeL7BJFq9VS6?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「聖豐早餐」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Mske3DZHytyxGhuCA?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「包饌手工包子饅頭（彰化店）」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/jcqbc4UDdRYmMnt78?g_st=com.google.maps.preview.copy",
        "登登登登～☀️\n\n今日早餐推薦🥪：「魯家扁食麵」\n\n距離校門口「步行1️⃣0️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/1crVR279tUzuZQcP7?g_st=com.google.maps.preview.copy",

    ],
    "午餐": [
        "登登登登～🕛\n\n今日午餐推薦🍱：「雲南小吃」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/9bmWAC4gW3QaJfyH9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「義朵義麵坊」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/cf9CJeLgQwyPQ4Wy8?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「左岸小吃」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/NQTdrUx7NTpuhTH56?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「迪迪鬆餅店」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/SuyxgHnKrGwnAuHi6?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「711」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/5J2rsuzTbaCBqPqJ9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「蓋飯家族」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/2XcNRDsHbMupr3JcA?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「寶記港式麵館」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/KN5ctvRFs7nNcKrh9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「如意樂活蔬食早午餐」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/zTDE2dpqtRpBnzDq6?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「海盜飯鋪」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/uRGx8G91thY27ByP8?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「滿香早餐店」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ohcc1K3ZebPaydDL7?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「堡嗝BurgerSpace」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/XdhfYEeVJRGRSDsX8?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「品禾臭臭鍋」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/LVfFqYoYs1cL6mum9",
        "登登登登～🕛\n\n今日午餐推薦🍱：「府城」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/WUKXKcKjKVs32cGM8",
        "登登登登～🕛\n\n今日午餐推薦🍱：「賞口飯」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/DXbcEh2iBpj4TgjC6",
        "登登登登～🕛\n\n今日午餐推薦🍱：「蘇菠麵」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/fzyV2qJoGALNTQwQ7?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「太陽漢堡」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/khbnBb6iczgJYd5k6?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「天德鐵飯碗韓式海苔飯捲」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/mLZQRm4BHK4f7pDu9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「蕭張麵館」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Uw9tuPByE1FitJyi6?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「麥田早點」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/xNRBBWYbgj5fUQEw9",
        "登登登登～🕛\n\n今日午餐推薦🍱：「御之味」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/JPAAMmSTgGf6r2KN6",
        "登登登登～🕛\n\n今日午餐推薦🍱：「拉亞漢堡」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/QYdPzgZeiNbvFqHo8",
        "登登登登～🕛\n\n今日午餐推薦🍱：「品安美食館」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/FWMXVP9j3iNhVGjH7",
        "登登登登～🕛\n\n今日午餐推薦🍱：「風味主題炒飯」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Jkn9X4pZ1s27RJ1t5",
        "登登登登～🕛\n\n今日午餐推薦🍱：「台南自助快餐」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/8YMB44Rk1PGykfREA",
        "登登登登～🕛\n\n今日午餐推薦🍱：「大眾牛肉麵」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/B3ufGYZEuVG15yWw5",
        "登登登登～🕛\n\n今日午餐推薦🍱：「幸城自助餐便當」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/EsmwbpXtXiZdWvY78",
        "登登登登～🕛\n\n今日午餐推薦🍱：「點食成津簡餐」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Qeh6Ke9ChgenF4Bj7",
        "登登登登～🕛\n\n今日午餐推薦🍱：「博多拉麵」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/7z7XV6J2aaDUBLQFA",
        "登登登登～🕛\n\n今日午餐推薦🍱：「長江素食自助餐」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Xh35hRryLDHAnm5j6",
        "登登登登～🕛\n\n今日午餐推薦🍱：「大眾素食館」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/2tuaWyZVsGx4VeQN8",
        "登登登登～🕛\n\n今日午餐推薦🍱：「日沛義麵坊」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/TqQpgBtbCGgeFbyh7",
        "登登登登～🕛\n\n今日午餐推薦🍱：「酷樂豬」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/edoEuRtTWZdGq88g8",
        "登登登登～🕛\n\n今日午餐推薦🍱：「老K餐飲店」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/uEL8ACNf2hSujRtL7",
        "登登登登～🕛\n\n今日午餐推薦🍱：「白鳥餐飲店」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/vHfyisyfFHgGXTUb8",
        "登登登登～🕛\n\n今日午餐推薦🍱：「杏花村美食快餐」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/h2yAz3Yatj2gMSNA6",
        "登登登登～🕛\n\n今日午餐推薦🍱：「台灣阿城小吃店」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/D1CVzLavVUoPQH5S8",
        "登登登登～🕛\n\n今日午餐推薦🍱：「品味自助餐」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/XvrimbNQPXuiWDhk8",
        "登登登登～🕛\n\n今日午餐推薦🍱：「金色晨光早午餐」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Fbk8ueMJjAX89QHw7?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「孫記麵館」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/7GEQQy6Wa9BmPjiP9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「讚不絕口」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/971fwQARssrYueVB6?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「賞口拉麵」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/8oVtkLmxZ2sSrrLo9",
        "登登登登～🕛\n\n今日午餐推薦🍱：「犇食麵」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/GafYQAqm47VFbFd99",
        "登登登登～🕛\n\n今日午餐推薦🍱：「八方雲集」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/kz54QEhHofkHD6717",
        "登登登登～🕛\n\n今日午餐推薦🍱：「爭夯牛排館」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/WbZJqEXbAoTS2eBw9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「彰香豆腐麵」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/aHyH7Fm8nYh1fohz8?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「吳記大腸蚵仔麵線」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/C2jqCbin5psUvZMU6?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「香港明煌燒臘快餐」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/nfVu5JdHGaggEGAv9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「關東煮砂鍋麵」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/JmMhCtMzmJRnWzyE8?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「米嵐早午餐」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/8bPbagzxvDNt4mWH8?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「荷佳蔬食（素食）」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/8GiUWejGT7YqTXyA8",
        "登登登登～🕛\n\n今日午餐推薦🍱：「義麵17」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/GLoUchJxK2bab7j39",
        "登登登登～🕛\n\n今日午餐推薦🍱：「花蓮扁食 力行店」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/iJPD3FxPqsTQHjuN6?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「胖老爹」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/5cRRR9AdB4cjkA5G9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「弘爺漢堡」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/jR3NvU183xEnMURv8",
        "登登登登～🕛\n\n今日午餐推薦🍱：「禾豐海鮮粥」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/NMDu5WFRWeTjH4RL7",
        "登登登登～🕛\n\n今日午餐推薦🍱：「九品現炒炒飯炒麵」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/qjsAGzG8HkE4L6mMA?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「7-11」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/11eTn77FMNNGhKwh7?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「弘爺漢堡 竹進店」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/PqhrBeGHquVUCpvS7?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「大大牛肉麵」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://g.co/kgs/6fTs3wh",
        "登登登登～🕛\n\n今日午餐推薦🍱：「聞香牛肉麵」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/mnet9kDx9SCAwxk77",
        "登登登登～🕛\n\n今日午餐推薦🍱：「嵐的壽司」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/PDTQTSjWVdsaUQDS7",
        "登登登登～🕛\n\n今日午餐推薦🍱：「黑輪姨關東煮」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/CH57LDaCgc9X52Bs9",
        "登登登登～🕛\n\n今日午餐推薦🍱：「晨間廚房」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/TT9AKN7xRRsLekPh9",
        "登登登登～🕛\n\n今日午餐推薦🍱：「紅燈籠臭豆腐」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/hJrYjNingTGz9HuG6?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「1+1炒麵」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/utCyUYTGjmzES6AW9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「擺肚人（鍋物放題）」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/DY6sbqcW4rqkhSap7?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「咖喱大叔」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/q7e7F5eY2tswyofY7",
        "登登登登～🕛\n\n今日午餐推薦🍱：「瑪西所」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/TNJwnvcEiKQhBi32A",
        "登登登登～🕛\n\n今日午餐推薦🍱：「早安美芝城」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/MbCW4S9zY12Tkao67",
        "登登登登～🕛\n\n今日午餐推薦🍱：「豚將拉麵」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/z47TxwUmrPSx4B6y8",
        "登登登登～🕛\n\n今日午餐推薦🍱：「森ㄧ食堂」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/brty7jEBMD248gwBA",
        "登登登登～🕛\n\n今日午餐推薦🍱：「麥味登 彰化力行店」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/zKDQ7PiCgWdEhVhd9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「沐日食光」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/bYHKGs7AV9gB4pL68?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「喜得炭火燒三明治彰化師大店 （中山路」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/gz7PHpeL7BJFq9VS6?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「鴨肉飯」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/4c5mHZGT9swUUqtg9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「板井滷肉飯爌肉飯」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/68TYd6ocHpjWcKFL8?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「NU PASTA」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/wBEzSwUHc6zNFgi57",
        "登登登登～🕛\n\n今日午餐推薦🍱：「鬆餅娜娜」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/GrY5MpEhedqr5wYn6",
        "登登登登～🕛\n\n今日午餐推薦🍱：「包饌手工包子饅頭（彰化店）」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/jcqbc4UDdRYmMnt78?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「上德素食」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/wak18ZkTCz6swDjQ9?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「老三魯肉飯」\n\n距離校門口「步行9️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/fhCHrg3nvQgaMUjv7?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「魯家扁食麵」\n\n距離校門口「步行1️⃣0️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/1crVR279tUzuZQcP7?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「不只好食」\n\n距離校門口「步行1️⃣1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/bNRmAJmeea38741z7?g_st=com.google.maps.preview.copy",
        "登登登登～🕛\n\n今日午餐推薦🍱：「裕新嘉義火雞肉飯（彰化店）」\n\n距離校門口「步行1️⃣5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/GcHjxBRSyWwFWML69?g_st=com.google.maps.preview.copy"


        ],

    "晚餐": [
        "登登登登～🕕\n\n今日晚餐推薦🍜：「雲南小吃」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/9bmWAC4gW3QaJfyH9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「義朵義麵坊」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/cf9CJeLgQwyPQ4Wy8?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「左岸小吃」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/NQTdrUx7NTpuhTH56?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「迪迪鬆餅店」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/SuyxgHnKrGwnAuHi6?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「711」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/5J2rsuzTbaCBqPqJ9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「蓋飯家族」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/2XcNRDsHbMupr3JcA?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「寶記港式麵館」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/KN5ctvRFs7nNcKrh9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「海盜飯鋪」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/uRGx8G91thY27ByP8?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「我家炸雞」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/hcoBoASa6TSQSew59?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「故鄉滷味」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/a3a6i3nMfhEV4FUk6?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「無名鍋貼」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/1yTD2iMB5qEy5ZQk8",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「堡嗝BurgerSpace」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/XdhfYEeVJRGRSDsX8",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「品禾臭臭鍋」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/LVfFqYoYs1cL6mum9",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「府城」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/WUKXKcKjKVs32cGM8",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「賞口飯」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/DXbcEh2iBpj4TgjC6",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「蘇菠麵」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/fzyV2qJoGALNTQwQ7?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「天德鐵飯碗韓式海苔飯捲」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/mLZQRm4BHK4f7pDu9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「蕭張麵館」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Uw9tuPByE1FitJyi6?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「御之味」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/JPAAMmSTgGf6r2KN6",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「品安美食館」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/FWMXVP9j3iNhVGjH7",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「日香滷味」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/PEcof1svivVoe3Kf6",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「風味主題炒飯」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Jkn9X4pZ1s27RJ1t5",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「台南自助快餐」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/8YMB44Rk1PGykfREA",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「大眾牛肉麵」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/B3ufGYZEuVG15yWw5",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「幸城自助餐便當」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/EsmwbpXtXiZdWvY78",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「點食成津簡餐」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Qeh6Ke9ChgenF4Bj7",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「博多拉麵」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/7z7XV6J2aaDUBLQFA",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「小林湯包」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/dvc8RuQjvTMt5sLC8",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「日沛義麵坊」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/TqQpgBtbCGgeFbyh7",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「酷樂豬」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/edoEuRtTWZdGq88g8",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「食神滷味」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/9x78ggZvs7vdET9EA",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「老K餐飲店」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/uEL8ACNf2hSujRtL7",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「白鳥餐飲店」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/vHfyisyfFHgGXTUb8",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「杏花村美食快餐」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/h2yAz3Yatj2gMSNA6",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「台灣阿城小吃店」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/D1CVzLavVUoPQH5S8",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「品味自助餐」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/XvrimbNQPXuiWDhk8",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「孫記麵館」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/7GEQQy6Wa9BmPjiP9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「讚不絕口」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/971fwQARssrYueVB6?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「賞口拉麵」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/8oVtkLmxZ2sSrrLo9",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「犇食麵」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/GafYQAqm47VFbFd99",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「八方雲集」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/kz54QEhHofkHD6717",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「爭夯牛排館」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/WbZJqEXbAoTS2eBw9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「彰香豆腐麵」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/aHyH7Fm8nYh1fohz8?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「蜜汁燒烤」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/96acEQGgEqv8Dy8o6?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「吳記大腸蚵仔麵線」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/C2jqCbin5psUvZMU6?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「香港明煌燒臘快餐」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/nfVu5JdHGaggEGAv9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「關東煮砂鍋麵」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/JmMhCtMzmJRnWzyE8?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「荷佳蔬食（素食）」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/8GiUWejGT7YqTXyA8",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「義麵17」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/GLoUchJxK2bab7j39",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「花蓮扁食 力行店」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/iJPD3FxPqsTQHjuN6",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「胖老爹」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/5cRRR9AdB4cjkA5G9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「7-11」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ZYidyJXrEWxPNraq8",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「禾豐海鮮粥」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/NMDu5WFRWeTjH4RL7",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「滿大碗」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/HZjpYNPUJhPKjQmz5?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「九品現炒炒飯炒麵」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/qjsAGzG8HkE4L6mMA?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「7-11」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/11eTn77FMNNGhKwh7?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「彰工福州包」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/v5wTesuTYR5Fv3Jj9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「阿長可麗餅」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Q6gmuYAy5FJWqY8B6?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「彰師大肉圓」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/2SzDq23EqNY55ged9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「臭豆腐紅豆餅」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/CAnfAXF7y3h8M1Bt6?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「大大牛肉麵」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://g.co/kgs/6fTs3wh",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「聞香牛肉麵」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/mnet9kDx9SCAwxk77",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「買辣麻辣燙」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/tk6JceELNNRsEKx38",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「嵐的壽司」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/PDTQTSjWVdsaUQDS7",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「紅燈籠臭豆腐」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/hJrYjNingTGz9HuG6?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「1+1炒麵」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/utCyUYTGjmzES6AW9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「擺肚人（鍋物放題）」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/DY6sbqcW4rqkhSap7?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「咖喱大叔」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/q7e7F5eY2tswyofY7",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「瑪西所」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/TNJwnvcEiKQhBi32A",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「豚將拉麵」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/z47TxwUmrPSx4B6y8",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「森ㄧ食堂」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/brty7jEBMD248gwBA",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「沐日食光」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/bYHKGs7AV9gB4pL68?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「鴨肉飯」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/4c5mHZGT9swUUqtg9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「板井滷肉飯爌肉飯」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/68TYd6ocHpjWcKFL8?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「NU PASTA」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/wBEzSwUHc6zNFgi57",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「鬆餅娜娜」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/GrY5MpEhedqr5wYn6",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「包饌手工包子饅頭（彰化店）」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/jcqbc4UDdRYmMnt78?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「上德素食」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/wak18ZkTCz6swDjQ9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「董家炸雞」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ePtePrugH9PsoPrv6?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「老三魯肉飯」\n\n距離校門口「步行9️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/fhCHrg3nvQgaMUjv7?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「艾克島X’s island bar」\n\n距離校門口「步行9️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/TcT3h7h9daJCZZYd9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「有間水餃店」\n\n距離校門口「步行1️⃣0️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/2jiSMwtgewcSUaPo9?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「中山豆漿」\n\n距離校門口「步行1️⃣1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/MrNpGE7hToLUpR8s7?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「台化阿欽擔仔麵」\n\n距離校門口「步行1️⃣2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/qb8JAqHuKZXRbEeZ7?g_st=com.google.maps.preview.copy",
        "登登登登～🕕\n\n今日晚餐推薦🍜：「裕新嘉義火雞肉飯（彰化店）」\n\n距離校門口「步行1️⃣5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/GcHjxBRSyWwFWML69?g_st=com.google.maps.preview.copy"

    ],

    "宵夜": [
        "登登登登～🍢\n\n今日宵夜推薦🌙：「左岸小吃」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/NQTdrUx7NTpuhTH56?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「7-11」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/5J2rsuzTbaCBqPqJ9?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「我家炸雞」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/hcoBoASa6TSQSew59?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「故鄉滷味」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/a3a6i3nMfhEV4FUk6?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「麥仕佳 烘焙坊」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/GwB313VKRhfzxdGVA",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「爆Q美式炸雞」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/T2qKp5iduLCrwwqH7",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「享點雞蛋糕」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/2Cny6Doti9JFxGhD8?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「無名店剉冰」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/DKbJGWU8tZFSTdFG6?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「甜點子豆花店」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/6ciGdfN2YNhRb4t57?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「日香滷味」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/PEcof1svivVoe3Kf6",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「鼎豆芋圓」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/1LGoFMHU6LBmkS7w7",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「豪傳說雞排」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/a2guMkMY1rDN2f6N9",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「食神滷味」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/9x78ggZvs7vdET9EA",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「至尊咔啦脆皮雞排」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/UtTQwAAHtdr7hbNdA",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「3Q脆皮雞排」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/sVFhXkuyTM8pnXe77",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「ㄚ潭豆花」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/r5Ls378w155jjYtp8?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「八方雲集」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/kz54QEhHofkHD6717",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「九點宵夜」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ispwMDMHTVdiCGHd9?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「蜜汁燒烤」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/96acEQGgEqv8Dy8o6?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「關東煮砂鍋麵」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/JmMhCtMzmJRnWzyE8?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「胖老爹」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/5cRRR9AdB4cjkA5G9?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「7-11」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ZYidyJXrEWxPNraq8",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「滿大碗」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/HZjpYNPUJhPKjQmz5?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「7-11」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/11eTn77FMNNGhKwh7?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「原鄉人甘草芭樂」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/KgaHHdjnrd8JAzaL6",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「謝記燒烤」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/c9dSYgdAipvyLnV96",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「買辣麻辣燙」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/tk6JceELNNRsEKx38",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「紅燈籠臭豆腐」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/hJrYjNingTGz9HuG6?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「85度C-彰化師大店」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/EtgducAqaHskKnKZ8?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「潮麻吉-香雞潮牌」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/vQ9updFvxGTTtAFe7",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「清原芋圓」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/kUv44hoDRwk5KmKEA",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「森ㄧ食堂」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/brty7jEBMD248gwBA",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「老攤豆花」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ZZLCv6HxGrw6LDbz8?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「董家炸雞」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ePtePrugH9PsoPrv6?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「艾克島X’s island bar」\n\n距離校門口「步行9️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/TcT3h7h9daJCZZYd9?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「有間水餃店」\n\n距離校門口「步行1️⃣0️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/2jiSMwtgewcSUaPo9?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「永大藥房」\n\n距離校門口「步行1️⃣1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Lmg4v6STtGo8ZaHg6?g_st=com.google.maps.preview.copy",
        "登登登登～🍢\n\n今日宵夜推薦🌙：「台化阿欽擔仔麵」\n\n距離校門口「步行1️⃣2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/qb8JAqHuKZXRbEeZ7?g_st=com.google.maps.preview.copy"     
    ],

    "點心": [
        "登登登登～🍰\n\n今日點心推薦🥞：「迪迪鬆餅店」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/SuyxgHnKrGwnAuHi6?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「711」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/5J2rsuzTbaCBqPqJ9?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「我家炸雞」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/hcoBoASa6TSQSew59?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「故鄉滷味」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/a3a6i3nMfhEV4FUk6?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「麥仕佳 烘焙坊」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/GwB313VKRhfzxdGVA",
        "登登登登～🍰\n\n今日點心推薦🥞：「爆Q美式炸雞」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/T2qKp5iduLCrwwqH7",
        "登登登登～🍰\n\n今日點心推薦🥞：「享點雞蛋糕」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/2Cny6Doti9JFxGhD8?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「無名店剉冰」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/DKbJGWU8tZFSTdFG6?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「甜點子豆花店」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/6ciGdfN2YNhRb4t57?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「鼎豆芋圓」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/1LGoFMHU6LBmkS7w7",
        "登登登登～🍰\n\n今日點心推薦🥞：「豪傳說雞排」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/a2guMkMY1rDN2f6N9",
        "登登登登～🍰\n\n今日點心推薦🥞：「至尊咔啦脆皮雞排」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/UtTQwAAHtdr7hbNdA",
        "登登登登～🍰\n\n今日點心推薦🥞：「3Q脆皮雞排」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/sVFhXkuyTM8pnXe77",
        "登登登登～🍰\n\n今日點心推薦🥞：「ㄚ潭豆花」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/r5Ls378w155jjYtp8?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「甜蜜時刻義式手作冰淇淋」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/jAdLkEDw8o7SiWjG7?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「九點宵夜」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ispwMDMHTVdiCGHd9?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「蜜汁燒烤」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/96acEQGgEqv8Dy8o6?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「關東煮砂鍋麵」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/JmMhCtMzmJRnWzyE8?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「胖老爹」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/5cRRR9AdB4cjkA5G9?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「慢漫來手作蔥抓餅」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/5gf8qhE4L7aRnFHUA",
        "登登登登～🍰\n\n今日點心推薦🥞：「7-11」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ZYidyJXrEWxPNraq8",
        "登登登登～🍰\n\n今日點心推薦🥞：「滿大碗」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/HZjpYNPUJhPKjQmz5?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「7-11」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/11eTn77FMNNGhKwh7?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「彰工福州包」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/v5wTesuTYR5Fv3Jj9?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「阿長可麗餅」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Q6gmuYAy5FJWqY8B6?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「彰師大肉圓」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/2SzDq23EqNY55ged9?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「臭豆腐紅豆餅」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/CAnfAXF7y3h8M1Bt6?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「原鄉人甘草芭樂」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/KgaHHdjnrd8JAzaL6",
        "登登登登～🍰\n\n今日點心推薦🥞：「謝記燒烤」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/c9dSYgdAipvyLnV96",
        "登登登登～🍰\n\n今日點心推薦🥞：「買辣麻辣燙」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/tk6JceELNNRsEKx38",
        "登登登登～🍰\n\n今日點心推薦🥞：「紅燈籠臭豆腐」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/hJrYjNingTGz9HuG6?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「Q到你心裡地瓜球」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/gZmmRQZkQ6k8ayH36?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「85度C-彰化師大店」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/EtgducAqaHskKnKZ8?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「映麥冰沙冷飲」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ASH9h4o7pmG3r6aj8?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「潮麻吉-香雞潮牌」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/vQ9updFvxGTTtAFe7",
        "登登登登～🍰\n\n今日點心推薦🥞：「清原芋圓」\n\n距離校門口「步行7️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/kUv44hoDRwk5KmKEA",
        "登登登登～🍰\n\n今日點心推薦🥞：「鬆餅娜娜」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/GrY5MpEhedqr5wYn6",
        "登登登登～🍰\n\n今日點心推薦🥞：「老攤豆花」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ZZLCv6HxGrw6LDbz8?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「包饌手工包子饅頭（彰化店）」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/jcqbc4UDdRYmMnt78?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「董家炸雞」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ePtePrugH9PsoPrv6?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「石原省太郎彰化店」\n\n距離校門口「步行8️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/7h5WBLC8r5qpCtqF9?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「品佳豆花」\n\n距離校門口「步行9️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/jKrz51U35Fpt4Sf46?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「奇奇甜品」\n\n距離校門口「步行9️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/4Rie7ZCaSxmsDdUu7?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「有間水餃店」\n\n距離校門口「步行1️⃣0️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/2jiSMwtgewcSUaPo9?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「永大藥房」\n\n距離校門口「步行1️⃣1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Lmg4v6STtGo8ZaHg6?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「不只好食」\n\n距離校門口「步行1️⃣1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/bNRmAJmeea38741z7?g_st=com.google.maps.preview.copy",
        "登登登登～🍰\n\n今日點心推薦🥞：「豆花伯傳統豆花」\n\n距離校門口「步行1️⃣2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/sWp36Nzg1hs5HkV39?g_st=com.google.maps.preview.copy"

    ],

    "飲料": [
        "登登登登～🥤\n\n今日飲料推薦🍹：「水云茶堂」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/amRVrmPMBk2urZQDA",
        "登登登登～🥤\n\n今日飲料推薦🍹：「7-11」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/5J2rsuzTbaCBqPqJ9?g_st=com.google.maps.preview.copy",
        "登登登登～🥤\n\n今日飲料推薦🍹：「50嵐」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/MDUXhVUTsdmByeyC8?g_st=com.google.maps.preview.copy",
        "登登登登～🥤\n\n今日飲料推薦🍹：「隨緣珍珠奶茶」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/4HL4iUcbYm4f9Qkm7",
        "登登登登～🥤\n\n今日飲料推薦🍹：「牛媽媽茶坊」\n\n距離校門口「步行1️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/yc7U6kennxJFm6Rs6",
        "登登登登～🥤\n\n今日飲料推薦🍹：「三十九間茶」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/mzq7m5G6sj7aNB4N9?g_st=com.google.maps.preview.copy",
        "登登登登～🥤\n\n今日飲料推薦🍹：「喫茶小舖」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/nYcXJpnhJCehquvw6",
        "登登登登～🥤\n\n今日飲料推薦🍹：「Mr.Wish」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/TvSzvxBA6aWfF8rB7",
        "登登登登～🥤\n\n今日飲料推薦🍹：「TEA'S原味」\n\n距離校門口「步行2️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/fw4cPLqTGvVqKQw27",
        "登登登登～🥤\n\n今日飲料推薦🍹：「大肚量小肚量」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/NkzaFJsHMK5CppJS7",
        "登登登登～🥤\n\n今日飲料推薦🍹：「南海茶道」\n\n距離校門口「步行3️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/mk7eDf9hEjapra479",
        "登登登登～🥤\n\n今日飲料推薦🍹：「田原茶舖」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/X2m9MDBp13y9ciht7",
        "登登登登～🥤\n\n今日飲料推薦🍹：「呵喝茶」\n\n距離校門口「步行4️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/KXff4p4NCYLWF3oCA?g_st=com.google.maps.preview.copy",
        "登登登登～🥤\n\n今日飲料推薦🍹：「吳記茶舍」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/Aeod1ZWuhdrE5Fmc8?g_st=com.google.maps.preview.copy",
        "登登登登～🥤\n\n今日飲料推薦🍹：「7-11」\n\n距離校門口「步行5️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ZYidyJXrEWxPNraq8",
        "登登登登～🥤\n\n今日飲料推薦🍹：「85度C」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/CvurSKcoQHYV7cT49?g_st=com.google.maps.preview.copy",
        "登登登登～🥤\n\n今日飲料推薦🍹：「85度C-彰化師大店」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/EtgducAqaHskKnKZ8?g_st=com.google.maps.preview.copy",
        "登登登登～🥤\n\n今日飲料推薦🍹：「映麥冰沙冷飲」\n\n距離校門口「步行6️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/ASH9h4o7pmG3r6aj8?g_st=com.google.maps.preview.copy",
        "登登登登～🥤\n\n今日飲料推薦🍹：「品佳豆花」\n\n距離校門口「步行9️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/jKrz51U35Fpt4Sf46?g_st=com.google.maps.preview.copy",
        "登登登登～🥤\n\n今日飲料推薦🍹：「艾克島X’s island bar」\n\n距離校門口「步行9️⃣分鐘」\n\n詳細資訊：https://maps.app.goo.gl/TcT3h7h9daJCZZYd9?g_st=com.google.maps.preview.copy"
        
    ]
}

@app.route("/", methods=["GET"])
def home():
    return "伺服器正在運行～🚀"

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except Exception as e:
        print(f"❌ 錯誤：{e}")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    user_message = event.message.text.strip()
    print(f"📝 收到訊息：{user_message}")

    # 決定回什麼
    if user_message in responses:
        reply_text = random.choice(responses[user_message])
    else:
        reply_text = "呱？Sorry，我們無法個別回覆您😞請點選「早餐」、「午餐」、「晚餐」、「宵夜」、「點心」、「飲料」來獲得推薦吧！\n\n如果有任何問題或建議，歡迎填寫表單來告訴我們唷～\nhttps://forms.gle/57cf7gsHoRMuPyhN6"

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[
                    TextMessage(text=reply_text)
                ]
            )
        )

if __name__ == "__main__":
    app.run(port=8000, debug=True)
