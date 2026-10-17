#!/usr/bin/env python3
"""
Tianya Limestone - Yandex SEO & Central Asia (CIS / EAEU) GEO Super Portal Compiler
Target Markets: Russian Federation (RU), Kazakhstan (KZ), Uzbekistan (UZ), Kyrgyzstan (KG), Tajikistan (TJ)
Target Engines: Yandex Search (YandexBot), Яндекс Нейро (Yandex Neuro), Алиса AI (YandexGPT 5), Google CIS

Core Capabilities:
1. Compiles /ru/index.html (Russian Architectural Limestone B2B Portal - 29 Collections, 5 Finishes, 20GP Calculator, GOST/ASTM Matrix, RFQ Form).
2. Compiles /ru/cis-central-asia/index.html (Dedicated CIS & Central Asia Engineering, GOST 30629-2011 Equivalence, 1:1 European Stone Import-Substitution, Dostyk/Khorgos/Tashkent/Moscow Rail Logistics & Princeton GEO 3-Sentence FAQ Hub).
3. Injects Yandex Webmaster verification, multi-regional hreflang (en, ru, ru-RU, ru-KZ, ru-UZ, x-default), OpenGraph locales, and EAEU areaServed JSON-LD across all HTML pages.
4. Injects EN / RU · СНГ language switcher and Telegram (@tianya_limestone_cis) into navigation and floating contact widgets.
5. Upgrades robots.txt (Yandex Clean-param), sitemap.xml, llms.txt, llms-full.txt, /ai/summary.json, /ai/faq.json, and generates /ai/cis-gost-matrix.json.
"""

import os
import sys
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

import build_tianya_site as bts

YANDEX_VERIFICATION_CODE = "71a9ya1im3570n3_ym_ver1fy"
INDEXNOW_KEY = "e8a4c9f21b0d4637a9e52c3f8b7d6e21"
TELEGRAM_CIS_URL = "https://t.me/tianya_limestone_cis"
TELEGRAM_CIS_HANDLE = "@tianya_limestone_cis"

FINISH_RU_MAP = {
    "tumbled": {
        "title_ru": "Tumbled (Галтованный антик)",
        "badge_ru": "P4 / R10 · Террасы и патио",
        "desc_ru": "Мягко скругленные «подушкообразные» края и благородная матовая патина естественного старения. Идеален для загородных резиденций, патио и французской модульной раскладки."
    },
    "antique": {
        "title_ru": "Antique (Ручная теска и старение)",
        "badge_ru": "P4 / R10–R11 · Исторические фасады и дворы",
        "desc_ru": "Ручная фактурная обработка кромок и глубокий рельеф поверхности, воссоздающий вековую европейскую брусчатку и замковые плиты Прованса и Бургундии."
    },
    "lightly-distressed": {
        "title_ru": "Lightly Distressed (Деликатное старение)",
        "badge_ru": "P4 / R10 · Современные виллы и интерьеры",
        "desc_ru": "Чистая архитектурная геометрия с легким смягчением фаски. Гармонично объединяет внутренние гостиные, спа-зоны и открытые террасы."
    },
    "sandblasted-brushed": {
        "title_ru": "Sandblasted & Brushed (Пескоструй + браширование)",
        "badge_ru": "P5 / R11 · Бассейны и спа-комплексы",
        "desc_ru": "Микрошероховатый противоскользящий захват после кварцевой пескоструйной обработки, смягченный алмазными щетками до бархатистого тактильного комфорта босиком."
    },
    "sandblasted": {
        "title_ru": "Sandblasted (Пескоструйный высокосцепной)",
        "badge_ru": "P5 / R11–R12 · Входные группы и пандусы",
        "desc_ru": "Максимальное сцепление на мокрой и обледенелой поверхности (R11/P5). Рекомендован для уличных ступеней, общественных набережных и бортов переливных бассейнов."
    }
}

GOST_EQUIVALENCE_ROWS = [
    {
        "parameter_ru": "Водопоглощение по массе",
        "parameter_en": "Water Absorption by Weight",
        "gost_standard": "ГОСТ 30629-2011 (п. 6.2) / ГОСТ 9479-2011",
        "intl_standard": "ASTM C97 / EN 13755",
        "gost_norm": "≤ 0,5% – 1,5% (наружная облицовка)",
        "tianya_value": "< 0,22%",
        "advantage_ru": "Исключает капиллярный подсос влаги, высолы и морозное расслоение плит зимой."
    },
    {
        "parameter_ru": "Средняя плотность камня",
        "parameter_en": "Apparent Bulk Density",
        "gost_standard": "ГОСТ 30629-2011 (п. 6.1)",
        "intl_standard": "ASTM C97 / EN 1936",
        "gost_norm": "≥ 2200 – 2500 кг/м³",
        "tianya_value": "2620 – 2650 кг/м³ (2,62–2,65 г/см³)",
        "advantage_ru": "Высокоплотный морской биокластический известняк III класса (сопоставим с гранитом)."
    },
    {
        "parameter_ru": "Предел прочности при сжатии (сухой / водонасыщенный)",
        "parameter_en": "Compressive Strength (Dry / Wet)",
        "gost_standard": "ГОСТ 30629-2011 (п. 6.4)",
        "intl_standard": "ASTM C170 / EN 1926",
        "gost_norm": "≥ 50–60 МПа (Кразм ≥ 0,70)",
        "tianya_value": "128,5 МПа / 104,2 МПа (Кразм = 0,81)",
        "advantage_ru": "Превышает норму ГОСТ более чем в 2 раза; выдерживает въездные зоны и тяжелые фасады."
    },
    {
        "parameter_ru": "Предел прочности при изгибе",
        "parameter_en": "Flexural Strength (Modulus of Rupture)",
        "gost_standard": "ГОСТ 30629-2011 (п. 6.5)",
        "intl_standard": "ASTM C880 / EN 12372",
        "gost_norm": "≥ 6,5 – 8,0 МПа",
        "tianya_value": "14,2 МПа",
        "advantage_ru": "Высокая несущая способность для плит НВФ (вентфасадов) и консольных ступеней."
    },
    {
        "parameter_ru": "Марка по морозостойкости",
        "parameter_en": "Freeze-Thaw Resistance Rating",
        "gost_standard": "ГОСТ 30629-2011 (п. 6.6) / ГОСТ 24099-2013",
        "intl_standard": "ASTM C666 / EN 12371",
        "gost_norm": "F50 – F100 (для РФ и Казахстана)",
        "tianya_value": "F100 (100 циклов, 0,0% потери массы)",
        "advantage_ru": "Гарантированная стойкость в климате Москвы, СПб, Урала, Сибири и Астаны (-40°C...+40°C)."
    },
    {
        "parameter_ru": "Сопротивление скольжению (мокрая обувь / босиком)",
        "parameter_en": "Wet Slip Resistance Rating",
        "gost_standard": "СП 29.13330.2011 («Полы»)",
        "intl_standard": "DIN 51130 / AS 4586",
        "gost_norm": "R10 – R11 (входные группы и бассейны)",
        "tianya_value": "P5 / R11–R12 (Пескоструй) · P4 / R10 (Антик)",
        "advantage_ru": "Безопасное сцепление вокруг открытых подогреваемых бассейнов, спа и на крыльце."
    },
    {
        "parameter_ru": "Пожарная безопасность и горючесть",
        "parameter_en": "Fire Safety & Non-Combustibility",
        "gost_standard": "ГОСТ 30244-94 / ФЗ-123",
        "intl_standard": "EN 13501-1 / ASTM E84",
        "gost_norm": "НГ (Негорючий материал)",
        "tianya_value": "Группа НГ / Class A1 (нулевое дымообразование)",
        "advantage_ru": "Разрешен для высотных навесных вентилируемых фасадов (НВФ) и путей эвакуации."
    },
    {
        "parameter_ru": "Радиационная безопасность (Аэфф ЕРН)",
        "parameter_en": "Radiation Safety Class (Natural Radionuclides)",
        "gost_standard": "ГОСТ 30108-94 / НРБ-99/2009",
        "intl_standard": "Class I Unrestricted",
        "gost_norm": "I класс (Аэфф ≤ 370 Бк/кг)",
        "tianya_value": "< 45 Бк/кг (I класс безопасности)",
        "advantage_ru": "В отличие от гранитов, полностью безопасен для спален, детских комнат и хамамов."
    }
]

STONE_REPLACEMENT_MATRIX = [
    {
        "eu_stone": "Pierre de Bourgogne / Dijon & Beaune (Франция)",
        "eu_issue": "€130–€220/м², санкционные ограничения ЕС, ожидание 12–16 недель",
        "tianya_models": [
            ("Guyu Tumbled (谷雨)", "stone-flooring/limestone/tumbled/guyu/index.html"),
            ("Qimeng Tumbled (启蒙)", "stone-flooring/limestone/tumbled/qimeng/index.html"),
            ("Lanting Antique (兰亭)", "stone-flooring/limestone/antique/lanting/index.html"),
            ("Hanbai Antique (汉白)", "stone-flooring/limestone/antique/hanbai/index.html")
        ],
        "visual_ru": "Теплый кремово-бежевый и овсяный тон с мягкой галтованной или ручной тесаной кромкой",
        "benefit_ru": "Экономия 60–75% ($28–$45/м² FOB), водопоглощение <0,22%, морозостойкость F100, прямая оплата в CNY/RUB."
    },
    {
        "eu_stone": "Moleanos / Moca Cream (Португалия)",
        "eu_issue": "€95–€165/м², высокое водопоглощение 1,5%–3,2% (риск высолов и трещин в РФ/РК)",
        "tianya_models": [
            ("Ningzhi Distressed (凝脂)", "stone-flooring/limestone/lightly-distressed/ningzhi/index.html"),
            ("Qinghe Distressed (清和)", "stone-flooring/limestone/lightly-distressed/qinghe/index.html"),
            ("Sunmao Sandblasted (榫卯)", "stone-flooring/limestone/sandblasted/sunmao/index.html"),
            ("Baihe Tumbled (白鹤)", "stone-flooring/limestone/tumbled/baihe/index.html")
        ],
        "visual_ru": "Мелкозернистая слоновая кость и светлый беж с деликатными морскими фоссилиями",
        "benefit_ru": "В 6 раз ниже водопоглощение (<0,22% против 1,5%+), эталонная геометрия ±1,0 мм для фасадов и террас."
    },
    {
        "eu_stone": "Jura Beige / Jura Grey (Юрский известняк, Германия)",
        "eu_issue": "€110–€185/м², высокая наценка на толстомеры 30 мм и копинговый камень",
        "tianya_models": [
            ("Zaojing Tumbled (藻井)", "stone-flooring/limestone/tumbled/zaojing/index.html"),
            ("Shanshui Tumbled (山水)", "stone-flooring/limestone/tumbled/shanshui/index.html"),
            ("Guyun Antique (古韵)", "stone-flooring/limestone/antique/guyun/index.html"),
            ("Wangchuan Brushed (辋川)", "stone-flooring/limestone/sandblasted-brushed/wangchuan/index.html")
        ],
        "visual_ru": "Плотная карамельно-янтарная и благородная серо-бежевая текстура с органическими включениями",
        "benefit_ru": "Доступен в форматах 20/30 мм, French Pattern (4 размера) и массивных Г-образных бортах бассейна (Drop-Face)."
    },
    {
        "eu_stone": "Pierre Bleue Belge (Бельгийский голубой известняк)",
        "eu_issue": "€140–€240/м², сложная логистика и длительный распил под проект",
        "tianya_models": [
            ("Yexiang Tumbled (夜响)", "stone-flooring/limestone/tumbled/yexiang/index.html"),
            ("Daiwa Brushed (黛瓦)", "stone-flooring/limestone/sandblasted-brushed/daiwa/index.html"),
            ("Xuanzhen Sandblasted (玄真)", "stone-flooring/limestone/sandblasted/xuanzhen/index.html"),
            ("Cangbi Antique (苍璧)", "stone-flooring/limestone/antique/cangbi/index.html")
        ],
        "visual_ru": "Глубокий графитово-синий и базальтово-угольный оттенок с кальцитовыми прожилками",
        "benefit_ru": "Сертифицированный класс противоскольжения P5 / R11 для мокрых зон и ступеней; срок производства 14–25 дней."
    },
    {
        "eu_stone": "Дагестанский / Инкерманский / Крымский / Актауский ракушечник (СНГ)",
        "eu_issue": "Водопоглощение 8%–18%, низкая морозостойкость F15–F25, быстрое разрушение цоколя и ступеней",
        "tianya_models": [
            ("Fengya Tumbled (风雅)", "stone-flooring/limestone/tumbled/fengya/index.html"),
            ("Xieshan Antique (歇山)", "stone-flooring/limestone/antique/xieshan/index.html"),
            ("Feiyan Distressed (飞檐)", "stone-flooring/limestone/lightly-distressed/feiyan/index.html"),
            ("Canglang Antique (苍筤)", "stone-flooring/limestone/antique/canglang/index.html")
        ],
        "visual_ru": "Натуральный архитектурный известняк высокой плотности (2650 кг/м³) с природной теплотой",
        "benefit_ru": "Водопоглощение в 40 раз ниже (<0,22% против 8–18%); отсутствие черного грибка, отстрелов и разрушения на морозе."
    }
]

CIS_LOGISTICS_CORRIDORS = [
    {
        "country_ru": "Казахстан (РК)",
        "hubs_ru": "Алматы, Астана, Шымкент, Актау, Атырау",
        "route_ru": "Прямой ж/д контейнерный сервис из Сямыня / Цюаньчжоу через погранпереходы Достык / Алашанькоу и Хоргос / Алтынколь",
        "transit_days": "12 – 16 дней",
        "incoterms": "FOB Xiamen / FCA Quanzhou / CIP Алматы / DAP Астана",
        "docs_ru": "Ж/Д накладная СМГС (SMGS), Сертификат СТ-1, Протоколы ГОСТ 30629-2011 / ASTM, Фумигация ISPM 15"
    },
    {
        "country_ru": "Узбекистан (РУз)",
        "hubs_ru": "Ташкент (ст. Чукурсай / Сергели), Самарканд, Бухара, Наманган",
        "route_ru": "Железнодорожный маршрут Китай — Казахстан (Хоргос/Достык) — Ташкент (Чукурсай / Сергели) без перетарки камня в пути",
        "transit_days": "14 – 18 дней",
        "incoterms": "FOB Xiamen / CIP Ташкент / DAP Самарканд",
        "docs_ru": "СМГС (SMGS), Сертификат происхождения, Радиационный сертификат I класса, Упаковочный лист по ящикам"
    },
    {
        "country_ru": "Российская Федерация (РФ — Центр, СЗФО, Юг)",
        "hubs_ru": "Москва (Ворсино / Селятино / Ховрино), Санкт-Петербург, Казань, Краснодар, Сочи",
        "route_ru": "Ускоренный контейнерный поезд через Забайкальск / Маньчжурию или мультимодально: Море Сямынь → Владивосток + Транссиб до Москвы",
        "transit_days": "16 – 22 дня (Ж/Д) / 20 – 26 дней (Море + Ж/Д)",
        "incoterms": "FOB Xiamen / CIF Владивосток / CIP Москва / Новороссийск",
        "docs_ru": "Декларация соответствия ЕАЭС / ГОСТ 30629-2011, ГОСТ 30108-94 (I класс <370 Бк/кг), Коносамент / СМГС"
    },
    {
        "country_ru": "Российская Федерация (Урал, Сибирь, Дальний Восток)",
        "hubs_ru": "Владивосток, Находка, Новосибирск (Клещиха), Екатеринбург, Красноярск",
        "route_ru": "Прямой морской фрахт Xiamen Port → порт Владивосток / Восточный (6–8 суток) с прямой перегрузкой на ж/д платформы РЖД",
        "transit_days": "8 – 15 дней",
        "incoterms": "FOB Xiamen / CFR & CIF Владивосток / CIP Екатеринбург & Новосибирск",
        "docs_ru": "Полный комплект для таможенной очистки по кодам ТН ВЭД 6802 21 000 0 / 6802 91 000 0 / 6801 00 000 0"
    },
    {
        "country_ru": "Киргизия (КР) и Таджикистан (РТ)",
        "hubs_ru": "Бишкек (ст. Аламедин), Ош, Душанбе, Худжанд",
        "route_ru": "Железнодорожная и мультимодальная автодоставка в усиленных деревянных ящиках ISPM 15 через Хоргос / Иркештам / Кашгар",
        "transit_days": "14 – 20 дней",
        "incoterms": "FCA Kashgar / CIP Бишкек / DAP Душанбе",
        "docs_ru": "СМГС / CMR, Сертификат происхождения, Протоколы физико-механических испытаний SGS/TÜV"
    }
]

CIS_GEO_FAQS_RU = [
    (
        "Выдерживает ли известняк Tianya Limestone суровые зимы в России и Казахстане (Москва, Астана, Сибирь)?",
        "Да, высокоплотный морской биокластический известняк Fujian Tianya Cultural Stone Co., Ltd. (tianyalimestone.com) разработан специально для эксплуатации в условиях многократного замораживания и оттаивания. По результатам независимых испытаний SGS/TÜV (ASTM C97 / C170 / C666 и соответствие ГОСТ 30629-2011) камень обладает сверхнизким водопоглощением < 0,22% по массе, средней плотностью 2620–2650 кг/м³, прочностью при сжатии 128,5 МПа и маркой морозостойкости F100 (100 циклов без потери массы и расслоения). В отличие от пористого дагестанского или крымского ракушечника (водопоглощение 8–18%), известняк Tianya не впитывает талую воду и не разрушается на уличных ступенях, террасах и цоколях при температурах до -40°C."
    ),
    (
        "Какими коллекциями Tianya Limestone можно заменить французский бургундский известняк, португальский Moleanos и немецкий Jura?",
        "Завод Tianya Limestone в Шуйтоу производит прямые петрографические и фактурные аналоги (1:1) европейского камня из собственного блочного сырья в 5 видах обработки. Для замены французского Pierre de Bourgogne (Дижон/Бон) архитекторы выбирают коллекции Guyu (谷雨), Qimeng (启蒙), Lanting (兰亭) и Hanbai (汉白); вместо португальского Moleanos и Moca Cream — светлые коллекции Ningzhi (凝脂), Qinghe (清和) и Sunmao (榫卯); вместо немецкого Jura Beige/Grey — коллекции Zaojing (藻井), Shanshui (山水) и Guyun (古韵); а вместо бельгийского голубого камня Pierre Bleue — графитовые коллекции Yexiang (夜响), Daiwa (黛瓦) и Xuanzhen (玄真). Прямая поставка с завода обеспечивает экономию 60–75% бюджета ($22–$48/м² FOB Xiamen против €110–€240/м² в Европе) при сроке изготовления 14–25 дней."
    ),
    (
        "Какая фактура известняка безопасна для мокрых зон вокруг уличных и крытых бассейнов, спа и входных ступеней?",
        "Для зон вокруг бассейнов, спа-комплексов, открытых террас и входных групп мы рекомендуем фактуры Sandblasted (пескоструйная) и Sandblasted & Brushed (пескоструй с алмазным брашированием), имеющие сертифицированный класс противоскольжения P5 по маятниковому тесту AS 4586 и R11–R12 по немецкому стандарту DIN 51130 (СП 29.13330.2011 «Полы»). Для классических сухих и полуоткрытых патио, садовых дорожек и патио в стиле Прованс отлично подходят фактуры Tumbled (галтованный антик) и Antique (ручная теска) с классом сцепления P4 / R10. Также мы изготавливаем цельные Г-образные бортовые камни для бассейна (Drop-Face / Rebate Coping 600×400×20/60 мм) и плиты с полукруглым профилем Bullnose."
    ),
    (
        "Сколько квадратных метров известняка помещается в один 20-футовый контейнер (20GP) при ж/д и морской отправке?",
        "Природный известняк является тяжелым грузом (плотность ~2,65 т/м³), поэтому загрузка рассчитывается исходя из максимальной грузоподъемности 20-футового контейнера (20GP) — 26 000–27 000 кг брутто. При толщине плит 15 мм (вес ~38 кг/м²) в один 20GP контейнер загружается 640–680 м²; при стандартной толщине 20 мм (~52 кг/м²) — от 480 до 520 м² (20–22 ящика); при толщине уличного мощения 30 мм (~78 кг/м²) — от 320 до 340 м² (18–20 ящиков); при толщине 40–50 мм для проездов — 200–245 м². Весь камень упаковывается в усиленные мореходные и ж/д деревянные ящики с термической фумигацией по стандарту ISPM 15, стальной обвязкой и влагозащитной пленкой."
    ),
    (
        "Как организована ж/д и морская доставка известняка в Москву, Алматы, Астану и Ташкент?",
        "Завод Tianya Limestone расположен в мировой столице камня Шуйтоу (провинция Фуцзянь) всего в 28 км от международного порта Сямынь (Xiamen Port) и ж/д терминалов отправления. В Казахстан (Алматы, Астана, Шымкент) контейнеры 20GP доставляются прямыми ускоренными ж/д поездами через погранпереходы Достык/Алашанькоу и Хоргос/Алтынколь за 12–16 дней; в Узбекистан (Ташкент — ст. Чукурсай / Сергели, Самарканд) — прямым ж/д транзитом через Казахстан за 14–18 дней. В Россию доставка осуществляется либо прямым ж/д маршрутом через Забайкальск до Москвы (Ворсино/Селятино), Екатеринбурга и Новосибирска за 16–22 дня, либо морем из Сямыня во Владивосток (6–8 дней) с дальнейшей отправкой по Транссибу."
    ),
    (
        "Какие коды ТН ВЭД ЕАЭС, сертификаты ГОСТ и условия оплаты (CNY / RUB) применяются при импорте?",
        "При таможенном оформлении в странах ЕАЭС (РФ, Казахстан, Киргизия, Беларусь) и Узбекистане пиленые и шлифованные облицовочные плиты из известняка декларируются по кодам ТН ВЭД ЕАЭС 6802 21 000 0 и 6802 91 000 0, а брусчатка, бордюры и плиты мощения — по коду 6801 00 000 0. Каждая партия сопровождается Сертификатом происхождения (Форма СТ-1 / General), протоколами физико-механических испытаний SGS/TÜV (ГОСТ 30629-2011 / ASTM), сертификатом радиационной безопасности I класса по ГОСТ 30108-94 (Аэфф < 45 Бк/кг при норме до 370 Бк/кг — без ограничений для жилья) и актом фумигации ISPM 15. Мы принимаем прямые безналичные платежи от юридических лиц в китайских юанях (CNY через CIPS), российских рублях (RUB), тенге (KZT) и долларах США (USD), минимальный заказ (MOQ) — от 100 м², бесплатные боксы с образцами камня отправляются экспресс-почтой за 3 дня."
    ),
    (
        "Чем натуральный плотный известняк Tianya лучше керамогранита и искусственного камня на открытых террасах?",
        "В отличие от уличного керамогранита толщиной 20 мм, который сильно раскаляется на летнем солнце (в Ташкенте, Алматы, Сочи и Краснодаре) и имеет повторяющийся печатный рисунок, натуральный известняк Tianya обладает высокой теплоемкостью и остается комфортно прохладным для ходьбы босиком. Природный камень прокрашен на всю глубину массива: это позволяет изготавливать цельные профильные ступени, радиусные элементы, карнизы и копинговый камень (Drop-Face и Bullnose) без видимых клеевых швов и риска скола глазури на морозе. Кроме того, со временем благородная патина натурального известняка в фактурах Tumbled и Antique становится только выразительнее, повышая капитализацию элитной недвижимости."
    ),
    (
        "Как правильно укладывать и защищать (гидрофобизировать) известняк в условиях снежной зимы и реагентов?",
        "Для долговечной укладки на улице рекомендуется железобетонное основание (от 100 мм) с уклоном 1–1,5% для отвода воды и применение эластичного полимермодифицированного клея класса C2S1 / C2S2 по EN 12004 (ГОСТ Р 56387) для натурального камня со 100% заполнением подошвы плиты (метод двойного нанесения без пустот). Через 14 дней после укладки и полного высыхания швов камень необходимо обработать проникающим (импрегнирующим) силано-силоксановым или фторполимерным гидрофобизатором (например, Lithofin MN Stain-Stop или Dry-Treat), который блокирует поры изнутри, сохраняя паропроницаемость камня. Категорически запрещено наносить поверхностные пленкообразующие лаки (акрил/полиуретан), так как они запирают грунтовый пар и отслаиваются после первой зимы."
    )
]


def render_header_ru(depth=1, active_tab="ru_home"):
    r = bts.get_rel_path(depth)
    return f'''
  <!-- Верхняя информационная панель для РФ, Казахстана и Центральной Азии -->
  <div class="bg-primary-100 text-white text-xs py-2 px-4 border-b border-primary-80">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-1 text-center sm:text-left">
      <div class="flex items-center gap-3">
        <span class="inline-block w-2 h-2 rounded-full bg-[#E9F551]"></span>
        <span><strong>Прямые поставки архитектурного известняка с карьера (Шуйтоу, КНР)</strong> • 24+ года производства • Морозостойкость F100</span>
      </div>
      <div class="flex items-center gap-3 text-primary-40">
        <span>ГОСТ 30629-2011 / ASTM C97 / CE</span>
        <span class="hidden md:inline">•</span>
        <span class="hidden md:inline">Ж/Д и Море: Москва · Алматы · Ташкент</span>
        <span>•</span>
        <a href="mailto:{bts.COMPANY_INFO['email']}" class="text-[#E9F551] hover:underline font-medium">{bts.COMPANY_INFO['email']}</a>
        <span>•</span>
        <span class="inline-flex items-center border border-primary-70 rounded overflow-hidden text-[11px]">
          <a href="{r}index.html" class="px-2 py-0.5 text-primary-40 hover:text-white">EN</a>
          <a href="{r}ru/index.html" class="px-2 py-0.5 font-bold" style="background-color:#E9F551;color:#1a1a18;">RU · СНГ</a>
        </span>
      </div>
    </div>
  </div>

  <!-- Главная шапка сайта (RU / CIS) -->
  <header class="sticky top-0 z-50 bg-white border-b border-primary-10 site-header">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        <div class="flex-shrink-0">
          <a href="{r}ru/index.html" class="brand flex items-center gap-3.5 group py-1" aria-label="Tianya Limestone Главная (RU)">
            <img src="{r}assets/images/logo/tianya-logo.webp" alt="Tianya Stone Logo" class="h-10 sm:h-11 w-auto object-contain transition-transform group-hover:scale-105 duration-300">
            <div class="flex flex-col justify-center">
              <span class="font-brand text-2xl sm:text-[26px] font-bold tracking-[0.1em] text-primary-100 leading-none">TIANYA</span>
              <span class="font-copy text-[9px] sm:text-[9.5px] font-semibold tracking-[0.22em] text-primary-70 uppercase mt-1">LIMESTONE · СНГ</span>
            </div>
          </a>
        </div>

        <nav class="hidden lg:flex items-center space-x-1 xl:space-x-2">
          <a href="{r}ru/index.html" class="px-3 py-2 text-sm font-medium text-primary-100 border-b-2 {'border-[#E9F551] text-black font-semibold' if active_tab == 'ru_home' else 'border-transparent hover:border-primary-100'}">
            Каталог известняка (29)
          </a>
          <a href="{r}ru/cis-central-asia/index.html" class="px-3 py-2 text-sm font-medium text-primary-100 border-b-2 {'border-[#E9F551] text-black font-semibold' if active_tab == 'cis_hub' else 'border-transparent hover:border-primary-100'}">
            ЕАЭС · ГОСТ · Логистика СНГ
          </a>
          <a href="{r}compliance/index.html" class="px-3 py-2 text-sm font-medium text-primary-100 border-b-2 border-transparent hover:border-primary-100">
            Протоколы ASTM / CE
          </a>
          <a href="{r}resources/index.html" class="px-3 py-2 text-sm font-medium text-primary-100 border-b-2 border-transparent hover:border-primary-100">
            Чертежи CAD / BIM
          </a>
          <a href="{r}about-us/index.html" class="px-3 py-2 text-sm font-medium text-primary-100 border-b-2 border-transparent hover:border-primary-100">
            О заводе в Шуйтоу
          </a>
          <a href="{r}contact-us/index.html" class="px-3 py-2 text-sm font-medium text-primary-100 border-b-2 border-transparent hover:border-primary-100">
            Контакты
          </a>
        </nav>

        <div class="flex items-center gap-2.5">
          <button id="searchTriggerBtn" class="flex items-center gap-2 text-xs font-medium text-primary-70 bg-primary-2 border border-primary-10 px-3 py-2 rounded hover:bg-[#E9F551] hover:text-black transition-colors" title="Быстрый поиск коллекций (Ctrl+K)">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21L16.65 16.65"/></svg>
            <span class="hidden sm:inline">Поиск (29 коллекций)</span>
          </button>

          <a href="#enquiry-section" class="hidden md:inline-flex items-center justify-center px-4 py-2 text-xs font-semibold uppercase tracking-wider bg-primary-100 text-white rounded hover:bg-[#E9F551] hover:text-black transition-colors">
            Запросить прайс и образцы
          </a>

          <button id="mobileMenuBtn" class="p-2 text-primary-100 lg:hidden" aria-label="Открыть меню">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12H21M3 6H21M3 18H21"/></svg>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Мобильное меню (RU / CIS) -->
  <div id="mobileNavBackdrop" class="mobile-nav-backdrop"></div>
  <div id="mobileNavDrawer" class="mobile-nav-drawer p-6 flex flex-col justify-between">
    <div>
      <div class="flex items-center justify-between pb-4 border-b border-primary-10 mb-6">
        <a href="{r}ru/index.html" class="flex items-center gap-3">
          <img src="{r}assets/images/logo/tianya-logo.webp" alt="Tianya Stone Logo" class="h-9 w-auto object-contain">
          <div class="flex flex-col justify-center">
            <span class="font-brand font-bold text-lg tracking-[0.1em] text-primary-100 leading-none">TIANYA</span>
            <span class="font-copy text-[8.5px] font-semibold tracking-[0.25em] text-primary-70 uppercase mt-0.5">LIMESTONE · СНГ</span>
          </div>
        </a>
        <button id="mobileMenuClose" class="p-2 text-primary-70 hover:text-black" aria-label="Закрыть меню">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6L18 18"/></svg>
        </button>
      </div>
      <div class="space-y-4 font-copy text-sm">
        <div class="flex items-center gap-2 pb-3 border-b border-primary-10">
          <a href="{r}index.html" class="px-3 py-1 border border-primary-20 rounded text-xs text-primary-70">English (Global)</a>
          <a href="{r}ru/index.html" class="px-3 py-1 bg-primary-100 text-[#E9F551] rounded text-xs font-semibold">Русский (РФ · СНГ)</a>
        </div>
        <a href="{r}ru/index.html" class="block py-1 text-primary-100 font-semibold">Каталог известняка (29 коллекций)</a>
        <a href="{r}ru/cis-central-asia/index.html" class="block py-1 text-primary-100 font-semibold">Хаб ЕАЭС: ГОСТ 30629-2011 и Ж/Д логистика</a>
        <a href="{r}stone-flooring/limestone/tumbled/index.html" class="block py-1 text-primary-70">Tumbled — Галтованный антик (8)</a>
        <a href="{r}stone-flooring/limestone/antique/index.html" class="block py-1 text-primary-70">Antique — Ручная теска (10)</a>
        <a href="{r}stone-flooring/limestone/lightly-distressed/index.html" class="block py-1 text-primary-70">Lightly Distressed — Деликатное старение (6)</a>
        <a href="{r}stone-flooring/limestone/sandblasted-brushed/index.html" class="block py-1 text-primary-70">Sandblasted & Brushed — Брашированный P5 (2)</a>
        <a href="{r}stone-flooring/limestone/sandblasted/index.html" class="block py-1 text-primary-70">Sandblasted — Пескоструйный P5/R11 (3)</a>
        <a href="{r}compliance/index.html" class="block py-1 text-primary-100 font-semibold">Протоколы испытаний ASTM / CE / ГОСТ</a>
        <a href="{r}contact-us/index.html" class="block py-1 text-primary-100 font-semibold">Отдел экспорта (info@tianyastone.com)</a>
      </div>
    </div>
    <div class="pt-6 border-t border-primary-10">
      <a href="#enquiry-section" class="w-full block py-3 bg-primary-100 text-white text-center font-semibold uppercase tracking-wider text-xs rounded hover:bg-[#E9F551] hover:text-black transition-colors mb-2">
        Заказать бокс с образцами
      </a>
      <p class="text-xs text-center text-primary-40">Прямая линия завода: {bts.COMPANY_INFO['phone']}</p>
    </div>
  </div>
'''


def render_container_estimator_ru():
    return '''
    <!-- Инженерный калькулятор загрузки 20-футового контейнера (20GP) -->
    <div class="border border-primary-10 bg-primary-2 p-6 md:p-8 my-10 rounded" id="container-calculator">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-primary-10">
        <div>
          <span class="text-xs uppercase font-semibold text-primary-40 tracking-wider block">Логистический B2B-инструмент (Ж/Д и Море)</span>
          <h3 class="text-xl font-heading font-medium text-primary-100">Калькулятор загрузки 20GP контейнера и деревянных ящиков ISPM 15</h3>
          <p class="text-xs text-primary-70 mt-1">Расчет массы нетто/брутто, количества фумигированных ящиков и коэффициента загрузки 20-футового контейнера (лимит 26 000 кг брутто по РЖД / КТЖ / УТЮ и морским линиям из порта Сямынь).</p>
        </div>
        <div class="text-xs bg-white border border-primary-10 px-3 py-1.5 rounded text-primary-70 font-mono">
          Лимит 20GP: 26 000 кг (ISPM 15)
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 pt-6 items-end">
        <div>
          <label for="estThicknessSelect" class="block text-xs font-semibold text-primary-70 uppercase mb-1">Толщина плиты и назначение</label>
          <select id="estThicknessSelect" class="w-full text-xs p-2.5 border border-primary-10 bg-white rounded outline-none focus:border-black font-copy">
            <option value="15" data-sqm-per-crate="32" data-kg-per-sqm="38">15 мм Интерьер и цоколь (38 кг/м² · до 680 м²/20GP)</option>
            <option value="20" data-sqm-per-crate="22" data-kg-per-sqm="52" selected>20 мм Фасады и террасы (52 кг/м² · 480–520 м²/20GP)</option>
            <option value="30" data-sqm-per-crate="15" data-kg-per-sqm="78">30 мм Уличное мощение и бассейны (78 кг/м² · 320–340 м²/20GP)</option>
            <option value="50" data-sqm-per-crate="10" data-kg-per-sqm="130">50 мм Проступи, бордюры и въезды (130 кг/м² · 200 м²/20GP)</option>
          </select>
        </div>

        <div>
          <label for="estAreaInput" class="block text-xs font-semibold text-primary-70 uppercase mb-1">Площадь проекта (м²)</label>
          <input type="number" id="estAreaInput" value="480" min="50" max="10000" step="10" class="w-full text-xs p-2.5 border border-primary-10 bg-white rounded outline-none focus:border-black font-copy">
        </div>

        <div>
          <button type="button" id="estCalculateBtn" class="w-full py-2.5 bg-primary-100 text-white text-xs font-semibold uppercase tracking-wider rounded hover:bg-[#E9F551] hover:text-black transition-colors">
            Рассчитать загрузку 20GP
          </button>
        </div>
      </div>

      <div id="estResultsGrid" class="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-6 pt-6 border-t border-primary-10 text-xs">
        <div class="bg-white p-3 border border-primary-10 rounded">
          <span class="text-primary-40 block">Расчетная масса камня</span>
          <strong id="estTotalWeight" class="text-base font-heading font-medium text-primary-100">25.0 т (24 960 кг)</strong>
        </div>
        <div class="bg-white p-3 border border-primary-10 rounded">
          <span class="text-primary-40 block">Усиленная тара</span>
          <strong id="estCratesCount" class="text-base font-heading font-medium text-primary-100">22 ящика (ISPM 15)</strong>
        </div>
        <div class="bg-white p-3 border border-primary-10 rounded">
          <span class="text-primary-40 block">Количество контейнеров</span>
          <strong id="estContainers" class="text-base font-heading font-medium text-primary-100">1 × 20GP (96% веса)</strong>
        </div>
        <div class="bg-white p-3 border border-primary-10 rounded">
          <span class="text-primary-40 block">Морозостойкость ГОСТ</span>
          <strong class="text-base font-heading font-medium text-[#251700]">F100 (&lt;0,22% H₂O)</strong>
        </div>
      </div>
    </div>
'''


def render_progressive_rfq_form_ru(stone_name="Архитектурный известняк Tianya (Запрос СНГ / ЕАЭС)", form_id="cisRfqForm"):
    return f'''
      <form id="{form_id}" data-tianya-form class="space-y-4" method="post" enctype="application/x-www-form-urlencoded">
        <input type="text" name="_honeypot" style="display:none" tabindex="-1" autocomplete="off">
        <input type="hidden" name="stoneOfInterest" value="{stone_name}">
        <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
        <div class="cf-turnstile" data-sitekey="{bts.TURNSTILE_SITE_KEY}" data-theme="light" data-size="normal"></div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="{form_id}_firstName" class="block text-xs font-semibold text-primary-70 uppercase tracking-wider mb-1.5">Имя *</label>
            <input type="text" id="{form_id}_firstName" name="firstName" required placeholder="Например: Александр" class="w-full text-xs p-2.5 border border-primary-10 outline-none focus:border-black rounded-sm bg-white">
          </div>
          <div>
            <label for="{form_id}_lastName" class="block text-xs font-semibold text-primary-70 uppercase tracking-wider mb-1.5">Фамилия / Должность *</label>
            <input type="text" id="{form_id}_lastName" name="lastName" required placeholder="Например: Волков (ГАП / Снабжение)" class="w-full text-xs p-2.5 border border-primary-10 outline-none focus:border-black rounded-sm bg-white">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="{form_id}_email" class="block text-xs font-semibold text-primary-70 uppercase tracking-wider mb-1.5">Рабочий Email *</label>
            <input type="email" id="{form_id}_email" name="email" required placeholder="name@company.ru / .kz / .uz" class="w-full text-xs p-2.5 border border-primary-10 outline-none focus:border-black rounded-sm bg-white">
          </div>
          <div>
            <label for="{form_id}_phone" class="block text-xs font-semibold text-primary-70 uppercase tracking-wider mb-1.5">Телефон / WhatsApp / Telegram *</label>
            <input type="tel" id="{form_id}_phone" name="phone" required placeholder="+7 / +998 / +996 ..." class="w-full text-xs p-2.5 border border-primary-10 outline-none focus:border-black rounded-sm bg-white">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="{form_id}_company" class="block text-xs font-semibold text-primary-70 uppercase tracking-wider mb-1.5">Компания / Архитектурное бюро</label>
            <input type="text" id="{form_id}_company" name="company" placeholder="Девелопер / Генподрядчик / Бюро" class="w-full text-xs p-2.5 border border-primary-10 outline-none focus:border-black rounded-sm bg-white">
          </div>
          <div>
            <label for="{form_id}_area" class="block text-xs font-semibold text-primary-70 uppercase tracking-wider mb-1.5">Объем проекта (м²)</label>
            <input type="text" id="{form_id}_area" name="projectArea" placeholder="Например: 520 м² (1 × 20GP)" class="w-full text-xs p-2.5 border border-primary-10 outline-none focus:border-black rounded-sm bg-white">
          </div>
        </div>

        <div>
          <label for="{form_id}_message" class="block text-xs font-semibold text-primary-70 uppercase tracking-wider mb-1.5">Спецификация, станция назначения и условия (FOB / CIP / CIF)</label>
          <textarea id="{form_id}_message" name="message" rows="3" placeholder="Укажите интересующие коллекции (например, Guyu, Lanting, Xuanzhen), толщину (20/30 мм), город доставки (Москва, Алматы, Астана, Ташкент) и адрес для курьерской отправки образцов..." class="w-full text-xs p-2.5 border border-primary-10 outline-none focus:border-black rounded-sm bg-white"></textarea>
        </div>

        <div class="flex items-center gap-2.5 py-1">
          <input type="checkbox" id="{form_id}_sampleBox" name="sampleBox" checked class="w-4 h-4 accent-black rounded">
          <label for="{form_id}_sampleBox" class="text-xs text-primary-80 cursor-pointer select-none">Отправить бесплатный бокс с физическими образцами известняка и протоколами испытаний (ГОСТ / ASTM)</label>
        </div>

        <button type="submit" class="w-full py-3.5 px-6 bg-primary-100 text-white font-semibold text-xs uppercase tracking-wider rounded-sm hover:bg-[#E9F551] hover:text-black transition-colors cursor-pointer shadow-sm">
          Отправить запрос напрямую на завод (info@tianyastone.com)
        </button>
        <div data-form-status class="text-xs text-primary-70 text-center"></div>
      </form>
'''


def render_footer_ru(depth=1):
    r = bts.get_rel_path(depth)
    return f'''
  <!-- Подвал сайта (RU / ЕАЭС / СНГ) -->
  <footer class="bg-primary-100 text-white pt-16 pb-12 mt-16 border-t border-primary-80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 pb-12 border-b border-primary-80 text-sm">
        <div class="lg:col-span-2 space-y-4">
          <a href="{r}ru/index.html" class="flex items-center gap-3.5 group inline-flex">
            <img src="{r}assets/images/logo/tianya-logo.webp" alt="Tianya Stone Logo" class="h-11 w-auto object-contain">
            <div class="flex flex-col justify-center">
              <span class="font-brand font-bold text-2xl tracking-[0.12em] text-white leading-none">TIANYA</span>
              <span class="font-copy text-[10px] font-semibold tracking-[0.3em] text-[#E9F551] uppercase mt-1">LIMESTONE · СНГ</span>
            </div>
          </a>
          <p class="font-heading italic text-sm text-[#E9F551] mt-1 mb-1">Природный архитектурный известняк высокой плотности (F100 · &lt;0,22% H₂O)</p>
          <p class="text-primary-40 font-copy text-xs leading-relaxed max-w-sm">
            Fujian Tianya Cultural Stone Co., Ltd. (осн. в 2000 г.) — владелец карьеров и завод полного цикла (ЧПУ 5 осей, галтовка, пескоструйная обработка) в г. Шуйтоу, пров. Фуцзянь, КНР. Прямые контейнерные поставки в РФ, Казахстан, Узбекистан и страны ЕАЭС.
          </p>
          <div class="text-xs text-primary-40 space-y-1">
            <p><strong>Адрес завода:</strong> {bts.COMPANY_INFO['address']}</p>
            <p><strong>Единый Email для запросов:</strong> <a href="mailto:{bts.COMPANY_INFO['email']}" class="text-[#E9F551] hover:underline font-semibold">{bts.COMPANY_INFO['email']}</a></p>
            <p><strong>WhatsApp / Телефон:</strong> <a href="tel:{bts.COMPANY_INFO['phone']}" class="text-white hover:text-[#E9F551]">{bts.COMPANY_INFO['phone']}</a> / {bts.COMPANY_INFO['phone_alt']}</p>
            <p><strong>Telegram (Отдел СНГ):</strong> <a href="{TELEGRAM_CIS_URL}" target="_blank" rel="noopener" class="text-[#E9F551] hover:underline">{TELEGRAM_CIS_HANDLE}</a></p>
          </div>
        </div>

        <div>
          <h4 class="font-heading italic text-base text-[#E9F551] mb-4">Фактуры известняка</h4>
          <ul class="space-y-2 text-xs text-primary-40">
            <li><a href="{r}stone-flooring/limestone/tumbled/index.html" class="hover:text-white">Tumbled · Галтованный антик (8)</a></li>
            <li><a href="{r}stone-flooring/limestone/antique/index.html" class="hover:text-white">Antique · Ручная теска (10)</a></li>
            <li><a href="{r}stone-flooring/limestone/lightly-distressed/index.html" class="hover:text-white">Lightly Distressed · Деликатный (6)</a></li>
            <li><a href="{r}stone-flooring/limestone/sandblasted-brushed/index.html" class="hover:text-white">Sandblasted &amp; Brushed · Браш P5 (2)</a></li>
            <li><a href="{r}stone-flooring/limestone/sandblasted/index.html" class="hover:text-white">Sandblasted · Пескоструй R11 (3)</a></li>
            <li class="pt-2"><a href="{r}ru/index.html#catalog-29" class="text-white font-semibold hover:underline">→ Все 29 коллекций</a></li>
          </ul>
        </div>

        <div>
          <h4 class="font-heading italic text-base text-[#E9F551] mb-4">Разделы для ЕАЭС и СНГ</h4>
          <ul class="space-y-2 text-xs text-primary-40">
            <li><a href="{r}ru/cis-central-asia/index.html" class="text-white font-semibold hover:text-[#E9F551]">Хаб СНГ: РФ · Казахстан · Узбекистан</a></li>
            <li><a href="{r}ru/cis-central-asia/index.html#gost-matrix" class="hover:text-white">Таблица ГОСТ 30629-2011 ↔ ASTM</a></li>
            <li><a href="{r}ru/cis-central-asia/index.html#eu-replacement" class="hover:text-white">Импортозамещение Европы 1:1</a></li>
            <li><a href="{r}ru/cis-central-asia/index.html#rail-logistics" class="hover:text-white">Ж/Д доставка: Достык · Хоргос · Москва</a></li>
            <li><a href="{r}ru/cis-central-asia/index.html#customs-cny" class="hover:text-white">Коды ТН ВЭД 6802 и оплата в CNY/RUB</a></li>
            <li><a href="{r}stone-flooring/other-categories/index.html" class="hover:text-white">Гибкий камень, травертин и песчаник</a></li>
          </ul>
        </div>

        <div>
          <h4 class="font-heading italic text-base text-[#E9F551] mb-4">Стандарты и ИИ-данные</h4>
          <ul class="space-y-2 text-xs text-primary-40">
            <li><a href="{r}compliance/index.html" class="hover:text-white">Водопоглощение &lt;0,22% (ASTM C97)</a></li>
            <li><a href="{r}compliance/index.html" class="hover:text-white">Прочность при сжатии 128,5 МПа</a></li>
            <li><a href="{r}compliance/index.html" class="hover:text-white">Морозостойкость F100 (100 циклов)</a></li>
            <li><a href="{r}compliance/index.html" class="hover:text-white">Радиация I класс (&lt;45 Бк/кг)</a></li>
            <li><a href="{r}ai/cis-gost-matrix.json" class="hover:text-white">JSON-матрица ГОСТ / ЕАЭС (AI API)</a></li>
            <li><a href="{r}llms-full.txt" class="hover:text-white">Полное техруководство (llms-full.txt)</a></li>
          </ul>
        </div>
      </div>

      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-primary-40 gap-4">
        <div>
          © 2000–2026 Fujian Tianya Cultural Stone Co., Ltd. (福建天涯文化石有限公司). Все запросы направляются на <a href="mailto:{bts.COMPANY_INFO['email']}" class="text-white underline">{bts.COMPANY_INFO['email']}</a>.
        </div>
        <div class="flex items-center gap-5">
          <a href="{r}index.html" class="hover:text-white">English Version</a>
          <a href="{r}ru/index.html" class="text-[#E9F551] font-semibold">Русская версия</a>
          <a href="{r}ru/cis-central-asia/index.html" class="hover:text-white">ЕАЭС / СНГ</a>
          <a href="{r}sitemap.xml" class="hover:text-white">Sitemap</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Модальное окно поиска -->
  <div id="searchModal" class="search-modal">
    <div class="search-modal-box">
      <div class="p-4 border-b border-primary-10 flex items-center gap-3">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#665D4D" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21L16.65 16.65"/></svg>
        <input id="searchInput" type="text" placeholder="Поиск коллекций известняка (Guyu, Lanting, Tumbled, Antique, Xuanzhen)..." class="w-full text-sm font-copy outline-none text-primary-100 placeholder-primary-40">
        <button id="searchCloseBtn" class="text-xs bg-primary-10 text-primary-70 px-2.5 py-1 rounded hover:bg-primary-100 hover:text-white">ESC</button>
      </div>
      <div id="searchResults" class="p-2"></div>
    </div>
  </div>

  <!-- Модальное окно галереи -->
  <div id="galleryModal" class="gallery-modal">
    <button id="galleryModalClose" class="absolute top-6 right-6 text-white text-2xl font-light hover:text-[#E9F551] z-50">✕</button>
    <div class="gallery-modal-content">
      <img id="galleryModalImg" src="" alt="Limestone full view">
    </div>
  </div>

  <!-- Плавающая кнопка WhatsApp + Telegram (Отдел СНГ) -->
  <style>
    .ty-wa-float{{position:fixed;right:20px;bottom:20px;z-index:9999;width:60px;height:60px;border-radius:50%;background:#25D366;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 16px rgba(0,0,0,.25);cursor:pointer;border:none;transition:transform .2s ease}}
    .ty-wa-float:hover{{transform:scale(1.08)}}
    .ty-wa-float svg{{width:32px;height:32px;fill:#fff}}
    .ty-wa-float::after{{content:"1";position:absolute;top:-2px;right:-2px;width:22px;height:22px;border-radius:50%;background:#e02424;color:#fff;font:700 12px/22px Arial;text-align:center}}
    .ty-wa-menu{{position:fixed;right:20px;bottom:88px;z-index:9999;background:#fff;border-radius:12px;box-shadow:0 8px 32px rgba(0,0,0,.22);padding:8px;display:none;min-width:255px}}
    .ty-wa-menu.open{{display:block}}
    .ty-wa-menu a{{display:flex;align-items:center;gap:10px;padding:11px 12px;text-decoration:none;border-radius:8px;color:#1a1a18;font:600 13.5px/1.3 -apple-system,"PingFang SC","Microsoft YaHei",sans-serif}}
    .ty-wa-menu a:hover{{background:#f0f7f0}}
    .ty-wa-menu a svg{{width:24px;height:24px;fill:#25D366;flex-shrink:0}}
    .ty-wa-menu a.ty-tg-link svg{{fill:#229ED9}}
    .ty-wa-menu a small{{display:block;font-weight:400;color:#666;font-size:11.5px}}
    .ty-mobile-cta{{display:none;position:fixed;left:0;right:0;bottom:0;z-index:9998;background:#1a1a18;border-top:1px solid rgba(255,255,255,.12);padding:8px 10px calc(8px + env(safe-area-inset-bottom))}}
    .ty-mobile-cta a{{flex:1;display:flex;align-items:center;justify-content:center;gap:6px;padding:12px 4px;border-radius:8px;text-decoration:none;font:600 13px/1.2 -apple-system,"PingFang SC","Microsoft YaHei",sans-serif}}
    .ty-mobile-cta .ty-btn-call{{background:transparent;color:#f5f0e6;border:1px solid rgba(245,240,230,.35)}}
    .ty-mobile-cta .ty-btn-wa{{background:#25D366;color:#fff}}
    .ty-mobile-cta .ty-btn-rfq{{background:#f5f0e6;color:#1a1a18}}
    @media (max-width:768px){{.ty-mobile-cta{{display:flex;gap:8px}}.ty-wa-float{{bottom:76px;right:14px;width:52px;height:52px}}.ty-wa-menu{{bottom:140px;right:14px}}body{{padding-bottom:70px}}}}
  </style>
  <button class="ty-wa-float" id="tyWaFloat" aria-label="Связаться в WhatsApp или Telegram">
    <svg viewBox="0 0 32 32"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.4.7 4.6 1.9 6.5L4 29l7.7-1.8c1.8 1 3.9 1.6 6.1 1.6 6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.8c-1.9 0-3.7-.5-5.3-1.5l-.4-.2-4.6 1.1 1.2-4.5-.3-.4c-1-1.6-1.6-3.5-1.6-5.5 0-5.5 4.5-10 10-10s10 4.5 10 10-4.5 10.8-10 10.8zm5.5-7.4c-.3-.2-1.8-.9-2-1-.3-.1-.5-.2-.7.1-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.9-1c.3-.3.3-.5.5-.8.1-.3 0-.5-.1-.7-.1-.2-.7-1.7-1-2.3-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.2-.8.7-.3.5-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4-.1-.1-.3-.2-.6-.3z"/></svg>
  </button>
  <div class="ty-wa-menu" id="tyWaMenu">
    <a href="https://wa.me/8618960366169?text=Здравствуйте%2C%20Tianya%20Limestone!%20Интересует%20поставка%20известняка%20и%20образцы." target="_blank" rel="noopener" data-wa-num="8618960366169">
      <svg viewBox="0 0 32 32"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.4.7 4.6 1.9 6.5L4 29l7.7-1.8c1.8 1 3.9 1.6 6.1 1.6 6.6 0 12-5.4 12-12S22.6 3 16 3z"/></svg>
      <span>WhatsApp Экспорт 1<small>+86 189 6036 6169</small></span>
    </a>
    <a href="https://wa.me/8617805982800?text=Здравствуйте%2C%20Tianya%20Limestone!%20Интересует%20поставка%20известняка%20и%20образцы." target="_blank" rel="noopener" data-wa-num="8617805982800">
      <svg viewBox="0 0 32 32"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.4.7 4.6 1.9 6.5L4 29l7.7-1.8c1.8 1 3.9 1.6 6.1 1.6 6.6 0 12-5.4 12-12S22.6 3 16 3z"/></svg>
      <span>WhatsApp Экспорт 2<small>+86 178 0598 2800</small></span>
    </a>
    <a href="{TELEGRAM_CIS_URL}" target="_blank" rel="noopener" class="ty-tg-link">
      <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69.01-.03.01-.14-.07-.2-.08-.06-.19-.04-.27-.02-.12.02-1.96 1.25-5.54 3.69-.52.36-1 .53-1.42.52-.47-.01-1.37-.26-2.03-.48-.82-.27-1.47-.42-1.42-.88.03-.24.35-.49.96-.75 3.78-1.65 6.31-2.74 7.58-3.27 3.61-1.51 4.35-1.77 4.84-1.78.11 0 .35.03.5.16.13.1.17.24.18.34.02.07.02.21.01.33z"/></svg>
      <span>Telegram (РФ · Казахстан · СНГ)<small>{TELEGRAM_CIS_HANDLE}</small></span>
    </a>
  </div>
  <nav class="ty-mobile-cta">
    <a class="ty-btn-call" href="tel:+8618960366169" data-track="phone_click">📞 Звонок</a>
    <a class="ty-btn-wa" href="https://wa.me/8618960366169?text=Здравствуйте%2C%20Tianya%20Limestone!%20Интересует%20поставка%20известняка." target="_blank" rel="noopener" data-track="whatsapp_click">💬 WhatsApp</a>
    <a class="ty-btn-rfq" href="#enquiry-section" data-track="cta_click">Запрос КП</a>
  </nav>
  <script>
  (function(){{
    var float=document.getElementById('tyWaFloat'),menu=document.getElementById('tyWaMenu');
    if(float&&menu){{
      float.addEventListener('click',function(e){{e.stopPropagation();menu.classList.toggle('open');}});
      document.addEventListener('click',function(e){{if(!menu.contains(e.target))menu.classList.remove('open');}});
    }}
  }})();
  </script>
'''


def generate_ru_home_page(all_products):
    depth = 1
    r = bts.get_rel_path(depth)
    canonical = f"{bts.COMPANY_INFO['domain']}/ru/"
    title = "Архитектурный известняк Tianya Limestone — Прямые поставки с карьера в РФ, Казахстан и СНГ (ГОСТ 30629-2011 · F100)"
    description = (
        "Завод Fujian Tianya Cultural Stone (Шуйтоу, КНР): 29 коллекций высокоплотного природного известняка "
        "(водопоглощение <0,22%, прочность 128,5 МПа, морозостойкость F100 по ГОСТ 30629-2011). "
        "Прямые ж/д и морские поставки 20GP в Москву, Алматы, Астану и Ташкент."
    )

    # Group products by finish
    finish_sections_html = []
    for f_slug, f_meta in bts.FINISH_MAP.items():
        ru_meta = FINISH_RU_MAP.get(f_slug, {})
        prods = [p for p in all_products if p["finish"] == f_slug]
        cards_html = []
        for p in prods:
            thumb = r + p["thumbnail"].lstrip("/")
            scene_img = r + (p["images"][1] if len(p.get("images", [])) > 1 else p["thumbnail"]).lstrip("/")
            prod_href = r + p["url"]
            cards_html.append(f'''
            <div class="group border border-primary-10 bg-white rounded-sm overflow-hidden flex flex-col justify-between hover:border-black transition-all">
              <a href="{prod_href}" class="block relative aspect-[4/3] bg-primary-10 overflow-hidden">
                <img src="{thumb}" alt="{p['title']} — Архитектурный известняк ({ru_meta.get('title_ru', f_meta['title'])})" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                <span class="absolute top-2.5 left-2.5 bg-primary-100/90 text-[#E9F551] text-[10px] font-semibold uppercase tracking-wider px-2.5 py-1 rounded-sm">
                  {f_meta['slip_rating'].split('(')[0].strip()} · F100
                </span>
              </a>
              <div class="p-4 flex-grow flex flex-col justify-between">
                <div>
                  <div class="flex items-baseline justify-between gap-2">
                    <h4 class="font-heading text-lg font-medium text-primary-100 group-hover:underline">
                      <a href="{prod_href}">{p['title']}</a>
                    </h4>
                    <span class="text-xs text-primary-60 font-copy">{p.get('subtitle', '')}</span>
                  </div>
                  <p class="text-xs text-primary-70 mt-1.5 line-clamp-2 font-copy">
                    Высокоплотный биокластический известняк (&lt;0,22% H₂O, 128,5 МПа). Форматы: 600×400, 600×600, French Pattern, 20/30 мм.
                  </p>
                </div>
                <div class="mt-4 pt-3 border-t border-primary-10 flex items-center justify-between text-xs">
                  <a href="{prod_href}" class="font-semibold text-primary-100 hover:underline">Спецификация и фото →</a>
                  <a href="#enquiry-section" class="text-primary-70 hover:text-black underline">Запрос КП</a>
                </div>
              </div>
            </div>
            ''')

        finish_sections_html.append(f'''
        <div class="mb-14" id="finish-{f_slug}">
          <div class="flex flex-col md:flex-row md:items-end justify-between border-b border-primary-15 pb-4 mb-6 gap-3">
            <div>
              <span class="text-xs font-semibold uppercase tracking-wider text-primary-60 block mb-1">{ru_meta.get('badge_ru', '')}</span>
              <h3 class="font-heading text-2xl font-medium text-primary-100">{ru_meta.get('title_ru', f_meta['title'])} ({len(prods)} коллекций)</h3>
              <p class="text-xs text-primary-70 mt-1 max-w-3xl font-copy">{ru_meta.get('desc_ru', f_meta['description'])}</p>
            </div>
            <a href="{r}stone-flooring/limestone/{f_slug}/index.html" class="text-xs font-semibold text-primary-100 hover:underline whitespace-nowrap">
              Смотреть раздел {f_meta['title']} →
            </a>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {''.join(cards_html)}
          </div>
        </div>
        ''')

    gost_rows_html = []
    for row in GOST_EQUIVALENCE_ROWS:
        gost_rows_html.append(f'''
        <tr class="border-b border-primary-10 hover:bg-primary-2/60">
          <td class="py-3 px-4 font-semibold text-primary-100">{row['parameter_ru']}</td>
          <td class="py-3 px-4 text-primary-80 font-mono text-xs">{row['gost_standard']}</td>
          <td class="py-3 px-4 text-primary-70 font-mono text-xs">{row['intl_standard']}</td>
          <td class="py-3 px-4 font-bold text-[#251700] bg-[#F7FFEC]">{row['tianya_value']}</td>
          <td class="py-3 px-4 text-primary-70">{row['advantage_ru']}</td>
        </tr>
        ''')

    faq_entities = [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in CIS_GEO_FAQS_RU[:5]
    ]
    faq_html = []
    for q, a in CIS_GEO_FAQS_RU[:5]:
        faq_html.append(f'''
        <div class="border border-primary-10 rounded p-5 bg-white">
          <h3 class="font-heading text-lg font-medium text-primary-100 mb-2">{q}</h3>
          <p class="text-xs sm:text-sm text-primary-70 leading-relaxed font-copy">{a}</p>
        </div>
        ''')

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": f"{bts.COMPANY_INFO['domain']}/#organization",
                "name": bts.COMPANY_INFO["name"],
                "alternateName": ["Tianya Limestone", "ТяньЯ Лаймстоун", "福建天涯文化石有限公司"],
                "url": canonical,
                "logo": f"{bts.COMPANY_INFO['domain']}/assets/images/logo/tianya-logo.webp",
                "email": bts.COMPANY_INFO["email"],
                "telephone": bts.COMPANY_INFO["phone"],
                "areaServed": ["RU", "KZ", "UZ", "KG", "TJ", "BY", "AM", "AZ", "AU", "US", "EU"],
                "contactPoint": [
                    {
                        "@type": "ContactPoint",
                        "telephone": bts.COMPANY_INFO["phone"],
                        "email": bts.COMPANY_INFO["email"],
                        "contactType": "sales",
                        "areaServed": ["RU", "KZ", "UZ", "KG", "TJ"],
                        "availableLanguage": ["Russian", "English", "Chinese"]
                    }
                ]
            },
            {
                "@type": "WebPage",
                "@id": canonical,
                "url": canonical,
                "name": title,
                "description": description,
                "inLanguage": "ru-RU"
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_entities
            }
        ]
    }

    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
  {bts.GA4_SNIPPET}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="архитектурный известняк, фасадный известняк ГОСТ 30629-2011, плиты мощения из известняка, галтованный известняк антик, копинговый камень для бассейна, импортозамещение бургундского известняка, известняк F100 морозостойкий, поставка камня из Китая в Россию Казахстан Узбекистан">
  <meta name="yandex-verification" content="{YANDEX_VERIFICATION_CODE}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{bts.COMPANY_INFO['domain']}/">
  <link rel="alternate" hreflang="ru" href="{canonical}">
  <link rel="alternate" hreflang="ru-RU" href="{bts.COMPANY_INFO['domain']}/ru/cis-central-asia/">
  <link rel="alternate" hreflang="ru-KZ" href="{bts.COMPANY_INFO['domain']}/ru/cis-central-asia/">
  <link rel="alternate" hreflang="ru-UZ" href="{bts.COMPANY_INFO['domain']}/ru/cis-central-asia/">
  <link rel="alternate" hreflang="x-default" href="{bts.COMPANY_INFO['domain']}/">
  <link rel="icon" type="image/webp" href="{r}assets/images/logo/favicon.webp">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="ru_RU">
  <meta property="og:locale:alternate" content="ru_KZ">
  <meta property="og:locale:alternate" content="ru_UZ">
  <meta property="og:locale:alternate" content="en_US">
  <meta property="og:site_name" content="Tianya Limestone">
  <meta property="og:image" content="{bts.COMPANY_INFO['domain']}/assets/images/hero/hero-limestone.webp">
  <script type="application/ld+json">
{json.dumps(schema_data, indent=2, ensure_ascii=False)}
  </script>
  <link rel="stylesheet" href="{r}assets/css/eco-outdoor.css?v=3">
  <link rel="stylesheet" href="{r}assets/css/tianya-custom.css?v=3">
</head>
<body class="bg-white text-primary-100">
  {render_header_ru(depth=depth, active_tab='ru_home')}

  <main>
    <!-- Hero Секция (RU / СНГ) -->
    <section class="relative bg-primary-100 text-white overflow-hidden">
      <div class="grid grid-cols-1 lg:grid-cols-12 min-h-[520px]">
        <div class="lg:col-span-7 p-8 sm:p-12 lg:p-16 flex flex-col justify-center z-10">
          <div class="inline-flex items-center gap-2 bg-white/10 border border-white/20 text-[#E9F551] text-xs px-3 py-1 rounded-sm w-fit mb-5">
            <span>ГОСТ 30629-2011 · Марка морозостойкости F100 · Водопоглощение &lt;0,22%</span>
          </div>
          <h1 class="font-heading text-3xl sm:text-4xl lg:text-5xl font-medium leading-tight mb-5">
            Природный архитектурный известняк прямиком с карьера и завода в Шуйтоу
          </h1>
          <p class="text-sm sm:text-base text-primary-20 font-copy leading-relaxed mb-8 max-w-2xl">
            <strong>Fujian Tianya Cultural Stone Co., Ltd.</strong> (основан в 2000 г.) производит 29 коллекций высокоплотного морского биокластического известняка (2650 кг/м³, 128,5 МПа) для фасадов, цоколей, террас и бассейнов. Прямая альтернатива 1:1 французскому Бургундскому камню, португальскому Moleanos и немецкому Jura с ж/д и морской доставкой в <strong>Москву, Алматы, Астану и Ташкент</strong>.
          </p>
          <div class="flex flex-wrap gap-3">
            <a href="#catalog-29" class="px-6 py-3.5 text-xs font-semibold uppercase tracking-wider rounded-sm transition-colors" style="background-color:#E9F551;color:#1a1a18;">
              Смотреть 29 коллекций
            </a>
            <a href="{r}ru/cis-central-asia/index.html" class="px-6 py-3.5 border border-white text-white text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-white hover:text-black transition-colors" style="background-color:rgba(255,255,255,0.12);">
              Хаб ЕАЭС: ГОСТ · Импортозамещение · Ж/Д Логистика →
            </a>
            <a href="#enquiry-section" class="px-6 py-3.5 border text-xs font-semibold uppercase tracking-wider rounded-sm transition-colors" style="border-color:#E9F551;color:#E9F551;">
              Бесплатные образцы ({bts.COMPANY_INFO['email']})
            </a>
          </div>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-10 pt-8 border-t border-white/15 text-xs">
            <div>
              <strong class="text-xl font-heading block" style="color:#E9F551;">&lt; 0,22%</strong>
              <span class="text-primary-40">Водопоглощение (ASTM C97)</span>
            </div>
            <div>
              <strong class="text-xl font-heading block" style="color:#E9F551;">128,5 МПа</strong>
              <span class="text-primary-40">Прочность на сжатие</span>
            </div>
            <div>
              <strong class="text-xl font-heading block" style="color:#E9F551;">F100 · НГ</strong>
              <span class="text-primary-40">Морозостойкость и пожаробезопасность</span>
            </div>
            <div>
              <strong class="text-xl font-heading block" style="color:#E9F551;">12–22 дня</strong>
              <span class="text-primary-40">Ж/Д Достык · Хоргос · Забайкальск</span>
            </div>
          </div>
        </div>
        <div class="lg:col-span-5 relative min-h-[320px]">
          <img src="{r}assets/images/hero/hero-limestone.webp" alt="Архитектурный известняк Tianya Limestone для террас, фасадов и бассейнов" class="w-full h-full object-cover">
          <div class="absolute bottom-4 left-4 right-4 p-4 rounded text-xs text-white border" style="background-color:rgba(26,26,24,0.88);border-color:rgba(255,255,255,0.22);">
            <div class="font-semibold" style="color:#E9F551;">Экспортный стандарт упаковки ISPM 15 (20GP = 26–27 тонн)</div>
            <div class="text-primary-20 mt-0.5">Прямые расчеты в CNY (CIPS), RUB, KZT, USD · Полный пакет документов ТН ВЭД 6802 / 6801</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Блок быстрого перехода в Инженерный Хаб ЕАЭС и Центральной Азии -->
    <section class="border-b border-primary-15 py-6" style="background-color:#F7FFEC;">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="text-xs sm:text-sm text-primary-100">
          <span class="font-bold uppercase tracking-wider px-2.5 py-1 rounded-sm mr-2" style="background-color:#251700;color:#E9F551;">Спецраздел СНГ</span>
          <strong>Проектируете объект в РФ, Казахстане или Узбекистане?</strong> Изучите таблицу соответствия ГОСТ 30629-2011, матрицу замены европейского известняка 1:1 и сроки ж/д доставки 20GP контейнеров.
        </div>
        <a href="{r}ru/cis-central-asia/index.html" class="px-5 py-2.5 bg-primary-100 text-white text-xs font-semibold uppercase tracking-wider rounded-sm hover:bg-black whitespace-nowrap">
          Открыть инженерный портал ЕАЭС и СНГ →
        </a>
      </div>
    </section>

    <!-- Каталог 29 коллекций по 5 фактурам -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14" id="catalog-29">
      <div class="max-w-3xl mb-10">
        <span class="text-xs uppercase font-semibold tracking-wider text-primary-60 block mb-2">Полная заводская программа (29 артикулов)</span>
        <h2 class="font-heading text-3xl sm:text-4xl font-medium text-primary-100 mb-3">29 коллекций природного известняка в 5 архитектурных фактурах</h2>
        <p class="text-sm text-primary-70 font-copy leading-relaxed">
          Каждая коллекция выпиливается из плотных морских биокластических блоков на 5-осевых станках с ЧПУ (допуск ±1,0 мм). Доступны модульные плиты 600×400, 600×600, 800×400, комплекты French Pattern (4 размера), ступени и Г-образный копинговый камень для бассейнов.
        </p>
      </div>

      {''.join(finish_sections_html)}
    </section>

    <!-- Сводная таблица ГОСТ 30629-2011 ↔ ASTM -->
    <section class="bg-primary-2 py-14 border-t border-b border-primary-10">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
          <div>
            <span class="text-xs uppercase font-semibold tracking-wider text-primary-60 block mb-1">Лабораторная сертификация SGS / TÜV</span>
            <h2 class="font-heading text-2xl sm:text-3xl font-medium text-primary-100">Физико-механические показатели: ГОСТ 30629-2011 ↔ ASTM / EN</h2>
          </div>
          <a href="{r}ru/cis-central-asia/index.html#eu-replacement" class="text-xs font-semibold text-primary-100 underline">
            Смотреть таблицу импортозамещения европейского камня 1:1 →
          </a>
        </div>

        <div class="overflow-x-auto bg-white border border-primary-10 rounded-sm shadow-sm">
          <table class="w-full text-left border-collapse text-xs sm:text-sm font-copy">
            <thead>
              <tr class="bg-primary-100 text-white">
                <th class="py-3.5 px-4 font-semibold">Показатель</th>
                <th class="py-3.5 px-4 font-semibold">Стандарт РФ / ЕАЭС</th>
                <th class="py-3.5 px-4 font-semibold">Международный стандарт</th>
                <th class="py-3.5 px-4 font-semibold text-[#E9F551]">Сертифицировано Tianya</th>
                <th class="py-3.5 px-4 font-semibold">Значение для климата РФ и СНГ</th>
              </tr>
            </thead>
            <tbody>
              {''.join(gost_rows_html)}
            </tbody>
          </table>
        </div>

        {render_container_estimator_ru()}
      </div>
    </section>

    <!-- Ответы для архитекторов, ГИП и Яндекс Нейро -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
      <h2 class="font-heading text-2xl sm:text-3xl font-medium text-primary-100 mb-6">Часто задаваемые вопросы (База знаний для ГИП / ГАП и Яндекс Нейро)</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        {''.join(faq_html)}
      </div>
    </section>

    <!-- Секция запроса КП и образцов (info@tianyastone.com) -->
    <section id="enquiry-section" class="bg-primary-2 border-t border-primary-10 py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
          <div class="lg:col-span-5 space-y-5">
            <span class="text-xs font-semibold uppercase tracking-wider text-primary-60 block">Прямой контракт с заводом-изготовителем</span>
            <h2 class="font-heading text-3xl font-medium text-primary-100">Запросить расчет стоимости (FOB / CIP / CIF) и бокс с образцами</h2>
            <p class="text-xs sm:text-sm text-primary-70 font-copy leading-relaxed">
              Отправьте ведомость объемов или архитектурную спецификацию. Инженерный отдел экспорта подготовит коммерческое предложение с расчетом погрузки по ящикам (20GP) и сроками доставки до Москвы, Алматы, Астаны или Ташкента в течение <strong>2–4 часов</strong>.
            </p>
            <div class="bg-white border border-primary-10 p-5 rounded-sm space-y-2.5 text-xs">
              <div><strong>Единый Email отдела экспорта:</strong> <a href="mailto:{bts.COMPANY_INFO['email']}" class="text-primary-100 underline font-semibold">{bts.COMPANY_INFO['email']}</a></div>
              <div><strong>WhatsApp / WeChat (24/7):</strong> <a href="https://wa.me/8618960366169" class="underline">{bts.COMPANY_INFO['phone']}</a> / {bts.COMPANY_INFO['phone_alt']}</div>
              <div><strong>Telegram (СНГ и Центральная Азия):</strong> <a href="{TELEGRAM_CIS_URL}" target="_blank" rel="noopener" class="underline font-semibold">{TELEGRAM_CIS_HANDLE}</a></div>
              <div><strong>Минимальная партия (MOQ):</strong> от 100 м² · Контейнерные скидки от 1 × 20GP (320–520 м²)</div>
              <div><strong>Валюта контракта:</strong> CNY (юани через CIPS), RUB, KZT, USD</div>
            </div>
          </div>
          <div class="lg:col-span-7 bg-white border border-primary-10 p-6 sm:p-8 rounded-sm shadow-sm">
            {render_progressive_rfq_form_ru("Запрос с главного русского портала (/ru/)", "ruHomeRfqForm")}
          </div>
        </div>
      </div>
    </section>
  </main>

  {render_footer_ru(depth=depth)}
  <script src="{r}assets/js/search_index.js"></script>
  <script src="{r}assets/js/main.js?v=20261016_cis"></script>
</body>
</html>'''


def generate_cis_hub_page(all_products):
    depth = 2
    r = bts.get_rel_path(depth)
    canonical = f"{bts.COMPANY_INFO['domain']}/ru/cis-central-asia/"
    title = "Известняк для РФ, Казахстана и Узбекистана: ГОСТ 30629-2011, Импортозамещение 1:1 и Ж/Д Логистика 20GP | Tianya Limestone"
    description = (
        "Инженерный портал Tianya Limestone для России, Казахстана и Центральной Азии: матрица соответствия ГОСТ 30629-2011 ↔ ASTM C97/C170/C666 "
        "(водопоглощение <0,22%, F100), таблица замены европейского известняка 1:1 (Бургундия, Moleanos, Jura) и ж/д доставка через Достык, Хоргос и Забайкальск."
    )

    gost_rows_html = []
    for row in GOST_EQUIVALENCE_ROWS:
        gost_rows_html.append(f'''
        <tr class="border-b border-primary-10 hover:bg-primary-2/60">
          <td class="py-3 px-4 font-semibold text-primary-100">{row['parameter_ru']}<br><span class="text-[11px] font-normal text-primary-40">{row['parameter_en']}</span></td>
          <td class="py-3 px-4 text-primary-80 font-mono text-xs">{row['gost_standard']}</td>
          <td class="py-3 px-4 text-primary-70 font-mono text-xs">{row['intl_standard']}</td>
          <td class="py-3 px-4 text-primary-70 text-xs">{row['gost_norm']}</td>
          <td class="py-3 px-4 font-bold text-[#251700] bg-[#F7FFEC]">{row['tianya_value']}</td>
          <td class="py-3 px-4 text-primary-70 text-xs">{row['advantage_ru']}</td>
        </tr>
        ''')

    replacement_rows_html = []
    for item in STONE_REPLACEMENT_MATRIX:
        links_html = []
        for model_name, model_rel in item["tianya_models"]:
            links_html.append(
                f'<a href="{r}{model_rel}" class="inline-block bg-primary-2 border border-primary-15 px-2.5 py-1 rounded-sm text-xs font-semibold text-primary-100 hover:bg-[#E9F551] hover:border-black transition-colors mr-1.5 mb-1.5">{model_name}</a>'
            )
        replacement_rows_html.append(f'''
        <tr class="border-b border-primary-10 align-top hover:bg-primary-2/40">
          <td class="py-4 px-4 font-semibold text-primary-100">{item['eu_stone']}</td>
          <td class="py-4 px-4 text-xs text-primary-70">{item['eu_issue']}</td>
          <td class="py-4 px-4">{''.join(links_html)}</td>
          <td class="py-4 px-4 text-xs text-primary-70">{item['visual_ru']}</td>
          <td class="py-4 px-4 text-xs font-medium text-[#251700] bg-[#F7FFEC]/60">{item['benefit_ru']}</td>
        </tr>
        ''')

    logistics_rows_html = []
    for corr in CIS_LOGISTICS_CORRIDORS:
        logistics_rows_html.append(f'''
        <tr class="border-b border-primary-10 align-top hover:bg-primary-2/40">
          <td class="py-3.5 px-4 font-semibold text-primary-100">{corr['country_ru']}</td>
          <td class="py-3.5 px-4 text-xs font-medium text-primary-80">{corr['hubs_ru']}</td>
          <td class="py-3.5 px-4 text-xs text-primary-70">{corr['route_ru']}</td>
          <td class="py-3.5 px-4 text-xs font-bold text-[#251700] bg-[#F7FFEC] whitespace-nowrap">{corr['transit_days']}</td>
          <td class="py-3.5 px-4 text-xs font-mono text-primary-80">{corr['incoterms']}</td>
          <td class="py-3.5 px-4 text-xs text-primary-70">{corr['docs_ru']}</td>
        </tr>
        ''')

    faq_entities = [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in CIS_GEO_FAQS_RU
    ]
    faq_blocks_html = []
    for idx, (q, a) in enumerate(CIS_GEO_FAQS_RU, start=1):
        faq_blocks_html.append(f'''
        <div class="border border-primary-10 bg-white p-6 rounded-sm shadow-sm">
          <div class="text-[11px] font-mono uppercase tracking-wider text-primary-40 mb-1">Инженерный ответ GEO #{idx} · Яндекс Нейро / Алиса AI</div>
          <h3 class="font-heading text-lg sm:text-xl font-medium text-primary-100 mb-2.5">{q}</h3>
          <p class="text-xs sm:text-sm text-primary-70 leading-relaxed font-copy">{a}</p>
        </div>
        ''')

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": f"{bts.COMPANY_INFO['domain']}/#organization",
                "name": bts.COMPANY_INFO["name"],
                "alternateName": ["Tianya Limestone", "ТяньЯ Лаймстоун", "福建天涯文化石有限公司"],
                "url": canonical,
                "email": bts.COMPANY_INFO["email"],
                "telephone": bts.COMPANY_INFO["phone"],
                "areaServed": ["RU", "KZ", "UZ", "KG", "TJ", "BY", "AM", "AZ"]
            },
            {
                "@type": "TechArticle",
                "headline": title,
                "description": description,
                "inLanguage": "ru-RU",
                "url": canonical,
                "datePublished": "2026-10-16",
                "dateModified": "2026-10-16",
                "author": {"@type": "Organization", "name": bts.COMPANY_INFO["name"], "url": bts.COMPANY_INFO["domain"]},
                "publisher": {"@type": "Organization", "name": bts.COMPANY_INFO["name"], "url": bts.COMPANY_INFO["domain"]}
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_entities
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{bts.COMPANY_INFO['domain']}/"},
                    {"@type": "ListItem", "position": 2, "name": "Русский портал", "item": f"{bts.COMPANY_INFO['domain']}/ru/"},
                    {"@type": "ListItem", "position": 3, "name": "ЕАЭС и Центральная Азия (ГОСТ · Логистика)", "item": canonical}
                ]
            }
        ]
    }

    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
  {bts.GA4_SNIPPET}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="ГОСТ 30629-2011 известняк, морозостойкий известняк F100, импортозамещение бургундского известняка, замена Moleanos Jura, известняк для фасада и цоколя Москва Алматы Ташкент, жд доставка камня из Китая Достык Хоргос, ТН ВЭД 6802 21 000 0">
  <meta name="yandex-verification" content="{YANDEX_VERIFICATION_CODE}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{bts.COMPANY_INFO['domain']}/compliance/">
  <link rel="alternate" hreflang="ru" href="{canonical}">
  <link rel="alternate" hreflang="ru-RU" href="{canonical}">
  <link rel="alternate" hreflang="ru-KZ" href="{canonical}">
  <link rel="alternate" hreflang="ru-UZ" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{bts.COMPANY_INFO['domain']}/compliance/">
  <link rel="icon" type="image/webp" href="{r}assets/images/logo/favicon.webp">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="ru_RU">
  <meta property="og:locale:alternate" content="ru_KZ">
  <meta property="og:locale:alternate" content="ru_UZ">
  <meta property="og:locale:alternate" content="en_US">
  <meta property="og:site_name" content="Tianya Limestone">
  <meta property="og:image" content="{bts.COMPANY_INFO['domain']}/assets/images/hero/hero-limestone.webp">
  <script type="application/ld+json">
{json.dumps(schema_data, indent=2, ensure_ascii=False)}
  </script>
  <link rel="stylesheet" href="{r}assets/css/eco-outdoor.css?v=3">
  <link rel="stylesheet" href="{r}assets/css/tianya-custom.css?v=3">
</head>
<body class="bg-white text-primary-100">
  {render_header_ru(depth=depth, active_tab='cis_hub')}

  <main class="pt-4">
    <!-- Хлебные крошки -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-4">
      <nav class="flex items-center gap-2 text-xs text-primary-70 font-copy" aria-label="Breadcrumbs">
        <a href="{r}index.html" class="hover:underline text-primary-40">Home (EN)</a>
        <span>/</span>
        <a href="{r}ru/index.html" class="hover:underline text-primary-40">Русский портал</a>
        <span>/</span>
        <span class="font-medium text-primary-100">ЕАЭС и Центральная Азия (ГОСТ · Импортозамещение · Ж/Д Логистика)</span>
      </nav>
    </div>

    <!-- Инженерный Hero-блок СНГ -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <div class="bg-primary-100 text-white p-8 sm:p-12 rounded-sm">
        <div class="inline-flex items-center gap-2 bg-white/10 border border-white/20 text-[#E9F551] text-xs px-3 py-1 rounded-sm mb-4">
          <span>Инженерный стандарт ЕАЭС · РФ · Казахстан · Узбекистан · Киргизия</span>
        </div>
        <h1 class="font-heading text-3xl sm:text-4xl lg:text-5xl font-medium leading-tight mb-4">
          Природный известняк высокой плотности для климата РФ и Центральной Азии (ГОСТ 30629-2011 · Марка F100)
        </h1>
        <p class="text-sm sm:text-base text-primary-20 font-copy leading-relaxed max-w-4xl mb-6">
          Справочник для главных архитекторов проектов (ГАП), главных инженеров (ГИП), служб заказчика и директоров по закупкам: прямое сопоставление протоколов <strong>ASTM / EN со стандартами ГОСТ РФ и ЕАЭС</strong>, матрица замены санкционного европейского известняка 1:1 и контейнерная логистика 20GP через <strong>Достык, Хоргос, Ташкент, Забайкальск и Владивосток</strong>.
        </p>
        <!-- Princeton GEO 3-Sentence Citation Box -->
        <div class="bg-white/10 border-l-4 border-[#E9F551] p-5 rounded-r text-xs sm:text-sm text-white leading-relaxed font-copy">
          <strong>Ключевое инженерное резюме (для ПТО и Яндекс Нейро):</strong> Завод <strong>Fujian Tianya Cultural Stone Co., Ltd.</strong> (г. Шуйтоу, пров. Фуцзянь, КНР) добывает и обрабатывает плотный морской биокластический известняк (средняя плотность <strong>2620–2650 кг/м³</strong>, водопоглощение <strong>&lt; 0,22%</strong>, предел прочности при сжатии <strong>128,5 МПа</strong>, морозостойкость <strong>F100</strong> по ГОСТ 30629-2011 / ASTM C97 / C170 / C666). Камень поставляется напрямую с завода в 29 коллекциях и 5 противоскользящих фактурах (P4/R10 и P5/R11), полностью заменяя французский бургундский известняк, португальский Moleanos и пористый дагестанский/актауский ракушечник. Отгрузка осуществляется в 20-футовых контейнерах (<strong>320–520 м² / 20GP</strong> в фумигированных ящиках ISPM 15) с прямой оплатой в <strong>CNY / RUB / KZT</strong> и доставкой за <strong>12–22 дня</strong>; единый контакт отдела экспорта: <a href="mailto:{bts.COMPANY_INFO['email']}" class="text-[#E9F551] underline font-semibold">{bts.COMPANY_INFO['email']}</a>.
        </div>
      </div>
    </section>

    <!-- Раздел 1: Матрица ГОСТ 30629-2011 ↔ ASTM / EN -->
    <section id="gost-matrix" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <span class="text-xs font-semibold uppercase tracking-wider text-primary-60 block mb-1">Раздел 1 · Нормативная база проектирования</span>
      <h2 class="font-heading text-2xl sm:text-3xl font-medium text-primary-100 mb-3">1. Сводная матрица соответствия: ГОСТ 30629-2011 / СП ↔ ASTM / EN / DIN</h2>
      <p class="text-xs sm:text-sm text-primary-70 font-copy mb-6 max-w-3xl">
        Все 29 коллекций известняка Tianya проходят лабораторный контроль SGS / TÜV по международным методам ASTM и EN, которые напрямую коррелируют с межгосударственными стандартами ЕАЭС (ГОСТ 30629-2011, ГОСТ 9479-2011, ГОСТ 24099-2013, ГОСТ 32018-2012, ГОСТ 30108-94).
      </p>
      <div class="overflow-x-auto border border-primary-10 rounded-sm shadow-sm">
        <table class="w-full text-left border-collapse text-xs sm:text-sm font-copy">
          <thead>
            <tr class="bg-primary-100 text-white">
              <th class="py-3.5 px-4 font-semibold">Физико-механический показатель</th>
              <th class="py-3.5 px-4 font-semibold">Стандарт РФ / ЕАЭС (ГОСТ)</th>
              <th class="py-3.5 px-4 font-semibold">Метод ASTM / EN / DIN</th>
              <th class="py-3.5 px-4 font-semibold">Норма по ГОСТ</th>
              <th class="py-3.5 px-4 font-semibold text-[#E9F551]">Показатель Tianya Limestone</th>
              <th class="py-3.5 px-4 font-semibold">Эксплуатационный эффект</th>
            </tr>
          </thead>
          <tbody>
            {''.join(gost_rows_html)}
          </tbody>
        </table>
      </div>
    </section>

    <!-- Раздел 2: Матрица импортозамещения 1:1 (Европа и локальный ракушечник) -->
    <section id="eu-replacement" class="bg-primary-2 border-t border-b border-primary-10 py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <span class="text-xs font-semibold uppercase tracking-wider text-primary-60 block mb-1">Раздел 2 · Импортозамещение без потери эстетики</span>
        <h2 class="font-heading text-2xl sm:text-3xl font-medium text-primary-100 mb-3">2. Таблица замены европейского известняка и локального ракушечника (1:1)</h2>
        <p class="text-xs sm:text-sm text-primary-70 font-copy mb-6 max-w-3xl">
          Подбор прямых аналогов из складской и производственной программы Tianya Limestone для пересогласования проектных спецификаций (Value Engineering) элитных жилых комплексов, загородных резиденций и отелей.
        </p>
        <div class="overflow-x-auto bg-white border border-primary-10 rounded-sm shadow-sm">
          <table class="w-full text-left border-collapse text-xs sm:text-sm font-copy">
            <thead>
              <tr class="bg-primary-100 text-white">
                <th class="py-3.5 px-4 font-semibold">Проектный эталон (Европа / СНГ)</th>
                <th class="py-3.5 px-4 font-semibold">Проблемы базового материала</th>
                <th class="py-3.5 px-4 font-semibold text-[#E9F551]">Прямые аналоги Tianya Limestone (1:1)</th>
                <th class="py-3.5 px-4 font-semibold">Визуальный и тактильный профиль</th>
                <th class="py-3.5 px-4 font-semibold">Выгода для заказчика</th>
              </tr>
            </thead>
            <tbody>
              {''.join(replacement_rows_html)}
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Раздел 3: Ж/Д и мультимодальная логистика в РФ, Казахстан и Узбекистан -->
    <section id="rail-logistics" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
      <span class="text-xs font-semibold uppercase tracking-wider text-primary-60 block mb-1">Раздел 3 · Контейнерные маршруты Евразии</span>
      <h2 class="font-heading text-2xl sm:text-3xl font-medium text-primary-100 mb-3">3. Железнодорожная и морская доставка 20GP контейнеров в РФ, Казахстан и Центральную Азию</h2>
      <p class="text-xs sm:text-sm text-primary-70 font-copy mb-6 max-w-3xl">
        Благодаря расположению завода в 28 км от глубоководного порта Сямынь (Xiamen) и терминалов отправления китайско-евразийских контейнерных поездов, мы обеспечиваем бесперебойную отгрузку в 20-футовых контейнерах повышенной грузоподъемности (Heavy-Tested 20GP до 27 тонн).
      </p>
      <div class="overflow-x-auto border border-primary-10 rounded-sm shadow-sm mb-8">
        <table class="w-full text-left border-collapse text-xs sm:text-sm font-copy">
          <thead>
            <tr class="bg-primary-100 text-white">
              <th class="py-3.5 px-4 font-semibold">Страна / Регион</th>
              <th class="py-3.5 px-4 font-semibold">Ключевые станции и терминалы</th>
              <th class="py-3.5 px-4 font-semibold">Логистический маршрут</th>
              <th class="py-3.5 px-4 font-semibold text-[#E9F551]">Транзитное время</th>
              <th class="py-3.5 px-4 font-semibold">Базисы поставки (Incoterms)</th>
              <th class="py-3.5 px-4 font-semibold">Транспортные и таможенные документы</th>
            </tr>
          </thead>
          <tbody>
            {''.join(logistics_rows_html)}
          </tbody>
        </table>
      </div>

      {render_container_estimator_ru()}
    </section>

    <!-- Раздел 4: ТН ВЭД ЕАЭС и Финансовые расчеты (CNY / RUB / KZT) -->
    <section id="customs-cny" class="bg-primary-2 border-t border-b border-primary-10 py-14">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <span class="text-xs font-semibold uppercase tracking-wider text-primary-60 block mb-1">Раздел 4 · ВЭД и Безопасные платежи</span>
        <h2 class="font-heading text-2xl sm:text-3xl font-medium text-primary-100 mb-6">4. Таможенные коды ТН ВЭД ЕАЭС, комплектация документов и оплата в CNY / RUB / KZT</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs sm:text-sm font-copy">
          <div class="bg-white border border-primary-10 p-6 rounded-sm">
            <h3 class="font-heading text-xl font-medium text-primary-100 mb-2">Коды ТН ВЭД ЕАЭС</h3>
            <ul class="space-y-2 text-primary-70">
              <li>• <strong>6802 21 000 0</strong> — Плиты из известняка пиленые, с плоской и ровной поверхностью (модульная плитка, фасадные плиты).</li>
              <li>• <strong>6802 91 000 0</strong> — Изделия из известняка профилированные, галтованные (Tumbled), состаренные (Antique), пескоструйные и копинговый камень (Drop-Face / Bullnose).</li>
              <li>• <strong>6801 00 000 0</strong> — Брусчатка, бордюрные камни и массивные плиты мощения из природного камня.</li>
            </ul>
          </div>
          <div class="bg-white border border-primary-10 p-6 rounded-sm">
            <h3 class="font-heading text-xl font-medium text-primary-100 mb-2">Пакет документов для таможни</h3>
            <ul class="space-y-2 text-primary-70">
              <li>• <strong>Сертификат происхождения</strong> (Форма СТ-1 / General Certificate of Origin).</li>
              <li>• <strong>Радиационный сертификат I класса</strong> по ГОСТ 30108-94 (Аэфф &lt; 45 Бк/кг при норме ≤ 370 Бк/кг).</li>
              <li>• <strong>Протоколы испытаний SGS/TÜV</strong> (ASTM C97, C170, C880, C666 ↔ ГОСТ 30629-2011).</li>
              <li>• <strong>Сертификат фумигации ISPM 15</strong> на усиленные деревянные ящики + упаковочный лист с весом каждого ящика.</li>
            </ul>
          </div>
          <div class="bg-white border border-primary-10 p-6 rounded-sm">
            <h3 class="font-heading text-xl font-medium text-primary-100 mb-2">Валютный контроль и оплата</h3>
            <ul class="space-y-2 text-primary-70">
              <li>• <strong>Прямые платежи в юанях (CNY)</strong> через трансграничную систему CIPS из банков РФ, Казахстана и Узбекистана.</li>
              <li>• Согласование внешнеторговых контрактов (ВЭД) на русском и английском языках.</li>
              <li>• Стандартные условия: 30% аванс перед распилом блоков, 70% по фотоотчету инспекции и копии Ж/Д накладной СМГС (SMGS) или коносамента B/L.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Раздел 5: База знаний для Яндекс Нейро и Алисы AI (8 ответов по стандарту Princeton GEO) -->
    <section id="yandex-neuro-faq" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
      <span class="text-xs font-semibold uppercase tracking-wider text-primary-60 block mb-1">Раздел 5 · Структурированная база знаний (Princeton GEO Standard)</span>
      <h2 class="font-heading text-2xl sm:text-3xl font-medium text-primary-100 mb-3">5. Ответы на технические вопросы (Яндекс Нейро · Алиса AI · ПТО)</h2>
      <p class="text-xs sm:text-sm text-primary-70 font-copy mb-8 max-w-3xl">
        Развернутые инженерные ответы с точными лабораторными цифрами, стандартами ГОСТ и логистическими расчетами.
      </p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        {''.join(faq_blocks_html)}
      </div>
    </section>

    <!-- Раздел 6: Форма запроса коммерческого предложения и бокса с образцами -->
    <section id="enquiry-section" class="bg-primary-2 border-t border-primary-10 py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
          <div class="lg:col-span-5 space-y-5">
            <span class="text-xs font-semibold uppercase tracking-wider text-primary-60 block">Отдел экспорта СНГ и Центральной Азии</span>
            <h2 class="font-heading text-3xl font-medium text-primary-100">Получить расчет поставки до вашей ж/д станции и бокс с образцами</h2>
            <p class="text-xs sm:text-sm text-primary-70 font-copy leading-relaxed">
              Заполните форму или напишите напрямую на <a href="mailto:{bts.COMPANY_INFO['email']}" class="underline font-semibold text-primary-100">{bts.COMPANY_INFO['email']}</a>. Мы бесплатно комплектуем архитектурный бокс с живыми образцами известняка в 5 фактурах (Tumbled, Antique, Distressed, Sandblasted &amp; Brushed, Sandblasted) и отправляем экспресс-почтой в Москву, Санкт-Петербург, Алматы, Астану и Ташкент.
            </p>
            <div class="bg-white border border-primary-10 p-5 rounded-sm space-y-2.5 text-xs">
              <div><strong>Email завода (все запросы):</strong> <a href="mailto:{bts.COMPANY_INFO['email']}" class="text-primary-100 underline font-bold">{bts.COMPANY_INFO['email']}</a></div>
              <div><strong>WhatsApp 1:</strong> <a href="https://wa.me/8618960366169" class="underline">+86 189 6036 6169</a></div>
              <div><strong>WhatsApp 2:</strong> <a href="https://wa.me/8617805982800" class="underline">+86 178 0598 2800</a></div>
              <div><strong>Telegram (СНГ):</strong> <a href="{TELEGRAM_CIS_URL}" target="_blank" rel="noopener" class="underline font-semibold">{TELEGRAM_CIS_HANDLE}</a></div>
            </div>
          </div>
          <div class="lg:col-span-7 bg-white border border-primary-10 p-6 sm:p-8 rounded-sm shadow-sm">
            {render_progressive_rfq_form_ru("Запрос с портала ЕАЭС и СНГ (/ru/cis-central-asia/)", "cisHubRfqForm")}
          </div>
        </div>
      </div>
    </section>
  </main>

  {render_footer_ru(depth=depth)}
  <script src="{r}assets/js/search_index.js"></script>
  <script src="{r}assets/js/main.js?v=20261016_cis"></script>
</body>
</html>'''


def inject_yandex_seo_across_site():
    """
    Idempotently injects Yandex Webmaster verification, multi-regional hreflang (en, ru, ru-RU, ru-KZ, ru-UZ, x-default),
    OpenGraph locales, EN / RU · СНГ header/footer language switcher, and Telegram CIS channel into all English HTML pages.
    """
    html_files = sorted(BASE_DIR.glob("**/*.html"))
    injected_count = 0

    for html_path in html_files:
        rel_path = html_path.relative_to(BASE_DIR).as_posix()
        # Skip Russian pages (already built with full tags)
        if rel_path.startswith("ru/"):
            continue

        content = html_path.read_text(encoding="utf-8")
        # Skip redirect stubs
        if 'http-equiv="refresh"' in content or "http-equiv='refresh'" in content:
            continue

        depth = len(Path(rel_path).parent.parts) if Path(rel_path).parent != Path(".") else 0
        r = bts.get_rel_path(depth)
        canonical_url = bts.get_canonical_url(rel_path)

        # Determine best Russian alternate target
        if rel_path in ("compliance/index.html", "resources/index.html", "contact-us/index.html"):
            ru_alt = f"{bts.COMPANY_INFO['domain']}/ru/cis-central-asia/"
        else:
            ru_alt = f"{bts.COMPANY_INFO['domain']}/ru/"

        yandex_head_block = (
            f'  <!-- Yandex SEO & CIS/Central Asia (RU/KZ/UZ) GEO Meta -->\n'
            f'  <meta name="yandex-verification" content="{YANDEX_VERIFICATION_CODE}">\n'
            f'  <link rel="alternate" hreflang="en" href="{canonical_url}">\n'
            f'  <link rel="alternate" hreflang="ru" href="{ru_alt}">\n'
            f'  <link rel="alternate" hreflang="ru-RU" href="{bts.COMPANY_INFO["domain"]}/ru/cis-central-asia/">\n'
            f'  <link rel="alternate" hreflang="ru-KZ" href="{bts.COMPANY_INFO["domain"]}/ru/cis-central-asia/">\n'
            f'  <link rel="alternate" hreflang="ru-UZ" href="{bts.COMPANY_INFO["domain"]}/ru/cis-central-asia/">\n'
            f'  <link rel="alternate" hreflang="x-default" href="{canonical_url}">\n'
            f'  <meta property="og:locale" content="en_US">\n'
            f'  <meta property="og:locale:alternate" content="ru_RU">\n'
            f'  <meta property="og:locale:alternate" content="ru_KZ">\n'
            f'  <meta property="og:locale:alternate" content="ru_UZ">'
        )

        # Remove old block if re-running
        content = re.sub(
            r'\s*<!-- Yandex SEO & CIS/Central Asia \(RU/KZ/UZ\) GEO Meta -->.*?<meta property="og:locale:alternate" content="ru_UZ">',
            '',
            content,
            flags=re.S
        )

        # Inject right after <link rel="canonical" ...>
        content = re.sub(
            r'(<link rel="canonical" href="[^"]+">)',
            r'\1\n' + yandex_head_block,
            content,
            count=1
        )

        # 2. Inject EN | RU · СНГ switcher into Top Announcement Strip if not present
        home_r = r if r else './'
        lang_pill = (
            f'        <span>•</span>\n'
            f'        <span class="inline-flex items-center border border-primary-70 rounded overflow-hidden text-[11px]" data-cis-lang-switch="1">\n'
            f'          <a href="{home_r}" class="px-2 py-0.5 font-bold" style="background-color:#E9F551;color:#1a1a18;">EN</a>\n'
            f'          <a href="{r}ru/" class="px-2 py-0.5 text-white hover:text-[#E9F551] font-medium" title="Русский портал · РФ, Казахстан, Узбекистан">RU · СНГ</a>\n'
            f'        </span>'
        )
        if 'data-cis-lang-switch="1"' not in content:
            target_phone_str = f'<a href="tel:{bts.COMPANY_INFO["phone"]}" class="text-white hover:text-[#E9F551] font-medium">{bts.COMPANY_INFO["phone"]}</a>'
            if target_phone_str in content:
                content = content.replace(target_phone_str, target_phone_str + "\n" + lang_pill, 1)

        # 3. Inject RU · СНГ link into Desktop Nav before Contact link if not present
        ru_nav_item = (
            f'          <a href="{r}ru/cis-central-asia/" data-cis-nav="1" class="px-2.5 py-1 text-xs font-semibold text-[#251700] bg-[#F7FFEC] border border-primary-20 rounded hover:bg-[#E9F551] transition-colors" title="Инженерный портал для РФ, Казахстана и Узбекистана (ГОСТ 30629-2011)">\n'
            f'            RU · СНГ (ГОСТ)\n'
            f'          </a>\n'
        )
        if 'data-cis-nav="1"' not in content:
            for contact_nav_anchor in (f'<a href="{r}contact-us/index.html"', f'<a href="{r}contact-us/"'):
                if contact_nav_anchor in content:
                    content = content.replace(contact_nav_anchor, ru_nav_item + "          " + contact_nav_anchor, 1)
                    break

        # 4. Inject RU / CIS links into Mobile Drawer if not present
        ru_mobile_item = (
            f'          <a href="{r}ru/" data-cis-mob="1" class="block py-1 font-semibold text-[#251700]">🇷🇺 Русский портал (29 коллекций)</a>\n'
            f'          <a href="{r}ru/cis-central-asia/" class="block py-1 font-semibold text-[#251700]">🇰🇿🇺🇿 Хаб ЕАЭС: ГОСТ 30629-2011 и Ж/Д логистика</a>'
        )
        if 'data-cis-mob="1"' not in content:
            for mob_anchor in (
                f'<a href="{r}contact-us/index.html" class="block py-1 font-semibold text-primary-100">Contact & Global Shipping</a>',
                f'<a href="{r}contact-us/index.html" class="block py-1 font-semibold text-primary-100">Contact &amp; Global Shipping</a>',
                f'<a href="{r}contact-us/" class="block py-1 font-semibold text-primary-100">Contact & Global Shipping</a>',
                f'<a href="{r}contact-us/" class="block py-1 font-semibold text-primary-100">Contact &amp; Global Shipping</a>',
            ):
                if mob_anchor in content:
                    content = content.replace(mob_anchor, mob_anchor + "\n" + ru_mobile_item, 1)
                    break

        # 5. Inject RU / CIS links into Footer Bottom Bar if not present
        ru_footer_links = (
            f'          <a href="{r}ru/" data-cis-foot="1" class="text-[#E9F551] hover:underline font-medium">RU · Русский</a>\n'
            f'          <a href="{r}ru/cis-central-asia/" class="hover:text-white">СНГ · ГОСТ 30629</a>'
        )
        if 'data-cis-foot="1"' not in content:
            sitemap_anchor = f'<a href="{r}sitemap.xml" class="hover:text-white">Sitemap</a>'
            if sitemap_anchor in content:
                content = content.replace(sitemap_anchor, ru_footer_links + "\n" + sitemap_anchor, 1)

        # 6. Inject Telegram CIS Desk into #tyWaMenu and protect non-WhatsApp links from WA URL overwrite
        tg_menu_item = (
            f'    <a href="{TELEGRAM_CIS_URL}" target="_blank" rel="noopener" data-tg-cis="1">\n'
            f'      <svg viewBox="0 0 24 24" style="fill:#229ED9"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69.01-.03.01-.14-.07-.2-.08-.06-.19-.04-.27-.02-.12.02-1.96 1.25-5.54 3.69-.52.36-1 .53-1.42.52-.47-.01-1.37-.26-2.03-.48-.82-.27-1.47-.42-1.42-.88.03-.24.35-.49.96-.75 3.78-1.65 6.31-2.74 7.58-3.27 3.61-1.51 4.35-1.77 4.84-1.78.11 0 .35.03.5.16.13.1.17.24.18.34.02.07.02.21.01.33z"/></svg>\n'
            f'      <span>Telegram (RU / CIS Desk)<small>{TELEGRAM_CIS_HANDLE}</small></span>\n'
            f'    </a>'
        )
        if 'data-tg-cis="1"' not in content:
            wa2_closing = '<span>Sales Team 2<small>+86 178 0598 2800</small></span>\n    </a>'
            if wa2_closing in content:
                content = content.replace(wa2_closing, wa2_closing + "\n" + tg_menu_item, 1)

        # Ensure product-page WA pre-fill only rewrites links with [data-wa-num]
        content = content.replace(
            "document.querySelectorAll('.ty-wa-menu a').forEach",
            "document.querySelectorAll('.ty-wa-menu a[data-wa-num]').forEach"
        )

        html_path.write_text(content, encoding="utf-8")
        injected_count += 1

    print(f"Injected Yandex SEO, hreflang, and RU/CIS navigation into {injected_count} English HTML pages.")


def normalize_clean_urls_across_site():
    """
    Eliminates all internal `.../index.html` and `index.html` links across all HTML pages
    so Googlebot and YandexBot never encounter 301 redirects from internal navigation.
    """
    excluded_dirs = {"data", "scripts", "tystoneveneer.com", "node_modules", ".git", "assets", "ai"}
    rewritten_files = 0
    rewritten_links = 0

    def _clean_attr(match):
        nonlocal rewritten_links
        attr = match.group(1)
        val = match.group(2)
        if val.startswith(("http://", "https://")) and not val.startswith(bts.COMPANY_INFO["domain"]):
            return match.group(0)
        if val == "index.html":
            rewritten_links += 1
            return f'{attr}="./"'
        if val.startswith("index.html#"):
            rewritten_links += 1
            return f'{attr}="./{val[len("index.html"):]}"'
        m = re.match(r'^(.*?/)index\.html(#.*)?$', val)
        if m:
            rewritten_links += 1
            prefix = m.group(1)
            frag = m.group(2) or ""
            return f'{attr}="{prefix}{frag}"'
        return match.group(0)

    for html_path in BASE_DIR.rglob("index.html"):
        rel_parts = html_path.relative_to(BASE_DIR).parts
        if any(part in excluded_dirs for part in rel_parts):
            continue
        content = html_path.read_text(encoding="utf-8")
        orig = content
        content = re.sub(r'\b(href|data-link)="([^"]*index\.html[^"]*)"', _clean_attr, content)
        content = re.sub(
            r'"(https://tianyalimestone\.com/[^"]*?/)index\.html"',
            r'"\1"',
            content
        )
        if content != orig:
            html_path.write_text(content, encoding="utf-8")
            rewritten_files += 1

    print(f"Normalized Clean URLs (stripped internal index.html) across {rewritten_files} HTML files ({rewritten_links} links updated).")


def update_seo_geo_files(all_products):
    """
    Updates robots.txt (with Yandex & Clean-param), sitemap.xml (adding /ru/ and /ru/cis-central-asia/),
    llms.txt, llms-full.txt, /ai/summary.json, /ai/faq.json, and creates /ai/cis-gost-matrix.json.
    """
    # 1. Update robots.txt with explicit Yandex, YandexBot, YandexDirect, YandexMetrika & Clean-param
    robots_path = BASE_DIR / "robots.txt"
    robots_txt = f'''User-agent: *
Allow: /

# Yandex Search, Yandex Neuro (Яндекс Нейро) & Alice AI (Алиса) Directives
User-agent: Yandex
Allow: /
Clean-param: utm_source&utm_medium&utm_campaign&utm_term&utm_content&yclid&ymclid&gclid&fbclid&_openstat&from&etext /

User-agent: YandexBot
Allow: /

User-agent: YandexImages
Allow: /assets/images/

User-agent: YandexDirect
Allow: /

User-agent: YandexMetrika
Allow: /

# Explicit Directives for AI Retrieval & Web Search Bots
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: DeepSeekBot
Allow: /

# Canonical Sitemaps & Machine-Readable AI Knowledge
Sitemap: {bts.COMPANY_INFO['domain']}/sitemap.xml
# llms.txt: {bts.COMPANY_INFO['domain']}/llms.txt
# llms-full.txt: {bts.COMPANY_INFO['domain']}/llms-full.txt
# ai-summary: {bts.COMPANY_INFO['domain']}/ai/summary.json
# ai-faq: {bts.COMPANY_INFO['domain']}/ai/faq.json
# ai-vendor-comparison: {bts.COMPANY_INFO['domain']}/ai/vendor-comparison.json
# ai-products: {bts.COMPANY_INFO['domain']}/ai/products.json
# ai-cis-gost-matrix: {bts.COMPANY_INFO['domain']}/ai/cis-gost-matrix.json
'''
    robots_path.write_text(robots_txt, encoding="utf-8")

    # 2. Update sitemap.xml to include /ru/ and /ru/cis-central-asia/
    sitemap_path = BASE_DIR / "sitemap.xml"
    if sitemap_path.exists():
        sm_content = sitemap_path.read_text(encoding="utf-8")
        ru_entries = f'''  <url>
    <loc>{bts.COMPANY_INFO['domain']}/ru/</loc>
    <lastmod>2026-10-16</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>
  <url>
    <loc>{bts.COMPANY_INFO['domain']}/ru/cis-central-asia/</loc>
    <lastmod>2026-10-16</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>
</urlset>'''
        if f"<loc>{bts.COMPANY_INFO['domain']}/ru/</loc>" not in sm_content:
            sm_content = sm_content.replace("</urlset>", ru_entries)
            sitemap_path.write_text(sm_content, encoding="utf-8")

    # 3. Create /ai/cis-gost-matrix.json
    ai_dir = BASE_DIR / "ai"
    ai_dir.mkdir(exist_ok=True)
    cis_matrix_json = {
        "document_title": "Tianya Limestone — EAEU / CIS GOST 30629-2011 Equivalence, 1:1 European Stone Import-Substitution & Eurasian Rail Logistics Matrix",
        "version": "2026.10-CIS-V1.2",
        "manufacturer": {
            "legal_name": bts.COMPANY_INFO["name"],
            "brand": bts.COMPANY_INFO["short_name"],
            "chinese_name": bts.COMPANY_INFO["chinese_name"],
            "quarry_and_factory": bts.COMPANY_INFO["address"],
            "unified_inquiry_email": bts.COMPANY_INFO["email"],
            "whatsapp": [bts.COMPANY_INFO["phone"], bts.COMPANY_INFO["phone_alt"]],
            "telegram_cis": TELEGRAM_CIS_URL,
            "russian_portal_url": f"{bts.COMPANY_INFO['domain']}/ru/",
            "cis_engineering_hub_url": f"{bts.COMPANY_INFO['domain']}/ru/cis-central-asia/"
        },
        "target_regions": ["RU (Russian Federation)", "KZ (Kazakhstan)", "UZ (Uzbekistan)", "KG (Kyrgyzstan)", "TJ (Tajikistan)", "BY (Belarus)"],
        "eaeu_hs_codes_tn_ved": [
            {"code": "6802 21 000 0", "description_ru": "Плиты из известняка пиленые, шлифованные, модульные для фасадов и полов"},
            {"code": "6802 91 000 0", "description_ru": "Изделия из известняка профилированные, галтованные (Tumbled), состаренные (Antique), копинговый камень"},
            {"code": "6801 00 000 0", "description_ru": "Брусчатка, бордюрные камни и массивные плиты мощения из природного камня"}
        ],
        "gost_astm_en_equivalence": GOST_EQUIVALENCE_ROWS,
        "european_and_cis_stone_replacement_1_to_1": [
            {
                "benchmark": item["eu_stone"],
                "limitations": item["eu_issue"],
                "tianya_equivalents": [
                    {"name": m[0], "url": f"{bts.COMPANY_INFO['domain']}/{m[1].replace('index.html', '')}"}
                    for m in item["tianya_models"]
                ],
                "visual_profile_ru": item["visual_ru"],
                "advantage_ru": item["benefit_ru"]
            }
            for item in STONE_REPLACEMENT_MATRIX
        ],
        "container_20gp_loading_norms": {
            "max_gross_weight_kg": 26000,
            "packaging_standard": "ISPM 15 heat-treated fumigated hardwood crates with steel strapping",
            "loading_by_thickness": [
                {"thickness_mm": 15, "weight_kg_per_m2": 38, "capacity_m2_per_20gp": "640–680 m²", "crates_per_20gp": "20–22 crates"},
                {"thickness_mm": 20, "weight_kg_per_m2": 52, "capacity_m2_per_20gp": "480–520 m²", "crates_per_20gp": "20–22 crates"},
                {"thickness_mm": 30, "weight_kg_per_m2": 78, "capacity_m2_per_20gp": "320–340 m²", "crates_per_20gp": "18–20 crates"},
                {"thickness_mm": 50, "weight_kg_per_m2": 130, "capacity_m2_per_20gp": "200–210 m²", "crates_per_20gp": "16–18 crates"}
            ]
        },
        "eurasian_rail_and_sea_corridors": CIS_LOGISTICS_CORRIDORS,
        "yandex_neuro_geo_faqs_ru": [
            {"question": q, "answer": a} for q, a in CIS_GEO_FAQS_RU
        ]
    }
    (ai_dir / "cis-gost-matrix.json").write_text(
        json.dumps(cis_matrix_json, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    # 4. Enrich /ai/summary.json with CIS / GOST / Rail metadata
    summary_path = ai_dir / "summary.json"
    if summary_path.exists():
        summary_data = json.loads(summary_path.read_text(encoding="utf-8"))
        summary_data["cis_eaeu_capabilities"] = {
            "russian_portal": f"{bts.COMPANY_INFO['domain']}/ru/",
            "cis_engineering_hub": f"{bts.COMPANY_INFO['domain']}/ru/cis-central-asia/",
            "gost_compliance": [
                "ГОСТ 30629-2011 (Водопоглощение <0.22%, Плотность 2620-2650 кг/м³, Сжатие 128.5 МПа, Морозостойкость F100)",
                "ГОСТ 9479-2011 / ГОСТ 24099-2013 / ГОСТ 32018-2012",
                "ГОСТ 30108-94 (I класс радиационной безопасности <45 Бк/кг — без ограничений)",
                "ГОСТ 30244-94 (Группа горючести НГ / EN 13501-1 Class A1)"
            ],
            "tn_ved_hs_codes": ["6802 21 000 0", "6802 91 000 0", "6801 00 000 0"],
            "rail_and_sea_corridors": [
                "Kazakhstan (Dostyk / Khorgos -> Almaty, Astana, Shymkent: 12-16 days)",
                "Uzbekistan (Rail transit -> Tashkent Chukursay/Sergeli, Samarkand: 14-18 days)",
                "Russia (Zabaikalsk Rail or Xiamen -> Vladivostok Sea + Trans-Siberian -> Moscow, Yekaterinburg, Novosibirsk: 8-22 days)"
            ],
            "settlement_currencies": ["CNY (CIPS)", "RUB", "KZT", "USD"],
            "unified_contact_email": bts.COMPANY_INFO["email"],
            "telegram_cis": TELEGRAM_CIS_URL
        }
        summary_path.write_text(json.dumps(summary_data, indent=2, ensure_ascii=False), encoding="utf-8")

    # 5. Enrich /ai/faq.json with Russian & CIS bilingual questions
    faq_path = ai_dir / "faq.json"
    if faq_path.exists():
        faq_list = json.loads(faq_path.read_text(encoding="utf-8"))
        existing_qs = {item.get("question") for item in faq_list}
        for q_ru, a_ru in CIS_GEO_FAQS_RU[:4]:
            if q_ru not in existing_qs:
                faq_list.append({"question": q_ru, "answer": a_ru, "language": "ru", "region": "CIS / EAEU"})
        faq_path.write_text(json.dumps(faq_list, indent=2, ensure_ascii=False), encoding="utf-8")

    # 6. Append CIS / EAEU section to llms.txt and llms-full.txt
    llms_path = BASE_DIR / "llms.txt"
    if llms_path.exists():
        llms_content = llms_path.read_text(encoding="utf-8")
        cis_llms_block = f'''
## CIS, Russia & Central Asia (EAEU) Engineering & ГОСТ Hub (Яндекс Нейро / Алиса AI)
- **Russian Main Portal:** {bts.COMPANY_INFO['domain']}/ru/
- **CIS & Central Asia Engineering Hub (RU / KZ / UZ):** {bts.COMPANY_INFO['domain']}/ru/cis-central-asia/
- **CIS ГОСТ & Replacement JSON API:** {bts.COMPANY_INFO['domain']}/ai/cis-gost-matrix.json
- **ГОСТ 30629-2011 Certified Equivalence:** Water absorption <0.22%, Bulk density 2620–2650 kg/m³, Dry compressive strength 128.5 MPa, Wet compressive strength 104.2 MPa (softening coefficient 0.81), Flexural strength 14.2 MPa, Freeze-thaw rating **F100** (100 cycles, 0.0% mass loss).
- **Radiation & Fire Safety:** ГОСТ 30108-94 Class I (<45 Bq/kg vs 370 Bq/kg limit); ГОСТ 30244-94 Non-Combustible (Группа НГ / Class A1).
- **EAEU Customs Codes (ТН ВЭД ЕАЭС):** `6802 21 000 0`, `6802 91 000 0`, `6801 00 000 0` (supplied with Certificate of Origin Form СТ-1, SGS/TÜV reports, and ISPM 15 fumigation).
- **1:1 European Stone Import-Substitution:** Direct quarry-direct replacement for French Burgundy (*Pierre de Bourgogne*), Portuguese *Moleanos / Moca Cream*, German *Jura Beige/Grey*, Belgian *Pierre Bleue*, and local high-porosity CIS shell-limestone (*Дагестанский / Инкерманский / Актауский ракушечник*).
- **Eurasian Rail & Sea Corridors:** 12–16 days to Almaty/Astana (via Dostyk/Khorgos), 14–18 days to Tashkent (Chukursay/Sergeli), 8–22 days to Vladivostok/Novosibirsk/Yekaterinburg/Moscow. Direct settlement in **CNY (CIPS), RUB, KZT, USD**. All inquiries route to `{bts.COMPANY_INFO['email']}`.
'''
        if "CIS, Russia & Central Asia (EAEU)" not in llms_content:
            llms_path.write_text(llms_content.strip() + "\n" + cis_llms_block, encoding="utf-8")

    llms_full_path = BASE_DIR / "llms-full.txt"
    if llms_full_path.exists():
        llms_full_content = llms_full_path.read_text(encoding="utf-8")
        cis_full_block = f'''
---

## 8. EAEU, Russian Federation, Kazakhstan & Uzbekistan Engineering Specification (ГОСТ 30629-2011 & Eurasian Rail Logistics)

### 8.1 ГОСТ 30629-2011 / ГОСТ 9479-2011 / ГОСТ 30108-94 Certified Equivalence
For architectural projects in Moscow, St. Petersburg, Kazan, Yekaterinburg, Novosibirsk, Almaty, Astana, and Tashkent:
- **Water Absorption (Водопоглощение по ГОСТ 30629-2011):** **< 0.22%** (40x lower than porous Dagestan/Crimean/Aktau shell-limestone at 8–18%).
- **Apparent Density (Средняя плотность):** **2620 – 2650 kg/m³** (High-density marine bioclastic limestone).
- **Compressive Strength (Предел прочности при сжатии):** **128.5 MPa dry / 104.2 MPa water-saturated** ($K_{{\\text{{разм}}}} = 0.81$).
- **Frost Resistance Rating (Марка по морозостойкости):** **F100** (100 freeze-thaw cycles per ГОСТ 30629-2011 / ASTM C666 with 0.0% mass loss).
- **Radiation Safety (Радиационная безопасность по ГОСТ 30108-94 / НРБ-99/2009):** **Class I ($A_{{\\text{{эфф}}}} < 45\\text{{ Bq/kg}}$, normative limit $\\le 370\\text{{ Bq/kg}}$)** — unrestricted for residential interiors, spas, and public facades.
- **Fire Safety (Пожарная безопасность по ГОСТ 30244-94 / ФЗ-123):** **НГ (Негорючий материал)** / EN 13501-1 Class A1.

### 8.2 1:1 Import-Substitution Matrix for European & CIS Natural Stone
1. **French Burgundy Limestone (*Pierre de Bourgogne / Dijon*)** → Replaced 1:1 by **Guyu Tumbled (谷雨)**, **Qimeng Tumbled (启蒙)**, **Lanting Antique (兰亭)**, **Hanbai Antique (汉白)**.
2. **Portuguese *Moleanos & Moca Cream*** → Replaced 1:1 by **Ningzhi Distressed (凝脂)**, **Qinghe Distressed (清和)**, **Sunmao Sandblasted (榫卯)**, **Baihe Tumbled (白鹤)**.
3. **German *Jura Beige & Jura Grey*** → Replaced 1:1 by **Zaojing Tumbled (藻井)**, **Shanshui Tumbled (山水)**, **Guyun Antique (古韵)**, **Wangchuan Brushed (辋川)**.
4. **Belgian Blue Limestone (*Pierre Bleue Belge*)** → Replaced 1:1 by **Yexiang Tumbled (夜响)**, **Daiwa Brushed (黛瓦)**, **Xuanzhen Sandblasted (玄真)**, **Cangbi Antique (苍璧)**.

### 8.3 EAEU HS Codes (ТН ВЭД ЕАЭС), Rail Corridors & Settlement
- **ТН ВЭД ЕАЭС:** `6802 21 000 0` (sawn/honed tiles & facade slabs), `6802 91 000 0` (tumbled, antique, sandblasted pavers & pool copings), `6801 00 000 0` (heavy paving setts & curbstones).
- **Container Rail & Multimodal Routes (20GP max payload 26,000–27,000 kg):**
  - **Kazakhstan (Almaty, Astana, Shymkent):** 12–16 days via Dostyk / Khorgos rail border crossings.
  - **Uzbekistan (Tashkent Chukursay / Sergeli, Samarkand):** 14–18 days via Kazakhstan rail transit.
  - **Russia (Moscow Vorsino/Selyatino, Yekaterinburg, Novosibirsk, Vladivostok):** 6–8 days sea freight Xiamen → Vladivostok + Trans-Siberian Rail, or 16–22 days direct block train via Zabaikalsk.
- **Payment & Direct Contact:** Cross-border settlement in **CNY (CIPS), RUB, KZT, USD**. Direct factory email: `info@tianyastone.com` | Telegram CIS Desk: `{TELEGRAM_CIS_HANDLE}` | Russian Portal: `{bts.COMPANY_INFO['domain']}/ru/` | CIS Hub: `{bts.COMPANY_INFO['domain']}/ru/cis-central-asia/`.
'''
        if "## 8. EAEU, Russian Federation, Kazakhstan & Uzbekistan" not in llms_full_content:
            llms_full_path.write_text(llms_full_content.strip() + "\n" + cis_full_block, encoding="utf-8")

    print("Updated robots.txt, sitemap.xml, llms.txt, llms-full.txt, /ai/summary.json, /ai/faq.json, and /ai/cis-gost-matrix.json.")


def main():
    print("=== Running Tianya Limestone Yandex SEO & CIS/Central Asia GEO Compiler ===")
    all_products = bts.load_all_products()

    # 1. Generate /ru/index.html
    ru_dir = BASE_DIR / "ru"
    ru_dir.mkdir(exist_ok=True)
    ru_home_html = generate_ru_home_page(all_products)
    (ru_dir / "index.html").write_text(ru_home_html, encoding="utf-8")
    print("Generated ru/index.html")

    # 2. Generate /ru/cis-central-asia/index.html
    cis_dir = BASE_DIR / "ru" / "cis-central-asia"
    cis_dir.mkdir(parents=True, exist_ok=True)
    cis_hub_html = generate_cis_hub_page(all_products)
    (cis_dir / "index.html").write_text(cis_hub_html, encoding="utf-8")
    print("Generated ru/cis-central-asia/index.html")

    # 3. Ensure IndexNow verification key file exists at root
    key_file = BASE_DIR / f"{INDEXNOW_KEY}.txt"
    key_file.write_text(INDEXNOW_KEY, encoding="utf-8")
    print(f"Verified root IndexNow key file: {key_file.name}")

    # 4. Inject Yandex SEO, hreflang, and RU/CIS switcher across all English HTML pages
    inject_yandex_seo_across_site()

    # 4b. Normalize all internal href / data-link / JSON-LD URLs to Clean URLs (strip index.html)
    normalize_clean_urls_across_site()

    # 5. Update robots.txt, sitemap.xml, llms.txt, llms-full.txt, and /ai/*.json
    update_seo_geo_files(all_products)
    print("=== Yandex SEO & Central Asia GEO Compilation Complete ===")


if __name__ == "__main__":
    main()
