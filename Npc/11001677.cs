using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001677: Royal Guard
/// </summary>
public class _11001677 : NpcScript {
    internal _11001677(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 1:
                // $script:0704194107006574$ 
                // - How may I help you?
                return true;
            case 50:
                // $script:0704194107006579$ 
                // - Welcome to $map:02000001$. How may I help you?
                switch (selection) {
                    // $script:0704194107006580$
                    // - Sell me on this $map:02000001$ business.
                    case 0:
                        Id = 51;
                        return false;
                    // $script:0704194107006581$
                    // - What happened to the empress's celebration?
                    case 1:
                        Id = 52;
                        return false;
                    // $script:0704194107006582$
                    // - Hey there. I'm new in town.
                    case 2:
                        Id = 0; // TODO: 61,62,63,64,65,66,67,68,69,70,80,90 | 
                        return false;
                }
                return true;
            case 51:
                // $script:0704194107006584$ 
                // - $map:02000001$ is the biggest city in all of Maple World and the seat of $npcName:11000075[gender:1]$'s power.
                // $script:0704194107006585$ 
                // - $map:02000025$ watches over the city from the north. It's off-limits to the public, I'm afraid. Her majesty's safety takes priority over the curiosity of tourists.
                // $script:0704194107006586$ 
                // - The $map:02000188$, the Banners of Glory, and a taxi stop are all conveniently located in the center of the city. For a reasonable fee, you can hire a taxi to take you to any other taxi stop you've visited, you know. Oh, and the job instructors from all over are gathered in the $map:02000188$.
                // $script:0704194107006587$ 
                // - The Banners of Glory in front of the palace mark the victories of certain powerful guilds and individuals. We update the banners all the time, so you can stop by whenever you like to see who has the most trophies and victories.
                // $script:0704194107006588$ 
                // - In the northern parts of the city, you'll find the royal office and library. $map:02000031$ is a must-see for any book lover, of course. It's not the biggest library in Maple World, but I like to think that it's the best. When I'm off-duty, I love to wander the stacks.
                // $script:0704194107006589$ 
                // - Behind the library is a shopping district where you can find special items, anything from home decor to mounts.
                // $script:0704194107006590$ 
                // - To the southwest, you'll find shops that sell equipment and other supplies. $npcName:11000004[gender:0]$ is one of the best smiths in the land, and $npcName:11000010[gender:1]$ sells all the latest herbs and potions. Never pick a fight without a stack of potions, I always say.
                // $script:0704194107006591$ 
                // - Head southeast and you'll find the residential district and hospital. Kick your feet up and relax after a long journey at $map:02000033$. Have your ailments treated by Tria's finest physician at $map:02000125$. And there's nothing $npcName:11000038[gender:0]$ can't cure.
                // $script:0704194107006592$ 
                // - And that's $map:02000001$ in a nutshell. A long, wordy nutshell. If I told you everything about the city, you'd be here all night. Is there anything else you want to know?
                return true;
            case 52:
                // $script:0704194107006593$ 
                // - I know that you probably came from very far away to see the empress, but these things can't be helped. Thank you for understanding that we had to cancel the open court in the face of unexpected disaster.
                // $script:0704194107006594$ 
                // - $map:02000001$ is the political, economic, and cultural heart of Maple World, so it's always crowded. But in preparation for open court, there must have been ten times the normal number of people here.
                // $script:0704194107006595$ 
                // - Of course, when you have so many people in one place, problems are certain to crop up. Thieves, con artists, and the incident at the celebra—Oops. Maybe I shouldn't have said that.
                // $script:0704194107006596$ 
                // - Anyway, Captain $npcName:11000119[gender:0]$ is determined to keep the peace. Enjoy your stay here, and stay out of trouble. For your own sake.
                return true;
            case 53:
                // $script:0704194107006611$ 
                // - Everyone in Maple World dreams of having a home to call their own. The empress and her court work tirelessly to open up new plots of land, but there's only so much space, so not many people can have the luxury of owning a magnicifent villa.
                // $script:0704194107006612$ 
                // - If you don't have a house yet, you should consider $map:02000001$. Property in the city proper is expensive, but the outlying suburb of $map:02000002$ is partially subsidized by the empress. And there's always $map:02000119$... And $map:02000064$...
                // $script:0704194107006613$ 
                // - There are many advantages to owning a house, you know. These days, every home comes with a device that will let you teleport there at anytime from almost anywhere. Let me tell you, it's saved my butt plenty of times after a long day of patrolling $map:02000092$.
                // $script:0704194107006614$ 
                // - And the merchants in $map:02000036$, west of $map:02000023$, have all kinds of interesting furnishings for sale. Decorate your floors, walls, furniture, and yard to create a house that's unique to you. Some merchants will even sell buildings you can place on your lot! When you're ready to buy, go to $map:02000036$ to shop for your house.
                // $script:0704194107006615$ 
                // - If you already have a house, you could always hire an assistant or two to keep you company. $npcName:11000700[gender:1]$ in the northwestern district of $map:02000001$ hires them out. But first thing's first. You have to buy a house before you can get an assistant!
                return true;
            case 61:
                // $script:0704194107006599$ 
                // - Gosh, you're a Knight! I may be a humble guard now, but someday I want to be just like you.
                return true;
            case 62:
                // $script:0704194107006600$ 
                // - You know, an old friend of mine left town to become a Berserker. I wonder how he's doing...
                return true;
            case 63:
                // $script:0704194107006601$ 
                // - If you're a Wizard, then you'll want to visit $map:02000031$. Even the fairies of $map:02000023$ say our library is the best.
                return true;
            case 64:
                // $script:0704194107006602$ 
                // - It is an honor to serve you, Priest. How is the empress doing?
                return true;
            case 65:
                // $script:0704194107006603$ 
                // - You're a Green Hood, aren't you? That's great. We guard could use the support of people like you during these crazy times.
                return true;
            case 66:
                // $script:0704194107006604$ 
                // - You're a Heavy Gunner, aren't you? I've always wanted to visit $map:2000270$.
                return true;
            case 67:
                // $script:0704194107006605$ 
                // - We're watching you, Thief. You are a guest of the kingdom, but we won't abide any criminal activity.
                return true;
            case 68:
                // $script:0704194107006606$ 
                // - Know this, Assassin. $map:02000001$ is a city of light.
                return true;
            case 69:
                // $script:0704194107006597$ 
                // - If you're looking to take up a job, you should make a stop at the $map:02000188$ in the center of $map:02000001$. Job masters from all over the world are gathered there.
                // $script:0704194107006598$ 
                // - The timing is pretty lucky for you. If it weren't for the empress's court, they wouldn't be here. Of course, if you aren't at least level 10, they won't even talk to you.
                return true;
            case 70:
                // $script:0704194107006607$ 
                // - They say Runeblades are masters of swordsmanship and magic. Being good at either one is hard enough... How did you manage to master both?
                return true;
            case 80:
                // $script:0704194107006608$ 
                // - Hey, you're the Gray Wolf of $map:02000100$, aren't you? They say that you're a master martial artist and that you're taking the fight straight to the gangsters! A real champion of the people! You're my hero! Though... I thought you'd be taller.
                switch (selection) {
                    // $script:0704194107006609$
                    // - You've mistaken me for someone else.
                    case 0:
                        Id = 81;
                        return false;
                }
                return true;
            case 81:
                // $script:0704194107006610$ 
                // - R-really? I'm sorry. I always wanted to meet $male:him,female:her$ in person. I guess I just got excited.
                return true;
            case 90:
                // $script:0805235907007127$ 
                // - Not many people know this, but there's a sect of animal people who live in the mountains and practice mysterious martial arts. I've heard legends that they can even bring the dead back to life...
                return true;
            default:
                return true;
        }
    }
}
