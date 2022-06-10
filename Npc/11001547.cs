using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001547: Vasara Chen
/// </summary>
public class _11001547 : NpcScript {
    internal _11001547(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0516130207006115$ 
                // - What is it?
                return true;
            case 20:
                // $script:0531170907006247$ 
                // - What do <i>you</i> want?
                switch (selection) {
                    // $script:0531170907006248$
                    // - I've heard stories about you.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0531170907006249$ 
                // - The idiots here have big mouths. Well go on, what did they tell you?
                switch (selection) {
                    // $script:0531170907006250$
                    // - They say you're impossibly strong.
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0531170907006251$ 
                // - Strength is relative. If these idiots think I'm strong, it's only because they've never faced true power.
                switch (selection) {
                    // $script:0531170907006252$
                    // - I know a thing or two about strength.
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:0531170907006253$ 
                // - I see. If you're that confident, maybe you'll present an actual challenge.
                switch (selection) {
                    // $script:0531170907006254$
                    // - Not everyone is so quick to believe me.
                    case 0:
                        Id = 60;
                        return false;
                }
                return true;
            case 60:
                // $script:0531170907006255$ 
                // - This one time, I had a match against this bird-man who was on a journey to test his strength. He didn't look much—heck, he looked weaker than most. Nobody took him seriously.
                // $script:0531170907006256$ 
                // - But when he stepped into that ring, he tore through his opponents like they were made of paper. Even I couldn't do better than draw against him. He taught me not to judge a book by its cover.
                switch (selection) {
                    // $script:0531170907006257$
                    // - You think I'm like that bird guy?
                    case 0:
                        Id = 70;
                        return false;
                }
                return true;
            case 70:
                // $script:0531170907006258$ 
                // - Hah! No, if anything, you're more like <i>me</i>. There's a certain electricity in the air around fighters like you and I. Most people can't even sense it. But the strong can always recognize each other.
                // $script:0531170907006260$ 
                // - Of course, you can also be strong without knowing how to fight. The only way to <i>really</i> know someone is to face them in the ring. I don't know about you, but I'm looking forward to our fight.
                //   <font color="#909090">(The air around him grows heavy and terrifying.)</font>
                switch (selection) {
                    // $script:0607145407006337$
                    // - Face me in the ring.
                    case 0:
                        Id = 80;
                        return false;
                }
                return true;
            case 80:
                // $script:0531170907006263$ 
                // - That's the plan... Can't wait.
                return true;
            default:
                return true;
        }
    }
}
