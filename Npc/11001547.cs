using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001547: Vasara Chen
/// </summary>
public class _11001547 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0516130207006115$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0531170907006247$
                // - What do <i>you</i> want?
                switch (selection) {
                    // $script:0531170907006248$
                    // - I've heard stories about you.
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0531170907006249$
                // - The idiots here have big mouths. Well go on, what did they tell you?
                switch (selection) {
                    // $script:0531170907006250$
                    // - They say you're impossibly strong.
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0531170907006251$
                // - Strength is relative. If these idiots think I'm strong, it's only because they've never faced true power.
                switch (selection) {
                    // $script:0531170907006252$
                    // - I know a thing or two about strength.
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:0531170907006253$
                // - I see. If you're that confident, maybe you'll present an actual challenge.
                switch (selection) {
                    // $script:0531170907006254$
                    // - Not everyone is so quick to believe me.
                    case 0:
                        return 60;
                }
                return -1;
            case (60, 0):
                // $script:0531170907006255$
                // - This one time, I had a match against this bird-man who was on a journey to test his strength. He didn't look much—heck, he looked weaker than most. Nobody took him seriously.
                return 60;
            case (60, 1):
                // $script:0531170907006256$
                // - But when he stepped into that ring, he tore through his opponents like they were made of paper. Even I couldn't do better than draw against him. He taught me not to judge a book by its cover.
                switch (selection) {
                    // $script:0531170907006257$
                    // - You think I'm like that bird guy?
                    case 0:
                        return 70;
                }
                return -1;
            case (70, 0):
                // $script:0531170907006258$
                // - Hah! No, if anything, you're more like <i>me</i>. There's a certain electricity in the air around fighters like you and I. Most people can't even sense it. But the strong can always recognize each other.
                return 70;
            case (70, 1):
                // $script:0531170907006260$
                // - Of course, you can also be strong without knowing how to fight. The only way to <i>really</i> know someone is to face them in the ring. I don't know about you, but I'm looking forward to our fight.
                //   <font color="#909090">(The air around him grows heavy and terrifying.)</font>
                switch (selection) {
                    // $script:0607145407006337$
                    // - Face me in the ring.
                    case 0:
                        return 80;
                }
                return -1;
            case (80, 0):
                // $script:0531170907006263$
                // - That's the plan... Can't wait.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.Next,
            (60, 1) => NpcTalkButton.SelectableDistractor,
            (70, 0) => NpcTalkButton.Next,
            (70, 1) => NpcTalkButton.SelectableDistractor,
            (80, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
