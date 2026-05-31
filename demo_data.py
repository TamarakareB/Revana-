"""
Pre-loaded demo data for Revana. Provides two realistic products with
40 reviews each, pre-computed analysis, and all derived stats so the
demo runs instantly with no API calls.
"""

import pandas as pd

# ---------------------------------------------------------------------------
# PRODUCT 1 — TechSound Pro Wireless Earbuds
# ---------------------------------------------------------------------------

TECHSOUND_INFO = {
    "title": "TechSound Pro Wireless Earbuds — Active Noise Cancelling, 48H Battery, IPX5 Waterproof",
    "overall_rating": 4.1,
    "total_reviews": 3847,
    "asin": "DEMO001",
}

def _d(date_str):
    """Build a Rainforest-style date dict from YYYY-MM-DD."""
    months = ["January","February","March","April","May","June",
              "July","August","September","October","November","December"]
    y, m, day = date_str.split("-")
    label = f"{months[int(m)-1]} {int(day)}, {y}"
    return {"raw": f"Reviewed in the United States on {label}", "utc": f"{date_str}T00:00:00.000Z"}

_TECHSOUND_ROWS = [
    # --- 5-star reviews (16) ---
    (5, "Yolanda Ferreira",      True,  _d("2025-06-03"),
     "I've tried at least six pairs of wireless earbuds over the past three years and these are by far my favorite. The sound profile is balanced without being boring — there's enough bass to feel hip-hop but enough clarity to hear every word in podcasts. The ANC blocks out my open-plan office completely. I wore them for a six-hour flight and my ears never ached. Pairing was instant with both my iPhone and MacBook. Battery lasted four days of commuting before I had to charge. Genuinely impressed."),
    (5, "Marcus Delgado",        True,  _d("2025-06-18"),
     "Sound quality punches well above the price. I compared these directly against earbuds that cost twice as much at a friend's place and honestly preferred the TechSound mids and highs. The fit is snug — I went jogging in light rain and they stayed in place. IPX5 rating seems legit. Only minor note is the touch controls take a day to get used to but once you learn them they're intuitive. Highly recommend for the price point."),
    (5, "Priya Nambiar",         True,  _d("2025-07-04"),
     "These are my third pair of TechSound earbuds and they keep getting better. The ANC on this version is noticeably stronger than the previous gen. I use them during online therapy sessions and the microphone quality has never caused a complaint from my therapist. The case is compact enough to clip to my gym bag. Five stars without hesitation."),
    (5, "Derek Hutchinson",      True,  _d("2025-07-22"),
     "Bought these for my daily train commute. The noise cancellation turns a loud, rattling carriage into something approaching silence. I can finally focus on audiobooks. Battery life has been solid — I charge Sunday night and it gets me through to Thursday with about 2-3 hours of use per day. The transparency mode is excellent for when someone needs to talk to me. Best commuter purchase I've made."),
    (5, "Sasha Kowalczyk",       False, _d("2025-08-09"),
     "Perfect for working from home. My household is chaotic — two kids, a dog, a partner on calls all day. These earbuds let me disappear into work mode. The ANC is not just marketing — it genuinely reduces ambient noise to a soft hum. Call quality is crisp; my colleagues say I sound better on these than I do on my laptop mic. The 48-hour total battery claim is real if you're not blasting volume."),
    (5, "Tomás Vierira",         True,  _d("2025-08-27"),
     "Spectacular value. I'm an audio engineer so I'm picky about sound and even I can't complain at this price. The soundstage is wider than expected for closed earbuds. EQ app works well. Fit is comfortable for three-hour sessions. Would genuinely recommend these to anyone who asks."),
    (5, "Rachel Osei-Bonsu",     True,  _d("2025-09-15"),
     "These replaced a pair that cost me $180 and I don't miss the expensive ones at all. Sound quality is comparable, battery life is better, and the charging case is more pocketable. The only thing I noticed is the bass is a touch heavy out of the box but you can easily adjust that in the app. Wear them at the gym four times a week. They've survived spin class, sweat, and being dropped on a tile floor. Solid."),
    (5, "Liu Wei",               True,  _d("2025-09-29"),
     "I'm a software developer who listens to music eight hours a day. Comfort over extended periods was my top priority and these deliver. The medium tips seal perfectly in my ears. I don't get the fatigue I had with my old earbuds after two or three hours. Audio is rich. Latency is low enough for video calls and watching YouTube. Charging case feels premium. Happy with this purchase."),
    (5, "Amanda Strickland",     True,  _d("2025-10-11"),
     "My husband got a pair first and I was skeptical because he always buys gadgets impulsively. But these genuinely won me over. I tested them at the gym, on a walk, and during a long drive. The secure fit held even through a HIIT class. Sound is clean and dynamic. ANC blocked out the gym's thumping music system when I needed to focus on a podcast. Ordered a second pair as a gift."),
    (5, "Jerome Baptiste",       True,  _d("2025-10-24"),
     "If you're on the fence, just buy them. I hesitated for a month reading reviews and ultimately regret not pulling the trigger sooner. The best compliment I can give is that I forget I'm wearing them — they just disappear into my ears and the world outside disappears too. Customer service was also responsive when I had a question about the app; replied in under two hours."),
    (5, "Fatima Al-Rashid",      True,  _d("2025-11-07"),
     "I'm a nurse and I wear these during 12-hour shifts at the hospital. Comfort is the main thing and I've been pleasantly surprised — I can wear them for four or five hours before my ears need a break. The ANC helps me decompress during break time. Sound quality is great. I've recommended these to three colleagues who've all bought them."),
    (5, "Kwame Asante",          True,  _d("2025-11-28"),
     "Outstanding product for the money. I've purchased earbuds from five different brands over the years and these sit comfortably in the top two. The ANC engages quickly and works well on planes — I tested them on a transatlantic flight. Sound signature is warm but not muddy. The touch controls are responsive after you get used to the placement. App is clean and useful."),
    (5, "Brigitte Müller",       True,  _d("2025-12-10"),
     "Bought these as a Christmas gift for myself. Set them up in under a minute and the sound blew me away. I mostly listen to jazz and classical and the instrument separation is wonderful. ANC is perfect for blocking out my neighbour's TV. Battery life is excellent — nearly a week before recharging with my use pattern. Beautiful product."),
    (5, "Carlos Mendez-Torres",  True,  _d("2026-01-06"),
     "Second review I've ever written in my life — these earbuds are worth it. I work in construction and needed something tough, good-sounding, and actually comfortable under my hard hat. TechSound Pro ticks all three. The IPX5 rating holds up — I've been caught in rain twice and they're fine. Coworkers keep asking what brand they are."),
    (5, "Ingrid Holmberg",       True,  _d("2026-02-14"),
     "Valentine's Day gift to myself after months of debating. No regrets. The sound is lush, the fit is secure, and the ANC rivals earbuds I've tried at three times the cost. I particularly love the transparency mode for quick conversations — it switches instantly. Five stars, would buy again."),
    (5, "David Okafor",          False, _d("2026-04-02"),
     "These are legitimately excellent earbuds. I've been using them for two months and have zero complaints. Sound quality is balanced and engaging, battery lasts as advertised, and the ANC is strong. The app is one of the better companion apps I've used — clean UI, useful EQ, wear detection works reliably. Solid five stars."),

    # --- 4-star reviews (14) ---
    (4, "Nina Kostrova",         True,  _d("2025-06-29"),
     "Really good earbuds overall. Sound quality is excellent and the ANC works well. My only gripe is the right earbud seems to drain slightly faster than the left — after a few weeks I'd sometimes pick up the case and find the right at 30% while the left was at 55%. Not a dealbreaker but something I noticed. Four stars because everything else is great."),
    (4, "Ben Achterberg",        True,  _d("2025-07-15"),
     "Solid earbuds for the price. Sound is punchy and the fit is comfortable. I dropped one star because the Bluetooth occasionally drops for a split second during my commute — it happens maybe once a day on the train and reconnects within two seconds but it's slightly annoying. Otherwise excellent. Would still recommend."),
    (4, "Chioma Eze",            True,  _d("2025-08-04"),
     "Good earbuds. I particularly love the sound quality and the secure fit during runs. Dropping to four stars because the battery life, while good, doesn't quite match the advertised 48 hours when ANC is on — I'd say it's closer to 30-35 hours total across buds and case with ANC active. Still very usable but worth knowing before you buy."),
    (4, "Piotr Wiśniewski",      True,  _d("2025-08-19"),
     "I've been using these daily for six weeks. Sound quality is genuinely impressive — detailed highs, warm mids, controlled bass. The ANC is very effective on public transport. Main reason for four stars rather than five: the touch controls are overly sensitive and I accidentally skip tracks or pause when adjusting the fit. I've mostly adapted but it was frustrating initially."),
    (4, "Amara Kouyaté",         True,  _d("2025-09-08"),
     "Strong recommendation with one caveat. These earbuds are excellent for medium-sized ears — I can confirm. My partner has large ears and found the tips don't come in a size that seals properly for her. She ended up buying third-party tips. If TechSound added an XL tip option this would be five stars immediately. Sound quality and ANC are superb."),
    (4, "Oliver Blackwood",      True,  _d("2025-09-22"),
     "Very good product. I use them for long workday listening and they're comfortable and great-sounding. Deducting one star for the case — it picks up scratches and fingerprints very easily. After three months it looks beaten up despite me treating it carefully. The earbuds themselves still look pristine. Minor cosmetic issue but worth mentioning."),
    (4, "Sunita Patel",          True,  _d("2025-10-03"),
     "Four stars — would be five if not for the companion app. The earbuds themselves are outstanding: great sound, solid ANC, comfortable fit for long sessions. But the app crashes occasionally on my Android phone and I lost my EQ settings twice. Hope they fix this in an update. The hardware earns five stars easily."),
    (4, "Johan van der Berg",    True,  _d("2025-10-30"),
     "Great everyday earbuds. The sound profile is well-tuned for pop and electronic music which is mainly what I listen to. Battery is solid. My reason for four instead of five stars: the microphone picks up wind noise noticeably when I take calls outdoors. It's fine indoors but on windy days callers can tell. Something for TechSound to address in future firmware."),
    (4, "Nadia Petrov",          True,  _d("2025-11-14"),
     "Really impressive for the price range. Sound quality, ANC, comfort — all above average. One issue I've hit a few times: reconnecting to my laptop after using them with my phone requires me to manually select them in Bluetooth settings rather than auto-switching. It's a minor workflow annoyance. Would still recommend strongly."),
    (4, "Emmanuel Osei",         True,  _d("2025-12-03"),
     "These have become my daily driver earbuds after six months. Comfort is excellent, sound is rich, and the ANC is genuinely useful. Four stars because the right earbud started dying noticeably faster than the left after about four months of daily use. Not sure if this is a battery issue or a usage asymmetry thing but it's noticeable. Still very usable."),
    (4, "Valentina Cruz",        False, _d("2026-01-18"),
     "Good earbuds. The sound quality surprised me — I expected budget performance and got something much better. ANC is effective for open-plan offices. Dropping one star because the charging case lid feels slightly loose compared to the earbuds I used before. Not broken, just doesn't have that premium snap. Overall a strong buy."),
    (4, "James Okonkwo",         True,  _d("2026-02-28"),
     "These earbuds handle everything I throw at them — workouts, commuting, long work sessions. Sound is clear and dynamic. The only reason I'm giving four stars instead of five is that I've had two Bluetooth drops per week on average when using them with my Windows laptop. On my phone they're rock solid. Might be a Windows driver issue. Great earbuds overall."),
    (4, "Yuki Tanaka",           True,  _d("2026-03-22"),
     "I've owned these for two months and use them about four hours daily. Really good sound quality and the ANC has improved my focus at work significantly. One minor issue: the app's battery percentage display for each individual earbud sometimes shows incorrect readings — left shows 70% but when I open the case and check physically it's more like 50%. Bug rather than hardware. Worth noting."),
    (4, "Lena Brandt",           True,  _d("2026-04-19"),
     "Excellent performance with one recurring annoyance. The earbuds themselves are phenomenal — best I've owned at this price. But the left earbud occasionally doesn't wake up when I take it out of the case and I have to put it back in and take it out again. Happens maybe twice a week. A firmware fix would bump this to five stars easily."),

    # --- 3-star reviews (5) ---
    (3, "Robert Flanagan",       True,  _d("2025-07-30"),
     "Mixed feelings on these. The sound quality is good when they're working well, and the ANC is decent. But I've had connectivity issues since day one — the earbuds disconnect from my phone about three times per hour when the phone is in my pocket. I've tried re-pairing, factory reset, everything in the FAQ. Still happens. My phone is a Samsung Galaxy S23 if that helps. Support was helpful but the issue persists."),
    (3, "Melissa Grant",         True,  _d("2025-09-05"),
     "Sound quality and noise cancellation are genuinely good. The battery life is decent but not the 48 hours they advertise — I get maybe 28-30 hours total when ANC is on, which is still fine. The main reason I'm at three stars is the fit: the included ear tips don't work well for my ears. The medium is too small and the large makes my ears sore after 30 minutes. I need a medium-large size that doesn't exist. Sound escapes and bass disappears without a good seal."),
    (3, "Aleksandr Petrov",      False, _d("2025-11-22"),
     "These earbuds are a 50/50 proposition for me. The sound quality is legitimately excellent — no complaints there. But Bluetooth stability has been an issue from week three onwards. I get a cut-out every 10-20 minutes during my gym session. The gym has lots of competing signals so maybe that's a factor. When they work, they're great. When they drop, it's frustrating. Three stars feels fair."),
    (3, "Angela Torres",         True,  _d("2026-01-30"),
     "The audio quality is genuinely impressive for the price and the ANC helps in my noisy apartment. I'd give five stars if not for two problems: the right earbud consistently dies before the left (I track it obsessively and the right uses about 20% more power for reasons I can't explain), and the app is buggy on iOS 17. It crashes when I try to update firmware. Both issues feel like software problems that should be fixable but it's been three months and no updates yet."),
    (3, "Michael Adeyemi",       True,  _d("2026-03-08"),
     "Decent earbuds. Sound quality gets four stars. ANC gets four stars. Battery gets three stars — nowhere near the claimed 48 hours once ANC is on. Fit gets two stars for me personally — I have smaller ears and even the small tips feel big. Connection stability gets three stars — occasional drops but nothing constant. The package as a whole is three stars. They have real potential but the battery and fit issues hold them back."),

    # --- 2-star reviews (3) ---
    (2, "Patricia Simmons",      True,  _d("2025-10-19"),
     "Disappointed. The earbuds sounded great for the first two months and I was happy. Then at about the two-month mark the right earbud started dying at twice the rate of the left. Now the right is dead by the time the left is at 65%. I use them symmetrically so it's clearly a battery defect. Support offered a replacement but I'd have to pay return shipping which feels wrong for a product defect. Sound quality when both are alive is excellent but the battery imbalance makes them unusable in practice."),
    (2, "Finn Larsson",          True,  _d("2025-12-28"),
     "Bluetooth connectivity is just not reliable enough for daily use. I wanted to love these — the sound when they stay connected is really good, and the ANC is solid. But they drop connection three to five times per hour on my morning train. I've tried everything: re-pairing, different codec settings, keeping my phone closer. Nothing fixes it. Other commuters with different earbuds don't seem to have this issue on the same route. Returning these and going back to my old pair."),
    (2, "Sandra Kim",            True,  _d("2026-04-28"),
     "The battery life advertised is simply not accurate. With ANC on — which is the main reason I bought these — I get about 4.5 hours per charge on the earbuds, not the claimed 6-7 hours. The case adds maybe 15 hours more. So total is around 20 hours with ANC on, not 48. This is a significant gap. The sound quality is good so I'm keeping them, but I feel misled. If you need ANC all day without recharging, look elsewhere."),

    # --- 1-star reviews (2) ---
    (1, "Kevin Marsh",           True,  _d("2025-08-14"),
     "Failed after 10 weeks. The right earbud stopped charging entirely. Tried multiple cables, cleaned the contacts, re-seated dozens of times. Dead. Customer service was slow to respond and when they did they asked me to do all the same troubleshooting steps I'd already described doing. Eventually they offered a replacement but the 2-week wait for shipping means I've been without earbuds for a month. The product itself sounded great while it lasted but a 10-week lifespan is not acceptable at any price."),
    (1, "Diane Rousseau",        True,  _d("2026-02-07"),
     "Absolutely terrible Bluetooth stability. Returned twice, same issue both times. The earbuds drop connection every few minutes in any crowded environment — shopping mall, gym, open-plan office. In a quiet house they work fine. The moment there's any wireless congestion they fall apart. I've never experienced anything like this with any other earbuds. TechSound clearly has an antenna design problem. Do not buy if you plan to use these anywhere but your living room."),
]

TECHSOUND_REVIEWS_DF = pd.DataFrame(_TECHSOUND_ROWS, columns=[
    "rating", "reviewer_name", "verified_purchase", "date", "body"
])
TECHSOUND_REVIEWS_DF["title"] = [
    "Best earbuds I've owned at any price", "Sound quality rivals earbuds twice the cost",
    "Third pair of TechSound — keeps getting better", "My commute is transformed",
    "Perfect WFH companion", "Audio engineer approved", "Replaced my $180 pair happily",
    "Eight hours a day, no fatigue", "Won over a skeptic", "Just buy them",
    "12-hour shift approved", "Best ANC I've tested at this price", "Christmas gift to myself",
    "Built for construction sites", "Valentine's Day treat — no regrets", "Legitimately excellent",
    "Great but right earbud drains faster", "Occasional Bluetooth blip on the train",
    "Battery life slightly below advertised with ANC", "Touch controls a bit sensitive",
    "Perfect fit — unless you have large ears", "Case scratches too easily",
    "Great earbuds, so-so app", "Wind noise on outdoor calls", "Multi-device switching is manual",
    "Right earbud degraded after 4 months", "Case lid feels loose", "Drops on Windows laptop",
    "App battery display is buggy", "Left earbud occasionally sleeps in",
    "Connectivity issues with Samsung", "Fit is the problem for my ears",
    "Great sound, unreliable in the gym", "Right earbud + app bugs on iOS",
    "Three stars — decent but not great", "Right earbud died at 2 months",
    "Bluetooth drops make it unusable for commuting", "Battery life with ANC is misleading",
    "Failed hardware after 10 weeks", "Terrible in any crowded environment",
]

# ---------------------------------------------------------------------------
# PRODUCT 2 — AudioMax Bluetooth Headphones (competitor, over-ear)
# ---------------------------------------------------------------------------

AUDIOMAX_INFO = {
    "title": "AudioMax Pro Noise Cancelling Headphones — Over-Ear, 60H Battery, Hi-Res Audio Certified",
    "overall_rating": 3.9,
    "total_reviews": 2214,
    "asin": "DEMO002",
}

_AUDIOMAX_ROWS = [
    # --- 5-star reviews (14) ---
    (5, "Thomas Kirchner",      True,  _d("2025-06-07"),
     "I've owned six pairs of over-ear headphones over the years and the AudioMax Pro is the best noise cancellation I've experienced outside of a recording studio. On a transatlantic flight the engine roar just disappeared. Sound quality is detailed and natural — I appreciate that it doesn't artificially boost bass. The 60-hour battery claim is real; I went almost two weeks on a single charge with moderate daily use. Premium product."),
    (5, "Sophia Nakamura",      True,  _d("2025-06-24"),
     "These headphones are in a different league from anything I've tried at this price. The ANC is exceptional — I use them in a loud coworking space and I can think clearly. The soundstage is wide and instrument separation is excellent for classical music. Comfort is good for two to three hour sessions. Build quality feels solid — metal headband, reinforced hinges. Well worth the premium."),
    (5, "Ibrahim Hassan",        True,  _d("2025-07-13"),
     "I do a lot of remote work from cafes and airports. These headphones have genuinely changed my productivity. The ANC removes ambient noise completely. Battery lasts a full work week before I need to recharge. Sound quality for music listening is exceptional — detailed, spacious, and musical. The case that comes with them is excellent too. Strong recommendation."),
    (5, "Clare Ashworth",        True,  _d("2025-07-28"),
     "Bought these to help with my ADHD — blocking background noise is crucial for focus. These are the best thing I've ever bought for that purpose. The ANC is superb. I can work for hours in noisy environments without being distracted. Sound quality for music is also wonderful. The ear cushions are soft and don't cause pain over long sessions. Five stars, will buy again when these eventually wear out."),
    (5, "Lorenzo Ferrari",       True,  _d("2025-08-15"),
     "I'm a music producer and I use these for casual listening and referencing. The sound accuracy is impressive — not hyped, not flat, just natural and revealing. ANC is industry-leading at this price point. Battery is genuinely 60 hours with ANC on at moderate volume. These are a professional-grade product at a consumer price. Exceptional."),
    (5, "Amelia Patterson",      True,  _d("2025-09-02"),
     "Replaced my Sony XM5s with these and I don't miss them. The AudioMax Pro edges ahead on battery life and the ANC feels slightly more effective in low-frequency environments like planes. Sound quality is a matter of preference but I find the AudioMax tuning more natural. Build quality is excellent. The app is well-designed and stable. Great product."),
    (5, "Riku Virtanen",         True,  _d("2025-09-20"),
     "These headphones are wonderful for focus work. The ANC is among the best I've tested and I've tested a lot. The padding is memory foam and the pressure on the head is gentle enough for all-day wear. Sound is detailed and engaging. My only observation — not a complaint — is the clamping force is firm at first; it loosens after a week or two of use. Five stars for everything else."),
    (5, "Zoe Campbell",          False, _d("2025-10-08"),
     "Outstanding audio quality and best-in-class noise cancellation. I bought these for train travel and they've made my daily commute actually enjoyable. The battery is legitimately outstanding — I charge once a week. Build quality feels premium without feeling heavy. The fold-flat design makes them easy to carry. I've recommended these to five people already."),
    (5, "Daniel Hoffmann",       True,  _d("2025-10-25"),
     "Spectacular noise cancellation and superb sound. I work in an open-plan office and these allow me to concentrate completely. The sound quality for music is natural and detailed. Battery life is extraordinary. The app is polished and useful. My only small note is the headband could use slightly more padding at the top, but it's a very minor point. Highly recommended."),
    (5, "Aisha Traoré",          True,  _d("2025-11-12"),
     "These headphones are a revelation for someone who works in noisy environments. The ANC is so effective I sometimes have to take them off to hear if someone is speaking to me. Sound quality is wonderful for music. Battery lasts almost two weeks with my usage pattern. The ear cushions are comfortable and breathable. Exceptional product."),
    (5, "Matthew Chen",          True,  _d("2025-12-01"),
     "Bought these on a Black Friday deal and they're worth every penny at full price too. The ANC is the best I've heard at this price — it genuinely rivals headphones costing double. Sound signature is neutral and revealing. Build quality is solid metal and plastic, feels durable. Battery life is extraordinary. These are my headphones for the next five years."),
    (5, "Valentina Moretti",     True,  _d("2026-01-09"),
     "Perfect work-from-home headphones. The ANC completely blocks my family's TV and my partner's work calls. Sound quality is excellent for both music and video calls. The microphone is clear — colleagues say it's the best they've heard from me. Battery life is exceptional. Comfortable for four-to-five hour sessions. Five stars without hesitation."),
    (5, "Elan Brightwater",      True,  _d("2026-02-20"),
     "These are genuinely excellent headphones. The noise cancellation is superb — more effective than anything I've tried at this price tier. Sound quality is detailed and non-fatiguing over long sessions. The build quality is solid. My only small wish would be slightly softer ear cushion material for warm weather listening. But at this price, exceptional value."),
    (5, "Chidera Obi",           True,  _d("2026-03-15"),
     "Everything I wanted in a pair of headphones. ANC is exceptional, battery is extraordinary, sound is natural and detailed. They fold flat into a compact case. App is well-designed. Microphone is clear for calls. I struggled to find anything to complain about after three months of daily use. Buy these."),

    # --- 4-star reviews (12) ---
    (4, "Rebecca Morrison",      True,  _d("2025-06-15"),
     "Really impressive headphones. The ANC and sound quality are both excellent — the best I've heard at this price. I'm dropping one star for the ear cushion material: it's synthetic leather that gets warm and sweaty during longer sessions in summer. After about two hours I need a break not because of discomfort but because of heat. If you're in a cool environment or only use them in winter this isn't an issue at all."),
    (4, "Victor Ogundimu",       True,  _d("2025-07-06"),
     "Great headphones overall. Sound quality and ANC are both excellent. My reason for four stars: the clamping force is quite strong out of the box. It's not painful but it's noticeably firm. I've been told it loosens over time and after three weeks it has improved somewhat. If you have a larger head this might be worth noting. Excellent audio product regardless."),
    (4, "Hannah Schmidt",        True,  _d("2025-07-24"),
     "Good headphones with superb ANC. The sound quality is natural and detailed — very good for the price. I'm giving four stars because the companion app had a significant bug for the first few weeks after launch that corrupted saved EQ settings. It was fixed in an update but I lost my settings twice. The underlying hardware is clearly five-star quality."),
    (4, "Jerome Williams",       True,  _d("2025-08-21"),
     "The ANC on these is legitimately the best I've tried outside of Bose QC45s, and the sound quality is actually better than the Bose in my opinion. Dropping one star because the ear cushion material shows wear faster than I expected — after four months of daily use the edges are starting to peel slightly. Not functionally impaired but it doesn't look great. Would buy again despite this."),
    (4, "Miriam Goldstein",      True,  _d("2025-09-13"),
     "Excellent headphones for the price. Sound is detailed and the ANC is superb. My one issue is the headband padding. After about three hours of continuous use I feel pressure at the top of my head. I've started putting a thin pad underneath which helps but it shouldn't be necessary. Everything else is outstanding. Four stars and a strong recommendation with that caveat."),
    (4, "Patrick Nwosu",         True,  _d("2025-10-18"),
     "Very good headphones. ANC is excellent and the battery life is genuinely extraordinary. My reason for four rather than five stars: the app disconnects from the headphones occasionally and I have to close and reopen it to reconnect. Not a huge deal since the headphones work fine without the app, but it's a small annoyance. Hardware is a clear five stars."),
    (4, "Astrid Lindqvist",      False, _d("2025-11-05"),
     "Great product overall. The ANC and sound quality are both top-tier at this price. I'm deducting one star for the carry case — the zipper is already stiff after two months of use and I'm worried about its longevity. The headphones themselves feel very solid. Minor issue but the case is part of the premium you're paying for."),
    (4, "Samuel Boateng",        True,  _d("2025-12-18"),
     "Strong headphones. The ANC blocks out everything on my bus commute. Sound is crisp and the bass is controlled without being overwhelming. Four stars rather than five because after five months the ear cushion material has started to show subtle cracking at the folds. It's cosmetic so far but I'm watching it. The audio performance is unquestionably five-star."),
    (4, "Lily Anderson",         True,  _d("2026-01-25"),
     "These headphones are excellent for studio and focused work. The ANC is outstanding. Sound quality is detailed and accurate. My reason for four stars: the clamping force is too high for my head shape — I get a headache after about four hours. I've tried bending the headband slightly which helped a bit. I genuinely wish I could give this five stars because the audio performance is superb."),
    (4, "Nnamdi Okeke",          True,  _d("2026-02-08"),
     "Superb noise cancellation and impressive battery life. The sound quality is excellent for this tier. I'm leaving four stars rather than five because the ear pads started showing early wear after three months — the seams are slightly separating on the right cup. Not functionally impaired yet but I'd expect longer durability at this price point. TechSound should review their cushion material quality."),
    (4, "Sofia Reyes",           True,  _d("2026-03-04"),
     "Really excellent headphones. I use them for eight-hour workdays and the ANC and battery life make them perfect for this. My small complaint: the plastic headband adjustment mechanism makes a slight creaking sound when I move my head. It's very minor and doesn't affect function. The sound quality is exceptional and the ANC is among the best I've used. Recommended."),
    (4, "Tom Fletcher",          True,  _d("2026-04-11"),
     "Very good product. ANC and sound quality are both excellent. I'm at four stars because the ear cushion material — despite being described as premium leatherette — feels cheaper than expected and I've started noticing slight wear at the edges after four months. The core audio product is five-star quality. A better cushion material would make these truly exceptional."),

    # --- 3-star reviews (6) ---
    (3, "Kristin Larsen",        True,  _d("2025-08-31"),
     "The sound quality and ANC are both genuinely impressive — I can see why people rate these highly. But at this price point I expected better build quality. The headband creaks when adjusted, the ear cushion material feels cheaper than the marketing suggests, and the case zipper is already stiff. Also the clamping force gives me a headache after two to three hours. I'd rate the audio performance five stars and the physical product two stars — splitting the difference at three."),
    (3, "Patrick O'Sullivan",    True,  _d("2025-10-06"),
     "Mixed product. The noise cancellation is extraordinary — genuinely best-in-class for the price. The sound quality is also very good. But these things are expensive and the ear cushions started showing wear at three months. The headband could use more padding. And the clamping force is too strong for extended use — I get headaches. I feel like the engineering budget went into the audio and ANC technology and the physical ergonomics were an afterthought."),
    (3, "Monique Dupont",        True,  _d("2025-12-14"),
     "The audio quality is exceptional and I have no complaints about the ANC or battery. But I have to be honest about the physical product: the ear cushion material is deteriorating faster than I'd expect. After five months of daily use the leatherette is peeling at the edges. This is disappointing at this price point. The technology inside is first class; the materials outside need work. Three stars reflects my overall mixed experience."),
    (3, "Gareth Evans",          False, _d("2026-01-14"),
     "I wanted to love these. The ANC is excellent, battery life is genuinely extraordinary, and the sound quality is good. But the clamping force is too strong for my head and I get a headache within three hours. I've tried the stretch trick — bending the headband over a stack of books overnight — and it helped marginally. For people with average or smaller heads this probably isn't an issue. For me, a product with this much potential but an ergonomic flaw that prevents long use is a three-star experience."),
    (3, "Beatrix Wagner",        True,  _d("2026-02-03"),
     "Splitting my review into two halves. Audio product: five stars. The ANC is superb, sound is detailed and natural, battery lasts forever. Physical product: one or two stars. The ear cushions are deteriorating after four months. The headband produces a subtle creak. The case zipper is gummy. The price premium feels unjustified for the build quality even if the technology is excellent. Overall three stars, which I think is fair."),
    (3, "Olumide Adeyemi",       True,  _d("2026-04-05"),
     "The audio performance is excellent. ANC is exceptional. Battery life is real and extraordinary. But two physical issues prevent me recommending these without caveats. First, the clamping pressure gives me a headache after four hours. Second, after five months of use the leatherette ear pads are beginning to crack. At this price these issues matter. Three stars — the audio earns five, the physical product earns one, the average is three."),

    # --- 2-star reviews (5) ---
    (2, "Andrew Peterson",       True,  _d("2025-07-18"),
     "Returned after three weeks. The clamping force was simply too painful for extended use. I have a slightly larger than average head and these headphones gave me consistent headaches after two hours of wear. I tried the stretching technique, I tried adjusting the headband, I tried everything suggested in reviews and in the support chat. Nothing helped enough. The sound quality is excellent but a pair of headphones that causes pain is not usable. Disappointing."),
    (2, "Janet Oduya",           True,  _d("2025-09-27"),
     "I'm at two stars because of the ear cushion situation. After four months of moderate use — maybe two hours a day — the leatherette ear cushions are peeling. I don't sweat heavily, I store them properly in the case, I don't expose them to heat. They just peeled. This is a known issue according to comments I've seen elsewhere. The audio performance is five-star but peeling cushions on a premium product after four months is simply not acceptable."),
    (2, "Mark Johansson",        True,  _d("2025-11-20"),
     "The audio performance is phenomenal. The ANC is the best I've heard at any price. The sound quality is reference-grade. But the clamping force issue is real and it's not exaggerated. I have a normal-sized head and these give me a headache within three hours. I spent three months trying to adapt and adjust. I cannot use them for more than two to three hours without significant discomfort. Amazing technology, unusable ergonomics for me personally."),
    (2, "Claire Beaumont",       True,  _d("2026-01-03"),
     "Ear cushions started peeling at three months. This seems to be a pattern based on other reviews. The material looks cheap once it starts peeling and the exposed foam is unpleasant against the ear. I contacted support — they offered replacement cushions at a cost. A known defect should be covered under warranty. The audio quality is genuinely excellent but I can't recommend a product with this quality control issue at this price point."),
    (2, "Winston Hayward",       False, _d("2026-03-28"),
     "Two issues that together kill the product for me. First: clamping force too high — headache after two hours. Second: ear cushions started peeling at four months. Both issues are apparently common. At this price these are not acceptable. The ANC is incredible and the battery life is extraordinary but if you can't wear them comfortably and the cushions fall apart, none of that matters. Two stars because the technology is genuinely impressive."),

    # --- 1-star reviews (3) ---
    (1, "Naomi Blackwell",       True,  _d("2025-08-08"),
     "Returned. The ear cushions started peeling after six weeks of light use. Six weeks. The leatherette literally began separating from the foam. I use these at a desk — I don't work out in them, I don't expose them to moisture, I store them in the case when not in use. Six weeks is simply not an acceptable lifespan for ear cushions on a premium product. Support told me this wasn't covered under warranty as it was 'cosmetic wear'. Outrageous."),
    (1, "Christoph Bauer",       True,  _d("2025-11-01"),
     "Complete failure of quality control on the ear cushions. Both pads were peeling within two months of purchase. I've been through this before with cheaper headphones but not with a product at this price. The audio technology is outstanding — I've tried them on borrowed cushions from a friend's older model and the sound and ANC are both incredible. But the standard cushions are defective. Selling premium audio tech with budget cushion materials is a fundamental product failure. One star until this is addressed systemically."),
    (1, "Fatou Diallo",          True,  _d("2026-04-24"),
     "The clamping force physically injured me. I'm not exaggerating. After a four-hour session on a long flight I had genuine pain in my temples and jaw for 24 hours. I have a normal adult head size. I tried the stretching technique before the flight as precaution — it made minimal difference. The ANC is the best I've ever heard and the sound quality is exceptional but headphones that injure the wearer are not fit for purpose. Returning and filing a complaint."),
]

AUDIOMAX_REVIEWS_DF = pd.DataFrame(_AUDIOMAX_ROWS, columns=[
    "rating", "reviewer_name", "verified_purchase", "date", "body"
])
AUDIOMAX_REVIEWS_DF["title"] = [
    "Best ANC I've experienced at any price", "In a different league",
    "Changed my remote work life", "Best purchase for my ADHD",
    "Music producer approved", "Edges out the Sony XM5", "Best tested ANC at this tier",
    "Made commuting enjoyable", "Allows complete concentration", "A revelation",
    "Worth every penny at full price", "Perfect WFH headphones",
    "Genuinely excellent, struggled to find complaints", "Everything I wanted",
    "Excellent but ear cushions get warm", "Great but strong clamping force",
    "Superb but app bug lost my EQ settings", "Better than Bose but cushions wear",
    "Outstanding but headband pressure", "Excellent — app disconnects occasionally",
    "Top-tier but carry case zipper", "Great but cushion material cracking",
    "Four stars — clamping force issue", "Cushion wear after 3 months",
    "Excellent headphones, slight creak", "Great ANC, cushion starting to show wear",
    "Audio five stars, physical two stars", "Audio excellent, clamping painful",
    "Amazing technology, unusable ergonomics for me", "Ear cushions peeled at 4 months",
    "Clamping force gives me headaches", "Worth caveats",
    "Excellent audio, problematic ergonomics", "Five stars audio, one star physical",
    "Both issues together kill it for me", "Cushions peeling at 3 months",
    "Clamping force too painful — returned", "Ear cushion peeling issue",
    "Clamping force physically injured me", "Defective ear cushions — returning",
]

# ---------------------------------------------------------------------------
# PRE-COMPUTED FILTER STATS
# ---------------------------------------------------------------------------

TECHSOUND_FILTER_STATS = {
    "total_reviews_analyzed": 40,
    "trusted_count": 34,
    "flagged_count": 6,
    "fake_percentage": 15.0,
    "verified_purchase_rate": 87.5,
    "average_trust_score": 74.2,
}

AUDIOMAX_FILTER_STATS = {
    "total_reviews_analyzed": 40,
    "trusted_count": 35,
    "flagged_count": 5,
    "fake_percentage": 12.5,
    "verified_purchase_rate": 87.5,
    "average_trust_score": 72.8,
}

# ---------------------------------------------------------------------------
# PRE-COMPUTED VOICE OF CUSTOMER ANALYSIS — TechSound Pro
# ---------------------------------------------------------------------------

TECHSOUND_ANALYSIS = {
    "executive_summary": (
        "TechSound Pro Wireless Earbuds deliver genuinely strong audio performance and effective ANC "
        "that earns loyal five-star reviews, but three recurring hardware themes — battery imbalance "
        "between earbuds, Bluetooth instability in crowded environments, and overstated ANC battery life "
        "— are suppressing the rating from a potential 4.5+ to 4.1. These are fixable engineering and "
        "marketing issues. The product has a passionate customer base and strong word-of-mouth; resolving "
        "the right earbud battery drain alone could materially improve the rating."
    ),
    "overall_health_score": 72,
    "complaint_themes": [
        {
            "theme": "Right Earbud Battery Drains Faster Than Left",
            "frequency_pct": 27.5,
            "emotional_intensity": "high",
            "example_quotes": [
                "The right earbud consistently dies before the left — I track it obsessively and the right uses about 20% more power.",
                "After four months of daily use the right earbud started dying noticeably faster than the left.",
                "Right is dead by the time the left is at 65% — it's clearly a battery defect.",
            ],
            "improvement_recommendation": (
                "Investigate firmware-level power asymmetry in the right earbud. Implement automatic "
                "load-balancing in the companion app to equalize draw from both buds. Proactively "
                "replace affected units for customers who report this via support — the goodwill far "
                "outweighs the cost of a replacement."
            ),
            "estimated_rating_impact": "+0.4 stars if fixed",
        },
        {
            "theme": "Bluetooth Drops in Crowded/High-Interference Environments",
            "frequency_pct": 22.5,
            "emotional_intensity": "high",
            "example_quotes": [
                "They drop connection three to five times per hour on my morning train.",
                "Bluetooth stability is just not reliable enough for daily use.",
                "Terrible in any crowded environment — shopping mall, gym, open-plan office.",
            ],
            "improvement_recommendation": (
                "Prioritize antenna design review for the next hardware revision. In the interim, "
                "release a firmware update that improves frequency-hopping aggressiveness in "
                "high-congestion environments. Update marketing to honestly set expectations about "
                "crowded Bluetooth environments — this will reduce negative reviews from users "
                "who expected flawless connectivity everywhere."
            ),
            "estimated_rating_impact": "+0.3 stars if fixed",
        },
        {
            "theme": "Advertised 48H Battery Life Misleading with ANC On",
            "frequency_pct": 20.0,
            "emotional_intensity": "medium",
            "example_quotes": [
                "With ANC on I get about 4.5 hours per charge on the earbuds, not the claimed 6-7 hours.",
                "Total is around 20 hours with ANC on, not 48. I feel misled.",
                "Battery life is decent but nowhere near 48 hours when ANC is on.",
            ],
            "improvement_recommendation": (
                "Immediately update listing copy and packaging to clearly distinguish battery life "
                "with ANC off (48H) vs ANC on (approximately 20-22H total). Use a table format so "
                "buyers can see exactly what to expect. The current spec is technically accurate "
                "but feels deceptive to customers. Transparency here will reduce 1-2 star reviews "
                "from disappointed buyers."
            ),
            "estimated_rating_impact": "+0.2 stars if fixed",
        },
        {
            "theme": "Ear Tip Sizing Gap (No Medium-Large Option)",
            "frequency_pct": 12.5,
            "emotional_intensity": "medium",
            "example_quotes": [
                "The medium is too small and the large makes my ears sore after 30 minutes.",
                "My partner has large ears and found the tips don't come in a size that seals properly.",
                "If TechSound added an XL tip option this would be five stars immediately.",
            ],
            "improvement_recommendation": (
                "Add an XL ear tip to the accessory lineup and include it in the box. This is a "
                "low-cost hardware addition that directly addresses a documented fit gap. Also add "
                "a sizing guide with ear tip selection instructions to the listing images — many "
                "customers don't know how to identify the right size."
            ),
            "estimated_rating_impact": "+0.15 stars if fixed",
        },
        {
            "theme": "Companion App Instability (iOS and Android)",
            "frequency_pct": 10.0,
            "emotional_intensity": "low",
            "example_quotes": [
                "The app crashes when I try to update firmware. It's been three months and no updates.",
                "The app crashes occasionally on my Android phone and I lost my EQ settings twice.",
                "The app's battery percentage display sometimes shows incorrect readings.",
            ],
            "improvement_recommendation": (
                "Prioritize a stability release for the companion app targeting iOS 17+ and Android 13+. "
                "Add local EQ setting backup so users don't lose custom configurations on crash. "
                "Set up automated crash reporting to catch regressions faster. A stable app converts "
                "4-star reviews into 5-star reviews."
            ),
            "estimated_rating_impact": "+0.1 stars if fixed",
        },
    ],
    "praise_themes": [
        {
            "theme": "Sound Quality Exceeds Price Expectation",
            "frequency_pct": 77.5,
            "example_quotes": [
                "Sound quality punches well above the price.",
                "I compared these directly against earbuds that cost twice as much and honestly preferred the TechSound mids and highs.",
                "I'm an audio engineer so I'm picky about sound and even I can't complain at this price.",
            ],
            "marketing_angle": (
                "Lead with social proof: 'Customers say TechSound Pro out-sounds earbuds costing 2× more.' "
                "Use the audio engineer quote as a featured review in A+ content. Position value explicitly: "
                "'Premium sound, accessible price' as a headline claim."
            ),
        },
        {
            "theme": "ANC Delivers Real-World Focus and Quiet",
            "frequency_pct": 65.0,
            "example_quotes": [
                "The ANC turns a loud, rattling carriage into something approaching silence.",
                "The ANC blocks out my open-plan office completely.",
                "ANC helps me decompress during break time — I'm a nurse doing 12-hour shifts.",
            ],
            "marketing_angle": (
                "Target high-noise use cases specifically: open-plan offices, public transit, WFH with "
                "background noise. Use occupation-specific testimonials (nurse, developer, commuter) to "
                "show breadth of real-world scenarios where the ANC genuinely works."
            ),
        },
        {
            "theme": "Comfort Over Extended Sessions",
            "frequency_pct": 52.5,
            "example_quotes": [
                "I listen to music eight hours a day. Comfort over extended periods was my top priority and these deliver.",
                "I wore them for a six-hour flight and my ears never ached.",
                "I'm a nurse and I wear these during 12-hour shifts.",
            ],
            "marketing_angle": (
                "Own the 'all-day wear' positioning. Create a specific use-case message for remote workers "
                "and commuters: 'Built for eight-hour days.' The nurse and developer testimonials are "
                "compelling social proof for durability and comfort."
            ),
        },
        {
            "theme": "Battery Life Impresses in Practice",
            "frequency_pct": 45.0,
            "example_quotes": [
                "Battery lasted four days of commuting before I had to charge.",
                "I charge Sunday night and it gets me through to Thursday with about 2-3 hours of use per day.",
                "Best commuter purchase I've made.",
            ],
            "marketing_angle": (
                "Translate the 48H spec into real-world terms: 'Charge Sunday. Use all week.' Specific, "
                "relatable framing converts better than a raw hour count. Feature this in the listing "
                "title or first bullet."
            ),
        },
        {
            "theme": "Strong Word-of-Mouth and Repeat Purchases",
            "frequency_pct": 25.0,
            "example_quotes": [
                "Ordered a second pair as a gift.",
                "I've recommended these to three colleagues who've all bought them.",
                "I've been using TechSound earbuds for three generations — they keep getting better.",
            ],
            "marketing_angle": (
                "Activate this organic advocacy explicitly. Add a 'Give the gift of quiet' gift bundle "
                "option on the listing. Run a referral mechanism. Customers who gift-purchase are "
                "high-value evangelists — treat them as such."
            ),
        },
    ],
    "listing_bullets": [
        "SOUND QUALITY ENGINEERS APPROVE — Detailed highs, warm mids, and controlled bass that customers say rivals earbuds costing 2× more. Tuned for music, podcasts, and crystal-clear calls.",
        "ANC THAT ACTUALLY WORKS — Advanced noise cancellation blocks open-plan offices, train carriages, and busy cafes so you can focus or decompress wherever you are.",
        "WEAR THEM ALL DAY — Lightweight ergonomic design with three tip sizes for a secure, fatigue-free fit during 6-hour flights, 8-hour workdays, and 12-hour shifts.",
        "A WEEK ON ONE CHARGE — Up to 48H total battery (earbuds + case) with ANC off; approx. 20H with ANC on. Charge Sunday, use all week with typical daily commuter use.",
        "IPX5 WATERPROOF — Built for real life. Survived spin class, rain, and construction sites. Comes with a one-year warranty and responsive support.",
    ],
    "listing_title_suggestion": (
        "TechSound Pro Wireless Earbuds — Active Noise Cancelling, All-Day Comfort, "
        "48H Battery, IPX5 Waterproof | Earbuds That Sound Like They Cost Twice As Much"
    ),
    "buyer_personas": [
        {
            "persona_name": "The Daily Commuter",
            "percentage": 35,
            "description": "Takes public transit 45-60 mins each way. Needs reliable Bluetooth, good ANC, and a battery that survives the work week without daily charging.",
            "what_they_love": "ANC on the train, battery lasting all week, instant pairing with their phone.",
            "what_frustrates_them": "Bluetooth drops on the train, right earbud dying mid-commute.",
            "marketing_message": "Your commute, cancelled. TechSound Pro's ANC silences the carriage so you arrive focused, not frazzled.",
        },
        {
            "persona_name": "The Focused Remote Worker",
            "percentage": 30,
            "description": "Works from home or a coworking space 4-5 days/week. Background noise is a constant focus killer. Needs ANC + comfort for 6-8 hour sessions.",
            "what_they_love": "ANC blocking family, coworkers, and ambient noise. All-day comfort. Good mic for video calls.",
            "what_frustrates_them": "App bugs, right earbud dying in the middle of a long work session.",
            "marketing_message": "Deep work mode, activated. TechSound Pro blocks out the world so you can do your best work.",
        },
        {
            "persona_name": "The Value-Maximizing Audiophile",
            "percentage": 25,
            "description": "Cares deeply about sound quality but can't justify spending $250+ on earbuds. Reads comparison reviews obsessively before buying.",
            "what_they_love": "Sound quality that rivals premium brands, balanced tuning, EQ app.",
            "what_frustrates_them": "App instability losing EQ settings, advertised specs that don't match reality.",
            "marketing_message": "You know what good audio sounds like. So do we. TechSound Pro: the earbuds your ears deserve at a price your wallet accepts.",
        },
        {
            "persona_name": "The Active Lifestyle User",
            "percentage": 10,
            "description": "Goes to the gym 3-4x/week and runs outdoors. Needs secure fit, IPX protection, and stable Bluetooth.",
            "what_they_love": "IPX5 waterproofing, secure fit during workouts, strong sound for motivation.",
            "what_frustrates_them": "Bluetooth drops at the gym, connectivity issues in high-interference environments.",
            "marketing_message": "IPX5 waterproof, gym-tested, weather-ready. TechSound Pro keeps up with your workout.",
        },
    ],
    "risk_alerts": [
        {
            "alert_type": "Hardware Defect — Right Earbud Battery Asymmetry",
            "severity": "high",
            "description": "27.5% of reviews mention the right earbud dying significantly faster than the left. Multiple reviewers describe tracking the asymmetry over time. This appears to be a systematic issue, not individual unit failures.",
            "recommended_action": "Escalate to hardware QA immediately. Issue a firmware patch for power load balancing as a short-term fix. For customers who contact support with this issue, prioritize proactive replacement. This single issue is responsible for most 1-2 star reviews.",
        },
        {
            "alert_type": "Misleading Battery Spec — ANC On vs Off",
            "severity": "high",
            "description": "Multiple reviewers feel deceived by the 48H battery claim. With ANC active, actual total battery is approximately 20-22H — less than half the headline figure. This gap between expectation and reality is generating negative reviews from otherwise satisfied customers.",
            "recommended_action": "Update listing immediately: add a spec table showing battery with ANC on vs off. This is both a trust issue and potentially an FTC/ASA concern if the spec is prominently featured without proper qualification.",
        },
        {
            "alert_type": "Bluetooth Reliability — Crowded Environments",
            "severity": "medium",
            "description": "22.5% of reviewers report Bluetooth drops specifically in high-interference environments (trains, gyms, open offices). This is a use case that represents TechSound's core customer — the fix is critical.",
            "recommended_action": "Investigate Bluetooth chipset firmware. Release an update targeting coexistence performance in 2.4GHz-congested environments. Add honest connectivity guidance to listing FAQs.",
        },
        {
            "alert_type": "App Quality — iOS and Android Instability",
            "severity": "low",
            "description": "The companion app crashes on both iOS 17+ and Android 13, causing loss of saved EQ settings. App issues are suppressing 4→5 star conversions among technically engaged users.",
            "recommended_action": "Ship a stability-focused app update. Implement local + cloud EQ backup. Set up crash analytics to catch future regressions before they reach customers.",
        },
    ],
    "keyword_opportunities": [
        "wireless earbuds for commuting",
        "noise cancelling earbuds under $100",
        "earbuds for open plan office",
        "waterproof earbuds for gym",
        "earbuds with long battery life",
        "wireless earbuds for remote work",
        "best earbuds for focus",
        "earbuds that stay in during running",
        "noise cancelling earbuds for travel",
    ],
    "pricing_sentiment": (
        "Price is not a driver of complaints. Reviewers consistently describe TechSound Pro as "
        "exceptional value — 'punches above its price', 'rivals earbuds at twice the cost', and "
        "'best investment I've made' are representative phrases. The product over-delivers on "
        "perceived value, which means there may be room to test a modest price increase without "
        "losing conversion. Negative reviews are driven by hardware and software issues, not price."
    ),
    "seasonal_patterns": (
        "Review volume is consistent throughout the year with slight upticks in June-July and "
        "December-January, suggesting gift purchases and summer purchases. The year-round "
        "distribution reflects a product bought primarily for daily use rather than as a "
        "seasonal gift item. Marketing should run consistently with peak spend in Q4 "
        "(gift season) and late summer (back-to-school/back-to-office)."
    ),
}

# ---------------------------------------------------------------------------
# PRE-COMPUTED VOICE OF CUSTOMER ANALYSIS — AudioMax
# ---------------------------------------------------------------------------

AUDIOMAX_ANALYSIS = {
    "executive_summary": (
        "AudioMax Pro Headphones deliver industry-leading ANC and exceptional battery life that generates "
        "genuine customer evangelism, but a persistent and well-documented physical product quality issue — "
        "ear cushion deterioration and excessive clamping force — is driving a significant portion of "
        "1-3 star reviews and creating a 'great tech, bad ergonomics' reputation online. These are "
        "materials and tooling decisions that can be corrected; if fixed, the product has the audio "
        "credentials to command a higher price and a higher rating."
    ),
    "overall_health_score": 68,
    "complaint_themes": [
        {
            "theme": "Ear Cushion Leatherette Deteriorates Within Months",
            "frequency_pct": 35.0,
            "emotional_intensity": "critical",
            "example_quotes": [
                "The ear cushions started peeling after six weeks of light use. Six weeks.",
                "After four months of moderate use the leatherette is peeling at the edges.",
                "A known defect should be covered under warranty — a premium product shouldn't do this.",
            ],
            "improvement_recommendation": (
                "Switch immediately to a higher-grade protein leather or premium PU that has been "
                "validated for 18+ months of daily use. Include free replacement cushions in the "
                "box and offer a one-year cushion replacement guarantee explicitly in the listing. "
                "Proactively replace cushions for all existing customers who report peeling under "
                "warranty — the PR cost of denying warranty claims for a systematic defect is severe."
            ),
            "estimated_rating_impact": "+0.5 stars if fixed",
        },
        {
            "theme": "Clamping Force Causes Headaches During Extended Use",
            "frequency_pct": 32.5,
            "emotional_intensity": "high",
            "example_quotes": [
                "After a four-hour session I had genuine pain in my temples and jaw for 24 hours.",
                "I get a headache within three hours — I've tried everything.",
                "The engineering budget went into the audio and ANC; ergonomics were an afterthought.",
            ],
            "improvement_recommendation": (
                "Reduce the default clamp tension by 15-20% in the next hardware revision — this is "
                "a spring tension change in the headband and can be validated quickly. In the interim, "
                "add a break-in guide to packaging and the app that walks users through gentle headband "
                "stretching. Also add clamping force disclosure to the listing for buyers who know "
                "they have larger or more pressure-sensitive heads."
            ),
            "estimated_rating_impact": "+0.4 stars if fixed",
        },
        {
            "theme": "Headband Padding Causes Crown Pressure on Long Sessions",
            "frequency_pct": 17.5,
            "emotional_intensity": "medium",
            "example_quotes": [
                "After about three hours of continuous use I feel pressure at the top of my head.",
                "I've started putting a thin pad underneath which helps but it shouldn't be necessary.",
                "The headband could use more padding — the audio earns five stars, the physical product earns one.",
            ],
            "improvement_recommendation": (
                "Increase headband padding thickness by 4-5mm and use a breathable memory foam material. "
                "This is a low-cost change that directly unlocks the 4→5 hour use case that many "
                "customers are trying to achieve. Alternatively, offer a headband cushion accessory "
                "as a free add-on in the box to address existing inventory."
            ),
            "estimated_rating_impact": "+0.2 stars if fixed",
        },
        {
            "theme": "Carry Case Zipper Durability",
            "frequency_pct": 10.0,
            "emotional_intensity": "low",
            "example_quotes": [
                "The zipper is already stiff after two months of use.",
                "The case zipper is gummy — at this price these issues matter.",
            ],
            "improvement_recommendation": (
                "Upgrade to a YKK or equivalent rated zipper. The carry case is part of the premium "
                "product experience and a stiff zipper damages the unboxing and daily-use impression. "
                "This is a negligible BOM cost change."
            ),
            "estimated_rating_impact": "+0.05 stars if fixed",
        },
    ],
    "praise_themes": [
        {
            "theme": "Industry-Leading ANC at This Price Point",
            "frequency_pct": 87.5,
            "example_quotes": [
                "Best noise cancellation I've experienced outside of a recording studio.",
                "The ANC on these is legitimately the best I've tried outside of Bose QC45s.",
                "On a transatlantic flight the engine roar just disappeared.",
            ],
            "marketing_angle": (
                "Lead with the ANC credential unambiguously: 'Bose-level ANC at half the price — "
                "customers say so.' Use the flight, office, and ADHD testimonials to show the breadth "
                "of real-world impact. The ANC is a genuine competitive differentiator — own it loudly."
            ),
        },
        {
            "theme": "Extraordinary Battery Life (60H Verified by Customers)",
            "frequency_pct": 72.5,
            "example_quotes": [
                "I went almost two weeks on a single charge with moderate daily use.",
                "I charge once a week — the battery life is genuinely extraordinary.",
                "Battery life is extraordinary — the 60-hour claim is real.",
            ],
            "marketing_angle": (
                "Translate 60H into a lifestyle statement: 'Charge once a week.' This is more "
                "compelling than a raw number and it's verified by customer reviews. Specifically "
                "target users who are frustrated by charging other devices constantly."
            ),
        },
        {
            "theme": "Reference-Grade Sound Quality",
            "frequency_pct": 80.0,
            "example_quotes": [
                "The sound accuracy is impressive — not hyped, not flat, just natural and revealing.",
                "I'm a music producer and I use these for casual listening. The sound accuracy is impressive.",
                "Sound quality is detailed and natural — very good for this price tier.",
            ],
            "marketing_angle": (
                "Target audiophile-leaning buyers with precision: 'Hi-Res Audio certified. "
                "Music producer approved.' The natural, non-hyped tuning is a differentiator "
                "from competitors that oversell bass. Own the 'accurate sound' positioning."
            ),
        },
        {
            "theme": "Productivity and Focus Transformation",
            "frequency_pct": 42.5,
            "example_quotes": [
                "These headphones have genuinely changed my productivity.",
                "Bought these to help with my ADHD — blocking background noise is crucial for focus. These are the best thing I've ever bought for that purpose.",
                "I can think clearly in a loud coworking space.",
            ],
            "marketing_angle": (
                "The ADHD testimonial is powerful and underused. Create a 'Focus Mode' marketing "
                "angle that speaks directly to remote workers, students, and people with attention "
                "challenges. This is an underserved segment with strong purchase intent."
            ),
        },
    ],
    "listing_bullets": [
        "BOSE-LEVEL ANC AT HALF THE PRICE — Customers compare our noise cancellation directly to the Bose QC45. On planes, in offices, and at home — the outside world disappears on command.",
        "CHARGE ONCE A WEEK — Genuine 60-hour battery life verified by customers. Two weeks on a single charge with moderate use. The last headphones you'll need to think about charging.",
        "MUSIC PRODUCER APPROVED SOUND — Hi-Res Audio certified. Natural, detailed, non-fatiguing tuning for music, podcasts, and calls. What good audio is supposed to sound like.",
        "BUILT FOR FOCUS SESSIONS — Memory foam ear cushions, gentle headband pressure, and transformative ANC. Customers with ADHD call these 'the best thing I've ever bought for focus.'",
        "PREMIUM BUILD, PREMIUM SUPPORT — Metal reinforced headband, fold-flat carry case, and a warranty that covers you. Includes cushion replacement guarantee for the first year.",
    ],
    "listing_title_suggestion": (
        "AudioMax Pro Noise Cancelling Headphones — Bose-Level ANC, 60H Battery, "
        "Hi-Res Audio | Over-Ear Headphones for Deep Focus, Travel, and All-Day Work"
    ),
    "buyer_personas": [
        {
            "persona_name": "The Deep Focus Professional",
            "percentage": 40,
            "description": "Remote worker, developer, writer, or analyst. Background noise destroys their productivity. Spends 6-8 hours per day at a desk. Will pay for real ANC.",
            "what_they_love": "ANC that truly eliminates office/home noise, battery that lasts a work week, natural sound for long listening sessions.",
            "what_frustrates_them": "Clamping force headaches after 3-4 hours, cushion material wearing out.",
            "marketing_message": "Your most productive hours start when the world goes quiet. AudioMax Pro gives you that silence, all day.",
        },
        {
            "persona_name": "The Frequent Traveller",
            "percentage": 28,
            "description": "Flies monthly or more. Knows exactly what good ANC means for long-haul flights. Battery life is a top-five purchase criterion.",
            "what_they_love": "ANC eliminating engine noise on flights, extraordinary battery that survives long trips without a charge.",
            "what_frustrates_them": "Cushion deterioration from travel wear, carry case durability.",
            "marketing_message": "From boarding to landing, engine off. AudioMax Pro's ANC is the reason frequent fliers replace their Bose.",
        },
        {
            "persona_name": "The Audiophile on a Budget",
            "percentage": 22,
            "description": "Knows what accurate sound means. Compares specs obsessively. Would own Sonys or Boses if price weren't a constraint.",
            "what_they_love": "Hi-Res Audio certification, natural non-hyped sound signature, music producer endorsements.",
            "what_frustrates_them": "Cushion quality feeling inconsistent with the audio premium, app bugs affecting EQ.",
            "marketing_message": "Reference-grade sound shouldn't cost reference-grade money. Hi-Res certified. Music producer approved.",
        },
        {
            "persona_name": "The ADHD / Focus-Challenged User",
            "percentage": 10,
            "description": "Has attention challenges in noisy environments. Researches noise cancellation deeply before buying. Extremely loyal once they find something that works.",
            "what_they_love": "ANC so effective they forget external noise exists. Life-changing productivity impact.",
            "what_frustrates_them": "Clamping pressure over long sessions, any reason to take the headphones off.",
            "marketing_message": "The world's noise, cancelled. Customers with ADHD call AudioMax Pro the best focus tool they've ever bought.",
        },
    ],
    "risk_alerts": [
        {
            "alert_type": "Systematic Product Defect — Ear Cushion Delamination",
            "severity": "critical",
            "description": "35% of reviews mention ear cushion peeling, with failure timelines as short as 6 weeks. Multiple reviewers describe this as a known/systemic issue. Support refusing warranty coverage for 'cosmetic wear' is generating additional negative sentiment.",
            "recommended_action": "Immediate: extend warranty to cover cushion replacement for the first 12 months, no questions asked. Medium-term: source upgraded cushion material and ship replacement kits to registered owners. Long-term: redesign the cushion with validated 24-month durability before next production run.",
        },
        {
            "alert_type": "Ergonomic Design Risk — Clamping Force Injury",
            "severity": "high",
            "description": "One reviewer reports genuine physical pain (temple and jaw pain lasting 24 hours) from clamping force on a long flight. 32.5% of reviews mention headaches or discomfort from clamping. This is both a customer experience risk and a product liability consideration.",
            "recommended_action": "Reduce spring tension in the next production run. Add explicit clamping force break-in instructions to packaging immediately. Consider a proactive 'soft-start' firmware that reminds new owners to break in the headband before extended sessions.",
        },
        {
            "alert_type": "Brand Reputation — 'Great Tech, Bad Build' Narrative",
            "severity": "high",
            "description": "A clear narrative is forming in reviews: 'five-star audio, one-star physical product.' This narrative — when it takes hold — is very hard to reverse and actively supresses conversion from browsers who read reviews before buying.",
            "recommended_action": "The cushion and clamping fixes are the only solution. Additionally, engage proactively with negative reviews via public seller response, acknowledging the issue and offering a remedy. Visible seller responsiveness can offset negative sentiment while the hardware is being addressed.",
        },
    ],
    "keyword_opportunities": [
        "noise cancelling headphones for work from home",
        "over ear headphones long battery life",
        "best ANC headphones under $150",
        "headphones for ADHD focus",
        "travel headphones noise cancelling",
        "hi-res audio headphones",
        "headphones for open plan office",
        "noise cancelling headphones for studying",
        "over ear headphones all day comfort",
    ],
    "pricing_sentiment": (
        "Price is a point of tension in negative reviews — not because the product is expensive, "
        "but because the physical build quality (cushions, headband) feels inconsistent with the "
        "premium price positioning. Reviewers who are happy describe it as exceptional value; "
        "reviewers who experienced cushion deterioration feel deceived by the price-to-quality ratio. "
        "The risk is that a 'premium price, budget materials' reputation forms. Resolving the cushion "
        "issue would neutralize this entirely."
    ),
    "seasonal_patterns": (
        "Review volume spikes in July-August (travel season) and November-December (gift season), "
        "consistent with a product that markets strongly to travellers and is bought as a gift. "
        "The travel buyer persona is well-represented and should inform seasonal campaign timing. "
        "Consider targeted campaigns around summer travel planning (May-June) and Black Friday."
    ),
}

# ---------------------------------------------------------------------------
# PRE-COMPUTED COMPETITOR GAP ANALYSIS
# ---------------------------------------------------------------------------

GAP_ANALYSIS = {
    "my_advantages": [
        {
            "advantage": "No documented hardware quality failures — earbuds last years, not months",
            "evidence": "AudioMax competitor reviews: 'ear cushions started peeling after six weeks of light use' and 'this is a known/systemic issue'. TechSound Pro users report 'lasted me five years' and 'still going strong after multiple years'.",
            "marketing_angle": "Position TechSound Pro explicitly as built to last: 'No peeling. No cracking. Customers report 5+ years of daily use.' Run comparison copy that targets AudioMax's known cushion defect without naming the competitor.",
        },
        {
            "advantage": "Secure, pain-free fit for extended wear",
            "evidence": "AudioMax reviews: 'clamping force physically injured me — genuine pain in my temples and jaw for 24 hours', 'get a headache within three hours'. TechSound Pro reviews: 'wore them for a six-hour flight and my ears never ached', 'comfortable even after wearing them for several hours'.",
            "marketing_angle": "Lead with comfort duration in listing bullets: 'Wear-tested for 6-hour flights, 8-hour workdays, 12-hour shifts — zero discomfort.' This directly hits AudioMax's biggest vulnerability.",
        },
        {
            "advantage": "True portability — earbuds vs over-ear headphones",
            "evidence": "AudioMax carry case receives consistent criticism: 'zipper already stiff after two months', 'I'm worried about its longevity'. TechSound Pro's compact charging case is praised for pocketability and daily portability.",
            "marketing_angle": "Target mobile professionals and gym-goers who need earbuds that disappear into a pocket or gym bag. 'Pocketable. Waterproof. Always with you.' — a positioning AudioMax over-ear headphones cannot match.",
        },
        {
            "advantage": "IPX5 waterproofing for active use",
            "evidence": "AudioMax Pro has no waterproofing rating and is not marketed for active use. TechSound Pro reviewers confirm: 'survived spin class, sweat, and being dropped on a tile floor', 'IPX5 rating seems legit — jogging in light rain and they stayed in place'.",
            "marketing_angle": "Own the active lifestyle segment explicitly. Create gym/run-specific ads that highlight IPX5. AudioMax cannot credibly compete in this segment.",
        },
    ],
    "my_vulnerabilities": [
        {
            "vulnerability": "ANC is good but not AudioMax-level — high-frequency environments still bleed through",
            "evidence": "TechSound Pro reviews: 'connectivity issues in the gym — lots of competing signals', 'Bluetooth drops make it unusable for commuting'. AudioMax reviews: 'best noise cancellation I've experienced outside of a recording studio', 'engine roar just disappeared on a transatlantic flight'.",
            "fix_recommendation": "Invest in the next ANC hardware generation. In the interim, avoid head-to-head ANC comparisons in marketing against premium over-ear headphones. Instead, compete on value, fit, and portability where TechSound Pro wins.",
        },
        {
            "vulnerability": "Battery life (48H total) significantly lower than competitor (60H in earbuds use)",
            "evidence": "TechSound Pro reviews note the actual ANC-on battery is closer to 20H total. AudioMax reviewers say '60-hour claim is real — I charge once a week'. This is a measurable gap for heavy users.",
            "fix_recommendation": "Address the advertised spec discrepancy immediately (it damages trust). For the next hardware version, target 28-30H ANC-on as a competitive threshold. In the interim, position TechSound Pro for the daily commuter use case (4-6 hours/day) where the current battery is more than sufficient.",
        },
        {
            "vulnerability": "Right earbud battery asymmetry — systematic hardware defect affecting trust",
            "evidence": "27.5% of TechSound Pro reviews mention the right earbud dying faster than the left. No comparable hardware defect appears in AudioMax reviews. This creates a reliability perception gap.",
            "fix_recommendation": "This is the single highest-priority engineering fix in the entire product lineup. Until resolved, it will remain the most common negative theme and the primary driver of 1-2 star reviews.",
        },
        {
            "vulnerability": "Bluetooth reliability in crowded environments",
            "evidence": "TechSound Pro: 'terrible in any crowded environment — shopping mall, gym, office'. AudioMax is an over-ear Bluetooth headphone with no documented connectivity issues in the same contexts.",
            "fix_recommendation": "Prioritize antenna and firmware improvements for next hardware revision. This vulnerability directly affects TechSound Pro's core use case (commuting, busy environments).",
        },
    ],
    "market_opportunity": (
        "TechSound Pro and AudioMax Pro serve adjacent but distinct use cases: TechSound Pro is the "
        "better choice for active users, commuters who need portability and waterproofing, and anyone "
        "who needs earbuds rather than over-ear headphones. AudioMax dominates the deep-focus, "
        "travel, and audiophile segment where users will tolerate the ergonomic issues for the superior "
        "ANC and battery. The strategic play for TechSound Pro is not to compete on ANC raw power, but "
        "to own the 'all-day active life' positioning that AudioMax physically cannot occupy. Fix the "
        "right earbud battery defect and Bluetooth stability, and TechSound Pro becomes a clear #1 "
        "recommendation for the commuter and active professional segments."
    ),
    "positioning_statement": (
        "TechSound Pro: the wireless earbuds for people who actually move. Waterproof, pocketable, "
        "and comfortable for a 12-hour shift — while the competition gives you a headache and "
        "falling-apart cushions after three months."
    ),
    "head_to_head_scores": {
        "quality_perception":  {"mine": 7, "competitor": 6},
        "value_for_money":     {"mine": 8, "competitor": 6},
        "customer_service":    {"mine": 6, "competitor": 5},
        "shipping_packaging":  {"mine": 7, "competitor": 7},
        "ease_of_use":         {"mine": 8, "competitor": 7},
    },
}

# ---------------------------------------------------------------------------
# PRE-COMPUTED SENTIMENT TRENDS
# ---------------------------------------------------------------------------

TECHSOUND_TRENDS = {
    "monthly_data": [
        {"month": "2025-06", "review_count": 3, "average_rating": 4.67, "verified_purchase_rate": 66.7, "complaint_rate": 0.0,  "praise_rate": 100.0},
        {"month": "2025-07", "review_count": 4, "average_rating": 4.25, "verified_purchase_rate": 75.0, "complaint_rate": 0.0,  "praise_rate": 75.0},
        {"month": "2025-08", "review_count": 4, "average_rating": 3.75, "verified_purchase_rate": 75.0, "complaint_rate": 25.0, "praise_rate": 50.0},
        {"month": "2025-09", "review_count": 4, "average_rating": 4.25, "verified_purchase_rate": 100.0,"complaint_rate": 0.0,  "praise_rate": 75.0},
        {"month": "2025-10", "review_count": 4, "average_rating": 3.75, "verified_purchase_rate": 100.0,"complaint_rate": 25.0, "praise_rate": 50.0},
        {"month": "2025-11", "review_count": 4, "average_rating": 4.25, "verified_purchase_rate": 75.0, "complaint_rate": 0.0,  "praise_rate": 75.0},
        {"month": "2025-12", "review_count": 4, "average_rating": 3.75, "verified_purchase_rate": 100.0,"complaint_rate": 25.0, "praise_rate": 50.0},
        {"month": "2026-01", "review_count": 3, "average_rating": 3.67, "verified_purchase_rate": 66.7, "complaint_rate": 33.3, "praise_rate": 33.3},
        {"month": "2026-02", "review_count": 3, "average_rating": 3.67, "verified_purchase_rate": 66.7, "complaint_rate": 33.3, "praise_rate": 33.3},
        {"month": "2026-03", "review_count": 3, "average_rating": 3.67, "verified_purchase_rate": 100.0,"complaint_rate": 33.3, "praise_rate": 33.3},
        {"month": "2026-04", "review_count": 4, "average_rating": 3.75, "verified_purchase_rate": 100.0,"complaint_rate": 25.0, "praise_rate": 50.0},
        {"month": "2026-05", "review_count": 0, "average_rating": None,  "verified_purchase_rate": None,  "complaint_rate": 0.0,  "praise_rate": 0.0},
    ],
    "trend_direction": "declining",
    "trend_magnitude": -8.7,
    "spike_months": ["2026-01", "2026-02", "2026-03"],
    "insight": (
        "Sentiment is declining — recent average rating is 8.7% lower than the prior period. "
        "Complaint spikes in Q1 2026 (Jan–Mar) correlate with the right earbud battery issue "
        "appearing in reviews, suggesting a hardware batch problem that emerged around that time."
    ),
}

TECHSOUND_RATING_DIST = {
    "1": {"count": 2,  "percentage": 5.0},
    "2": {"count": 3,  "percentage": 7.5},
    "3": {"count": 5,  "percentage": 12.5},
    "4": {"count": 14, "percentage": 35.0},
    "5": {"count": 16, "percentage": 40.0},
}

AUDIOMAX_TRENDS = {
    "monthly_data": [
        {"month": "2025-06", "review_count": 3, "average_rating": 4.67, "verified_purchase_rate": 100.0,"complaint_rate": 0.0,  "praise_rate": 100.0},
        {"month": "2025-07", "review_count": 4, "average_rating": 4.00, "verified_purchase_rate": 75.0, "complaint_rate": 25.0, "praise_rate": 50.0},
        {"month": "2025-08", "review_count": 4, "average_rating": 3.50, "verified_purchase_rate": 100.0,"complaint_rate": 25.0, "praise_rate": 50.0},
        {"month": "2025-09", "review_count": 4, "average_rating": 3.75, "verified_purchase_rate": 75.0, "complaint_rate": 25.0, "praise_rate": 50.0},
        {"month": "2025-10", "review_count": 4, "average_rating": 3.50, "verified_purchase_rate": 75.0, "complaint_rate": 50.0, "praise_rate": 50.0},
        {"month": "2025-11", "review_count": 4, "average_rating": 3.75, "verified_purchase_rate": 75.0, "complaint_rate": 25.0, "praise_rate": 50.0},
        {"month": "2025-12", "review_count": 4, "average_rating": 4.25, "verified_purchase_rate": 75.0, "complaint_rate": 0.0,  "praise_rate": 75.0},
        {"month": "2026-01", "review_count": 3, "average_rating": 3.33, "verified_purchase_rate": 66.7, "complaint_rate": 33.3, "praise_rate": 33.3},
        {"month": "2026-02", "review_count": 3, "average_rating": 4.00, "verified_purchase_rate": 100.0,"complaint_rate": 0.0,  "praise_rate": 66.7},
        {"month": "2026-03", "review_count": 3, "average_rating": 3.67, "verified_purchase_rate": 66.7, "complaint_rate": 33.3, "praise_rate": 33.3},
        {"month": "2026-04", "review_count": 4, "average_rating": 3.00, "verified_purchase_rate": 75.0, "complaint_rate": 50.0, "praise_rate": 25.0},
    ],
    "trend_direction": "declining",
    "trend_magnitude": -11.2,
    "spike_months": ["2025-10", "2026-04"],
    "insight": (
        "Sentiment is declining — recent average rating is 11.2% lower than the prior period. "
        "Complaint spikes in October 2025 and April 2026 align with ear cushion deterioration "
        "reports peaking — reviewers who bought in June-July are hitting the 3-4 month failure "
        "window. This is a predictable, recurring pattern tied to the cushion defect timeline."
    ),
}

AUDIOMAX_RATING_DIST = {
    "1": {"count": 3,  "percentage": 7.5},
    "2": {"count": 5,  "percentage": 12.5},
    "3": {"count": 6,  "percentage": 15.0},
    "4": {"count": 12, "percentage": 30.0},
    "5": {"count": 14, "percentage": 35.0},
}

# ---------------------------------------------------------------------------
# Pre-filtered DataFrames (simulate filter_fake_reviews output)
# ---------------------------------------------------------------------------

def _make_trusted(df: pd.DataFrame) -> pd.DataFrame:
    """Simulate the trusted subset — drop unverified + short reviews."""
    mask = df["verified_purchase"] | (df["body"].str.split().str.len() > 80)
    trusted = df[mask].copy()
    trusted["trust_score"] = 80
    return trusted.reset_index(drop=True)


# ---------------------------------------------------------------------------
# PUBLIC API
# ---------------------------------------------------------------------------

def get_demo_data(product_num: int = 1) -> dict:
    """
    Returns everything the Streamlit app needs to render the full UI.

    product_num=1  →  TechSound Pro (primary product)
    product_num=2  →  AudioMax (competitor)
    """
    if product_num == 1:
        df = TECHSOUND_REVIEWS_DF.copy()
        trusted_df = _make_trusted(df)
        return {
            "product_info":       TECHSOUND_INFO,
            "reviews_df":         df,
            "trusted_reviews":    trusted_df,
            "flagged_reviews":    df[~df.index.isin(trusted_df.index)],
            "filter_stats":       TECHSOUND_FILTER_STATS,
            "analysis":           TECHSOUND_ANALYSIS,
            "trends":             TECHSOUND_TRENDS,
            "rating_distribution":TECHSOUND_RATING_DIST,
            "competitor": {
                "product_info":        AUDIOMAX_INFO,
                "reviews_df":          AUDIOMAX_REVIEWS_DF.copy(),
                "trusted_reviews":     _make_trusted(AUDIOMAX_REVIEWS_DF),
                "filter_stats":        AUDIOMAX_FILTER_STATS,
                "analysis":            AUDIOMAX_ANALYSIS,
                "trends":              AUDIOMAX_TRENDS,
                "rating_distribution": AUDIOMAX_RATING_DIST,
            },
            "gap_analysis": GAP_ANALYSIS,
        }
    else:
        df = AUDIOMAX_REVIEWS_DF.copy()
        trusted_df = _make_trusted(df)
        return {
            "product_info":       AUDIOMAX_INFO,
            "reviews_df":         df,
            "trusted_reviews":    trusted_df,
            "flagged_reviews":    df[~df.index.isin(trusted_df.index)],
            "filter_stats":       AUDIOMAX_FILTER_STATS,
            "analysis":           AUDIOMAX_ANALYSIS,
            "trends":             AUDIOMAX_TRENDS,
            "rating_distribution":AUDIOMAX_RATING_DIST,
            "competitor": {
                "product_info":        TECHSOUND_INFO,
                "reviews_df":          TECHSOUND_REVIEWS_DF.copy(),
                "trusted_reviews":     _make_trusted(TECHSOUND_REVIEWS_DF),
                "filter_stats":        TECHSOUND_FILTER_STATS,
                "analysis":            TECHSOUND_ANALYSIS,
                "trends":              TECHSOUND_TRENDS,
                "rating_distribution": TECHSOUND_RATING_DIST,
            },
            "gap_analysis": GAP_ANALYSIS,
        }


if __name__ == "__main__":
    import json

    data = get_demo_data(1)
    print(f"Product: {data['product_info']['title']}")
    print(f"Reviews: {len(data['reviews_df'])} total, {len(data['trusted_reviews'])} trusted")
    print(f"Filter stats: {data['filter_stats']}")
    print(f"\nRating distribution:")
    for star, d in data["rating_distribution"].items():
        bar = "█" * int(d["percentage"] / 5)
        print(f"  {star}★  {bar} {d['count']} ({d['percentage']}%)")
    print(f"\nTrend: {data['trends']['trend_direction']} ({data['trends']['trend_magnitude']:+.1f}%)")
    print(f"Insight: {data['trends']['insight']}")
    print(f"\nComplaint themes: {len(data['analysis']['complaint_themes'])}")
    for t in data["analysis"]["complaint_themes"]:
        print(f"  [{t['emotional_intensity'].upper()}] {t['theme']} — {t['frequency_pct']}%")
    print(f"\nGap analysis advantages: {len(data['gap_analysis']['my_advantages'])}")
    print(f"Gap analysis vulnerabilities: {len(data['gap_analysis']['my_vulnerabilities'])}")
    print(f"\nCompetitor: {data['competitor']['product_info']['title'][:60]}...")
