/// <summary>
/// 11000508: Ophelia
/// </summary>
public static class Event11000508 {
    public static (string, string, string) Event(int scriptId, int eventId) {
        return (scriptId, eventId) switch {
            // - So you want to change the bonus attributes on this gear, eh? Sounds good to me! Hey, why the anxious look on your face? If you don't like the new attributes, you can always keep the old ones, and then just try to change them again.
            (30, 9100) => ("$script:0323154410001461$", "ko/Npc/01000121", "Ophelia_normal"),
            // - I understand you want to change the bonus attributes on your gear, but I can't help you if you don't have the materials, Silly!
            //   Come back when you've got the right stuff, yeah?
            (30, 9000) => ("$script:0323154410001462$", "ko/Npc/00001208", "Ophelia_normal"),
            // - Okay, then! See if you like any of these new attributes. 
            //   You can choose anything you like. If you don't choose anything, then the new attributes will automatically overwrite the old ones. Choose carefully!
            (30, 9200) => ("$script:0323154410001463$", "ko/Npc/01000119", "Ophelia_normal"),
            // - How do you feel about the change of attributes? Overjoyed? Devastated? Ready to sue me? I hope not, ha ha! But seriously, if you're not happy, you can always try to change the attributes again. I'll be here. Just bring the materials! 
            (30, 9300) => ("$script:0323154410001464$", "ko/Npc/01000119", "Ophelia_normal"),
            // - Oh, wow. This gear is a little above my pay grade. Could I help you with anything less advanced?
            (30, 9001) => ("$script:0323154410001465$", "ko/Npc/00001208", "Ophelia_normal"),
            // - Hm. It is my expert opinion that this gear is not stable enough to be enchanted any further! You'll need to bring me different gear if you want me to help you.
            (31, 2) => ("$script:0330140710001960$", "", "Ophelia_normal"),
            // - You didn't forget that enchanting gear requires materials, did you? $itemPlural:40100001$ are available for purchase from gear merchants and supply merchants. You can get $itemPlural:40100023$ by dismantling gear that's level 20 or higher. Just use the Dismantle button in your inventory window. As for the $itemPlural:40100024$, that comes at a much higher cost. It only comes from dismantling gear that is epic or better.
            (31, 3) => ("$script:0330140710001961$", "", "Ophelia_normal"),
            // - Hey, now. If you want to enchant anything to +11 or better, you're going to need a spare piece of gear or two. Enchantments at this level take a little sacrifice. That said, I hear there's an item out there that will let you enchant without a sacrifice...
            (31, 4) => ("$script:0608144010002139$", "", "Ophelia_normal"),
            // - You're really going to try it? Remember, you can't increase your chances of success past 30% using the same gear.
            (31, 5) => ("$script:0608144010002138$", "", "Ophelia_normal"),
            // - You want to go for an even higher level? I understand you don't want to fail, but you need to face reality! With the current technology, it's impossible to increase the success rate more than this!
            (31, 6) => ("$script:0608190510002182$", "", "Ophelia_normal"),
            // - You want to go for an even higher level? I understand you don't want to fail, but you need to face reality! With the current technology, it's impossible to increase the success rate more than this!
            (31, 7) => ("$script:0608190510002183$", "", "Ophelia_normal"),
            (31, 1000) => Random(
                // - Wow! This is legendary! Where did you get it? I see gear from all over the world every day, but nothing like this. This is something truly special.
                ("$script:0330140710001962$", "ko/Npc/01000118", "Ophelia_normal")
                // - Whoa, this is a legendary item. I can't compensate you for anything that happens to such a valuable piece, so you need to be willing to assume all risk.
                ("$script:0330140710001963$", "ko/Npc/01000118", "Ophelia_normal")
            ),
            // - Ascendant gear?! Whoa! This is my chance to prove my skills!
            (31, 1001) => ("$script:0608144010002140$", "ko/Npc/01000118", "Ophelia_normal"),
            (31, 1100) => Random(
                // - This has never been enchanted, not even once. You'll be very happy when you see how much better I can make it.
                ("$script:0330140710001964$", "ko/Npc/01000117", "Ophelia_normal")
                // - You've never tried to enchant this gear? Just wait till you see what I can do with it!
                ("$script:0330140710001965$", "ko/Npc/01000117", "Ophelia_normal")
                // - Never-enchanted gear? That's great. It should be really easy to enchant this gear for the first time.
                ("$script:0330140710001966$", "ko/Npc/01000117", "Ophelia_normal")
            ),
            (31, 1101) => Random(
                // - This gear... Have I really failed in enchanting it 100 times? Gee. This hurts my pride. But you know what a blacksmith with real grit would do? Not give up! So let's try it again, this time with more experience and wiser minds, yeah?
                ("$script:0330140710001967$", "ko/Npc/01000113", "Ophelia_normal")
                // - But you've already tried to enchant this gear 100 times, and it's been a failure each and every time. You're going to ask me to enchant it no matter what I say, aren't you? Wow, you're stubborner than I am. All right, no guarantees it'll work, but here goes!
                ("$script:0330140710001968$", "ko/Npc/01000113", "Ophelia_normal")
            ),
            // - Have you really tried and failed to enchant this gear 1,000 times? I can't believe it! I thought I was stubborn, but I have nothing on you. Maybe all of us craftspeople on this street should give you an award for Best Customer.
            (31, 1102) => ("$script:0330140710001969$", "ko/Npc/01000112", "Ophelia_normal"),
            // - Hm. It is my expert opinion that this gear is not stable enough to be enchanted any further! You'll need to bring me different gear if you want me to help you.
            (31, 1103) => ("$script:0330140710001970$", "", "Ophelia_normal"),
            // - Hm. It is my expert opinion that this gear is not stable enough to be enchanted any further! You'll need to bring me different gear if you want me to help you.
            (31, 1104) => ("$script:0330140710001971$", "", "Ophelia_normal"),
            (31, 1198) => Random(
                // - I can't enchant this. I could hone my enchanting skills for the next hundred years, and I still wouldn't be able to do it. This gear is just too strong. You should be satisfied with it as it is.
                ("$script:0330140710001972$", "ko/Npc/01000109", "Ophelia_normal")
                // - I know you're the type who likes to rise to any challenge, but even you and your gear have limits. And sometimes, it's wiser to quit than to try to push things past their natural limit.
                ("$script:0330140710001973$", "ko/Npc/01000109", "Ophelia_normal")
                // - I can't enchant this gear any further. It's so unstable that it could blow up the whole street if I fail. You'll need to find someone with more expertise.
                ("$script:0330140710001974$", "ko/Npc/01000109", "Ophelia_serious")
                // - I understand you want to make your gear stronger. But some things just can't be done. It's already at a level that would scare away most blacksmiths. Don't get greedy.
                ("$script:0330140710001975$", "ko/Npc/01000109", "Ophelia_serious")
                // - Yes, I remember how happy you were last time, totally ignoring all logic and tempting fate. It seemed insane, but I have to admit... it was an incredible day for me... But look, as glorious as that was, I can't enchant this item any further! By golly, I'd need another decade of practice, at the very least!
                ("$script:0330140710001976$", "ko/Npc/01000109", "Ophelia_serious")
            ),
            (31, 1200) => Random(
                // - Put your mind at ease. Only another earthquake could make me fail at this simple of an enchantment.
                ("$script:0330140710001977$", "ko/Npc/01000123", "Ophelia_normal")
                // - Don't worry, I could do this with one hand tied behind my back. In fact, I could do a lot of smithing one-handed if I could just find someone to be my striker! Interested? Okay, okay, I can see you just want the enchantment... let's do this, then.
                ("$script:0330140710001978$", "ko/Npc/01000123", "Ophelia_normal")
                // - This enchantment will be so easy, it would actually be more difficult to fail than to succeed! You'd be foolish to pass up on those odds, I'd say.
                ("$script:0330140710001979$", "ko/Npc/01000123", "Ophelia_normal")
            ),
            (31, 1201) => Random(
                // - There's very little chance of error when the enchantment is this simple. Want me to give it a try?
                ("$script:0330140710001980$", "ko/Npc/01000123", "Ophelia_normal")
                // - Enchanting this gear will be a little tricky, but certainly not impossible. It's up to you, but I'd say the risk is well worth the potential reward.
                ("$script:0330140710001981$", "ko/Npc/01000123", "Ophelia_normal")
                // - This will be a piece of cake. Just believe in me a little!
                ("$script:0330140710001982$", "ko/Npc/01000123", "Ophelia_normal")
                // - Let's see... This gear has only been enchanted a handful of times, so I shouldn't have too much trouble with it... as long as you don't distract me!
                ("$script:0330140710001983$", "ko/Npc/01000123", "Ophelia_normal")
            ),
            (31, 1202) => Random(
                // - I should be able to enchant this gear safely, as long as you don't distract me with incessant chatting or stares, so find something to occupy yourself while I'm working.
                ("$script:0330140710001984$", "ko/Npc/01000123", "Ophelia_normal")
                // - Due to previous enchantments, there's some risk if you want me to enchant this gear. But still, there's a much greater chance that I will succeed. It's up to you.
                ("$script:0330140710001985$", "ko/Npc/01000123", "Ophelia_normal")
                // - Good news! Even though this item has been enchanted multiple times, it's still pretty stable. There's a chance that the new enchantment could go wrong, but that comes with the territory. It's your call.
                ("$script:0330140710001986$", "ko/Npc/01000123", "Ophelia_normal")
                // - There's an elevated chance of failure if I enchant this item, but it's not so high to really worry me. If it doesn't worry you either, go ahead and press the Enchant button.
                ("$script:0330140710001987$", "ko/Npc/01000123", "Ophelia_normal")
            ),
            (31, 1203) => Random(
                // - I'm pretty confident about this. And don't worry; if it doesn't work, you can always try again!
                ("$script:0330140710001988$", "", "Ophelia_normal")
                // - I'm going to give it a go, now. And hey, if I mess up, you can always try again!
                ("$script:0330140710001989$", "", "Ophelia_normal")
            ),
            (31, 1204) => Random(
                // - This is just too easy. Check it out!
                ("$script:0330140710001990$", "", "Ophelia_normal")
                // - To +7, huh? Shouldn't be too hard. Hand it over!
                ("$script:0330140710001991$", "", "Ophelia_normal")
            ),
            (31, 1205) => Random(
                // - This gear is a little delicate, but I'll use some finesse, and it should be fine.
                ("$script:0330140710001992$", "", "Ophelia_normal")
                // - Everybody makes mistakes, but this one should be no problem! 
                ("$script:0330140710001993$", "", "Ophelia_normal")
            ),
            (31, 1206) => Random(
                // - You know, the chances of successful enchantment for this piece are lower than I'd like, but I'll do it if you want me to.
                ("$script:0330140710001994$", "", "Ophelia_normal")
                // - This gear is within my ability to enchant, sure. But the chance of failure is a bit high, and I'm telling you that when other blacksmiths won't, because they're not as honest. So, do what you will with that information.
                ("$script:0330140710001995$", "", "Ophelia_normal")
                // - Think carefully. Your chances at enchanting this gear are pretty low. I mean, sure, you can always try again in the event of failure, but that'll cost another batch of materials.
                ("$script:0330140710001996$", "", "Ophelia_normal")
                // - Anything under +9 is easy. There's nothing to worry about at those levels.
                ("$script:0330140710001997$", "", "Ophelia_normal")
            ),
            // - You want to try a +10 enchant? Ooookay, but don't say I didn't warn you. The success rate is none too pretty, if you know what I mean.
            (31, 1207) => ("$script:0608144010002141$", "", "Ophelia_normal"),
            (31, 1208) => Random(
                // - Hey, +10 is already pretty snazzy. Are you sure you really want to push it?
                ("$script:0608144010002142$", "", "Ophelia_normal")
                // - +10 is decent. Do you really need to enchant this further? You're really gonna go for it, aren't you?
                ("$script:0608144010002143$", "", "Ophelia_normal")
            ),
            (31, 1209) => Random(
                // - You've been lucky so far. To make it all the way to +11? Psh, I know so many folks who'd love to be in your shoes. But hey, you're the boss.
                ("$script:0608144010002144$", "", "Ophelia_normal")
                // - You're really going to try it? If it fails, you're going to lose all the material items. You get that, right?
                ("$script:0608144010002145$", "", "Ophelia_normal")
            ),
            (31, 1210) => Random(
                // - +12 is already amazing, but you're pushing even further? You're braver than I am, that's for sure.
                ("$script:0608144010002146$", "", "Ophelia_normal")
                // - Whoa, are you sure you really want to keep pushing? +12 is already amazing!
                ("$script:0608144010002147$", "", "Ophelia_normal")
            ),
            (31, 1211) => Random(
                // - Whoooooa, you're going for +14? I can't tell if you're a fool or an idiot. Hahaha, but sure, we can give it a shot.
                ("$script:0608144010002148$", "", "Ophelia_normal")
                // - Now let's just take a moment here, calm down, and think about this. Your chances of failure during the next enchantment are dangerously high. It would be absurd to keep going. Don't you realize a failure means you'll have to get the same equipment all over again? Think about this.
                ("$script:0608144010002149$", "", "Ophelia_normal")
            ),
            (31, 1212) => Random(
                // - No, this is crazy. I'm not going to do it, no matter what you say. I'm a blacksmith, and I hate to see good gear wasted. 
                ("$script:0608144010002150$", "", "Ophelia_normal")
                // - You want to try for +15... Have you completely lost your mind? No one with a shred of conscience would try this! To risk harming gear that's already so strong... Please take my advice and be satisfied with this gear as it is... which is fantastic, by the way!
                ("$script:0608144010002151$", "", "Ophelia_normal")
            ),
            (31, 1999) => Random(
                // - The truth about enchanting gear is that it requires both skill and luck.
                ("$script:0330140710002010$", "ko/Npc/01000126", "Ophelia_normal")
                // - Blacksmithing is tough, but fascinating. When I look into the flames, I feel like a god.
                ("$script:0330140710002011$", "ko/Npc/01000126", "Ophelia_normal")
                // - Sure, it'd be great if enchantments never failed. But then again, that would make us blacksmiths go broke! Ha ha!
                ("$script:0330140710002012$", "ko/Npc/01000126", "Ophelia_normal")
            ),
            (31, 2000) => Random(
                // - It worked! Told you I'm the best blacksmith on this street.
                ("$script:0330140710002013$", "ko/Npc/01000119", "Ophelia_smile")
                // - See? No problem at all!
                ("$script:0330140710002014$", "ko/Npc/01000119", "Ophelia_smile")
            ),
            (31, 2001) => Random(
                // - The enchantment was successful! Here you are... nice doing business with ya!
                ("$script:0330140710002015$", "ko/Npc/01000119", "Ophelia_smile")
                // - Your materials were excellent, and the enchantment worked! A great day's work for both of us.
                ("$script:0330140710002016$", "ko/Npc/01000119", "Ophelia_smile")
                // - I told you, this is nothing! Choose me again next time!
                ("$script:0330140710002017$", "ko/Npc/01000119", "Ophelia_smile")
            ),
            // - It worked! And you deserve a lot of the credit. Your persistence made this possible.
            (31, 2002) => ("$script:0330140710002018$", "ko/Npc/01000119", "Ophelia_smile"),
            // - I've succeeded in a +10 enchantment! I'm glad we went for it!
            (31, 2003) => ("$script:0330140710002019$", "ko/Npc/01000119", "Ophelia_smile"),
            // - I made it +11! I gotta tell everyone I know!
            (31, 2004) => ("$script:0330140710002020$", "ko/Npc/01000119", "Ophelia_smile"),
            // - Huh? Did that enchantment really succeed just now? Yes! The gear's +12 now! I'm better than I thought!
            (31, 2005) => ("$script:0330140710002021$", "ko/Npc/01000119", "Ophelia_smile"),
            // - This can't be true. Did I really make it +13? Oh my... I mean, part of it is luck, but still, I think I need to increase my prices!
            (31, 2006) => ("$script:0330140710002022$", "ko/Npc/01000119", "Ophelia_smile"),
            // - +14... This is unbelievable! $MyPCName$, this is the greatest achievement of my life! Congratulations! Congratulations on owning such amazing gear!
            (31, 2007) => ("$script:0330140710002023$", "ko/Npc/01000120", "Ophelia_smile"),
            // - +15...? P-plus fif-fifteen? I...
            //   <font color="#909090">(She's too shocked to speak.)</font>
            (31, 2008) => ("$script:0330140710002024$", "ko/Npc/01000120", "Ophelia_smile"),
            (31, 2100) => Random(
                // - Did  you see that?! The item shook a little, but I kept control over it and the enchantment was successful! That was close, but what a reward! Here's your improved item!
                ("$script:0330140710002025$", "ko/Npc/01000119", "Ophelia_smile")
                // - It worked! My skill aside, the materials you brought were truly excellent. We work well together. I hope you choose me again next time!
                ("$script:0330140710002026$", "ko/Npc/01000119", "Ophelia_smile")
            ),
            (31, 2104) => Random(
                // - Uh-oh. It seems the ratio of $itemPlural:40100023$ was off. That caused some destabilization, and it decreased your gear's enchantment level by one. I'm sorry; I misjudged the carbon content in your gear.
                ("$script:0330140710002027$", "ko/Npc/01000115", "Ophelia_serious")
                // - I knew the $itemPlural:40100023$ were too unstable. Your gear's enchantment level has decreased by one. I'm sorry, but I'm sure I warned you...
                ("$script:0330140710002028$", "ko/Npc/01000115", "Ophelia_serious")
            ),
            (31, 2203) => Random(
                // - What...? This shouldn't have happened! I can't believe it, is it because I saw a black cat on my way to work today?
                ("$script:0330140710002029$", "ko/Npc/01000116", "Ophelia_serious")
                // - Oh, the enchantment failed. It's not our fault... Whoever made this gear didn't case-harden it enough, so it's random chance whether it can tolerate enchantments.
                ("$script:0330140710002030$", "ko/Npc/01000116", "Ophelia_serious")
            ),
            (31, 2300) => Random(
                // - I thought it'd be easy. What did I do wrong? I'll practice more and get better.
                ("$script:0330140710002031$", "ko/Npc/01000116", "Ophelia_shy")
                // - This has never happened before... and when I said it was going to be so easy! It must have been something random, like my hand slipping...
                ("$script:0330140710002032$", "ko/Npc/01000116", "Ophelia_shy")
            ),
            // - Oh no! Your gear got damaged! I'm sorry, oh gosh, I'm so sorry. I didn't mean to! Look, I managed to save these $itemPlural:40100025$. Please, take them. At least if you collect enough of those, you could find some use for them.
            (31, 2400) => ("$script:0330140710002033$", "ko/Npc/03000398", "Ophelia_serious"),
            (31, 2401) => Random(
                // - I feared this would happen, and now my fears have come true. The gear can no longer be enchanted. Its enchantment level has been retained, but that's all the good news there is.
                ("$script:0330140710002034$", "ko/Npc/01000114", "Ophelia_shy")
                // - ...I was afraid this would happen. My sympathies are with you. 
                ("$script:0330140710002035$", "ko/Npc/01000114", "Ophelia_shy")
            ),
            // - Uh-oh, the enchantment failed.  Well... the good news is that it didn't destabilize your gear! Try to look at the glass half-full!
            (31, 2500) => ("$script:0330140710002036$", "ko/Npc/03000398", "Ophelia_serious"),
            // - Hm... This gear would be quite difficult for me. I'd rather help you with some different gear, if you have any.
            (31, 1) => ("$script:0330140710002037$", "ko/Npc/01000110", "Ophelia_normal"),
            _ => ("", "", ""),
        };
    }
}
