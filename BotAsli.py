from email import message
import secrets
from pyrogram import Client, filters, client
import random
import time
from pyrogram.types import Message
from datetime import datetime
from ast import Await
from pyrogram.types import ChatPermissions
from pyrogram.errors import UserNotParticipant
from logging import WARN, WARNING
from googletrans import Translator
import asyncio
import re

API_ID = '23920856'
API_HASH = 'a04021e7192d6974beefb422705e225d'
BOT_TOKEN = '7686509114:AAGWJFtHHDxfshJfy-7oSpFsyqvYl0iT5TQ'
app = Client("مامان سهیل کسناموسلعون", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

Fohsh = ["گوردون فریمن میشم با دیلم میفتم به جون ایزوگام ناموست", "مادرت رو سالار معمولی کراش زده",
         "مامانت طرفدار آهنگای نگین فضلیه", "مادرت با آهنگای داریوش تبهکار گل میکشه",
         "برای جشن تولد مادرت نوکیا 001 خریدم جای اینکه یه هفته بهم رایگان کس بده گفت من ایفون ۱۶ پرومکس میخوام منم همون نوکیارو زدم تو کلش ضربه مغزی شد مرد",
         "با کیر آقای قادر ترکی شتک میزنم به لنگ و لونگ تنگ تونگ چرب و چیل کل کثیف مادرت,"
         "مادرت به کارتل مواد مکزیک تریاک بدهکاره",
         "کابل hdmi مانیتور مادرتو بجای کارت گرافیک به مادربرد وصل کردم فک کنه کامپیوترش سوخته گریه کنه",
         "مادرتو مجبور میکنم هر صبح منو با نوازش کیرم از خواب بلند کنه تا امید به زندگیم بره بالا",
         "مادرتو به عنوان معلم زبان پایه نهم استخدام میکنم تا simple present درس بده",
         "مادرتو به عنوان اشکنه مرغ تو سوپ حل کردم", "برای مامانت چای سبز ریختم تا آروم شه",
         "مادرتو مجبور میکنم رو مادربرد h410m-R سی پی یو i7 12700 k ببنده", "سبزی خورشتی های فریز مادرتو دزدیدم",
         "حدیث های اسلام سر مادرت کلاه گذاشتن پس با تون تون تون تون ساحور به استقبال مرگ مادرت میروم",
         "با استفاده از جایگاه اجتمایی و شغلی بالایی که در طی سالها زحمت بهش رسیدم، مادر خدمتکارت رو میگام و هر روز روانیش میکنم",
         "با توپ مادرت تنیس بازی کردم",
         "برا سیستم ویندوز ویستا مادرت یه فایل bat مخرب فرستادم بهش گفتم این رو اجرا کنه ویندوزش تبدیل به مک M4 Ultra میشه",
         "مامانتو جای شهاب سنگ توی برنامه دیوار گذاشتم با قیمت توافقی",
         "مامانتو به جرم تجاوز انداختم زندان تو زندان نزدیک ۶۰ نفر بهش تجاوز کردن بعد سه سال که فهمیدم بی گناه بود گفتم ببخشید بعدش ازادش کردم",
         "مادرت نشست رو صورت ونوم",
         "سنباده نرم به گردن مادرت کشیدم که کبود شه و بعد با سنباده درجه ۱۲ چنان ممه های مادرتو تیکه پاره کردم تا پدرت سر ظهر با دیدن بدن مادرت فکر کنه ونوم به اون تجاوز کرده",
         "مادرت توی مسابقه قرائت قرآن مقام اول رو کسب کرد",
         "مادرت معتقده که امیر تتلو فوش نمی‌ده حقیقت هارو میگه😏😏😏۷۸",
         "برای مادرت آلبوم V - Halmstad از Shining رو رو تکرار پخش میکنم انقد غمگین شه خودکشی کنه",
         "مامانت از مامان پارسا جنده تره", "ناموست از ناموس آرمان کونی تره",
         "یه معجون نابی تو تهرانپارس میخورم میام ی تنه کل ناموستو میزنم زمین",
         "خواهرت دنیارو بهم داد مادرت یه دنیا بهم داد", "انتالپی واکنش مادرت عدد حقیقی نبود", "چشای مادرت مایل به سبزه",
         "کله مادرتو میبرم و میدم میلاد محمدی با پشتک پرتابش کنه طرف کون آقای جاکشت",
         "عامل اصلی حادثه هیروشیما گوزای مادرت بود ", "عامل اصلی حادثه هیروشیما گوزای مادرت بود ",
         "آپتیموس پرایم مادرتو گایید، نتیجه سکسشون شد لوله اگزوز خاور", "کون مادرتو آچار کشی کردم",
         "لپای ابجی کوچیکتو با انبر دست کشیدم", "صبر مادرتو با کیر ندادن بهش و گذاشتن ی کیر جلوش مورد آزمایش قرار دادم",
         "مامانت اومد تو هلیکوپتر از سیستم ایجکت استفاده کرد وقتی پرتاب شد هوا، ملخه های هلیکوپتر مادرتو تیکه تیکه کردن",
         "قطر مویرگهای بدنم از رگ غیرت بابات کلفت تره", "سنگ قبر مادرتو دزدیدم",
         "کون مامانت پشم داره", "کسمادرتو جنگیری کردم روز بعدش جنه اومد ازم تشکر کرد",
         "فیلم مورد علاقه مادرت کیردزدان دریایی کارئیبه",
         "الهی روده های مادرت قد بادکنک های شب تولد ابجی کوچیکت باد کنن بترکه",
         "حشمت فردوس شدم گوزیدم تو کس ناموست صابر از خنده زیاد اسهال کرد دهن زنش",
         "داییت تو خط شهدا نیست (برای درک به میم قدیمی کیرم به کس خار یک یکشون مراجعه کنید)",
         "رابطه من و مادرت انقدر خوب بود که نه قلب من شکست نه قلب مادرت فقط تخت خونتون شکست",
         "با تحقیقات به این نتیجه رسیدم که شیر گاو های امروزی چون بهشون هورمون میزنن بدرد نمیخوره بنابرین خط تولید شیر گاو رو یک تنه سپردم دست ننت و انقد از ی جفت ممه 95 مادرت شیر دوشیدم که کل شرکت های میهن و دامداران و چوپان رامک به تولید انبوه شیر مامانت رسیدن",
         "الهی بواسیر مادرت پاره شه رو صورت خواهرت",
         "منوی رستوران مورد مادرت:\nجلو کباب\nچلو کیر\nچلو ماهیچه با کردن\nراسته کباب",
         "دیروز به مامانت محل ندادم رفت به یه محل داد", "مادرت رم دو بود و منم جی تی ای 6",
         "سبحان مامانتو تو گیم نتش گایید", "من رفیقای علی بودم و مادرت خود علی و کسمادرت گوشی علی",
         "تاحا رو ناموست جق شورتی میزنه", "گوسفندا و چوب دستی قابوس تو کسوکون مامانت",
         "با عمامه سه متری مهدی مادرتو دار میزنم", "با دینامیت و بمب های سجاد مامانتو ترور میکنم",
         "ننگ و نفرین و لعن و لعنت و اه و دشنام و هزاران تف و فحش بر روح کثیف و خبیث و نحیف و کریح مادرت",
         "دالگتو تکه تکه میکنم میدم به خارکوچیکت مثه پازل بچینتشون کنار هم", "یاکریم میشم روی شکم مادرت لونه میکنم",
         "پوشک مادربزرگتو میدزدم بعد قلقلکش میدم ۱۰ کیلو اسهالی برینه وسط خونتون",
         "نیپلای مادرتو میکَنَم وصل میکنم به کنترلر پی اس فایوم به عنوان joystick",
         "مادرتو میفرستم با رافائل نادال تنیس بازی کنه",
         "کس دادن اگه بدنسازی بود مادرت الان بدنش از هادی چوپان پر حجم تر و گنده تر بود",
         "ناموست اگه بدن ساز بود اسمش میشد کونی گوهمن",
         "مادرت از توپخونه به خونه بهبود حمله کرد رحمت رید تو خودش قسمت بعدی با آریشگاه آنلاین موهای مادرتو از ته میزنه",
         "سهم واجبی مادرتو نمیدم", "بهروز بادیگارد ناموست شد",
         "عن مادرتو طرح مجسمه ازادی امریکا برشکاری کردم",
         "کیرمو میکنم تو پوشک مادربزرگت به عن اغشته شه بعد میکنمش دهن مادرت",
         "بواسیر ناموستو کشیدم صدای جق جقش در اومد", "ویلچر ناموستو توربو شارژ کردم",
         "شومبول قیطانی کردم دهن پدر خوش غیرتت بعد سیبیلای موشکی باباتو کردم تو کس ننت ناموس شلغم",
         "مامانت ناهار خورشت کرفس درست کرد زدم زیر قابلمش همش ریخت رو زمین", "همسایه خونتون مرد، مادرت عزادار شد‌.",
         "با پول ننت اتریوم خریدم نگه داشتم ننت که قیمتشو دید مجبور شد برای جبران ضرر بره به ساتوشی کس بده",
         "وایمیسم حکومت عوض شه پهلوی بیاد ارزونی بشه النگو های مادرت که بخاطرشون یک عمر جندگی کردو بفروشم",
         "مادرت چنل دیلی داره توش از خاطرات اولین تجاوزش تعریف می‌کنه و با قربانیان تجاوز هم‌دردی می‌کنه",
         "از آبکیر مادرت به عنوان خمیر سیلیکون کامپیوتر عمو فردوس خواهر کوچیکت استفاده کردم",
         "اسید ریختم تو کون مادرت انقدر تو حموم صابون شیاف کرده بود سالیان سال که اسید تو کونش حل شد",
         "کره بادام زمینی شکالاتی مادرتو دزدیدم توش گوز قلیایی با چگالی بالا دادم",
         "به مادرت گفتم عاشقمی یا برا پول باهامی گفت کسخل تو نه پول داری نه قیافه معلومه واسه 20 سانت کیرته باهاتم",
         "خواهر زن باجناق باباتو گاییدم", "به ناموست ۳۰ دقیقه ویس دادم", "مادرت رو کونش تتو کرده دی سی",
         "مادرت به صاحب سوپرمارکت کوسلی کون داد", "مادرت نچه یاشندا هووووش",
         "علت منقرض شدن دایناسورا شهاب سنگ نبود علت اصلیش این بود که مامانت با کون بزرگش افتاد رو زمین",
         "مامانت از سزار گوه تره", "کون مامانت از دماغ متین گنده تره", "مامانت از ماحی کاپوت نیسان تره",
         "مادرت از ملیکا نیک منش جنده تره", "بابات از یوسف نیک منش بی غیرت تره",
         "بابات از روح الله (بابای مائده) گوه تر و بیغیرت تره", "مامانتو تبعید کردم به گمیش تپه",
         "گوشای سبحان تو کون ننت اصلا", "رنگ موهای مادرت از  رنگ موی تاحا قشنگ تره",
         "آجرای جیزز دهن ناموست", "گوسفند های قابوس تو کس ننت", "الهی متر بشم مامانتو جای غذای ناهار امروز بخورم",
         "کیر محمد طاها رمضانی کلاس دهم فنی دهن ناموست", "هربار اومدم بگم که من عن دارم زبونم بند اومد ریدم توی ناموست",
         "مادرت از رها افغان کیری تره", "دسیمون میشم صورت مامانتو چکی میکنم", "مادرت از آرساکیا گوه تره",
         "موجی میشم با مادرت رل میزنم یه چنل دوتایی میزنیم اسمامونو سنجاق میکنیم توش",
         "علی میشم تو کسمادرت رنک 5 اف بی ای میگیرم", "مادرت از محراب گوه تره",
         "رستو میشم جیمیل مادرتو عوض میکنم هی لاگین میکنم تو اکانتش رمزشو عوض میکنم (آرین هم گریه کنه)",
         "خانوم معلم 25 ساله میشم به مادرت آموزش میدم", "وارالوس میشم با تیپ کونی مانند مخ مادرتو میزنم",
         "صاحب سوپرمارکت کوسلی مادرتو بگاد", "به مامانت گفتم عاشقتم😂😂😂😂😂😂😂",
         "زنجیر متین تو کسمادرت", "سهیل ناجی میشم پیش مامانت گریه میکنم که منو نزنه من میخوام هلپر شم",
         "گربه دانیال کس مامانتو لیس زد بعدش فوت شد", "گوزای علی مادرتو بی‌هوش کرد", "آروغای طاها کسمادرتو بودایی کرد",
         "مامانت یخشی الله کژدری باباخاخاس", "صدای مامانت از دسیمون نازک تره", "گوشای مادرت از سبحان هم تیز تره",
         "هی تو اگه پسر خدام باشی مادرتو میگام", "الهی مادرت مثل ملیکا نیک منش بشه",
         "الهی مامانتو مثل سزار بگام در عرض یک ساعت دلیت اکانت کنه بره به بدبختیاش فکر کنه",
         "مامانتو مثل سزار با مثلث طاها،سبحان،مهدی گاییدم دلیت اکانت زد", "مامانتو عنمال کردم",
         "لای کون مامانت عن گیر کرده", "شمع های امین مشهدی و انار های امین ساوه ای تو کون ننت",
         "خون پریودی مادرتو بستنی توت فرنگی کردم", "مادرت با موتور میره مخ دخترا رو میزنه بعد باهاشون لز میکنه",
         "کس مادرتو جوری کردم که مثل دره شده با داد زدن صدا اکو میشه",
         "سرعتی که کامیار باهاش پیام  فوروارد میکنه تو چنل، از سرعت مادرت حین ساک دارکوبی زدن کمتره",
         "حرف های مادرت سر کون ندادنش عین وعده صادق  میمونه \nهر دو توخالی و دروغین",
         "مخ مادرت تو سیزده بدر زدم دیگه پسر بی‌غیرتش رو نمیشناسه",
         "کسمادرت بعد از پنجاه سالگی تفاوتی با سیاه‌چاله نخواهد داشت.\nکسمادرت ده دقیقه آینده را نخواهد دید",
         "مادرت تینیجر بازی در میآورد می‌گفت بزار اول فیلم ببینیم داغ بشیم بعد سکس کنیم ولی من از ثانیه اول خودشو مادرشو میگاییدم",
         "اشتون هال میشم چهار دقیقه تو هوا مادرتو میگام",
         "به اشتون هال وقتی داره ویدیو روتین میگیره بهش به جا لیمو ناموس رنده شده‌تو میدم دستش فشار بده ناموست پودر شه توی آب گاز دار اونم کله‌شو بکنه توی ناموست",
         "میدونی چرا مادرت گیاهخوار نمیشه؟/nچون از خوردن کیر من تا ابد محروم میشه", "ناموست گوجه رو با پوست خورد",
         "مادرت شتریه که روی همه میخوابه",
         "با ابجی  شیمیل 7 سالت ازدواج  میکنم تا حاملم کنه و وقتی باردار  شدم بچه رو از شکمم میکشم بیرون میکنمش تو کونم تا پدر مادر افغانیت فکر این نباشن که بخوان جمعیتشون رو زیاد کنن تا ایران رو بگیرن و دق کنن",
         "مادرت قله اورست رو فتح میکنه ، خبرنگارها جمع میشن و ازش می پرسند : آقا رمز موفقیت شما چی بود\nمادرت میگه : والله نمیدونم من ولی اگه بازم بهم بار بخوره میارم این بالا",
         "مادرت میخواسته خودکشی کنه، می‌ره عطاری میگه یه مرگ موش بده\nفروشنده میگه نداریم\nمیگه اشکال نداره بجاش یه تله موش بده",
         "روی مادربرد ddr5 دست دوم قسطی مادرت سی لیتر شاشیدم",
         "بهتاش میشم مادرتو گاز میگیرم تا مثل میمون بشه و وقتی عصبی شد با قابلمه بکوبه رو میزی که پدرت با حقوق ۹ ماهش خریده بود",
         "تو مراسم خاستگاری مادرت که داماد حلقه رو گذشته بود تو کیک ورود کردم و کیکو‌ کردم‌ تو کونم",
         "روی لپتاپ لنووا اقتصادی استوک میام برچسب اپل میزنم روش کروم او اس نصب میکنم به ننت میگم مک بوکه با آخرین مدل مک او اس",
         "مادرتو انقدر خوب کردم پدرت به عنوان اشانتیون خواهرتم داد بکنم",
         "با زردی دندان مادرت حدود ۱۵ دستگاه تاکسی ساختم",
         "از کسمادرت خرگوش میکشم بیرون سوپرایز بشه بابات بلند میشه واسم دست میزنه میگه یه دکل نفت هم واسمون رو کن",
         "میدم کیرمو مامانت عینه جارو برقی سه موتوره بکشه تو دهنش",
         "مادرتو میگام یه آبجی جدید واست به دنیا بیاره دردو دل هاتو باهاش در میون بزاری",
         "مادرت میخواست سیگار روشن کنه \nابراهیم هی دست میزد به فندکش",
         "به قولی انقده تزریق کرده که جنازشو بندازی رو اب شناور میمونه و ۱۰۰۰ سال طول میکشه تا بدنش تجزیه شه",
         "مادر پیرت انقده به خودش ژل و بوتاکس زده تا خودشو سکسی و جوون نشون بده و مردمو اغوا کنه که بهش میگم plastic bitch",
         "کیرمو عین پرچم میکوبم تو کس مادرت تا همه بفهمن خاک ناموست صاحب داره",
         "رو مادرت ویندوز ۷ نصب میکنم تا قابلیت اجرای استیم رو نداشته باشه و بصورت خودکار شروع کنه به حذف کردن خودش",
         "نوح درختای چوب برای کشتی رو تو کسمادرت پرورش میداد", "ابراهیم بُت بزرگو خراب کرد انداخت گردن مادرت",
         "بوی گندم داریوش تو کس مادرت پلی کن میشه بوی ماهی",
         "مادرت مثل خط بریله \nهر باری که کیر میره توش منظور نیت بکنشو میفهمه",
         "شبا که خوابی ننتو میبرم بوم کرج بش آیس پک میدم", "پدرت ایده پرداز سایت شهوانیه",
         "مادرت عامل پشت پرده صلح امریکا با ایرانه(به ترامپ مجانی کون داد)",
         "نقش مادرت در پاییتخت 8 دوست دختر ارسطو", "مادرت امروز پیامبر آمریکا و ایران بود", "مادرت ادمین رشتی تایمه",
         "غیرت پدرت مثل روکش کاکائویی بستنی زمستونیه", "مادرت از سرشیر ماست طبیعی هم چرب تره",
         "مثل عذابی که به قوم لوط وارد شد کیرم بر سر مادرت نازل شد",
         "رو پیامای مامانت ریکشن فیک میزنم تا فکر کنه خیلی حرفاش خفن و حقه",
         "با ته استکان چایی زدم تو سر مادرت", "قیافه مادرت شبیه فیوز چراغ راهنمای 405 عه",
         "قیافه مادرت شبیه اونور خیابونه", "قیافە مادرت شبیە تە کتریە",
         "مادرتو تو اتاق سرور زندانی میکنم که جای سخت افزار، به سایت ها امکانات هاست ارائه بده",
         "قیافه مادرت شبیه ترموستات سماور برقی عه",
         "مادرت خریدار صلحه ولی کسی قیمت نمیده", "مادرت میره جلو پنکه میگه کـــــیــــر صداش میلرزه میخنده",
         "بلیط پرواز تهران به مشهد مادرتو کنسل کردم",
         "چوس بر پایه فیزیک کوانتوم زدم دهن ابجیت غیرت پدرت دچار ساختارشکنی شد و برای همیشه صفر شد",
         "مادرت تو خیابون سهروردی ساندویچی اژدر زاپاتا داره",
         "استیو مادرتو گایید الان مادرت مثل همستر مربعی میرینه", "داداشت تو مسابقه غیرت آخر شد",
         "مادرت اون پشت با سالار چیکار میکرد", "غیرت پدرت مثل قضیه جفت گیری کلاغه(هیشکی ندیدتش)",
         "پدر بی غیرت معتادت انقده خمار مواد بود که مادر و خواهرتو در ازای یه گرم تریاک فروخت(حتی مادر و خواهرت رو هم ارزش یه گرم تریاکم ندارن)",
         "واسه ام دی اف رفته بودم خونه ناموست (کمد) درست میکردم تابستون بودو گرمم شد تو اتاق تنها بودم ننه آقات هال بودن، گفتم چقد گرمه یهو یکی زیر تخت با صدای کلفت گفت: \nداداش منو چی میگی از دیشب اینجام تخمام جوجه شد",
         "مادرت تحلیل گر رمز ارز بود یکی دو بار اشتباه گفت ممبرای چنلش ننتو به هفتاد و دو روش unlimited order گاییدن",
         "وقتی مادرت داشت ظرف میشست خیلی رمانتیک و عاشقانه قدم قدم نزدیکش شدم",
         "بساط جوراب فروشی مادرتو تو بلوار معلم بهم زدم",
         "فوری فوری🔴\nمادرت گمشده، از یابنده تقاضا میشود امشب واسه خودش فردا بیاد مادرتو بده ما که ما هم پسفردا تحویل خانوادش بدیم",
         "مامانتو انداختم تو یه قایق کاغذی ولش کردم وسط اقیانوس",
         "تو خونه ننت انجیل جاساز کردم به جرم تشکیل و عضویت در کلیسای خانگی بازداشتش کردن",
         "تراژدی فقط بابات و اون آقا سیاه پوسته که ننه اتو میگاد",
         "مادرت تو نقطه صفر مرزی ساعت ۴ صبح شاخ و شونه میکشید گنده گوزی میکرد با پهباد زدن عین عن چسبید به زمین",
         "لباس چمنی میپوشم میرم تو پارک سر کوچتون واسه خوردن کس مادرت استتار میکنم",
         "بیژن پاکزاد میشم از مادر کون لختت به عنوان مدل برای طراحی جدیدم استفاده میکنم میزنم بیلبوردای LA",
         "از دست مامان بیش فعالت قفل کودک لباسشویی رو فعال کردم تا با کمر نره توش کونش رو قمبل کنه",
         "پلی تایم my femboy roommate رو اکانت استیم مادرت ۴۱۶ ساعته",
         "تبدیل به فردین میشم ی کف گرگی میخوابونم جلد پیشونی ننه ناکِست",
         "به مادرت کتاب بیگانه البر کامو رو میدم بخونه افسرده شه خودکشی کنه",
         "مادرت گوهمو از گوشت کوبیده تشخیص نداد تا تهشو خورد",
         "به مادرت غذا دادم چاق و چله شد اقا گرگه اومد کونش گذاشت", "آرایش مادرتو پاک کردم افتاد پادگان 05 کرمان",
         "زیست شناس میشم ننت با علمم دستکاری ژنتیکی میکنم  2 تا سوراخ هاش بشه 8 تا کیر کل همسایه ها همزمان ساپورت کنه",
         "شمع روشن میکنم قطره های پارافین که قطره ایی میریزه رو هدایت میکنم رو چوچول مادرت تا از شدت درد سرش بزنه به در دیوار",
         "قبل گاییدن مادرت بسم الله نگفتم شیطان هم شریک شد", "چکای مادرتو برگشت زدم",
         "بیمه تامین اجتماعی ننتو باطل کردم", "شیر نفت ناموستو بستم تجهیزات استخراج نفت چینی بمونه رو دستش",
         "مادرت چوس پتروشیمی زد مافیای نفت شدم والا",
         "من بدون صدا صحبت میکنم بدون پا میدوم بدون سکس حامله میشم من چی‌ام؟ آفرین مادرت",
         "مردم هيپنوتيزم میشن مادرت کیرنوتیزم میشه"]

# Manager Commands

OWNERS_ID = [6549274440, 1561426715, 5790387235, 6618721118, 7258689816, 6780020142, 6425835981, 1714747422,
             "butwhowins", "LordOfNaSeR"]
attackers = {}
attack_active = {}
group_closed = False
translator = Translator()


@app.on_chat_member_updated()
async def welcome(client, chat_member):
    if chat_member.new_chat_member.status == "member":
        user = chat_member.new_chat_member.user
        await client.send_message(chat_member.chat.id,
                                  f"سلام {user.mention}! به گروه خوش آمدی!\n امیدوارم لحظات خوبی رو در این سیرک سپری کنی!\n(اگه دختری کیرت دهنم)")
    elif chat_member.new_chat_member.status == "left":
        user = chat_member.new_chat_member.user
        await client.send_message(chat_member.chat.id,
                                  f"کس مادرت {user.mention}!\n اگه بدخواه نبودی که هیچی؛ اگه بودی کیر تو کسو کون ایلوتبارت ننه کونی لفت دادی مامانت زن تک تک اعضای گروه شد!")


@app.on_message(filters.command("Bot") & filters.group)
async def bot(client, message):
    await message.reply("بات آنلاینه گلم")


@app.on_message(filters.command("start") & filters.group)
async def start(client, message):
    await message.reply("Created by: @LordOfNaSeR\n@RealmOfDark_Comment for ever")


@app.on_message(filters.command("Help") & filters.group)
async def Help(client, message):
    await message.reply(
        "سلام؛ اول از همه بگم این ربات توسط @butwhowins ساخته شده و فقط توسط ادمین های Dark Comment قابل استفاده هست؛ پس الکی جایی ادش نکن و پیویش استارت نزن مرسی\nدرضمن تمامی دستورات باید با ریپلای زده بشن تا دستور کار کنه\nCommands List:\n1-/Ban: بن کردن شخص\n2-/Unban: آنبن کردن شخص\n3-/Mute: میوت کردن شخص\n4-/Unmute: آنمیوت کردن شخص\n4-/Warn: اخطار به شخص\n5-/Unwarn: حذف اخطار شخص\n6-/CloseGroup: بستن گروه\n7-/OpenGroup: بازکردن گروه\n8-/Translate: ترجمه *کلمه* مورد نظر(کلمه را جلوی دستور بنویسید)\n\nAttacker Commands:\n1-/Attack: قفل تگ\n2-/StopAttack: متوقف کردن قفل تگ\n3-/Setreply: قفل ریپلای\n4-/Stopreply: متوقف کردن قفل ریپلای\n5-/Setenemy: تنظیم دشمن\n6-/Removeenemy: حذف دشمن\n7-/Protection: حفاظت از فرد با ریپلای\n8-/Deleteprotection: حذف حفاظت فرد با ریپلای\n\n/Help: نمایش همین پیام")


@app.on_message(filters.command("Ban") & filters.group)
async def ban(client, message):
    if message.reply_to_message:
        if message.from_user.id in OWNERS_ID:
            try:
                await message.chat.ban_member(message.reply_to_message.from_user.id)
                await message.reply_text(
                    f"کاربر {message.reply_to_message.from_user.mention} به دستور شما از گروه اخراج شد!")
            except Exception as e:
                await message.reply_text(f"مشکلی برای اخراج کاربر به وجود آمد!\n {str(e)}")
        else:
            await message.reply_text("شما مجاز به استفاده از این دستور نیستید!")
    else:
        await message.reply_text("لطفا روی کاربری که می‌خواهید اخراج کنید ریپلای کنید!")


@app.on_message(filters.command("Mute") & filters.reply)
async def mute(client, message):
    if message.reply_to_message:
        if message.from_user.id in OWNERS_ID:
            try:
                user = message.reply_to_message.from_user
                user_id = user.id
                permissions = ChatPermissions(
                    can_send_messages=False,
                    can_send_media_messages=False,
                    can_send_other_messages=False,
                    can_add_web_page_previews=False,
                )
                await client.restrict_chat_member(chat_id=message.chat.id, user_id=user_id, permissions=permissions)
                await message.reply_text(f"کاربر {user.username or user.first_name} به دستور شما در گروه سکوت شد! ")
            except Exception as e:
                await message.reply_text(f"مشکلی برای سکوت کاربر به وجود آمد!\n {str(e)}")
        else:
            await message.reply_text("شما مجاز به استفاده از این دستور نیستید!")
    else:
        await message.reply_text("لطفا روی کاربری که میخواهید سکوت کنید ریپلای کنید!")


@app.on_message(filters.command("Unban") & filters.reply)
async def unban(client: Client, message: Message):
    if message.from_user.id not in OWNERS_ID:
        await message.reply("شما مجاز به استفاده از این دستور نیستید!")
        return
    replied_message = message.reply_to_message
    if not replied_message:
        await message.reply("!لطفا به پیام کاربر مورد نظر ریپلای کنید.")
        return
    try:
        user_id = replied_message.from_user.id
        chat_id = message.chat.id
        await client.unban_chat_member(chat_id, user_id)
        await message.reply(f"کاربر {replied_message.from_user.mention} به دستور شما از لیست سیاه خارج شد!")
    except UserNotParticipant:
        await message.reply("این کاربر در لیست سیاه گروه نیست!")
    except Exception as e:
        await message.reply(f"مشکلی در حذف کاربر از لیست سیاه به وجود آمد!\n {str(e)} ")


@app.on_message(filters.command("Unmute") & filters.reply)
async def unmute(client, message):
    if message.from_user.id not in OWNERS_ID:
        await message.reply_text("شما مجوز لازم برای این کار را ندارید!")
        return
    replied_user = message.reply_to_message.from_user
    if replied_user:
        try:
            await client.unban_chat_member(message.chat.id, replied_user.id)
            await message.reply_text(f"کاربر {replied_user.mention} به دستور شما از حالت سکوت خارج شد!")
        except Exception as e:
            await message.reply_text(f"مشکلی برای حذف سکوت کاربر پیش آمد!:\n {str(e)}")
    elif not replied_user:
        await message.reply_text("لطفا روی پیام کاربری که میخواهید از سکوت خارج کنید ریپلای کنید!")


@app.on_message(filters.command("CloseGroup") & filters.user(OWNERS_ID))
async def close_group(client, message):
    try:
        bot_member = await client.get_chat_member(message.chat.id, client.me.id)
        if bot_member.status not in ["administrator", "creator"]:
            return await message.reply("ربات باید مدیر گروه باشد!")

        global group_closed
        group_closed = True
        permissions = ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False
        )
        await client.restrict_chat_member(message.chat.id, message.from_user.id, permissions=permissions)
        await message.reply("گروه بسته شد!")
    except Exception as e:
        await message.reply(f"مشکلی در بستن گروه پیش آمد\n {str(e)}")


@app.on_message(filters.command("OpenGroup") & filters.user(OWNERS_ID))
async def open_group(client, message):
    try:
        chat_id = message.chat.id
        permissions = ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_invite_users=True
        )
        await client.set_chat_permissions(chat_id, permissions)
        await message.reply_text("گروه باز شد!")
    except Exception as e:
        await message.reply(f"مشکلی در باز کردن گروه پیش آمد!:\n{str(e)}")


@app.on_message(filters.command("Warn") & filters.reply)
async def warn(client: Client, message: Message):
    try:
        warned_user = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        if message.from_user.id not in OWNERS_ID:
            await message.reply("شما اجازه استفاده از این دستور را ندارید!")
            return
        if warned_user in WARNING:
            WARNING[warned_user] += 1
        else:
            WARNING[warned_user] = 1
        await message.reply(f"کاربر  {warned_user} توسط شما اخطار گرفت!\n تعداد اخطارها: {WARNING[warned_user]}")
        if WARNING[warned_user] >= 5:
            await app.ban_chat_member(chat_id, warned_user)
            await message.reply("کاربر به دلیل 5 اخطار از گروه اخراج شد!")
            del WARNING[warned_user]
    except Exception as e:
        await message.reply(f"مشکلی در اخطار به کاربر پیش آمد:\n {str(e)}")


WARNING = {}


@app.on_message(filters.command("Unwarn") & filters.user(OWNERS_ID))
async def unwarn(client: Client, message: Message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            if user_id in WARNING:
                WARNING[user_id] -= 1
                if WARNING[user_id] <= 0:
                    del WARNING[user_id]
                    await message.reply(f"تمام اخطارهای کاربر {user_id} حذف شد.")
                else:
                    await message.reply(f"کاربر {user_id} اکنون {WARNING[user_id]} اخطار دارد.")
            else:
                await message.reply(f"کاربر {user_id} هیچ اخطاری ندارد.")
        else:
            await message.reply("لطفاً یک کاربر را ریپلای کنید.")
    except Exception as e:
        await message.reply(f"مشکلی در حذف اخطار کاربر به وجود آمد!:\n {str(e)}")


@app.on_message(filters.command("Translate"))
async def translate(client, message):
    try:
        if len(message.command) > 1:
            word_to_translate = message.command[1]
            translation = await translator.translate(word_to_translate, src='en', dest='fa')
            response = f'کلمه "{word_to_translate}" به معنای "{translation.text}" است.'
        else:
            response = "لطفاً یک کلمه برای ترجمه وارد کنید."

        await message.reply(response)
    except Exception as e:
        await message.reply(f"مشکلی در ترجمه پیش آمد!:\n {str(e)}")


# Attacker Commands

@app.on_message(filters.command("Attack") & filters.user(OWNERS_ID))
async def attack(client, message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.username
        chat_id = message.chat.id
        attackers[chat_id] = user
        attack_active[chat_id] = True

        await message.reply("اتک  به نوامیس این یارو که گفتی شروع شد!")

        while attack_active.get(chat_id, False):
            u = random.choice(Fohsh)
            await client.send_message(chat_id, f"{u} @{user}")
            await asyncio.sleep(2)
    else:
        await message.reply("لطفاً برای حمله به یک کاربر، روی پیام اون مادرجنده ریپلای کنید.")


@app.on_message(filters.command("StopAttack") & filters.user(OWNERS_ID))
async def stop_attack(client, message):
    chat_id = message.chat.id
    if chat_id in attackers:
        attack_active[chat_id] = False
        await message.reply("اتک به ناموس این یارو متوقف شد!")
        del attackers[chat_id]
    else:
        await message.reply("❗️ هیچ حمله‌ای برای متوقف کردن وجود نداره!")


replying = False
user_id = None


@app.on_message(filters.command("Setreply") & filters.user(OWNERS_ID))
async def set_reply(client, message):
    global replying, user_id
    if replying:
        await message.reply("قفل ریپلای قبلاً روی یه کسکش مادر شروع شده.")
        return

    replying = True
    user_id = message.reply_to_message.from_user.id
    await message.reply("قفل ریپلای روی این ننه الاغ شروع شد!...")

    for i in range(20000000000000000000000000):
        if not replying:
            break
        z = random.choice(Fohsh)
        await message.reply_to_message.reply(z)
        time.sleep(2)


@app.on_message(filters.command("Stopreply") & filters.user(OWNERS_ID))
async def stop_reply(client, message):
    global replying
    replying = False
    await message.reply("قفل ریپلای متوقف شد!")


protection_list = []


@app.on_message(filters.command("Protection") & filters.user(OWNERS_ID))
async def add_to_protection(client, message):
    user_id = message.reply_to_message.from_user.id
    if user_id not in protection_list:
        protection_list.append(user_id)
        await message.reply("کاربر به لیست محافظت اضافه شد!")
    else:
        await message.reply("این کاربر قبلاً در لیست محافظت هست!")


@app.on_message(filters.command("Deleteprotection") & filters.user(OWNERS_ID))
async def remove_from_protection(client, message):
    user_id = message.reply_to_message.from_user.id
    if user_id in protection_list:
        protection_list.remove(user_id)
        await message.reply("کاربر از لیست محافظت حذف شد!")
    else:
        await message.reply("کاربر در لیست محافظت وجود ندارد!")


Fahashi = ["کسننت", "کس ننت", "کسمادرت", "کس مادرت", "ناموس", "مادرجنده", "مادر جنده", "مادر", "مامان", "خواهر", "آبجی",
           "ابجی"]


@app.on_message(filters.reply & filters.text)
async def reply_to_user(client, message):
    if message.reply_to_message.from_user.id in protection_list:
        if any(bad_word in message.text for bad_word in Fahashi):
            k = random.choice(Fohsh)
            await message.reply(f"اگه خودی نبودی و چیزی که گفتی رو با کسی که روش ریپلای کردی بودی\n{k}",
                                reply_to_message_id=message.id)


# Self Commands

enemies = []


@app.on_message(filters.group & filters.command("removeenemy") & filters.user(OWNERS_ID))
async def remove_enemy(client, message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            user_username = message.reply_to_message.from_user.username

            if user_id in enemies:
                enemies.remove(user_id)
                await message.reply(f"این یارو @{user_username} از لیست دشمنا حذف شد!")
            else:
                await message.reply(f"این یارو @{user_username} در لیست دشمنا نیست.")
    except Exception as e:
        await message.reply(f"مشکلی در حذف دشمن پیش آمد:\n {e}")


@app.on_message(filters.group & filters.command("setenemy") & filters.user(OWNERS_ID))
async def add_enemy(client, message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            user_username = message.reply_to_message.from_user.username

            if user_id not in enemies:
                enemies.append(user_id)
                await message.reply(f"این مامان کسکش @{user_username} به لیست دشمنا اضافه شد!")
            else:
                await message.reply(f"این مامان کونی @{user_username} قبلاً به لیست دشمنا اضافه شده .")
    except Exception as e:
        await message.reply(f"مشکلی در تنظیم دشمن پیش آمد:\n {e}")


@app.on_message(filters.group)
async def greet_enemy(client, message):
    try:
        if message.from_user.id in enemies:
            y = random.choice(Fohsh)
            await message.reply(y)
    except Exception as e:
        await message.reply(f"Error:\n {e}")


app.run()