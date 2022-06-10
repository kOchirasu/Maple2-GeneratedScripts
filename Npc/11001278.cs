using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001278: Shun
/// </summary>
public class _11001278 : NpcScript {
    internal _11001278(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1208175407004838$ 
                // - The Baaz watch over us all. 
                return true;
            case 30:
                // $script:1211023307004939$ 
                // - The Baaz watch over us all. 
                switch (selection) {
                    // $script:1211023307004940$
                    // - I have some questions.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1211023307004941$ 
                // - What would you like to ask? 
                switch (selection) {
                    // $script:1211023307004942$
                    // - How did Terrun Calibre get started?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:1211023307004943$
                    // - Why are there sects in Terrun Calibre?
                    case 1:
                        Id = 50;
                        return false;
                    // $script:1211023307004944$
                    // - What are the Eight Blades?
                    case 2:
                        Id = 60;
                        return false;
                }
                return true;
            case 40:
                // $script:1211023307004945$ 
                // - Long ago, there lived two masters: a rune mage and a swordsman. Each was convinced that their art was the greater of the two, and so they had a duel. When they proved to be evenly matched, they decided to merge their martial arts and established Terrun Calibre to teach their new fighting style. 
                // $script:1211023307004946$ 
                // - These were the first Runeblades, Jibritta and Pelgia. Together, they created a legacy of master warrior-mages. 
                // $script:1211023307004947$ 
                // - They realized they could never reach true mastery of the new fighting style in their lifetime, so instead they focused on recruiting and training skilled warriors. Terrun Calibre continues that tradition to this day. 
                switch (selection) {
                    // $script:1211023307004948$
                    // - I have another question.
                    case 0:
                        Id = 70;
                        return false;
                }
                return true;
            case 50:
                // $script:1211023307004949$ 
                // - Every Runeblade knows the names of the first masters, Jibritta and Pelgia. But before these two founded Terrun Calibre, they already had martial arts schools of their own. 
                // $script:1211023307004950$ 
                // - Not all of their students agreed with the vision of combining rune magic and swordsmanship. Even though these schools were united under Terrun Calibre, the original students of each tradition continued to bump heads. 
                // $script:1211023307004951$ 
                // - Today, the Runeblades have embraced the combination of magic and martial skill, but these old factions remain—and so do the old loyalties. 
                // $script:1211023307004952$ 
                // - The members of the Jibritta Sect believe in the superiority of a learned mind, and devote themselves to mastery of the elements. Those in the Pelgia Sect, on the other hand, value physical strength, and spend countless hours honing their bodies into a tool of blade and magic. 
                // $script:1211030007004978$ 
                // - Each sect has its own leader. Before Arazard was killed, he was the leader of both the Pelgias Sect and Terrun Calibre as a whole, which was unheard of. 
                // $script:1211023307004953$ 
                // - When $npcName:11001231[gender:0]$ was the leader of the Jibritta Sect, the tension between the two factions reached a new height. 
                switch (selection) {
                    // $script:1211023307004954$
                    // - Which sect do the scouts belong to?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1211023307004955$ 
                // - $npcName:11001265[gender:1]$ was one of the sixteen disciples of Arazard, which makes her a Pelgia. But most of the scouts under her are Jibritta. 
                switch (selection) {
                    // $script:1211023307004956$
                    // - But aren't the Jibritta the ones who started this mess?
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:1211023307004957$ 
                // - No, attitudes like <i>that</i> did. $npcName:11001231[gender:0]$ may have led the Jibritta Sect, but not all Jibritta agree with him. I'm a Jibritta myself, and I'd like nothing more than to see him brought to justice. 
                switch (selection) {
                    // $script:1211023307004958$
                    // - I have another question.
                    case 0:
                        Id = 70;
                        return false;
                }
                return true;
            case 60:
                // $script:1211023307004959$ 
                // - The eight greatest Runeblades of each generation are named the Eight Blades. They represent the strength of Terrun Calibre.  
                switch (selection) {
                    // $script:1211023307004960$
                    // - So, how strong are they?
                    case 0:
                        Id = 61;
                        return false;
                }
                return true;
            case 61:
                // $script:1211023307004961$ 
                // - I think you know the answer to that already. Your teacher is one of them. 
                // $script:1211023307004962$ 
                // - $npc:11001246[gender:0]$ is probably one of the five strongest Runeblades of all time. And you'd better believe that $npcName:11001230[gender:0]$ is just as strong. 
                switch (selection) {
                    // $script:1211023307004963$
                    // - So, who's the very strongest?
                    case 0:
                        Id = 62;
                        return false;
                }
                return true;
            case 62:
                // $script:1211023307004964$ 
                // - In terms of skill alone, it would have to be $npcName:11001231[gender:0]$. He's a genius and the best of this generation's Eight Blades. But he betrayed us, and so his genius has become Terrun Calibre's greatest shame. 
                switch (selection) {
                    // $script:1211023307004965$
                    // - I have another question.
                    case 0:
                        Id = 70;
                        return false;
                }
                return true;
            case 70:
                // $script:1211023307004966$ 
                // - Is there anything else you want to ask? 
                switch (selection) {
                    // $script:1211023307004967$
                    // - How did Terrun Calibre get started?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:1211023307004968$
                    // - Why are there sects in Terrun Calibre?
                    case 1:
                        Id = 50;
                        return false;
                    // $script:1211023307004969$
                    // - What are the Eight Blades?
                    case 2:
                        Id = 60;
                        return false;
                    // $script:1211023307004970$
                    // - I need to be going.
                    case 3:
                        Id = 71;
                        return false;
                }
                return true;
            case 71:
                // $script:1211023307004971$ 
                // - May the Baaz guide you. 
                return true;
            default:
                return true;
        }
    }
}
