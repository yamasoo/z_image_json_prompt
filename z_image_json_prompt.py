import os
import random
import time
import json
import shutil
from datetime import datetime

class ZImageJSONPrompting:
    # 定義所有選項內容（保持雙語內容）
    OPTION_DATA = {
        "scene": {
            "scene_description.txt": [
                "霓虹閃爍的賽博朋克街道 | Neon-lit cyberpunk street",
                "寧靜的日式庭院 | Tranquil Japanese garden",
                "繁忙的現代都市街頭 | Busy modern city street",
                "神秘的遠古遺跡 | Mysterious ancient ruins",
                "夢幻的童話森林 | Enchanted fairy tale forest",
                "科幻的太空站內景 | Sci-fi space station interior",
                "古典的歐洲城堡大廳 | Classical European castle hall",
                "炎熱的沙漠綠洲 | Hot desert oasis",
                "寒冷的北極冰川 | Cold arctic glacier",
                "雨後的都市夜景 | City night scene after rain",
                "霧氣瀰漫的山林小徑 | Misty mountain forest path",
                "繁華的夜市小吃街 | Bustling night market street",
                "廢棄的工業廠房 | Abandoned industrial factory",
                "未來主義的實驗室 | Futuristic laboratory",
                "熱帶海島沙灘 | Tropical island beach",
                "秋天的楓葉公園 | Autumn maple leaf park",
                "星空下的草原 | Grassland under starry sky",
                "水下珊瑚礁世界 | Underwater coral reef world",
                "蒸汽龐克風格城市 | Steampunk-style city",
                "末日後的廢墟都市 | Post-apocalyptic ruined city",
                "魔幻的空中浮島 | Magical floating island in sky",
                "傳統的中式古鎮 | Traditional Chinese ancient town",
                "現代的購物中心 | Modern shopping mall",
                "寧靜的圖書館內景 | Quiet library interior",
                "熱鬧的音樂節現場 | Lively music festival scene"
            ],
            "time_atmosphere.txt": [
                "黃金時刻的溫暖陽光 | Warm sunlight during golden hour",
                "深夜的神秘月光 | Mysterious moonlight late at night",
                "午後的柔和光線 | Soft afternoon light",
                "黎明的曙光微露 | First light of dawn",
                "黃昏的浪漫餘暉 | Romantic glow of dusk",
                "正午的強烈陽光 | Strong midday sunlight",
                "暴風雨前的壓抑氛圍 | Oppressive atmosphere before storm",
                "霧氣瀰漫的清晨 | Misty morning",
                "晴朗無雲的藍天 | Clear cloudless blue sky",
                "多雲的陰天光線 | Cloudy overcast light",
                "暴雨中的模糊景象 | Blurred scene in heavy rain",
                "薄霧籠罩的夜晚 | Thin fog shrouded night",
                "夕陽西下的剪影 | Silhouette at sunset",
                "月光如水灑落 | Moonlight shining like water",
                "清晨露珠晶瑩 | Morning dew sparkling",
                "午後雷陣雨後 | Afternoon after thunderstorm",
                "深夜街燈昏黃 | Late night street lamps dim yellow",
                "極光舞動的天空 | Aurora dancing in the sky",
                "煙火綻放的夜晚 | Fireworks blooming night",
                "燭光搖曳的室內 | Candlelight flickering indoors",
                "霓虹燈閃爍的雨夜 | Neon lights flickering on rainy night",
                "日出時分的寧靜 | Peaceful at sunrise",
                "日落時分的溫暖 | Warm at sunset",
                "午夜的神秘時刻 | Mysterious midnight moment",
                "午夜的寂靜時刻 | Silent midnight moment"
            ],
            "environment_setting.txt": [
                "潮濕的街道反射燈光 | Wet streets reflecting lights",
                "乾燥的沙漠風吹沙粒 | Dry desert with blowing sand",
                "綠意盎然的自然環境 | Lush green natural environment",
                "鋼筋混凝土的都市叢林 | Concrete jungle of the city",
                "水晶般清澈的水下世界 | Crystal clear underwater world",
                "煙霧繚繞的神秘空間 | Smoke-filled mysterious space",
                "積雪覆蓋的冬日景觀 | Snow-covered winter landscape",
                "落葉繽紛的秋季公園 | Autumn park with falling leaves",
                "花卉盛開的春季花園 | Spring garden in full bloom",
                "高科技的未來實驗室 | High-tech futuristic laboratory",
                "藤蔓纏繞的古老建築 | Vine-covered ancient building",
                "玻璃幕牆的現代大樓 | Glass curtain wall modern building",
                "鵝卵石鋪成的古老街道 | Cobblestone ancient street",
                "金屬結構的工業廠房 | Metal structured industrial factory",
                "雲端之上的高樓頂部 | Top of skyscraper above clouds",
                "地下洞穴的神秘空間 | Mysterious underground cave",
                "廢棄車輛堆積的場地 | Abandoned vehicle scrap yard",
                "鮮花裝飾的婚禮現場 | Flower-decorated wedding venue",
                "書籍堆積的古老書房 | Book-filled ancient study",
                "科技感十足的指揮中心 | High-tech command center",
                "原始自然的叢林深處 | Deep in primitive jungle",
                "繁忙的交通十字路口 | Busy traffic intersection",
                "寧靜的湖畔小屋旁 | By peaceful lakeside cabin",
                "擁擠的地鐵站內部 | Crowded subway station interior",
                "開闊的山頂觀景台 | Open mountaintop viewing platform"
            ]
        },
        "subject": {
            "character_features.txt": [
                "年輕的亞洲男性 | Young Asian male",
                "優雅的歐洲女性 | Elegant European female",
                "中年的非裔商人 | Middle-aged African businessman",
                "年長的智者形象 | Elderly wise figure",
                "活潑的拉丁裔青年 | Lively Latino youth",
                "神秘的蒙面人物 | Mysterious masked figure",
                "強壯的運動員體格 | Strong athletic build",
                "纖細的舞者身材 | Slender dancer's physique",
                "華麗的奇幻種族 | Lavish fantasy race",
                "簡約的現代上班族 | Minimalist modern office worker",
                "可愛的兒童形象 | Cute child figure",
                "性感的模特兒身材 | Sexy model physique",
                "威武的軍人形象 | Majestic soldier figure",
                "慈祥的老奶奶 | Kindly old grandmother",
                "叛逆的青少年 | Rebellious teenager",
                "自信的企業家 | Confident entrepreneur",
                "害羞的學生 | Shy student",
                "狂野的搖滾樂手 | Wild rock musician",
                "優雅的芭蕾舞者 | Graceful ballet dancer",
                "強悍的武術家 | Tough martial artist",
                "神秘的巫師 | Mysterious wizard",
                "帥氣的機車騎士 | Handsome motorcycle rider",
                "美麗的精靈族 | Beautiful elf race",
                "強壯的半獸人 | Strong orc race",
                "可愛的獸人族 | Cute beast race"
            ],
            "clothing_style.txt": [
                "黑色皮夾克配牛仔褲 | Black leather jacket with jeans",
                "優雅的晚禮服長裙 | Elegant evening gown",
                "實用的戶外探險裝備 | Practical outdoor exploration gear",
                "傳統的民族服飾 | Traditional ethnic clothing",
                "未來的科技感服裝 | Futuristic tech-style clothing",
                "休閒的運動服套裝 | Casual sportswear set",
                "正式的西裝領帶 | Formal suit and tie",
                "奇幻的魔法師長袍 | Fantasy mage robe",
                "復古的搖滾風格 | Retro rock style",
                "極簡的單色搭配 | Minimalist monochrome outfit",
                "華麗的宮廷禮服 | Lavish court dress",
                "破舊的流浪者服裝 | Tattered流浪者clothing",
                "專業的廚師制服 | Professional chef uniform",
                "性感的比基尼泳裝 | Sexy bikini swimwear",
                "溫暖的冬季大衣 | Warm winter coat",
                "輕便的夏日洋裝 | Light summer dress",
                "軍裝風格外套 | Military style jacket",
                "學生制服 | School uniform",
                "婚紗禮服 | Wedding dress",
                "睡衣家居服 | Pajamas homewear",
                "皮革盔甲裝備 | Leather armor equipment",
                "科幻太空服 | Sci-fi spacesuit",
                "傳統和服 | Traditional kimono",
                "印度紗麗 | Indian sari",
                "阿拉伯長袍 | Arabic thobe"
            ],
            "pose_expression.txt": [
                "站立微笑看向鏡頭 | Standing smiling at camera",
                "坐姿沉思看向遠方 | Sitting contemplating into distance",
                "奔跑中的動態姿勢 | Dynamic pose while running",
                "跳躍的瞬間捕捉 | Mid-jump moment captured",
                "倚靠物體的放鬆姿勢 | Relaxed pose leaning on object",
                "戰鬥準備的緊張姿態 | Tense combat-ready stance",
                "舞蹈中的優雅動作 | Elegant movement while dancing",
                "工作中的專注神情 | Focused expression while working",
                "驚訝的自然反應 | Natural surprised reaction",
                "憤怒的強烈情緒表達 | Strong expression of anger",
                "悲傷的低頭姿勢 | Sad低头pose",
                "快樂的跳躍姿勢 | Happy jumping pose",
                "思考的托腮動作 | Thinking with chin in hand",
                "指揮的專注神情 | Conducting with专注expression",
                "閱讀的安靜姿態 | Quiet reading posture",
                "演奏樂器的投入表情 | Engaged expression playing instrument",
                "繪畫的創作姿勢 | Creative painting posture",
                "瑜伽的伸展動作 | Yoga stretching pose",
                "親吻的浪漫時刻 | Romantic kissing moment",
                "擁抱的溫暖姿勢 | Warm hugging pose",
                "指向前方的動作 | Pointing forward动作",
                "揮手打招呼 | Waving hello",
                "跪下的虔誠姿態 | Kneeling虔诚posture",
                "躺下的放鬆姿勢 | Lying down relaxed pose",
                "飛翔的幻想姿勢 | Flying fantasy pose"
            ]
        },
        "photography": {
            "lens_parameters.txt": [
                "35mm f/1.4 廣角鏡頭 | 35mm f/1.4 wide-angle lens",
                "85mm f/1.8 人像鏡頭 | 85mm f/1.8 portrait lens",
                "24-70mm f/2.8 變焦鏡頭 | 24-70mm f/2.8 zoom lens",
                "50mm f/1.2 標準鏡頭 | 50mm f/1.2 standard lens",
                "135mm f/2.0 長焦鏡頭 | 135mm f/2.0 telephoto lens",
                "16-35mm f/4.0 超廣角 | 16-35mm f/4.0 ultra-wide angle",
                "70-200mm f/2.8 遠攝鏡頭 | 70-200mm f/2.8 telephoto zoom",
                "微距鏡頭 f/2.8 | Macro lens f/2.8",
                "魚眼鏡頭 8mm f/3.5 | Fisheye lens 8mm f/3.5",
                "移軸鏡頭 45mm f/2.8 | Tilt-shift lens 45mm f/2.8",
                "24mm f/1.4 超廣角大光圈 | 24mm f/1.4 ultra-wide aperture",
                "200mm f/2.0 長焦大光圈 | 200mm f/2.0 telephoto大光圈",
                "14mm f/2.8 超廣角鏡頭 | 14mm f/2.8 ultra-wide lens",
                "400mm f/2.8 超長焦鏡頭 | 400mm f/2.8 super telephoto",
                "50mm f/0.95 超大光圈 | 50mm f/0.95超大光圈",
                "100mm f/2.8 微距鏡頭 | 100mm f/2.8 macro lens",
                "28-75mm f/2.8 標準變焦 | 28-75mm f/2.8 standard zoom",
                "150-600mm f/5-6.3 超長變焦 | 150-600mm f/5-6.3 super zoom",
                "20mm f/1.8 廣角大光圈 | 20mm f/1.8 wide-angle大光圈",
                "300mm f/4.0 長焦定焦 | 300mm f/4.0 telephoto prime",
                "10-20mm f/4.5-5.6 超廣變焦 | 10-20mm f/4.5-5.6 ultra-wide zoom",
                "58mm f/1.2 特殊標準鏡 | 58mm f/1.2 special standard lens",
                "180mm f/3.5 微距鏡頭 | 180mm f/3.5 macro lens",
                "8-15mm f/4.0 魚眼變焦 | 8-15mm f/4.0 fisheye zoom",
                "600mm f/4.0 超長焦定焦 | 600mm f/4.0 super telephoto prime"
            ],
            "shooting_angle.txt": [
                "低角度仰拍 | Low angle looking up",
                "高角度俯拍 | High angle looking down",
                "水平視角 | Eye-level perspective",
                "鳥瞰視角 | Bird's-eye view",
                "蟲視角 | Worm's-eye view",
                "傾斜的荷蘭角 | Dutch angle tilt",
                "過肩拍攝角度 | Over-the-shoulder angle",
                "正面特寫角度 | Front close-up angle",
                "側面輪廓角度 | Side profile angle",
                "第一人稱視角 | First-person perspective",
                "微距特寫角度 | Macro close-up angle",
                "廣角全景視角 | Wide-angle panoramic view",
                "長焦壓縮視角 | Telephoto compressed perspective",
                "運動跟拍視角 | Motion tracking shot",
                "滑軌移動視角 | Slider moving perspective",
                "升降鏡頭視角 | Crane shot perspective",
                "搖臂鏡頭視角 | Jib arm shot perspective",
                "手持晃動視角 | Handheld shaky perspective",
                "航拍空中視角 | Aerial drone perspective",
                "水下拍攝視角 | Underwater shooting perspective",
                "窺視視角 | Peeking perspective",
                "反射鏡面視角 | Reflective mirror perspective",
                "框架構圖視角 | Framed composition perspective",
                "傾斜地平線視角 | Tilted horizon perspective",
                "極低角度視角 | Extreme low angle perspective"
            ],
            "film_style.txt": [
                "富士 Velvia 鮮豔色彩 | Fuji Velvia vivid colors",
                "柯達 Portra 柔和膚色 | Kodak Portra soft skin tones",
                "黑白 Tri-X 高對比 | Black & white Tri-X high contrast",
                "電影膠片 5219 電影感 | Motion picture film 5219 cinematic look",
                "復古 Polaroid 即時顯影 | Vintage Polaroid instant film",
                "過期膠片 懷舊色彩 | Expired film nostalgic colors",
                "Ektachrome 幻燈片風格 | Ektachrome slide film style",
                "Cinestill 800T 電影夜拍 | Cinestill 800T cinematic night",
                "Ilford HP5 黑白顆粒 | Ilford HP5 black & white grain",
                "Provia 100F 自然色彩 | Provia 100F natural colors",
                "柯達 Gold 200 溫暖色調 | Kodak Gold 200 warm tones",
                "富士 Pro 400H 柔和對比 | Fuji Pro 400H soft contrast",
                "柯達 Ektar 100 鮮豔飽和 | Kodak Ektar 100 vibrant saturation",
                "黑白 Ilford Delta 3200 高感光 | B&W Ilford Delta 3200 high ISO",
                "電影膠片 500T tungsten平衡 | Movie film 500T tungsten balance",
                "富士 Superia 400 日常色彩 | Fuji Superia 400日常colors",
                "柯達 T-Max 100 細膩顆粒 | Kodak T-Max 100 fine grain",
                "復古 Agfa Vista 鮮明色彩 | Vintage Agfa Vista鲜明colors",
                "電影膠片 250D 日光平衡 | Movie film 250D daylight balance",
                "黑白 Rollei Retro 特殊色調 | B&W Rollei Retro special tones",
                "富士 Natura 1600 高感光 | Fuji Natura 1600 high ISO",
                "柯達 ColorPlus 200 經濟型 | Kodak ColorPlus 200 economical",
                "電影膠片 50D 細膩畫質 | Movie film 50D fine quality",
                "黑白 Fomapan 400 經典顆粒 | B&W Fomapan 400 classic grain",
                "富士 Acros 100II 黑白細膩 | Fuji Acros 100II B&W fine detail"
            ]
        },
        "lighting": {
            "light_source_type.txt": [
                "自然日光 | Natural daylight",
                "月光與星光 | Moonlight and starlight",
                "霓虹燈光 | Neon lights",
                "燭光與火光 | Candlelight and firelight",
                "LED燈帶光線 | LED strip lighting",
                "熒光燈管照明 | Fluorescent tube lighting",
                "鎢絲燈溫暖光 | Tungsten warm lighting",
                "RGB彩色燈光 | RGB colored lighting",
                "聚光燈效果 | Spotlight effect",
                "柔光箱擴散光 | Softbox diffused light",
                "窗戶自然光 | Window natural light",
                "車燈光線 | Car headlights",
                "手機螢幕光 | Smartphone screen light",
                "電視螢幕光 | TV screen light",
                "電腦螢幕光 | Computer monitor light",
                "路燈照明 | Street lamp lighting",
                "舞台燈光 | Stage lighting",
                "攝影棚閃光燈 | Studio strobe lighting",
                "手電筒光束 | Flashlight beam",
                "投影機光線 | Projector light",
                "激光光束 | Laser beam",
                "螢光棒光線 | Glow stick light",
                "油燈光線 | Oil lamp light",
                "煤氣燈光 | Gas lamp light",
                "LED大屏幕光 | LED big screen light"
            ],
            "light_effect.txt": [
                "柔和的擴散光線 | Soft diffused lighting",
                "強烈的直射光線 | Strong direct lighting",
                "戲劇性的側光 | Dramatic side lighting",
                "神秘的逆光效果 | Mysterious backlighting",
                "均勻的正面光 | Even front lighting",
                "創意的輪廓光 | Creative rim lighting",
                "自然的光線衰減 | Natural light falloff",
                "動態的光影變化 | Dynamic light and shadow play",
                "反射的間接光線 | Reflected indirect lighting",
                "多光源混合照明 | Mixed multi-source lighting",
                "漸變過渡光效 | Gradient transition lighting",
                "斑駁的光影效果 | Dappled light and shadow",
                "強烈的對比光影 | Strong contrast light and shadow",
                "柔和的過渡陰影 | Soft transitional shadows",
                "硬朗的清晰陰影 | Hard clear shadows",
                "霧氣中的漫射光 | Diffused light in fog",
                "水面的反射光 | Reflective light on water",
                "玻璃的折射光 | Refracted light through glass",
                "金屬的反光效果 | Metallic reflective effect",
                "皮膚的次表面散射 | Skin subsurface scattering",
                "頭髮的邊緣光 | Hair rim light",
                "眼睛的反射光 | Eye reflection light",
                "衣服的材質光感 | Clothing material lighting",
                "環境的全局照明 | Environmental global illumination",
                "體積光的上帝光 | Volumetric god rays"
            ],
            "contrast_level.txt": [
                "高對比強光影 | High contrast with strong shadows",
                "低對比柔和過渡 | Low contrast with soft transitions",
                "中等對比平衡 | Medium contrast balanced",
                "極高對比黑白 | Extreme contrast black and white",
                "細膩的微對比 | Subtle micro-contrast",
                "動態範圍廣 | Wide dynamic range",
                "壓縮的暗部細節 | Compressed shadow details",
                "保留亮部細節 | Preserved highlight details",
                "S曲線對比調整 | S-curve contrast adjustment",
                "自然對比還原 | Natural contrast reproduction",
                "柔和的低對比 | Soft low contrast",
                "鮮明的中高對比 | Distinct medium-high contrast",
                "強烈的戲劇對比 | Strong dramatic contrast",
                "細膩的高光過渡 | Subtle highlight transition",
                "深沉的陰影層次 | Deep shadow gradation",
                "明亮的整體調性 | Bright overall tonality",
                "暗調的氛圍感 | Dark tone atmosphere",
                "中灰色調平衡 | Medium gray tone balance",
                "高動態範圍保留 | High dynamic range preservation",
                "膠片曲線對比 | Film curve contrast",
                "數位平面對比 | Digital flat contrast",
                "電影風格對比 | Cinematic style contrast",
                "復古褪色對比 | Vintage faded contrast",
                "清新通透對比 | Fresh transparent contrast",
                "厚重質感對比 | Heavy texture contrast"
            ]
        },
        "style": {
            "art_style.txt": [
                "賽博朋克風格 | Cyberpunk style",
                "蒸汽龐克風格 | Steampunk style",
                "奇幻藝術風格 | Fantasy art style",
                "超現實主義 | Surrealism style",
                "極簡主義風格 | Minimalist style",
                "印象派風格 | Impressionist style",
                "寫實主義風格 | Realism style",
                "卡通動畫風格 | Cartoon animation style",
                "油畫藝術風格 | Oil painting style",
                "水彩藝術風格 | Watercolor style",
                "像素藝術風格 | Pixel art style",
                "塗鴉藝術風格 | Graffiti art style",
                "復古插畫風格 | Retro illustration style",
                "科幻未來風格 | Sci-fi futuristic style",
                "恐怖驚悚風格 | Horror thriller style",
                "浪漫唯美風格 | Romantic aesthetic style",
                "抽象藝術風格 | Abstract art style",
                "概念藝術風格 | Concept art style",
                "日式動漫風格 | Japanese anime style",
                "美式漫畫風格 | American comic style",
                "迪士尼動畫風格 | Disney animation style",
                "吉卜力動畫風格 | Ghibli animation style",
                "新藝術運動風格 | Art Nouveau style",
                "裝飾藝術風格 | Art Deco style",
                "巴洛克藝術風格 | Baroque art style"
            ],
            "color_scheme.txt": [
                "青橙配色方案 | Teal and orange color scheme",
                "霓虹色彩搭配 | Neon color palette",
                "單色調配方案 | Monochromatic color scheme",
                "柔和粉彩色調 | Soft pastel colors",
                "鮮豔飽和色彩 | Vibrant saturated colors",
                "復古褪色色彩 | Vintage faded colors",
                "黑白高對比 | Black and white high contrast",
                "冷暖色調對比 | Warm and cool color contrast",
                "金屬色系搭配 | Metallic color palette",
                "自然大地色調 | Natural earth tones",
                "糖果色系搭配 | Candy color palette",
                "莫蘭迪色系 | Morandi color palette",
                "馬卡龍色系 | Macaron color palette",
                "賽博朋克色系 | Cyberpunk color scheme",
                "蒸汽龐克色系 | Steampunk color scheme",
                "奇幻魔法色系 | Fantasy magic color scheme",
                "科幻未來色系 | Sci-fi futuristic color scheme",
                "恐怖暗黑色系 | Horror dark color scheme",
                "浪漫粉色系 | Romantic pink color scheme",
                "清新藍綠色系 | Fresh aqua color scheme",
                "溫暖橙黃色系 | Warm orange-yellow color scheme",
                "冷靜藍紫色系 | Cool blue-purple color scheme",
                "自然綠色系 | Natural green color scheme",
                "奢華金黑色系 | Luxury gold-black color scheme",
                "復古褐黃色系 | Vintage sepia color scheme"
            ],
            "render_effects.txt": [
                "全局照明效果 | Global illumination effect",
                "景深模糊效果 | Depth of field blur effect",
                "動態模糊效果 | Motion blur effect",
                "體積霧效果 | Volumetric fog effect",
                "鏡頭光暈效果 | Lens flare effect",
                "色差效果 | Chromatic aberration effect",
                "電影顆粒效果 | Cinematic film grain",
                "光線追蹤反射 | Ray-traced reflections",
                "次表面散射 | Subsurface scattering",
                "環境光遮蔽 | Ambient occlusion",
                "運動模糊效果 | Motion blur effect",
                "散景效果 | Bokeh effect",
                "眩光效果 | Glare effect",
                "漏光效果 | Light leak effect",
                "暗角效果 | Vignetting effect",
                "銳化效果 | Sharpening effect",
                "模糊效果 | Blur effect",
                "馬賽克效果 | Mosaic effect",
                "像素化效果 | Pixelation effect",
                "故障藝術效果 | Glitch art effect",
                "雙重曝光效果 | Double exposure effect",
                "HDR效果 | HDR effect",
                "漫畫網點效果 | Comic halftone effect",
                "素描線條效果 | Sketch line effect",
                "水墨渲染效果 | Ink wash rendering effect"
            ]
        }
    }
    
    # 預設模板資料
    DEFAULT_TEMPLATES = {
        "cyberpunk": {
            "name": "賽博朋克 | Cyberpunk",
            "fields": {
                "scene_description": "霓虹閃爍的賽博朋克街道 | Neon-lit cyberpunk street",
                "time_atmosphere": "深夜的神秘月光 | Mysterious moonlight late at night",
                "color_scheme": "青橙配色方案 | Teal and orange color scheme",
                "art_style": "賽博朋克風格 | Cyberpunk style",
                "light_source_type": "霓虹燈光 | Neon lights",
                "render_effects": "鏡頭光暈效果 | Lens flare effect"
            }
        },
        "fantasy_magic": {
            "name": "奇幻魔法 | Fantasy Magic",
            "fields": {
                "scene_description": "夢幻的童話森林 | Enchanted fairy tale forest",
                "time_atmosphere": "霧氣瀰漫的清晨 | Misty morning",
                "color_scheme": "柔和粉彩色調 | Soft pastel colors",
                "art_style": "奇幻藝術風格 | Fantasy art style",
                "light_source_type": "自然日光 | Natural daylight",
                "render_effects": "體積霧效果 | Volumetric fog effect"
            }
        },
        "sci_fi_futuristic": {
            "name": "科幻未來 | Sci-fi Futuristic",
            "fields": {
                "scene_description": "科幻的太空站內景 | Sci-fi space station interior",
                "time_atmosphere": "多雲的陰天光線 | Cloudy overcast light",
                "color_scheme": "金屬色系搭配 | Metallic color palette",
                "art_style": "科幻未來風格 | Sci-fi futuristic style",
                "light_source_type": "LED燈帶光線 | LED strip lighting",
                "render_effects": "光線追蹤反射 | Ray-traced reflections"
            }
        },
        "retro_vintage": {
            "name": "復古懷舊 | Retro Vintage",
            "fields": {
                "scene_description": "古典的歐洲城堡大廳 | Classical European castle hall",
                "time_atmosphere": "黃金時刻的溫暖陽光 | Warm sunlight during golden hour",
                "color_scheme": "復古褪色色彩 | Vintage faded colors",
                "art_style": "復古插畫風格 | Retro illustration style",
                "light_source_type": "燭光與火光 | Candlelight and firelight",
                "render_effects": "電影顆粒效果 | Cinematic film grain"
            }
        },
        "natural_realism": {
            "name": "自然寫實 | Natural Realism",
            "fields": {
                "scene_description": "綠意盎然的自然環境 | Lush green natural environment",
                "time_atmosphere": "午後的柔和光線 | Soft afternoon light",
                "color_scheme": "自然大地色調 | Natural earth tones",
                "art_style": "寫實主義風格 | Realism style",
                "light_source_type": "自然日光 | Natural daylight",
                "render_effects": "全局照明效果 | Global illumination effect"
            }
        },
        "minimalism": {
            "name": "極簡主義 | Minimalism",
            "fields": {
                "scene_description": "簡約的現代室內空間 | Minimalist modern interior",
                "time_atmosphere": "均勻的正面光 | Even front lighting",
                "color_scheme": "單色調配方案 | Monochromatic color scheme",
                "art_style": "極簡主義風格 | Minimalist style",
                "light_source_type": "柔光箱擴散光 | Softbox diffused light",
                "render_effects": "環境光遮蔽 | Ambient occlusion"
            }
        },
        "cinematic_portrait": {
            "name": "電影人像 | Cinematic Portrait",
            "fields": {
                "scene_description": "戲劇性的室內場景 | Dramatic indoor scene",
                "time_atmosphere": "戲劇性的側光 | Dramatic side lighting",
                "color_scheme": "冷暖色調對比 | Warm and cool color contrast",
                "art_style": "電影風格 | Cinematic style",
                "light_source_type": "聚光燈效果 | Spotlight effect",
                "render_effects": "景深模糊效果 | Depth of field blur effect"
            }
        },
        "street_fashion": {
            "name": "街頭潮流 | Street Fashion",
            "fields": {
                "scene_description": "繁忙的現代都市街頭 | Busy modern city street",
                "time_atmosphere": "雨後的都市夜景 | City night scene after rain",
                "color_scheme": "霓虹色彩搭配 | Neon color palette",
                "art_style": "塗鴉藝術風格 | Graffiti art style",
                "light_source_type": "RGB彩色燈光 | RGB colored lighting",
                "render_effects": "動態模糊效果 | Motion blur effect"
            }
        },
        "anime_manga": {
            "name": "日式動漫 | Anime Manga",
            "fields": {
                "scene_description": "精緻的日式動漫場景 | Exquisite anime manga scene",
                "time_atmosphere": "晴朗無雲的藍天 | Clear cloudless blue sky",
                "color_scheme": "鮮豔飽和色彩 | Vibrant saturated colors",
                "art_style": "日式動漫風格 | Japanese anime style",
                "light_source_type": "自然日光 | Natural daylight",
                "render_effects": "卡通動畫效果 | Cartoon animation effect"
            }
        },
        "steampunk": {
            "name": "蒸汽龐克 | Steampunk",
            "fields": {
                "scene_description": "蒸汽龐克風格城市 | Steampunk-style city",
                "time_atmosphere": "薄霧籠罩的夜晚 | Thin fog shrouded night",
                "color_scheme": "復古褐黃色系 | Vintage sepia color scheme",
                "art_style": "蒸汽龐克風格 | Steampunk style",
                "light_source_type": "煤氣燈光 | Gas lamp light",
                "render_effects": "電影顆粒效果 | Cinematic film grain"
            }
        },
        "horror_thriller": {
            "name": "恐怖驚悚 | Horror Thriller",
            "fields": {
                "scene_description": "廢棄的工業廠房 | Abandoned industrial factory",
                "time_atmosphere": "暴風雨前的壓抑氛圍 | Oppressive atmosphere before storm",
                "color_scheme": "恐怖暗黑色系 | Horror dark color scheme",
                "art_style": "恐怖驚悚風格 | Horror thriller style",
                "light_source_type": "手電筒光束 | Flashlight beam",
                "render_effects": "暗角效果 | Vignetting effect"
            }
        },
        "romantic_aesthetic": {
            "name": "浪漫唯美 | Romantic Aesthetic",
            "fields": {
                "scene_description": "花卉盛開的春季花園 | Spring garden in full bloom",
                "time_atmosphere": "黃昏的浪漫餘暉 | Romantic glow of dusk",
                "color_scheme": "浪漫粉色系 | Romantic pink color scheme",
                "art_style": "浪漫唯美風格 | Romantic aesthetic style",
                "light_source_type": "燭光與火光 | Candlelight and firelight",
                "render_effects": "柔光效果 | Soft light effect"
            }
        },
        "watercolor_art": {
            "name": "水彩藝術 | Watercolor Art",
            "fields": {
                "scene_description": "夢幻的水彩畫風格場景 | Dreamy watercolor art scene",
                "time_atmosphere": "霧氣瀰漫的清晨 | Misty morning",
                "color_scheme": "柔和粉彩色調 | Soft pastel colors",
                "art_style": "水彩藝術風格 | Watercolor style",
                "light_source_type": "自然日光 | Natural daylight",
                "render_effects": "水墨渲染效果 | Ink wash rendering effect"
            }
        }
    }

    @classmethod
    def initialize_options_dir(cls):
        """初始化選項目錄和檔案"""
        options_dir = os.path.join(os.path.dirname(__file__), "z_image_options")
        
        # 如果目錄不存在，創建它
        if not os.path.exists(options_dir):
            os.makedirs(options_dir)
            print(f"[Z-Image] 已創建選項目錄: {options_dir}")
        
        # 創建分組子目錄（使用英文名稱）
        for group in cls.OPTION_DATA.keys():
            group_dir = os.path.join(options_dir, group)
            if not os.path.exists(group_dir):
                os.makedirs(group_dir)
                print(f"[Z-Image] 已創建分組目錄: {group_dir}")
        
        # 初始化所有選項檔案
        for group_name, files in cls.OPTION_DATA.items():
            group_dir = os.path.join(options_dir, group_name)
            for file_name, content_list in files.items():
                file_path = os.path.join(group_dir, file_name)
                
                # 如果檔案不存在，創建它
                if not os.path.exists(file_path):
                    try:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            # 寫入選項，每個選項佔一行
                            for item in content_list:
                                f.write(item + "\n")
                        print(f"[Z-Image] 已創建設定檔: {group_name}/{file_name}")
                    except Exception as e:
                        print(f"[Z-Image] 創建設定檔失敗 {group_name}/{file_name}: {str(e)}")
                else:
                    # 如果檔案存在，檢查是否需要更新
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            existing_lines = [line.strip() for line in f if line.strip()]
                        
                        # 如果檔案內容太少，可能是舊版本，重新寫入
                        if len(existing_lines) < len(content_list) / 2:
                            with open(file_path, 'w', encoding='utf-8') as f:
                                for item in content_list:
                                    f.write(item + "\n")
                            print(f"[Z-Image] 已更新設定檔: {group_name}/{file_name}")
                    except Exception as e:
                        print(f"[Z-Image] 讀取設定檔失敗 {group_name}/{file_name}: {str(e)}")
        
        # 創建模板目錄和檔案
        templates_dir = os.path.join(options_dir, "templates")
        if not os.path.exists(templates_dir):
            os.makedirs(templates_dir)
            print(f"[Z-Image] 已創建模板目錄: {templates_dir}")
        
        # 初始化模板檔案
        for template_id, template_data in cls.DEFAULT_TEMPLATES.items():
            template_file = os.path.join(templates_dir, f"{template_id}.json")
            if not os.path.exists(template_file):
                try:
                    with open(template_file, 'w', encoding='utf-8') as f:
                        json.dump(template_data, f, ensure_ascii=False, indent=2)
                    print(f"[Z-Image] 已創建模板檔案: templates/{template_id}.json")
                except Exception as e:
                    print(f"[Z-Image] 創建模板檔案失敗 {template_id}.json: {str(e)}")

    @classmethod
    def load_templates(cls):
        """載入所有模板"""
        templates_dir = os.path.join(os.path.dirname(__file__), "z_image_options", "templates")
        
        if not os.path.exists(templates_dir):
            # 如果模板目錄不存在，使用預設模板
            return cls.DEFAULT_TEMPLATES
        
        templates = {}
        try:
            # 掃描模板目錄中的所有 JSON 檔案
            for file_name in os.listdir(templates_dir):
                if file_name.endswith('.json'):
                    template_id = file_name[:-5]  # 移除 .json 擴展名
                    template_path = os.path.join(templates_dir, file_name)
                    
                    try:
                        with open(template_path, 'r', encoding='utf-8') as f:
                            template_data = json.load(f)
                        
                        # 確保模板有基本結構
                        if 'name' in template_data and 'fields' in template_data:
                            templates[template_id] = template_data
                        else:
                            print(f"[Z-Image] 模板檔案格式錯誤: {file_name}")
                    except Exception as e:
                        print(f"[Z-Image] 載入模板失敗 {file_name}: {str(e)}")
        except Exception as e:
            print(f"[Z-Image] 掃描模板目錄失敗: {str(e)}")
        
        # 如果沒有載入到模板，使用預設模板
        if not templates:
            templates = cls.DEFAULT_TEMPLATES
        
        return templates

    @classmethod
    def INPUT_TYPES(cls):
        # 初始化選項目錄和檔案
        cls.initialize_options_dir()
        
        # 載入模板
        templates = cls.load_templates()
        
        # 生成模板選項列表
        template_options = ["無模板 | No Template"]
        for template_id, template_data in templates.items():
            template_name = template_data.get('name', template_id)
            template_options.append(f"{template_name} | {template_id}")
        
        options_dir = os.path.join(os.path.dirname(__file__), "z_image_options")
        
        # 動態生成輸入類型，使用分組前綴
        input_types = {}
        
        # 定義分組映射（使用中文前綴顯示，英文檔案名稱）
        field_mapping = [
            # 【場景】組
            ("【場景】_場景描述", "scene", "scene_description.txt"),
            ("【場景】_時間氛圍", "scene", "time_atmosphere.txt"),
            ("【場景】_環境設定", "scene", "environment_setting.txt"),
            
            # 【主體】組
            ("【主體】_人物特徵", "subject", "character_features.txt"),
            ("【主體】_服裝造型", "subject", "clothing_style.txt"),
            ("【主體】_姿勢表情", "subject", "pose_expression.txt"),
            
            # 【攝影】組
            ("【攝影】_鏡頭參數", "photography", "lens_parameters.txt"),
            ("【攝影】_拍攝角度", "photography", "shooting_angle.txt"),
            ("【攝影】_膠片風格", "photography", "film_style.txt"),
            
            # 【燈光】組
            ("【燈光】_光源類型", "lighting", "light_source_type.txt"),
            ("【燈光】_光效描述", "lighting", "light_effect.txt"),
            ("【燈光】_對比層次", "lighting", "contrast_level.txt"),
            
            # 【風格】組
            ("【風格】_藝術風格", "style", "art_style.txt"),
            ("【風格】_色彩方案", "style", "color_scheme.txt"),
            ("【風格】_渲染效果", "style", "render_effects.txt"),
        ]
        
        # 為每個字段創建選項列表
        for field_name, group, file_name in field_mapping:
            file_path = os.path.join(options_dir, group, file_name)
            options = ["隨機 | Random", "無 | None"]
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # 讀取所有非空行
                    lines = [line.strip() for line in f if line.strip()]
                    options.extend(lines)
            except Exception as e:
                print(f"[Z-Image] 警告: 無法從 {file_path} 載入選項: {e}")
                # 使用記憶體中的選項作為備份
                if group in cls.OPTION_DATA and file_name in cls.OPTION_DATA[group]:
                    options.extend(cls.OPTION_DATA[group][file_name])
            
            input_types[field_name] = (options, {"default": "隨機 | Random"})
        
        # 添加語言選擇參數
        input_types["language_choice"] = (["中文", "English", "雙語 | Bilingual"], {"default": "雙語 | Bilingual"})
        
        # 添加風格模板選擇
        input_types["style_template"] = (template_options, {"default": "無模板 | No Template"})
        
        # 添加質量控制參數
        input_types["detail_level"] = (["簡略 | Simple", "標準 | Standard", "詳細 | Detailed", "極度詳細 | Extremely Detailed"], 
                                   {"default": "標準 | Standard"})
        
        # 添加負面提示
        input_types["negative_prompt"] = ("STRING", {
            "default": "低質量 | Low quality, 模糊 | Blurry, 變形 | Deformed, 解剖錯誤 | Bad anatomy, 多餘肢體 | Extra limbs, 水印 | Watermark, 簽名 | Signature",
            "multiline": True
        })

        return {"required": input_types}

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("json_prompt", "positive_text", "negative_prompt")
    FUNCTION = "generate_json_prompt"
    CATEGORY = "Z-Image"

    def generate_json_prompt(self, **kwargs):
        # 確保選項目錄和檔案存在
        self.initialize_options_dir()
        
        # 載入模板
        templates = self.load_templates()
        
        # 提取所有輸入參數
        language_choice = kwargs.get("language_choice", "雙語 | Bilingual")
        style_template = kwargs.get("style_template", "無模板 | No Template")
        detail_level = kwargs.get("detail_level", "標準 | Standard")
        negative_prompt = kwargs.get("negative_prompt", "")
        
        # 從模板名稱中提取模板ID
        selected_template_id = None
        for template_id, template_data in templates.items():
            template_name = template_data.get('name', template_id)
            if style_template.startswith(template_name) or template_id in style_template:
                selected_template_id = template_id
                break
        
        # 定義字段映射（去掉前綴的字段名）
        field_keys = [
            "scene_description", "time_atmosphere", "environment_setting",
            "character_features", "clothing_style", "pose_expression",
            "lens_parameters", "shooting_angle", "film_style",
            "light_source_type", "light_effect", "contrast_level",
            "art_style", "color_scheme", "render_effects"
        ]
        
        # 處理所有輸入字段
        fields = {}
        for key in field_keys:
            # 將key轉換為中文顯示名稱以匹配輸入參數
            chinese_name = self._get_chinese_field_name(key)
            prefixed_key = f"【{self._get_group_chinese(key)}】_{chinese_name}"
            value = kwargs.get(prefixed_key, "隨機 | Random")
            fields[key] = self._process_field_value(key, value, language_choice)
        
        # 應用風格模板
        if selected_template_id and selected_template_id in templates:
            fields = self._apply_style_template(fields, selected_template_id, templates, language_choice)
        
        # 根據細節等級調整
        fields = self._adjust_detail_level(fields, detail_level, language_choice)
        
        # 構建詳細的 JSON 結構
        json_data = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "generator": "Z-Image JSON Prompt Generator v3.0",
                "language": language_choice,
                "style_template": selected_template_id if selected_template_id else "none",
                "detail_level": detail_level
            },
            
            "scene_settings": {
                "description": fields["scene_description"],
                "time_atmosphere": fields["time_atmosphere"],
                "environment": fields["environment_setting"]
            },
            
            "subject_description": {
                "character": fields["character_features"],
                "clothing": fields["clothing_style"],
                "pose_expression": fields["pose_expression"]
            },
            
            "photography_technique": {
                "lens": fields["lens_parameters"],
                "angle": fields["shooting_angle"],
                "film_style": fields["film_style"]
            },
            
            "lighting_effects": {
                "light_source": fields["light_source_type"],
                "effect": fields["light_effect"],
                "contrast": fields["contrast_level"]
            },
            
            "style_rendering": {
                "art_style": fields["art_style"],
                "color_scheme": fields["color_scheme"],
                "render_effects": fields["render_effects"],
                "negative_guidance": self._process_language(negative_prompt, language_choice)
            }
        }

        # 生成 JSON 字串
        json_output = json.dumps(json_data, ensure_ascii=False, indent=2)

        # 生成四段式文本版本
        positive_text = self._generate_four_part_text(fields, language_choice, detail_level)

        return (json_output, positive_text, negative_prompt)

    def _get_chinese_field_name(self, field_name):
        """將英文字段名轉換為中文顯示名稱"""
        name_mapping = {
            "scene_description": "場景描述",
            "time_atmosphere": "時間氛圍",
            "environment_setting": "環境設定",
            "character_features": "人物特徵",
            "clothing_style": "服裝造型",
            "pose_expression": "姿勢表情",
            "lens_parameters": "鏡頭參數",
            "shooting_angle": "拍攝角度",
            "film_style": "膠片風格",
            "light_source_type": "光源類型",
            "light_effect": "光效描述",
            "contrast_level": "對比層次",
            "art_style": "藝術風格",
            "color_scheme": "色彩方案",
            "render_effects": "渲染效果"
        }
        return name_mapping.get(field_name, field_name)

    def _get_group_chinese(self, field_name):
        """根據字段名返回所屬分組（中文）"""
        group_mapping = {
            "scene_description": "場景", "time_atmosphere": "場景", "environment_setting": "場景",
            "character_features": "主體", "clothing_style": "主體", "pose_expression": "主體",
            "lens_parameters": "攝影", "shooting_angle": "攝影", "film_style": "攝影",
            "light_source_type": "燈光", "light_effect": "燈光", "contrast_level": "燈光",
            "art_style": "風格", "color_scheme": "風格", "render_effects": "風格"
        }
        return group_mapping.get(field_name, "未知")

    def _get_group(self, field_name):
        """根據字段名返回所屬分組（英文）"""
        group_mapping = {
            "scene_description": "scene", "time_atmosphere": "scene", "environment_setting": "scene",
            "character_features": "subject", "clothing_style": "subject", "pose_expression": "subject",
            "lens_parameters": "photography", "shooting_angle": "photography", "film_style": "photography",
            "light_source_type": "lighting", "light_effect": "lighting", "contrast_level": "lighting",
            "art_style": "style", "color_scheme": "style", "render_effects": "style"
        }
        return group_mapping.get(field_name, "unknown")

    def _process_field_value(self, field_name, value, language_choice):
        """處理字段值，包括隨機選擇和語言處理"""
        if value == "隨機 | Random":
            # 從對應文件中隨機選擇
            group = self._get_group(field_name)
            options_dir = os.path.join(os.path.dirname(__file__), "z_image_options")
            file_name = f"{field_name}.txt"
            file_path = os.path.join(options_dir, group, file_name)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    options = [line.strip() for line in f if line.strip()]
                    # 過濾掉"隨機 | Random"和"無 | None"選項
                    valid_options = [opt for opt in options if opt not in ["隨機 | Random", "無 | None"]]
                    if valid_options:
                        selected = random.choice(valid_options)
                        return self._process_language(selected, language_choice)
            except Exception as e:
                print(f"[Z-Image] 警告: 無法為 {field_name} 載入隨機選項: {e}")
                # 使用記憶體中的選項作為備份
                if group in self.OPTION_DATA and file_name in self.OPTION_DATA[group]:
                    valid_options = self.OPTION_DATA[group][file_name]
                    if valid_options:
                        selected = random.choice(valid_options)
                        return self._process_language(selected, language_choice)
            
            return ""
        elif value == "無 | None":
            return ""
        else:
            return self._process_language(value, language_choice)

    def _process_language(self, text, language_choice):
        """根據語言選擇處理文本"""
        if not text:
            return ""
        
        if language_choice == "中文":
            # 只返回中文部分
            parts = text.split(" | ")
            return parts[0].strip() if len(parts) > 0 else text
        elif language_choice == "English":
            # 只返回英文部分
            parts = text.split(" | ")
            return parts[1].strip() if len(parts) > 1 else text
        else:  # 雙語
            return text

    def _apply_style_template(self, fields, template_id, templates, language_choice):
        """應用風格模板"""
        if template_id not in templates:
            return fields
        
        template_data = templates[template_id]
        template_fields = template_data.get('fields', {})
        
        for key, value in template_fields.items():
            if key in fields and (not fields[key] or fields[key] == "無" or fields[key] == "None"):
                fields[key] = self._process_language(value, language_choice)
        
        return fields

    def _adjust_detail_level(self, fields, detail_level, language_choice):
        """根據細節等級調整字段內容"""
        # 提取細節等級名稱（去除語言部分）
        if " | " in detail_level:
            detail_level_name = detail_level.split(" | ")[0]
        else:
            detail_level_name = detail_level
            
        if detail_level_name == "簡略":
            # 簡略模式：只保留核心字段
            core_fields = ["scene_description", "character_features", "art_style"]
            for key in fields:
                if key not in core_fields:
                    fields[key] = ""
        elif detail_level_name == "詳細":
            # 詳細模式：添加更多描述詞
            descriptive_words = {
                "scene_description": ["精緻的 | Exquisite", "細膩的 | Detailed", "生動的 | Vivid"],
                "character_features": ["獨特的 | Unique", "鮮明的 | Distinct", "立體的 | Three-dimensional"],
                "art_style": ["強烈的 | Strong", "突出的 | Prominent", "明顯的 | Obvious"]
            }
            
            for key, words in descriptive_words.items():
                if fields[key] and not any(fields[key].startswith(word.split(" | ")[0]) for word in words):
                    selected_word = random.choice(words)
                    fields[key] = f"{self._process_language(selected_word, language_choice)}{fields[key]}"
        elif detail_level_name == "極度詳細":
            # 極度詳細模式：添加更多細節描述
            detail_descriptions = {
                "scene_description": "，充滿豐富的細節和層次 | , full of rich details and layers",
                "character_features": "，具有獨特的個人特質和表情 | , with unique personal characteristics and expressions",
                "clothing_style": "，展現精緻的材質和做工 | , showing exquisite materials and workmanship",
                "art_style": "，體現強烈的視覺衝擊和藝術感 | , reflecting strong visual impact and artistic sense"
            }
            
            for key, desc in detail_descriptions.items():
                if fields[key]:
                    desc_part = desc.split(" | ")[0] if language_choice == "中文" else desc.split(" | ")[1]
                    if not fields[key].endswith(desc_part):
                        fields[key] = f"{fields[key]}{desc_part}"
        
        return fields

    def _generate_four_part_text(self, fields, language_choice, detail_level):
        """生成四段式文本提示"""
        # 提取細節等級名稱
        if " | " in detail_level:
            detail_level_name = detail_level.split(" | ")[0]
        else:
            detail_level_name = detail_level
            
        parts = []
        
        # 第一段：核心描述（場景 + 主體 + 姿勢）
        part1 = []
        if fields["scene_description"]:
            part1.append(fields["scene_description"])
        if fields["character_features"]:
            part1.append(fields["character_features"])
        if fields["pose_expression"]:
            part1.append(fields["pose_expression"])
        
        if part1:
            if language_choice == "中文":
                parts.append(f"【核心描述】{'，'.join(part1)}")
            elif language_choice == "English":
                parts.append(f"【Core Description】{', '.join(part1)}")
            else:
                parts.append(f"【核心描述 | Core Description】{'，'.join(part1)}")
        
        # 第二段：環境細節（時間 + 環境）
        part2 = []
        if fields["time_atmosphere"]:
            part2.append(fields["time_atmosphere"])
        if fields["environment_setting"]:
            part2.append(fields["environment_setting"])
        if fields["clothing_style"]:
            if language_choice == "English":
                part2.append(f"wearing {fields['clothing_style']}")
            else:
                part2.append(f"穿著{fields['clothing_style']}")
        
        if part2:
            if language_choice == "中文":
                parts.append(f"【環境細節】{'，'.join(part2)}")
            elif language_choice == "English":
                parts.append(f"【Environment Details】{', '.join(part2)}")
            else:
                parts.append(f"【環境細節 | Environment Details】{'，'.join(part2)}")
        
        # 第三段：技術參數（攝影 + 燈光）
        part3 = []
        if fields["lens_parameters"]:
            part3.append(fields["lens_parameters"])
        if fields["shooting_angle"]:
            part3.append(fields["shooting_angle"])
        if fields["light_source_type"]:
            part3.append(fields["light_source_type"])
        if fields["light_effect"]:
            part3.append(fields["light_effect"])
        if fields["film_style"]:
            part3.append(fields["film_style"])
        if fields["contrast_level"]:
            part3.append(fields["contrast_level"])
        
        if part3:
            if language_choice == "中文":
                parts.append(f"【技術參數】{'，'.join(part3)}")
            elif language_choice == "English":
                parts.append(f"【Technical Parameters】{', '.join(part3)}")
            else:
                parts.append(f"【技術參數 | Technical Parameters】{'，'.join(part3)}")
        
        # 第四段：風格強化（藝術 + 色彩 + 渲染）
        part4 = []
        if fields["art_style"]:
            part4.append(fields["art_style"])
        if fields["color_scheme"]:
            part4.append(fields["color_scheme"])
        if fields["render_effects"]:
            part4.append(fields["render_effects"])
        
        # 根據細節等級添加額外描述
        if detail_level_name in ["詳細", "極度詳細"]:
            if language_choice == "中文":
                quality_words = ["高質量", "高解析度", "專業級", "大師級"]
                part4.append(f"{random.choice(quality_words)}作品")
            elif language_choice == "English":
                quality_words = ["High quality", "High resolution", "Professional grade", "Masterpiece"]
                part4.append(f"{random.choice(quality_words)} work")
            else:
                quality_words = ["高質量 | High quality", "高解析度 | High resolution", "專業級 | Professional grade", "大師級 | Masterpiece"]
                part4.append(f"{random.choice(quality_words)}作品 | work")
        
        if part4:
            if language_choice == "中文":
                parts.append(f"【風格強化】{'，'.join(part4)}")
            elif language_choice == "English":
                parts.append(f"【Style Enhancement】{', '.join(part4)}")
            else:
                parts.append(f"【風格強化 | Style Enhancement】{'，'.join(part4)}")
        
        # 合併所有段落
        separator = "\n\n" if detail_level_name in ["詳細", "極度詳細"] else "\n"
        return separator.join(parts)

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return f"{time.time()}"


# 註冊節點
NODE_CLASS_MAPPINGS = {
    "ZImageJSONPrompting": ZImageJSONPrompting
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ZImageJSONPrompting": "Z-Image JSON Prompt Generator"
}