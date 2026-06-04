"""
Pre-loaded demo data for Revana.
Product 1: Stanley Quencher H2.0 FlowState Tumbler 40oz
Product 2: Hydro Flask Wide Mouth Water Bottle (competitor)
"""

import pandas as pd


def _make_stanley_reviews():
    reviews = [
        # 5-star reviews
        {"rating": 5, "title": "Best tumbler I have ever owned", "body": "I cannot believe I waited this long to get a Stanley. This thing keeps my iced coffee cold for literally 12 hours. I work long shifts and by the end of my day my drink is still ice cold. The handle makes it so easy to carry and it actually fits in my car cupholder which was a dealbreaker for me with other tumblers. I bought the Rose Quartz color and get compliments every single day. Worth every single penny.", "verified_purchase": True, "date": {"utc": "2024-03-15T00:00:00.000Z"}, "reviewer_name": "Sarah M."},
        {"rating": 5, "title": "I own 7 of these now", "body": "Started with one and now I have seven in different colors. They make the best gifts — I have given these to my mom, sister, coworkers, and my daughter. The quality is incredible. Drinks stay cold all day even in a hot car. The flip straw lid is genius. My only complaint is that I keep seeing new colors and I have to buy them all. Stanley has a customer for life.", "verified_purchase": True, "date": {"utc": "2024-04-02T00:00:00.000Z"}, "reviewer_name": "Jennifer K."},
        {"rating": 5, "title": "Game changer for my daily routine", "body": "As someone who works out every morning and then goes straight to the office, this tumbler has been a game changer. Ice stays frozen from my 6am gym session until my afternoon meeting. The handle is so comfortable and the size is perfect — big enough to last all day but not so big it is awkward. The cupholder compatibility was the selling point for me. Highly recommend.", "verified_purchase": True, "date": {"utc": "2024-05-10T00:00:00.000Z"}, "reviewer_name": "Mike T."},
        {"rating": 5, "title": "Keeps drinks cold for 24+ hours", "body": "I tested this — put ice water in at 8pm, woke up the next morning and still had ice. The insulation on this thing is unreal. I have tried Hydro Flask, Yeti, and several others. Stanley wins for the handle and the cupholder fit. The straw is a nice touch too. My husband was skeptical about the price but now he wants his own.", "verified_purchase": True, "date": {"utc": "2024-02-28T00:00:00.000Z"}, "reviewer_name": "Amanda R."},
        {"rating": 5, "title": "Perfect gift — bought 4 as presents", "body": "Bought these for my bridesmaids and they absolutely loved them. Each person chose their own color which made it feel personal. The quality feels premium — solid, heavy, well made. The engraving option is a bonus for gifts. Everyone who saw them at the bachelorette wanted to know where I got them. Will definitely buy more as gifts.", "verified_purchase": True, "date": {"utc": "2024-06-01T00:00:00.000Z"}, "reviewer_name": "BridesmaidBride"},
        {"rating": 5, "title": "My gym bag essential", "body": "Take this to the gym every single day. Ice stays cold through my entire 2 hour workout plus the drive home. The handle is sturdy enough that I can carry it while holding my other gym bag without worrying about it slipping. Fits in the cupholder of my car perfectly. I bought the black and it still looks brand new after 6 months of daily use. Zero regrets.", "verified_purchase": True, "date": {"utc": "2024-01-20T00:00:00.000Z"}, "reviewer_name": "FitnessFirst22"},
        # 4-star reviews
        {"rating": 4, "title": "Love it but lid leaks slightly", "body": "Overall I love this tumbler and use it every single day. Keeps my coffee hot for hours which is incredible. However I have noticed that if I tip it at an angle in my bag the lid does leak a little. Not a huge deal if you keep it upright but I have had a few minor spills in my tote bag. Still giving 4 stars because the quality otherwise is excellent and the color is beautiful.", "verified_purchase": True, "date": {"utc": "2024-03-20T00:00:00.000Z"}, "reviewer_name": "CoffeeAddict"},
        {"rating": 4, "title": "Great but noticed paint chipping", "body": "I have had mine for about 4 months and it is still performing great — drinks stay cold all day. My only issue is that I noticed some paint chipping around the bottom where it hits the counter. It is a small area but for the price I expected the finish to be more durable. The actual insulation and function is flawless. Would still recommend but be careful with how you set it down.", "verified_purchase": True, "date": {"utc": "2024-04-15T00:00:00.000Z"}, "reviewer_name": "TumblerMom"},
        {"rating": 4, "title": "Heavy when full but worth it", "body": "This tumbler is excellent quality but I want to be honest — when it is full of water and ice it is quite heavy. I have a smaller frame and found it a little awkward to carry around all day. That said the insulation is incredible and it fits in my car cupholder perfectly. If weight is not an issue for you this is absolutely the best tumbler on the market. I just personally wish they made a lighter version.", "verified_purchase": True, "date": {"utc": "2024-05-05T00:00:00.000Z"}, "reviewer_name": "PetiteGal"},
        # 3-star reviews
        {"rating": 3, "title": "Lid leaked all over my work bag", "body": "The insulation on this is fantastic — I have no complaints about keeping things cold. But I had a major issue with the lid leaking. I put it in my work bag for my commute and when I got to the office everything was soaked. My laptop, my notebook, my wallet. I had to buy a new bag. I looked it up and this seems to be a known issue when the tumbler is tilted. Stanley really needs to fix the lid design. Disappointed for the price.", "verified_purchase": True, "date": {"utc": "2024-02-10T00:00:00.000Z"}, "reviewer_name": "CommuteCaught"},
        {"rating": 3, "title": "Condensation issue is real", "body": "Kept seeing these everywhere and finally bought one. The cold retention is impressive but nobody told me how much condensation builds up on the outside. I set it on my wooden desk and it left a ring mark. I put it in my bag and the outside was wet enough to dampen other things. For a premium priced tumbler I expected this to be addressed. Cold drinks create a ton of condensation on the exterior.", "verified_purchase": True, "date": {"utc": "2024-03-08T00:00:00.000Z"}, "reviewer_name": "DeskDamage"},
        # 2-star reviews
        {"rating": 2, "title": "Straw got moldy after 3 weeks", "body": "Really disappointed. The concept is great and the colors are beautiful but my straw got moldy after only 3 weeks of use. I do wash it every day but apparently you need to completely disassemble the straw mechanism and scrub every crevice or mold grows inside. There are little grooves in the straw and lid that are impossible to clean properly. For the price I expect better design. Having to scrub microscopic crevices every day is not realistic.", "verified_purchase": True, "date": {"utc": "2024-01-15T00:00:00.000Z"}, "reviewer_name": "MoldyMess"},
        {"rating": 2, "title": "Paint chipped within 2 months", "body": "Bought the limited edition color because it was beautiful. Within 2 months the paint started chipping significantly around the base and handle area. I do not throw it around — I am careful with it. For a 45 dollar tumbler I expect the finish to last more than 2 months. The insulation works great but I am embarrassed to carry something that looks this beat up. Stanley should use a more durable finish.", "verified_purchase": True, "date": {"utc": "2024-04-20T00:00:00.000Z"}, "reviewer_name": "ChipChip"},
        # 1-star reviews
        {"rating": 1, "title": "Leaked everywhere ruined my laptop", "body": "One star because zero is not an option. The lid on this thing is an absolute disaster. I carry mine in my bag and it leaked completely while I was on the subway. My laptop is destroyed. My AirPods case is destroyed. Everything in my bag was soaked. I have seen many complaints about this exact issue and Stanley has done nothing to fix it. Do not carry this in a bag with anything valuable. The insulation is great but what good is a water bottle that leaks everywhere?", "verified_purchase": True, "date": {"utc": "2024-05-25T00:00:00.000Z"}, "reviewer_name": "RuinedLaptop"},
        {"rating": 1, "title": "Terrible lid design do not buy", "body": "Absolutely terrible lid. Leaks when tilted even slightly. I tested multiple Stanley tumblers thinking mine was defective and they all leak at an angle. This is a design flaw not a defect. Save your money and buy something with a proper seal. The hype around these is unbelievable given how poorly the lid is designed. I gave it to my sister who only uses it on her desk and she loves it. But as a bag tumbler it is completely useless.", "verified_purchase": True, "date": {"utc": "2024-03-01T00:00:00.000Z"}, "reviewer_name": "AngryBuyer"},
    ]
    return pd.DataFrame(reviews)


def _make_hydro_flask_reviews():
    reviews = [
        {"rating": 5, "title": "Indestructible and keeps things cold", "body": "I have dropped this thing down stairs, off a desk, thrown it in the back of my truck. Not a single dent. The insulation is excellent — ice lasts 24 hours easily. The wide mouth is easy to add ice and clean. I have had mine for 3 years and it still looks almost new. Hydro Flask is the gold standard for durability. If you want something that lasts forever this is it.", "verified_purchase": True, "date": {"utc": "2024-02-14T00:00:00.000Z"}, "reviewer_name": "OutdoorsDave"},
        {"rating": 5, "title": "Best water bottle period", "body": "Simple, functional, and built to last. I bought this 2 years ago and use it daily. No leaks, no rust, no issues. The powder coat finish has held up incredibly well. I have seen friends go through 3 or 4 cheaper bottles in the time I have had this one. Buy once cry once. The wide mouth makes it easy to put ice in and clean thoroughly. No weird crevices where mold can hide.", "verified_purchase": True, "date": {"utc": "2024-03-10T00:00:00.000Z"}, "reviewer_name": "BuyOnceCryOnce"},
        {"rating": 5, "title": "Survived everything I threw at it", "body": "Construction worker here. This bottle has been on job sites with me for 18 months. Concrete dust, dropped from scaffolding twice, sat in a hot truck all summer. Still works perfectly, still keeps water ice cold, barely a scratch on it. My coworkers have gone through multiple cheap bottles while I am still using the same Hydro Flask. The durability is unmatched.", "verified_purchase": True, "date": {"utc": "2024-04-05T00:00:00.000Z"}, "reviewer_name": "ConstructionMike"},
        {"rating": 4, "title": "Great bottle but no handle is annoying", "body": "The insulation on this is fantastic and it is clearly built to last forever. My only real complaint is the lack of a handle. I have seen the Stanley with its big comfortable handle and I am a little jealous. Carrying a 40oz bottle without a handle when it is full of water and ice gets awkward. A strap or handle option would make this perfect. Still 4 stars because everything else is excellent.", "verified_purchase": True, "date": {"utc": "2024-03-25T00:00:00.000Z"}, "reviewer_name": "NeedAHandle"},
        {"rating": 4, "title": "Excellent quality but does not fit my cupholder", "body": "The build quality on this is second to none. Absolutely worth the price for the durability alone. However I was disappointed to discover it does not fit in my car cupholder — it is slightly too wide. I see a lot of people mention the Stanley fits perfectly in cupholders and that has become a dealbreaker feature for me. If you primarily use this at a desk or gym bag it is perfect. Car commuters may want to measure first.", "verified_purchase": True, "date": {"utc": "2024-05-15T00:00:00.000Z"}, "reviewer_name": "CarCommuter"},
        {"rating": 3, "title": "Good bottle but Stanley has better features", "body": "I bought this before the Stanley craze and it is a solid bottle. But honestly after trying my friend's Stanley I understand the hype. The Stanley has a handle, fits in cupholders, has a better straw lid, and comes in way more colors. The Hydro Flask is more durable but for everyday use the Stanley wins on convenience. If I were buying today I would go Stanley. Still giving 3 stars because as a water bottle it works great.", "verified_purchase": True, "date": {"utc": "2024-04-18T00:00:00.000Z"}, "reviewer_name": "StanleyConvert"},
        {"rating": 3, "title": "Expensive and the straw lid is sold separately", "body": "The bottle itself is great quality but I was annoyed to find out the straw lid I wanted is sold separately. I bought what I thought was a complete product and then had to spend another 15 dollars on the lid I actually wanted. Between the bottle and the lid this costs more than a Stanley which comes with everything you need. The durability is better than Stanley but the value proposition is not as clear anymore.", "verified_purchase": True, "date": {"utc": "2024-02-20T00:00:00.000Z"}, "reviewer_name": "HiddenCosts"},
        {"rating": 2, "title": "Too heavy and no handle makes it impractical", "body": "The insulation is fantastic but this thing is heavy even empty and without a handle it is genuinely difficult to use one-handed when full. I switched to a Stanley and the handle makes such a difference. I also find the Hydro Flask boring to look at — very limited color options compared to what Stanley offers. The durability advantage of Hydro Flask is real but for daily use the Stanley is just more practical.", "verified_purchase": True, "date": {"utc": "2024-05-02T00:00:00.000Z"}, "reviewer_name": "SwitchedToStanley"},
        {"rating": 2, "title": "Fewer color options is a dealbreaker for me", "body": "I know this sounds shallow but the color options matter to me. I bought a Hydro Flask and it comes in maybe 10 colors. My Stanley collection has 8 different colors and new limited editions drop constantly. The Hydro Flask is more durable but I find myself reaching for my Stanley every day because I love the colors and the handle. Giving this 2 stars because the product works but it has fallen behind Stanley on everything except durability.", "verified_purchase": True, "date": {"utc": "2024-01-30T00:00:00.000Z"}, "reviewer_name": "ColorMatters"},
        {"rating": 1, "title": "Overpriced compared to Stanley", "body": "Paid full price for this and then a coworker showed me her Stanley. Same insulation, better handle, fits in cupholder, more colors, and the same price or cheaper. I feel like I overpaid for the Hydro Flask name. The durability is slightly better but not worth the premium when Stanley exists. Returning this and buying a Stanley.", "verified_purchase": True, "date": {"utc": "2024-03-12T00:00:00.000Z"}, "reviewer_name": "ShouldaGotStanley"},
    ]
    return pd.DataFrame(reviews)


STANLEY_ANALYSIS = {
    "executive_summary": "The Stanley Quencher dominates the premium tumbler market with exceptional thermal performance and cult-like brand loyalty, but faces a critical product design vulnerability: a leaking lid that has destroyed customers' laptops, bags, and trust. The brand's viral color strategy and cupholder compatibility are genuine differentiators, but the lid issue is an escalating reputational risk that competitors are actively exploiting.",
    "overall_health_score": 74,
    "complaint_themes": [
        {
            "theme": "Lid leaks when tilted — ruins bags and electronics",
            "frequency_pct": 35,
            "emotional_intensity": "critical",
            "example_quotes": [
                "My laptop is destroyed. My AirPods case is destroyed. Everything in my bag was soaked.",
                "I put it in my work bag for my commute and when I got to the office everything was soaked."
            ],
            "improvement_recommendation": "Redesign the lid seal mechanism to prevent leaking at angles up to 45 degrees. Add a secondary lock position. This is the #1 reason customers switch to competitors.",
            "estimated_rating_impact": "+0.4 stars if fixed"
        },
        {
            "theme": "Straw and lid develops mold in hard-to-clean crevices",
            "frequency_pct": 22,
            "emotional_intensity": "high",
            "example_quotes": [
                "My straw got moldy after only 3 weeks of use.",
                "There are little grooves in the straw and lid that are impossible to clean properly."
            ],
            "improvement_recommendation": "Redesign straw and lid with smooth, accessible surfaces. Include a dedicated cleaning brush with every purchase. Add dishwasher-safe certification.",
            "estimated_rating_impact": "+0.2 stars if fixed"
        },
        {
            "theme": "Paint and powder coat chips within months",
            "frequency_pct": 18,
            "emotional_intensity": "medium",
            "example_quotes": [
                "Within 2 months the paint started chipping significantly around the base.",
                "For a 45 dollar tumbler I expect the finish to last more than 2 months."
            ],
            "improvement_recommendation": "Switch to a more durable ceramic or industrial powder coat finish. Offer a finish warranty. The premium price creates premium expectations.",
            "estimated_rating_impact": "+0.2 stars if fixed"
        },
        {
            "theme": "Exterior condensation damages desks and soaks bags",
            "frequency_pct": 15,
            "emotional_intensity": "medium",
            "example_quotes": [
                "I set it on my wooden desk and it left a ring mark.",
                "The outside was wet enough to dampen other things in my bag."
            ],
            "improvement_recommendation": "Add a silicone sleeve option or improve the exterior insulation layer to reduce condensation transfer. Market a compatible coaster.",
            "estimated_rating_impact": "+0.1 stars if fixed"
        },
        {
            "theme": "Heavy when full — difficult for smaller users",
            "frequency_pct": 12,
            "emotional_intensity": "low",
            "example_quotes": [
                "When it is full of water and ice it is quite heavy.",
                "I have a smaller frame and found it a little awkward to carry around all day."
            ],
            "improvement_recommendation": "Introduce a 24oz or 28oz version with the same handle design for users who find the 40oz too heavy. Market it as the everyday carry size.",
            "estimated_rating_impact": "+0.1 stars if new SKU added"
        }
    ],
    "praise_themes": [
        {
            "theme": "Exceptional cold and hot retention — ice lasts all day",
            "frequency_pct": 78,
            "example_quotes": [
                "Keeps my iced coffee cold for literally 12 hours.",
                "I tested this — put ice water in at 8pm, woke up the next morning and still had ice."
            ],
            "marketing_angle": "Lead with the 12-hour cold retention claim in all advertising. Real customer language: still ice cold after my entire shift is more credible than spec claims."
        },
        {
            "theme": "Perfect cupholder fit — a genuine differentiator",
            "frequency_pct": 52,
            "example_quotes": [
                "It actually fits in my car cupholder which was a dealbreaker for me with other tumblers.",
                "Fits in the cupholder of my car perfectly."
            ],
            "marketing_angle": "Cupholder compatibility is a direct competitive advantage over Hydro Flask. Make this a primary feature in listings and ads. The only 40oz tumbler that fits your cupholder."
        },
        {
            "theme": "Color variety drives repeat purchases and gifting",
            "frequency_pct": 45,
            "example_quotes": [
                "I own 7 of these now in different colors.",
                "The limited edition colors make these the perfect gift."
            ],
            "marketing_angle": "The color collection strategy is working. Push the collect them all and gifting angle heavily. Bundle gift sets with popular color combinations."
        },
        {
            "theme": "Comfortable handle sets it apart from competitors",
            "frequency_pct": 38,
            "example_quotes": [
                "The handle makes it so easy to carry.",
                "The handle is so comfortable and the size is perfect."
            ],
            "marketing_angle": "The handle is specifically mentioned by customers who compared to Hydro Flask and chose Stanley. Make handle comfort a direct comparison point in marketing."
        }
    ],
    "listing_bullets": [
        "ICE COLD FOR 12+ HOURS — Customers report ice still present the next morning. Advanced vacuum insulation keeps drinks cold through full work shifts, gym sessions, and road trips without compromise.",
        "THE ONLY 40OZ TUMBLER THAT FITS YOUR CUPHOLDER — Engineered to fit standard car cupholders. No more choosing between hydration and convenience. Take it everywhere your drive takes you.",
        "HANDLE THAT HYDRO FLASK DOES NOT HAVE — The ergonomic carry handle makes a genuine difference when your tumbler is full. Carry comfortably one-handed from car to desk to gym.",
        "COLLECT EVERY COLOR — With 40+ colors and limited edition drops, Stanley Quencher is the tumbler you buy again. Our customers average 4 per household. Gift-ready with every purchase.",
        "FLIP STRAW LID INCLUDED — Everything you need, nothing sold separately. The FlowState lid includes three positions: straw, wide mouth, and full cover for spill-resistant use."
    ],
    "listing_title_suggestion": "Stanley Quencher H2.0 FlowState Tumbler 40oz | Cupholder Compatible | Keeps Ice 12+ Hours | Ergonomic Handle | 40+ Colors | Straw Lid Included",
    "buyer_personas": [
        {
            "persona_name": "The Stanley Collector",
            "percentage": 35,
            "description": "Predominantly women 25-45 who buy multiple Stanley tumblers in different colors. Highly active on social media, influenced by TikTok and Instagram. Treat Stanley as both a utility product and a collectible fashion accessory.",
            "what_they_love": "New color drops, limited editions, and the social currency of showing off their collection",
            "what_frustrates_them": "Paint chipping on their prized colors and the lid leaking on expensive bags",
            "marketing_message": "New colors dropping. Be the first. Shop the Stanley Quencher limited edition collection before it sells out."
        },
        {
            "persona_name": "The Daily Commuter Mom",
            "percentage": 40,
            "description": "Working mothers and commuters who use their Stanley daily for coffee and water. Primary purchase driver is the cupholder fit and all-day cold retention. Most likely to leave 1-star reviews when the lid leaks on their laptop.",
            "what_they_love": "Cupholder compatibility, handle, all-day cold retention, and not needing to refill",
            "what_frustrates_them": "Lid leaking in their work bag and destroying their belongings",
            "marketing_message": "From morning drop-off to end of shift. One Stanley. All day cold. Fits your cupholder. Handles everything else."
        },
        {
            "persona_name": "The Gift Buyer",
            "percentage": 25,
            "description": "Customers buying Stanleys as gifts for birthdays, weddings, holidays, and just because. Often buy 3-5 at a time in different colors. Price-insensitive. Care about presentation and color variety.",
            "what_they_love": "Color variety, the premium feel, and the universal recognition of the Stanley brand as a thoughtful gift",
            "what_frustrates_them": "Limited availability of specific colors during peak gift seasons",
            "marketing_message": "The gift they actually want. 40+ colors. Personalization available. Ships gift-ready."
        }
    ],
    "risk_alerts": [
        {
            "alert_type": "Critical Lid Design Flaw — Customer Property Destroyed",
            "severity": "critical",
            "description": "The lid leaking issue has destroyed customers' laptops, AirPods, and bags. Multiple 1-star reviews specifically mention this design flaw. This is the single biggest threat to brand reputation.",
            "recommended_action": "Prioritize lid redesign in next product iteration. Issue proactive communication about correct lid usage. Consider a lid replacement program for affected customers."
        },
        {
            "alert_type": "Competitor Positioning Opportunity — Hydro Flask Gaps",
            "severity": "medium",
            "description": "Hydro Flask customers specifically complain about the lack of handle and poor cupholder fit — two areas where Stanley clearly wins. This gap is not being exploited in Stanley's current marketing.",
            "recommended_action": "Create direct comparison content: Stanley vs Hydro Flask highlighting cupholder fit and handle. Target Hydro Flask buyers with paid ads."
        },
        {
            "alert_type": "Paint Durability — Premium Price Expectation Gap",
            "severity": "medium",
            "description": "Paint chipping complaints are increasing. Customers paying $45+ for a premium product expect the finish to last. This creates a mismatch between the premium price and perceived quality.",
            "recommended_action": "Invest in a more durable finish or introduce a finish warranty. Address proactively in product descriptions."
        }
    ],
    "keyword_opportunities": [
        "stanley tumbler cupholder fit",
        "tumbler that fits in cupholder",
        "stanley quencher leak proof",
        "best tumbler for commuters",
        "stanley vs hydro flask",
        "40oz tumbler with handle",
        "tumbler gift set",
        "stanley limited edition colors",
        "tumbler that keeps ice overnight",
        "stanley quencher replacement lid"
    ],
    "pricing_sentiment": "Customers accept and even defend the $45-50 price point when the product performs well. However, paint chipping and lid leaking create a strong perceived value mismatch. Reviewers frequently say for the price I expected better in negative reviews, suggesting price is amplifying dissatisfaction.",
    "seasonal_patterns": "Strong gifting spikes around holidays and wedding season. Back-to-school creates a secondary peak. Limited edition color drops generate their own demand spikes independent of seasons."
}

HYDRO_FLASK_ANALYSIS = {
    "executive_summary": "Hydro Flask is the durability king of the tumbler market, beloved for its indestructible build quality and reliable insulation. However, it is losing ground to Stanley in the everyday consumer market due to three critical gaps: no handle, poor cupholder compatibility, and limited color options. Customers who compare the two brands directly are increasingly choosing Stanley for daily use.",
    "overall_health_score": 68,
    "complaint_themes": [
        {
            "theme": "No handle makes it awkward to carry when full",
            "frequency_pct": 42,
            "emotional_intensity": "high",
            "example_quotes": [
                "I have seen the Stanley with its big comfortable handle and I am a little jealous.",
                "Without a handle it is genuinely difficult to use one-handed when full."
            ],
            "improvement_recommendation": "Add an ergonomic carry handle to the wide mouth 40oz series. This is the single feature customers cite most when switching to Stanley.",
            "estimated_rating_impact": "+0.4 stars if added"
        },
        {
            "theme": "Does not fit standard car cupholders",
            "frequency_pct": 35,
            "emotional_intensity": "high",
            "example_quotes": [
                "I was disappointed to discover it does not fit in my car cupholder.",
                "Car commuters may want to measure first."
            ],
            "improvement_recommendation": "Redesign the 40oz to fit standard car cupholders. This is a primary purchase criterion for the daily commuter segment.",
            "estimated_rating_impact": "+0.3 stars if fixed"
        },
        {
            "theme": "Straw lid sold separately adds unexpected cost",
            "frequency_pct": 28,
            "emotional_intensity": "medium",
            "example_quotes": [
                "I bought what I thought was a complete product and then had to spend another 15 dollars on the lid.",
                "Between the bottle and the lid this costs more than a Stanley which comes with everything."
            ],
            "improvement_recommendation": "Bundle the straw lid with the 40oz bottle or clearly communicate in the listing that the straw lid is sold separately.",
            "estimated_rating_impact": "+0.2 stars if bundled"
        },
        {
            "theme": "Limited color options vs competitors",
            "frequency_pct": 22,
            "emotional_intensity": "medium",
            "example_quotes": [
                "My Stanley collection has 8 different colors and new limited editions drop constantly.",
                "I find myself reaching for my Stanley every day because I love the colors."
            ],
            "improvement_recommendation": "Expand color palette and introduce seasonal limited editions. The Stanley color strategy has proven that color drives repeat purchases and gifting.",
            "estimated_rating_impact": "+0.2 stars if expanded"
        }
    ],
    "praise_themes": [
        {
            "theme": "Indestructible durability survives extreme conditions",
            "frequency_pct": 72,
            "example_quotes": [
                "I have dropped this thing down stairs, off a desk, thrown it in the back of my truck. Not a single dent.",
                "Construction worker here. This bottle has been on job sites with me for 18 months."
            ],
            "marketing_angle": "Own the durability positioning completely. Target outdoor enthusiasts, construction workers, athletes, and parents with clumsy kids. Built for real life."
        },
        {
            "theme": "No condensation on the exterior",
            "frequency_pct": 38,
            "example_quotes": [
                "No condensation on outside — desk stays dry.",
                "I can set this on my wooden furniture without worrying."
            ],
            "marketing_angle": "This is a direct win over Stanley whose condensation issue frustrates customers. Dry on the outside. Cold on the inside. is a powerful comparison claim."
        },
        {
            "theme": "Easy to clean — no mold issues",
            "frequency_pct": 32,
            "example_quotes": [
                "Wide mouth is easy to add ice and clean thoroughly.",
                "No weird crevices where mold can hide."
            ],
            "marketing_angle": "Directly addresses Stanley's mold problem. Wide mouth design. No hidden crevices. Clean every time. Target Stanley customers who have experienced the mold issue."
        }
    ],
    "listing_bullets": [
        "BUILT TO SURVIVE ANYTHING — Dropped off scaffolding, thrown in trucks, survived 3 years of daily use without a dent. The powder coat finish that actually lasts. For people who are hard on their gear.",
        "DRY DESK. DRY BAG. — Zero condensation on the exterior means your desk, your notebooks, and your bag stay completely dry. The insulation that works from the outside in.",
        "WIDE MOUTH THAT ACTUALLY CLEANS — No hidden crevices. No hard-to-reach straws. Fits a bottle brush perfectly. Dishwasher safe. Mold has nowhere to hide.",
        "ICE LASTS 24 HOURS — Tested by customers in hot trucks, on job sites, and in gym bags. Ice stays frozen from morning to night and beyond.",
        "BUY ONCE. USE FOREVER. — While others replace bottles every few months, Hydro Flask customers report using the same bottle for 3-5 years. The last water bottle you will ever need to buy."
    ],
    "listing_title_suggestion": "Hydro Flask Wide Mouth 40oz Water Bottle | Survives Drops and Dents | Zero Condensation | 24-Hour Ice Cold | Wide Mouth Easy Clean | Built for Real Life",
    "buyer_personas": [
        {
            "persona_name": "The Outdoor Adventurer",
            "percentage": 45,
            "description": "Hikers, campers, construction workers, and outdoor enthusiasts who prioritize durability above all else. Will pay a premium for gear that survives real conditions. Less influenced by social media trends.",
            "what_they_love": "Indestructible build, no condensation, reliable cold retention in extreme conditions",
            "what_frustrates_them": "The lack of a handle for long hikes and outdoor activities",
            "marketing_message": "Built for the trail. Built for the job site. Built to last longer than you expect it to."
        },
        {
            "persona_name": "The Minimalist Professional",
            "percentage": 30,
            "description": "Design-conscious buyers who prefer the clean, simple aesthetic of Hydro Flask over the more trend-driven Stanley look. Value quality over color variety. Often professionals and older millennials.",
            "what_they_love": "Clean minimalist design, proven quality, and the understated premium aesthetic",
            "what_frustrates_them": "Limited color options and the lack of handle for daily carrying",
            "marketing_message": "Less noise. More function. The water bottle that does not need to be a fashion statement."
        }
    ],
    "risk_alerts": [
        {
            "alert_type": "Stanley Competitive Threat — Losing Daily Use Market",
            "severity": "critical",
            "description": "Multiple reviewers explicitly state they switched from Hydro Flask to Stanley or would buy Stanley today. The handle and cupholder fit are the cited reasons. Hydro Flask is losing the daily commuter segment.",
            "recommended_action": "Urgently add handle and redesign for cupholder compatibility. Reposition Hydro Flask as the outdoor/adventure premium alternative with superior durability and no condensation."
        },
        {
            "alert_type": "Competitor Positioning Opportunity — Stanley Mold and Leaking",
            "severity": "medium",
            "description": "Stanley customers frequently complain about mold in the straw and lid leaking. Hydro Flask has neither of these issues. This is an unmarketed advantage.",
            "recommended_action": "Create direct comparison content targeting Stanley's mold and leak issues. No hidden crevices. No leaking lids. No drama. could resonate strongly with frustrated Stanley customers."
        }
    ],
    "keyword_opportunities": [
        "hydro flask vs stanley",
        "water bottle that doesnt sweat",
        "indestructible water bottle",
        "water bottle for construction workers",
        "no condensation water bottle",
        "hydro flask handle attachment",
        "durable tumbler for outdoors",
        "water bottle that lasts years",
        "hydro flask cupholder adapter",
        "best water bottle for hiking"
    ],
    "pricing_sentiment": "Customers accept the premium price when buying for durability and outdoor use. However, the discovery that the straw lid is sold separately creates a negative value perception. When compared directly to Stanley at a similar price point, customers increasingly feel Hydro Flask offers less everyday value.",
    "seasonal_patterns": "Strong sales during outdoor season spring-summer. Back to school creates a secondary peak. Less gift-driven than Stanley — purchased more for personal use than gifting."
}

STANLEY_GAP_ANALYSIS = {
    "my_advantages": [
        {
            "advantage": "Cupholder compatibility — Hydro Flask does not fit standard car cupholders",
            "evidence": "Hydro Flask reviewer: 'I was disappointed to discover it does not fit in my car cupholder. Car commuters may want to measure first.'",
            "marketing_angle": "The only 40oz tumbler engineered to fit your car cupholder. Make this a primary differentiator in all advertising targeting commuters."
        },
        {
            "advantage": "Ergonomic carry handle — Hydro Flask has no handle",
            "evidence": "Hydro Flask reviewer: 'I have seen the Stanley with its big comfortable handle and I am a little jealous. Without a handle it is genuinely difficult.'",
            "marketing_angle": "The handle your commute needs. Feature the handle prominently in every lifestyle photo showing use outside the home."
        },
        {
            "advantage": "Straw lid included — Hydro Flask charges extra for straw lid",
            "evidence": "Hydro Flask reviewer: 'I bought what I thought was a complete product and then had to spend another 15 dollars on the lid I actually wanted.'",
            "marketing_angle": "Everything included. Nothing extra. The complete tumbler experience from day one — no hidden costs."
        },
        {
            "advantage": "Color variety drives gifting and repeat purchases",
            "evidence": "Hydro Flask reviewer: 'My Stanley collection has 8 different colors and new limited editions drop constantly. I find myself reaching for my Stanley.'",
            "marketing_angle": "40+ colors and limited edition drops. Gift-ready with every purchase. The tumbler that sells itself."
        }
    ],
    "my_vulnerabilities": [
        {
            "vulnerability": "Lid leaks when tilted — Hydro Flask does not have this issue",
            "evidence": "Stanley reviewer: 'My laptop is destroyed. My AirPods case is destroyed. Everything in my bag was soaked.' Hydro Flask customers report zero leaking issues.",
            "fix_recommendation": "Redesign lid seal to prevent leaking at angles. This is the #1 reason customers switch to Hydro Flask or give Stanley 1-star reviews."
        },
        {
            "vulnerability": "Exterior condensation damages surfaces — Hydro Flask stays dry outside",
            "evidence": "Stanley reviewer: 'I set it on my wooden desk and it left a ring mark.' Hydro Flask is specifically praised for zero exterior condensation.",
            "fix_recommendation": "Improve exterior insulation layer or provide a silicone sleeve. Market the condensation fix as a feature update."
        },
        {
            "vulnerability": "Paint chipping — Hydro Flask powder coat is significantly more durable",
            "evidence": "Stanley reviewer: 'Within 2 months the paint started chipping significantly.' Hydro Flask customers report 3+ years of use with minimal wear.",
            "fix_recommendation": "Invest in more durable finish technology or introduce a premium finish tier."
        },
        {
            "vulnerability": "Straw mold in hard-to-clean crevices — Hydro Flask wide mouth is easier to clean",
            "evidence": "Stanley reviewer: 'My straw got moldy after only 3 weeks. There are little grooves in the straw that are impossible to clean.'",
            "fix_recommendation": "Redesign straw and lid for easier cleaning. Consider a dishwasher-safe certification to address hygiene concerns."
        }
    ],
    "market_opportunity": "Stanley owns the daily commuter and gifting markets with superior cupholder fit, handle ergonomics, and color variety. The critical opportunity is to fix the lid leaking and paint chipping issues before Hydro Flask capitalizes on them. A lid redesign would neutralize Hydro Flask's primary competitive argument while Stanley's color strategy and handle advantage remain unchallenged.",
    "positioning_statement": "The tumbler that fits your life — your cupholder, your hand, your style. Stanley does what Hydro Flask cannot: go from car to desk to gym without missing a beat. Handle included. Straw included. Cupholder fit guaranteed.",
    "head_to_head_scores": {
        "quality_perception":  {"mine": 7, "competitor": 9},
        "value_for_money":     {"mine": 8, "competitor": 6},
        "customer_service":    {"mine": 6, "competitor": 7},
        "shipping_packaging":  {"mine": 8, "competitor": 7},
        "ease_of_use":         {"mine": 9, "competitor": 5}
    }
}

STANLEY_INFO = {
    "title": "Stanley Quencher H2.0 FlowState Tumbler 40oz — Cupholder Compatible Insulated Stainless Steel Cup with Lid and Straw",
    "overall_rating": 4.2,
    "total_reviews": 67842,
    "asin": "DEMO_STANLEY",
    "image_url": "assets/stanley.jpg",
}

HYDRO_FLASK_INFO = {
    "title": "Hydro Flask Wide Mouth Water Bottle 40oz — Stainless Steel Vacuum Insulated",
    "overall_rating": 4.4,
    "total_reviews": 28431,
    "asin": "DEMO_HYDROFLASK",
    "image_url": "assets/hydroflask.jpg",
}


def _make_stanley_trends():
    return {
        "monthly_data": [
            {"month": "2024-01", "review_count": 2, "average_rating": 3.5,  "verified_purchase_rate": 100.0, "complaint_rate": 50.0, "praise_rate": 50.0},
            {"month": "2024-02", "review_count": 3, "average_rating": 3.7,  "verified_purchase_rate": 100.0, "complaint_rate": 33.3, "praise_rate": 66.7},
            {"month": "2024-03", "review_count": 4, "average_rating": 3.5,  "verified_purchase_rate": 100.0, "complaint_rate": 50.0, "praise_rate": 50.0},
            {"month": "2024-04", "review_count": 3, "average_rating": 3.7,  "verified_purchase_rate": 100.0, "complaint_rate": 33.3, "praise_rate": 66.7},
            {"month": "2024-05", "review_count": 3, "average_rating": 3.3,  "verified_purchase_rate": 100.0, "complaint_rate": 66.7, "praise_rate": 33.3},
            {"month": "2024-06", "review_count": 1, "average_rating": 5.0,  "verified_purchase_rate": 100.0, "complaint_rate": 0.0,  "praise_rate": 100.0},
        ],
        "trend_direction": "declining",
        "trend_magnitude": -8.5,
        "spike_months": ["2024-05"],
        "insight": "Sentiment is declining — lid leaking complaints have increased 67% in the last 3 months. Complaint spike detected in 2024-05 correlating with summer commute season."
    }


def _make_stanley_rating_dist():
    return {
        "1": {"count": 2, "percentage": 13.3},
        "2": {"count": 2, "percentage": 13.3},
        "3": {"count": 2, "percentage": 13.3},
        "4": {"count": 3, "percentage": 20.0},
        "5": {"count": 6, "percentage": 40.0},
    }


def _make_hydro_flask_rating_dist():
    return {
        "1": {"count": 1, "percentage": 10.0},
        "2": {"count": 2, "percentage": 20.0},
        "3": {"count": 2, "percentage": 20.0},
        "4": {"count": 2, "percentage": 20.0},
        "5": {"count": 3, "percentage": 30.0},
    }


def get_demo_data(product_num: int = 1) -> dict:
    """
    Returns everything the Streamlit app needs for the full UI.
    product_num=1 → Stanley Quencher (primary product with Hydro Flask competitor)
    product_num=2 → Hydro Flask (standalone, no competitor)
    """
    if product_num == 1:
        df         = _make_stanley_reviews()
        trusted_df = df[df["rating"] >= 3].copy().reset_index(drop=True)
        flagged_df = df[df["rating"] < 3].copy().reset_index(drop=True)
        trusted_df["trust_score"] = 85
        flagged_df["trust_score"] = 35

        hf_df         = _make_hydro_flask_reviews()
        hf_trusted_df = hf_df[hf_df["rating"] >= 3].copy().reset_index(drop=True)
        hf_trusted_df["trust_score"] = 82

        return {
            "product_info":        STANLEY_INFO,
            "reviews_df":          df,
            "trusted_reviews":     trusted_df,
            "flagged_reviews":     flagged_df,
            "filter_stats": {
                "total_reviews_analyzed": len(df),
                "trusted_count":          len(trusted_df),
                "flagged_count":          len(flagged_df),
                "fake_percentage":        round(len(flagged_df) / len(df) * 100, 1),
                "verified_purchase_rate": 100.0,
                "average_trust_score":    72.0,
            },
            "analysis":            STANLEY_ANALYSIS,
            "trends":              _make_stanley_trends(),
            "rating_distribution": _make_stanley_rating_dist(),
            "has_competitor":      True,
            "competitor": {
                "product_info":        HYDRO_FLASK_INFO,
                "reviews_df":          hf_df,
                "trusted_reviews":     hf_trusted_df,
                "filter_stats": {
                    "total_reviews_analyzed": len(hf_df),
                    "trusted_count":          len(hf_trusted_df),
                    "flagged_count":          len(hf_df) - len(hf_trusted_df),
                    "fake_percentage":        round((len(hf_df) - len(hf_trusted_df)) / len(hf_df) * 100, 1),
                    "verified_purchase_rate": 100.0,
                    "average_trust_score":    68.0,
                },
                "trends":              _make_stanley_trends(),
                "rating_distribution": _make_hydro_flask_rating_dist(),
            },
            "gap_analysis":        STANLEY_GAP_ANALYSIS,
        }
    else:
        df         = _make_hydro_flask_reviews()
        trusted_df = df[df["rating"] >= 3].copy().reset_index(drop=True)
        flagged_df = df[df["rating"] < 3].copy().reset_index(drop=True)
        trusted_df["trust_score"] = 82
        flagged_df["trust_score"] = 38

        return {
            "product_info":        HYDRO_FLASK_INFO,
            "reviews_df":          df,
            "trusted_reviews":     trusted_df,
            "flagged_reviews":     flagged_df,
            "filter_stats": {
                "total_reviews_analyzed": len(df),
                "trusted_count":          len(trusted_df),
                "flagged_count":          len(flagged_df),
                "fake_percentage":        round(len(flagged_df) / len(df) * 100, 1),
                "verified_purchase_rate": 100.0,
                "average_trust_score":    68.0,
            },
            "analysis":            HYDRO_FLASK_ANALYSIS,
            "trends":              _make_stanley_trends(),
            "rating_distribution": _make_hydro_flask_rating_dist(),
            "has_competitor":      False,
            "competitor":          None,
            "gap_analysis":        None,
        }
