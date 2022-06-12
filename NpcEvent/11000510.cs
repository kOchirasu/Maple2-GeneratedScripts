/// <summary>
/// 11000510: Peachy
/// </summary>
public static class Event11000510 {
    public static (string, string, string) Event(int scriptId, int eventId) {
        return (scriptId, eventId) switch {
            // - Is this the gear you want to change? Okay! Don't worry, if you don't like the new attributes, you can keep the old ones.
            (30, 9100) => ("$script:0323154410001472$", "ko/Npc/00001268", "Peach_normal"),
            // - I would love to change your bonus attributes for you! I just need the necessary materials, hehe.
            (30, 9000) => ("$script:0323154410001473$", "ko/Npc/00001270", "Peach_normal"),
            // - What do you think? Do you like the new attributes? Remember, if you don't choose anything, the new attributes will automatically be applied.
            (30, 9200) => ("$script:0323154410001474$", "ko/Npc/00001244", "Peach_normal"),
            // - If you're not satisfied with the current attributes, you can always try again. Just bring the materials, hehe.
            (30, 9300) => ("$script:0323154410001475$", "ko/Npc/00001271", "Peach_normal"),
            // - Oh, dear. This gear is a bit advanced for me. Could I help you with a different piece, perhaps?
            (30, 9001) => ("$script:0323154410001476$", "ko/Npc/00001246", "Peach_normal"),
            // - I can't enchant this gear. The process to do so is too unstable. Perhaps you have a different item for me to enchant?
            (31, 2) => ("$script:1123232210001203$", "", "Peach_normal"),
            // - Oh no! You don't have all the materials you need! You can get $itemPlural:40100001$ from gear merchants and supply merchants and $itemPlural:40100023$ by dismantling level 20 or higher gear. $itemPlural:40100024$ are a bit more rare and only comes from dismantling gear that's epic or better. Use the Dismantle button in your inventory window to dismantle.
            (31, 3) => ("$script:1123232210001204$", "ko/Npc/00001253", "Peach_normal"),
            (31, 1000) => Random(
                // - Legendary gear! I see so many pieces every day, but it's rare for anyone to bring me an item this precious. It will be my honor to enchant this.
                ("$script:1123232210001205$", "ko/Npc/00001260", "Peach_normal")
                // - What?! This is legendary gear! I haven't worked on such a precious piece in a long time. I've got butterflies in my stomach.
                ("$script:1123232210001206$", "ko/Npc/00001260", "Peach_normal")
            ),
            (31, 1100) => Random(
                // - You picked a good piece of gear to be enchanted! Wait until you see how it turns out!
                ("$script:1123232210001207$", "ko/Npc/00001259", "Peach_normal")
                // - Oh! This piece has never been enchanted before. That should make it really easy for me, hehe.
                ("$script:1123232210001208$", "ko/Npc/00001259", "Peach_normal")
                // - This gear has never been enchanted before. Should be a cinch, then. Here goes...
                ("$script:1123232210001209$", "ko/Npc/00001259", "Peach_normal")
            ),
            (31, 1101) => Random(
                // - Oh, dear me! Someone failed at enchanting this item 100 items?!
                ("$script:1123232210001210$", "", "Peach_normal")
                // - You've failed in enchanting this gear 100 times, and you still want to try again? Are you sure? I really wish you'd brought this to me to begin with. Oh, dear.
                ("$script:1123232210001211$", "", "Peach_normal")
            ),
            // - Oh, dear!! Someone failed in enchanting this gear 1,000 times?! How is that even possible?
            (31, 1102) => ("$script:1123232210001212$", "", "Peach_normal"),
            // - I can't enchant this gear. The process to do so is too unstable. Perhaps you have a different item for me to enchant?
            (31, 1103) => ("$script:1123232210001213$", "", "Peach_normal"),
            // - I can't enchant this gear. The process to do so is too unstable. Perhaps you have a different item for me to enchant?
            (31, 1104) => ("$script:0212164210001437$", "", "Peach_normal"),
            (31, 1198) => Random(
                // - Oh my, it's impossible to enchant this gear any further. Don't look glum. It's already really strong!
                ("$script:0307102910001450$", "ko/Npc/00001251", "Peach_shy")
                // - I know you're the type who likes to rise to any challenge, but even you and your gear have limits. And sometimes, it's wiser to quit than to try to push things past their natural limit.
                ("$script:0307102910001451$", "ko/Npc/00001251", "Peach_shy")
                // - That piece of gear is beyond my ability to enchant. The $itemPlural:40100023$ required would become too instable during the process, you see. Even $npc:11000508[gender:1]$ agrees with me on that one.
                ("$script:0307102910001452$", "ko/Npc/00001251", "Peach_shy")
                // - Everyone has a piece of gear or two that they feel sentimental about. I have an entire closet full. But love isn't enough to allow you to enchant your gear an unlimited number of times.
                ("$script:0307102910001453$", "ko/Npc/00001251", "Peach_shy")
            ),
            (31, 1200) => Random(
                // - Easy peasy, hehe! Don't worry, you're in good hands!
                ("$script:1123232210001214$", "ko/Npc/00001264", "Peach_normal")
                // - Hehe, this is so straightforward, I could do it with my eyes closed. Want to see?
                ("$script:1123232210001215$", "ko/Npc/00001264", "Peach_normal")
                // - I think we know how this is going to turn out, hehe. Here goes!
                ("$script:1123232210001216$", "", "Peach_normal")
            ),
            (31, 1201) => Random(
                // - Hmm, this shouldn't be too difficult. Shall I begin?
                ("$script:1123232210001217$", "", "Peach_normal")
                // - I'm always happy to help. All you need to do is bring the materials, hehe.
                ("$script:1123232210001218$", "", "Peach_normal")
                // - Some of the others call my enchanting skills legendary, because I never fail. I don't know, though... My way requires a lot more materials. Does that really make it better?
                ("$script:1123232210001219$", "", "Peach_normal")
                // - Low level gear doesn't require many materials to enchant.
                ("$script:1123232210001220$", "", "Peach_normal")
            ),
            (31, 1202) => Random(
                // - This shouldn't be difficult.
                ("$script:1123232210001221$", "", "Peach_normal")
                // - I can guarantee success on this enchant, and it doesn't even require that many additional materials, hehe.
                ("$script:1123232210001222$", "", "Peach_normal")
                // - This piece of gear can be easily enchanted.
                ("$script:1123232210001223$", "", "Peach_normal")
                // - This shouldn't be too difficult.
                ("$script:1123232210001224$", "", "Peach_normal")
            ),
            (31, 1203) => Random(
                // - This piece of gear needs more materials to enchant than before, but success is guaranteed, hehe!
                ("$script:1123232210001225$", "", "Peach_normal")
                // - You'll need a lot of materials to enchant this, but if you provide it all, success is guaranteed, hehe.
                ("$script:1123232210001226$", "", "Peach_normal")
            ),
            (31, 1204) => Random(
                // - Do you have all the materials? Just remember, you're spending extra materials for a guaranteed result! I hope that motivates you, hehe.
                ("$script:1123232210001227$", "", "Peach_normal")
                // - I require a lot of materials, true... but I also never fail.
                ("$script:1123232210001228$", "", "Peach_normal")
            ),
            (31, 1205) => Random(
                // - You may need to invest extra time and effort to use my services, but I never ever fail.
                ("$script:1123232210001229$", "", "Peach_normal")
                // - For my method of enchanting, you get what you put in! It costs more materials, sure, but it's guaranteed success!
                ("$script:1123232210001230$", "", "Peach_normal")
            ),
            (31, 1206) => Random(
                // - Don't be intimidated by the material requirements... Think about the end result: guaranteed enchantment!
                ("$script:1123232210001231$", "", "Peach_normal")
                // - True, I ask for a lot of materials, but isn't it worth it?
                ("$script:1123232210001232$", "", "Peach_normal")
                // - I can enchant your gear as many times as you like, as long as you have all the materials.
                ("$script:1123232210001233$", "", "Peach_normal")
                // - I know other blacksmiths don't require as many materials as I do, but they fail in their work sometimes. I don't.
                ("$script:1123232210001234$", "", "Peach_normal")
            ),
            (31, 1207) => Random(
                // - I know I require a lot of materials, but that's the price of quality, hehe.
                ("$script:1123232210001235$", "", "Peach_normal")
                // - My service costs more, but you get that you pay for! Bad luck never gets in my way!
                ("$script:1123232210001236$", "", "Peach_normal")
            ),
            (31, 1208) => Random(
                // - I know some folks enjoy the thrill of a good deal. Just remember: my method allows me to enchant your gear with guaranteed success.
                ("$script:1123232210001237$", "", "Peach_normal")
                // - It'll be worth the material cost, I promise!
                ("$script:1123232210001238$", "", "Peach_normal")
            ),
            (31, 1209) => Random(
                // - From now on, I'll need even more materials. You might want to mentally prepare yourself, hehe.
                ("$script:1123232210001239$", "", "Peach_normal")
                // - Yes, I require a lot of materials, but remember... the enchantment I offer is fail-safe.
                ("$script:1123232210001240$", "", "Peach_normal")
            ),
            (31, 1210) => Random(
                // - Don't try to max out your gear's enchantment level all at once. It'd be too overwhelming.
                ("$script:1123232210001241$", "", "Peach_normal")
                // - $MyPCName$, I know it takes a lot of time and effort to gather so many materials, but once you have them, I promise to successfully enchant your gear. Hehe.
                ("$script:1123232210001242$", "", "Peach_normal")
            ),
            (31, 1211) => Random(
                // - You're going to try for +14? That will take a lot of materials! I can do it, sure, but it'll be quite a bit of work, hehe.
                ("$script:1123232210001243$", "", "Peach_normal")
                // - Do you think you'll be able to gather all the materials? It's really quite a lot!
                ("$script:1123232210001244$", "", "Peach_normal")
            ),
            (31, 1212) => Random(
                // - I can enchant gear as many times as you want, as long as you have enough materials. But I have to say, enchanting to +15 requires many, many materials. +14 is already very strong, isn't it?
                ("$script:1123232210001245$", "", "Peach_normal")
                // - +15... now that makes me nervous. I mean, reaching +15 has always been my dream, but it requires so very many materials. You can't possibly have all of them, can you?
                ("$script:1123232210001246$", "", "Peach_normal")
            ),
            (31, 1213) => Random(
                // - I could practice enchanting for the next hundred years and still wouldn't be able to enchant this piece of gear. It's already so strong!
                ("$script:1123232210001247$", "ko/Npc/00001251", "Peach_normal")
                // - Challenges are what make life interesting, but some challenges can't be overcome, and this is simply one of them.
                ("$script:1123232210001248$", "ko/Npc/00001251", "Peach_normal")
                // - I can't enchant this gear any further. It's so unstable that it could blow up the whole street if I fail.
                ("$script:1123232210001249$", "ko/Npc/00001251", "Peach_shy")
                // - +15 gear really exists! Amazing! Hehe, you realize that no blacksmith in the world can enchant this piece any further, don't you? I'd be happy to help you with other pieces of gear, though.
                ("$script:1123232210001250$", "ko/Npc/00001251", "Peach_shy")
                // - This piece of gear is already strong. I don't think I can make it any stronger...
                ("$script:1123232210001251$", "ko/Npc/00001251", "Peach_shy")
            ),
            (31, 1999) => Random(
                // - Enchanting gear requires precise skill and tons of practice.
                ("$script:1123232210001252$", "ko/Npc/00001249", "Peach_normal")
                // - Blacksmithing makes me smile. Nothing beats working over a flame!
                ("$script:1123232210001253$", "ko/Npc/00001249", "Peach_normal")
                // - Sure, it'd be great if enchantments never failed.
                //   But then again, that would make us blacksmiths go broke! Ha, ha!
                ("$script:1123232210001254$", "ko/Npc/00001249", "Peach_normal")
            ),
            (31, 2000) => Random(
                // - It worked! Hehe, it always works! But it still makes me so happy every single time.
                ("$script:1123232210001255$", "ko/Npc/00001261", "Peach_smile")
                // - Hehe, see? I told you the enchantment would go great!
                ("$script:1123232210001256$", "ko/Npc/00001261", "Peach_smile")
            ),
            (31, 2001) => Random(
                // - Success! Yes! Hehe. I hope you enjoyed my services!
                ("$script:1123232210001257$", "ko/Npc/00001261", "Peach_smile")
                // - Success! You provided lovely materials. Nicely done!
                ("$script:1123232210001258$", "ko/Npc/00001261", "Peach_smile")
                // - Hehehe, I'm not bad,right? See you again soon!
                ("$script:1123232210001259$", "ko/Npc/00001261", "Peach_smile")
            ),
            // - Hehe, nice, right? I hope we can work together again soon!
            (31, 2002) => ("$script:1123232210001260$", "", "Peach_smile"),
            // - Your gear has reached +10! Hey, you've earned it with your determination and courage in taking risks!
            (31, 2003) => ("$script:1123232210001261$", "", "Peach_smile"),
            // - Thank you for all your hard work, $MyPCName$!
            (31, 2004) => ("$script:1123232210001262$", "", "Peach_smile"),
            // - How did you gather so many materials? Incredible!
            (31, 2005) => ("$script:1123232210001263$", "", "Peach_smile"),
            // - I can't believe you gathered all of these materials. Very impressive!
            (31, 2006) => ("$script:1123232210001264$", "ko/Npc/00001261", "Peach_smile"),
            // - I will certainly remember you, $MyPCName$. Few people could have done what you did.
            (31, 2007) => ("$script:1123232210001265$", "", "Peach_smile"),
            // - Am I dreaming? Is this really happening? I always thought +15 was impossible, but we really did it!
            (31, 2008) => ("$script:1123232210001266$", "", "Peach_smile"),
            (31, 2100) => Random(
                // - I hope you're happy with my service, hehe! Come again!
                ("$script:1123232210001267$", "ko/Npc/00001261", "Peach_smile")
                // - All in a day's work, hehe.
                ("$script:1123232210001268$", "ko/Npc/00001261", "Peach_smile")
            ),
            (31, 2104) => Random(
                // - Uh-oh. It seems the ratio of $item:40100023$ was off, and it decreased your gear's enchantment level by one. I'm sorry; I misjudged the carbon content in your gear. I'll take responsibility for this one.
                ("$script:1123232210001269$", "ko/Npc/00001257", "Peach_shy")
                // - I knew the $item:40100023$ was unstable, but I never thought it would decrease the gear's enchantment level... I'mso, so sorry, but at least it only decreased by one.
                ("$script:1123232210001270$", "ko/Npc/00001257", "Peach_shy")
            ),
            (31, 2203) => Random(
                // - Um... well, the bad news is the enchantment failed. The good news is it could have been much worse.
                ("$script:1123232210001271$", "ko/Npc/00001258", "Peach_shy")
                // - Oh, the enchantment failed. It's not our fault... Whoever made this gear didn't case-harden it enough, so it's random chance whether it can tolerate enchantments.
                ("$script:1123232210001272$", "ko/Npc/00001258", "Peach_shy")
            ),
            (31, 2300) => Random(
                // - Oops, I thought this would be easy...
                ("$script:1123232210001273$", "ko/Npc/00001258", "Peach_surprise")
                // - I promise, this only happens once in a blue moon, and it's just random bad luck that it was your gear it happened to.
                ("$script:1123232210001274$", "ko/Npc/00001258", "Peach_surprise")
            ),
            // - Oh, geez, I damaged your gear during the attempt! I'm... I'm sorry! Maybe I'm in the wrong line of work...
            //    Look, I managed to save this $item:40100025$. Please, take it. At least if you collect enough of those, you could find some use for them.
            (31, 2400) => ("$script:0215183810001440$", "ko/Npc/00001246", "Peach_shy"),
            (31, 2401) => Random(
                // - Aww... I was full of dread when I started, and I was right to be so.
                //   Your gear couldn't handle the pressure of the enchantment, and it got damaged. 
                //   Its enchantment effects will reset in 10 days.
                //   And I'm sorry, but now it can never be enchanted again. 
                ("$script:1123232210001275$", "ko/Npc/00001256", "Peach_surprise")
                // - Oh no! This isn't good...
                ("$script:1123232210001276$", "ko/Npc/00001256", "Peach_surprise")
            ),
            // - Ah, the enchantment failed! 
            //   Well, at least your gear wasn't damaged. You got lucky this time, $MyPCName$. Please think carefully before you try another enchantment! It would be risky for your gear.
            (31, 2500) => ("$script:0212164210001438$", "ko/Npc/00001246", "Peach_shy"),
            // - This item is... difficult for me. Is there a different piece I could help you with?
            (31, 1) => ("$script:1123232210001277$", "ko/Npc/00001247", "Peach_normal"),
            _ => ("", "", ""),
        };
    }
}
